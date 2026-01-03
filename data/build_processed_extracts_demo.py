"""Build teaching cohort extracts from raw MIMIC-IV Demo tables.

This module creates small, analysis-ready cohort extracts used in L08–L11.

Design principles:
- Keep Python complexity low (explicit steps, minimal dependencies).
- Use only MIMIC-IV Demo tables that ship with the course downloader.
- Make defaults deterministic and robust for Google Colab.

Outputs (written under data/processed/ by default):
- cohort_L08_ps_ipw.parquet
- cohort_L09_gformula.parquet
- cohort_L10_survival.parquet
- cohort_L11_msm_longitudinal.parquet

Exposure mode:
- exposure_mode="admission_type" (default): A = 1 if admission_type contains "EMER" (e.g., "EW EMER.", "DIRECT EMER.")
- exposure_mode="vitals": A = 1 if mean heart rate in first 6h of ICU stay > hr_threshold
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import numpy as np
import pandas as pd


ExposureMode = Literal["admission_type", "vitals"]


@dataclass(frozen=True)
class Paths:
    raw_root: Path
    processed_root: Path

    @property
    def patients(self) -> Path:
        return self.raw_root / "hosp" / "patients.csv.gz"

    @property
    def admissions(self) -> Path:
        return self.raw_root / "hosp" / "admissions.csv.gz"

    @property
    def icustays(self) -> Path:
        return self.raw_root / "icu" / "icustays.csv.gz"

    @property
    def chartevents(self) -> Path:
        return self.raw_root / "icu" / "chartevents.csv.gz"


def _find_demo_root(data_raw_dir: Path, version: str = "2.2") -> Path:
    root = data_raw_dir / f"mimic-iv-demo-{version}"
    if not root.exists():
        raise FileNotFoundError(
            f"Raw demo folder not found: {root}\n"
            "Download it first via: python data/download_data.py --method python --out data/raw --version 2.2"
        )
    return root


def _to_datetime(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = pd.to_datetime(out[c], errors="coerce")
    return out


def _load_core_tables(paths: Paths) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    patients = pd.read_csv(paths.patients)
    admissions = pd.read_csv(paths.admissions)
    icu = pd.read_csv(paths.icustays)

    admissions = _to_datetime(admissions, ["admittime", "dischtime", "deathtime", "edregtime", "edouttime"])
    icu = _to_datetime(icu, ["intime", "outtime"])

    # Keep only columns we plan to use (pedagogical simplicity).
    patients = patients[["subject_id", "gender", "anchor_age"]].copy()
    admissions = admissions[
        [
            "subject_id",
            "hadm_id",
            "admittime",
            "dischtime",
            "deathtime",
            "admission_type",
            "race",
            "insurance",
            "hospital_expire_flag",
        ]
    ].copy()
    icu = icu[["subject_id", "hadm_id", "stay_id", "first_careunit", "intime", "outtime", "los"]].copy()

    return patients, admissions, icu


def _build_base_stay_cohort(paths: Paths) -> pd.DataFrame:
    patients, admissions, icu = _load_core_tables(paths)

    df = (
        icu.merge(admissions, on=["subject_id", "hadm_id"], how="left", validate="many_to_one")
        .merge(patients, on="subject_id", how="left", validate="many_to_one")
        .copy()
    )

    # Baseline covariates L (simple and available).
    df = df.rename(columns={"anchor_age": "age", "gender": "sex"})
    df["sex"] = df["sex"].astype(str)

    # Outcome Y (binary): in-hospital death indicator (simple, always available in admissions).
    df["Y"] = df["hospital_expire_flag"].astype(int)

    # Define time zero for ICU analyses (t0 = ICU intime).
    df["t0"] = df["intime"]

    return df


def _attach_exposure_admission_type(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    # MIMIC-IV Demo uses categories like "EW EMER." and "DIRECT EMER."
    adm = out["admission_type"].astype(str).str.upper()
    out["A"] = adm.str.contains("EMER", na=False).astype(int)
    out["A_label"] = "Admission type contains 'EMER' (1=yes)"
    return out


def _compute_mean_hr_first_hours(paths: Paths, stay_times: pd.DataFrame, hours: int = 6) -> pd.Series:
    # Heart Rate itemid (from d_items): 220045
    HR_ITEMID = 220045

    usecols = ["stay_id", "charttime", "itemid", "valuenum"]
    ce = pd.read_csv(paths.chartevents, usecols=usecols)
    ce = _to_datetime(ce, ["charttime"])

    ce = ce[(ce["itemid"] == HR_ITEMID) & ce["valuenum"].notna()].copy()

    st = stay_times[["stay_id", "intime"]].dropna().copy()
    st = st.rename(columns={"intime": "t0"})

    ce = ce.merge(st, on="stay_id", how="inner", validate="many_to_one")
    ce["dt_hours"] = (ce["charttime"] - ce["t0"]).dt.total_seconds() / 3600.0
    ce = ce[(ce["dt_hours"] >= 0) & (ce["dt_hours"] <= hours)].copy()

    hr = ce.groupby("stay_id")["valuenum"].mean()
    hr.name = "hr_mean_first6h"
    return hr


def _attach_exposure_vitals(df: pd.DataFrame, paths: Paths, hr_threshold: float = 100.0) -> pd.DataFrame:
    out = df.copy()
    hr = _compute_mean_hr_first_hours(paths, stay_times=out, hours=6)
    out = out.merge(hr.to_frame(), on="stay_id", how="left")
    out["A"] = (out["hr_mean_first6h"].fillna(out["hr_mean_first6h"].median()) > hr_threshold).astype(int)
    out["A_label"] = f"Mean HR first 6h > {hr_threshold:g} (1=yes)"
    return out


def build_cohort_L08_L09(
    paths: Paths,
    exposure_mode: ExposureMode = "admission_type",
    hr_threshold: float = 100.0,
) -> pd.DataFrame:
    df = _build_base_stay_cohort(paths)

    if exposure_mode == "admission_type":
        df = _attach_exposure_admission_type(df)
    else:
        df = _attach_exposure_vitals(df, paths=paths, hr_threshold=hr_threshold)

    # Keep a simple set of covariates for teaching.
    keep = [
        "subject_id",
        "hadm_id",
        "stay_id",
        "t0",
        "A",
        "Y",
        "age",
        "sex",
        "race",
        "insurance",
        "first_careunit",
        "los",
        "A_label",
    ]
    df = df[keep].copy()
    return df


def build_cohort_L10_survival(paths: Paths, exposure_mode: ExposureMode = "admission_type") -> pd.DataFrame:
    # Survival is defined at the hospital admission level for simplicity.
    patients, admissions, icu = _load_core_tables(paths)

    # One row per hospital admission (hadm_id). We attach baseline age/sex.
    df = admissions.merge(patients, on="subject_id", how="left", validate="many_to_one").copy()
    df = df.rename(columns={"anchor_age": "age", "gender": "sex"})
    df["sex"] = df["sex"].astype(str)

    # Exposure A (point exposure at baseline):
    # use "contains EMER" for robust support in Demo ("EW EMER.", "DIRECT EMER.", ...).
    adm = df["admission_type"].astype(str).str.upper()
    df["A"] = adm.str.contains("EMER", na=False).astype(int)

    # Outcome: in-hospital death, but treated as an event within follow-up.
    df["E"] = df["hospital_expire_flag"].astype(int)

    # Follow-up time in days (discrete). Administrative truncation at 28 days.
    dt = (df["dischtime"] - df["admittime"]).dt.total_seconds() / (24 * 3600)
    df["T"] = np.ceil(dt).clip(lower=0).fillna(0).astype(int)
    df["T"] = df["T"].clip(upper=28)

    # If E=1 but missing deathtime (rare), keep E=1 and use T as above.
    keep = ["subject_id", "hadm_id", "A", "E", "T", "age", "sex", "race", "insurance"]
    return df[keep].copy()


def build_cohort_L11_msm(paths: Paths, t_max: int = 7, hr_threshold: float = 100.0) -> pd.DataFrame:
    # Teaching MSM: build a simple person-day dataset from ICU stays using Heart Rate as time-varying covariate.
    base = _build_base_stay_cohort(paths)
    base = _attach_exposure_admission_type(base)  # baseline A (not the MSM A_t)

    # Time-varying covariate: daily mean HR from chartevents.
    HR_ITEMID = 220045
    usecols = ["stay_id", "charttime", "itemid", "valuenum"]
    ce = pd.read_csv(paths.chartevents, usecols=usecols)
    ce = _to_datetime(ce, ["charttime"])
    ce = ce[(ce["itemid"] == HR_ITEMID) & ce["valuenum"].notna()].copy()

    st = base[["stay_id", "intime", "outtime"]].dropna().copy()
    st = st.rename(columns={"intime": "t0", "outtime": "t_end"})
    ce = ce.merge(st, on="stay_id", how="inner", validate="many_to_one")

    ce["t_day"] = np.floor((ce["charttime"] - ce["t0"]).dt.total_seconds() / (24 * 3600)).astype(int)
    ce = ce[(ce["t_day"] >= 0) & (ce["t_day"] < t_max)].copy()

    hr_day = ce.groupby(["stay_id", "t_day"])["valuenum"].mean().reset_index()
    hr_day = hr_day.rename(columns={"valuenum": "hr_mean"})

    # Build person-day skeleton for each stay.
    idx = []
    for stay_id in base["stay_id"].dropna().unique():
        for t in range(t_max):
            idx.append((stay_id, t))
    skel = pd.DataFrame(idx, columns=["stay_id", "t_day"])

    long = skel.merge(hr_day, on=["stay_id", "t_day"], how="left")
    long = long.merge(
        base[["stay_id", "subject_id", "hadm_id", "age", "sex", "race", "insurance", "Y", "t0", "outtime"]],
        on="stay_id",
        how="left",
        validate="many_to_one",
    )

    # Simple time-varying “treatment”: indicator of high HR this day.
    # Pedagogical stand-in for a time-varying intervention decision rule.
    long["A_t"] = (long["hr_mean"].fillna(long["hr_mean"].median()) > hr_threshold).astype(int)

    # Censoring: after ICU outtime (no longer observed in ICU).
    outtime = pd.to_datetime(long["outtime"], errors="coerce")
    end_of_day = pd.to_datetime(long["t0"], errors="coerce") + pd.to_timedelta(long["t_day"] + 1, unit="D")
    long["C_t"] = ((outtime.notna()) & (end_of_day > outtime)).astype(int)

    # Keep only observed person-days (before censoring).
    long = long[long["C_t"] == 0].copy()

    # Required columns for teaching MSM scaffolding
    keep = ["subject_id", "hadm_id", "stay_id", "t_day", "A_t", "hr_mean", "age", "sex", "Y"]
    return long[keep].copy()


def build_processed_extracts(
    repo_root: Optional[Path] = None,
    exposure_mode: ExposureMode = "admission_type",
    hr_threshold: float = 100.0,
    t_max: int = 7,
    version: str = "2.2",
    write_parquet: Optional[bool] = None,
) -> dict[str, Path]:
    """Build and write all processed cohort extracts for L08–L11.

    Returns a dict mapping cohort name -> output path.
    """
    if repo_root is None:
        # assume this file lives in <repo>/data/
        repo_root = Path(__file__).resolve().parents[1]

    data_dir = repo_root / "data"
    raw_dir = data_dir / "raw"
    processed_dir = data_dir / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    demo_root = _find_demo_root(raw_dir, version=version)
    paths = Paths(raw_root=demo_root, processed_root=processed_dir)

    out: dict[str, Path] = {}

    if write_parquet is None:
        # Auto-detect parquet support; fall back to CSV to keep Colab friction low.
        try:
            import pyarrow  # noqa: F401

            write_parquet = True
        except Exception:
            write_parquet = False

    df_0809 = build_cohort_L08_L09(paths, exposure_mode=exposure_mode, hr_threshold=hr_threshold)

    for lec, fname in [("L08", "cohort_L08_ps_ipw"), ("L09", "cohort_L09_gformula")]:
        p = processed_dir / f"{fname}.parquet"
        if write_parquet:
            df_0809.to_parquet(p, index=False)
        else:
            p = processed_dir / f"{fname}.csv"
            df_0809.to_csv(p, index=False)
        out[lec] = p

    df10 = build_cohort_L10_survival(paths, exposure_mode=exposure_mode)
    p10 = processed_dir / ("cohort_L10_survival.parquet" if write_parquet else "cohort_L10_survival.csv")
    (df10.to_parquet(p10, index=False) if write_parquet else df10.to_csv(p10, index=False))
    out["L10"] = p10

    df11 = build_cohort_L11_msm(paths, t_max=t_max, hr_threshold=hr_threshold)
    p11 = processed_dir / ("cohort_L11_msm_longitudinal.parquet" if write_parquet else "cohort_L11_msm_longitudinal.csv")
    (df11.to_parquet(p11, index=False) if write_parquet else df11.to_csv(p11, index=False))
    out["L11"] = p11

    return out


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exposure-mode", choices=["admission_type", "vitals"], default="admission_type")
    parser.add_argument("--hr-threshold", type=float, default=100.0)
    parser.add_argument("--t-max", type=int, default=7)
    parser.add_argument("--version", default="2.2")
    parser.add_argument("--csv", action="store_true", help="Write CSV instead of Parquet.")
    args = parser.parse_args(argv)

    out = build_processed_extracts(
        exposure_mode=args.exposure_mode,
        hr_threshold=args.hr_threshold,
        t_max=args.t_max,
        version=args.version,
        write_parquet=(False if args.csv else None),
    )
    for k, v in out.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

