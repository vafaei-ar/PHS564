"""Download MIMIC-IV Demo (open access) and place it under data/raw/.

Design goals for this course:
  - Zero credentialing dependency for *homeworks*.
  - Everything should run in Google Colab or on a standard laptop.
  - Keep the toolchain simple and explicit.

Supported methods:
  (A) wget (recommended; fastest, preserves folder structure)
  (B) pure-Python downloader (downloads a small manifest of tables needed for the course)

Notes:
  - MIMIC-IV Demo is distributed by PhysioNet and is covered by the Open Data Commons ODbL.
  - Do NOT commit downloaded data to GitHub.
  - For full MIMIC-IV (credentialed), follow PhysioNet policies and never upload data to third-party services.

Usage:
  python data/download_data.py --method wget --out data/raw --version 2.2
  python data/download_data.py --method python --out data/raw --version 2.2
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence, Union
from urllib.request import urlopen

BASE_URL = "https://physionet.org/files/mimic-iv-demo/{version}/"

# Processed cohort extracts are distributed via GitHub Releases (public) so
# students can run L08–L11 without any local Python setup or credentialing.
GITHUB_OWNER = "vafaei-ar"
GITHUB_REPO = "PHS564"
DEFAULT_EXTRACTS_TAG = "cohort-extracts-v1"

# Canonical processed extracts expected by lecture notebooks (Parquet preferred).
EXTRACTS_BY_LECTURE = {
    "L08": "cohort_L08_ps_ipw.parquet",
    "L09": "cohort_L09_gformula.parquet",
    "L10": "cohort_L10_survival.parquet",
    "L11": "cohort_L11_msm_longitudinal.parquet",
    # Optional (if you publish an asset for it)
    "L12": "cohort_L12_capstone.parquet",
}


@dataclass(frozen=True)
class FileSpec:
    relpath: str
    sha256: Optional[str] = None  # optional integrity check


# Minimal manifest for course use (expand later if needed).
# Kept intentionally small to reduce friction.
COURSE_MANIFEST: Sequence[FileSpec] = (
    # hosp
    FileSpec("hosp/admissions.csv.gz"),
    FileSpec("hosp/patients.csv.gz"),
    FileSpec("hosp/diagnoses_icd.csv.gz"),
    FileSpec("hosp/d_icd_diagnoses.csv.gz"),
    # icu
    FileSpec("icu/icustays.csv.gz"),
    FileSpec("icu/d_items.csv.gz"),
    FileSpec("icu/chartevents.csv.gz"),
)


def _which(cmd: str) -> Optional[str]:
    return shutil.which(cmd)


def _run(cmd: Sequence[str]) -> None:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n\n{proc.stdout}")
    print(proc.stdout)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download_with_wget(version: str, out_dir: Path) -> None:
    if _which("wget") is None:
        raise RuntimeError("wget not found. Install wget or use --method python.")
    url = BASE_URL.format(version=version)
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = ["wget", "-r", "-N", "-c", "-np", url, "-P", str(out_dir)]
    print("Running:", " ".join(cmd))
    _run(cmd)
    print(f"Downloaded MIMIC-IV Demo v{version} into: {out_dir}")


def _download_one(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as r, dest.open("wb") as w:
        shutil.copyfileobj(r, w)


def download_with_python(version: str, out_dir: Path, manifest: Sequence[FileSpec]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    base = BASE_URL.format(version=version)
    for spec in manifest:
        url = base + spec.relpath
        dest = out_dir / f"mimic-iv-demo-{version}" / spec.relpath
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[skip] {dest}")
            continue
        print(f"[get ] {url}")
        _download_one(url, dest)

        if spec.sha256 is not None:
            got = _sha256(dest)
            if got.lower() != spec.sha256.lower():
                raise RuntimeError(f"SHA256 mismatch for {dest}: expected {spec.sha256}, got {got}")

    print(f"Downloaded manifest ({len(manifest)} files) into: {out_dir}")


def download_mimic_demo(
    out_dir: Union[str, Path] = "data/raw",
    version: str = "2.2",
    method: str = "python"
) -> None:
    """Download MIMIC-IV Demo data (Colab-friendly function).
    
    This function can be called directly from notebooks in Google Colab.
    It uses pure Python (no wget dependency) for maximum compatibility.
    
    Args:
        out_dir: Output directory (default: "data/raw")
        version: MIMIC-IV Demo version (default: "2.2")
        method: Download method, "python" or "wget" (default: "python")
    
    Example (in a notebook):
        from pathlib import Path
        import sys
        sys.path.insert(0, str(Path.cwd().parent.parent))
        from data.download_data import download_mimic_demo
        
        download_mimic_demo()  # Downloads to data/raw/
    """
    out_path = Path(out_dir).resolve()
    
    if method == "wget":
        download_with_wget(version, out_path)
    else:
        download_with_python(version, out_path, COURSE_MANIFEST)
    
    print(f"\n✓ MIMIC-IV Demo v{version} downloaded to: {out_path}")


def _download_url(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as r, dest.open("wb") as w:
        shutil.copyfileobj(r, w)


def download_course_extracts(
    lecture: str,
    out_dir: Union[str, Path] = "data/processed",
    tag: str = DEFAULT_EXTRACTS_TAG,
    overwrite: bool = False,
) -> Path:
    """Download the processed cohort extract for a lecture into data/processed/.

    These are the *analysis-ready* cohort files used in L08–L11.

    The files are expected to be hosted as assets in a GitHub Release:
      https://github.com/{owner}/{repo}/releases/tag/{tag}

    Args:
        lecture: Lecture code, e.g. "L08", "L09", "L10", "L11".
        out_dir: Output directory (default: data/processed).
        tag: Release tag name (default: cohort-extracts-v1).
        overwrite: Re-download even if the file exists.

    Returns:
        Path to the downloaded (or existing) file.
    """
    lec = lecture.strip().upper()
    if lec not in EXTRACTS_BY_LECTURE:
        raise ValueError(
            f"Unknown lecture '{lecture}'. Expected one of: {', '.join(sorted(EXTRACTS_BY_LECTURE))}"
        )

    out_path = Path(out_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    filename = EXTRACTS_BY_LECTURE[lec]
    dest = out_path / filename
    if dest.exists() and dest.stat().st_size > 0 and not overwrite:
        print(f"✓ Extract already present: {dest}")
        return dest

    url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/releases/download/{tag}/{filename}"
    print(f"Downloading {lec} processed cohort extract from GitHub Releases:")
    print(url)
    try:
        _download_url(url, dest)
    except Exception as e:
        raise RuntimeError(
            "Failed to download the processed cohort extract.\n"
            f"- Lecture: {lec}\n"
            f"- Expected release tag: {tag}\n"
            f"- Expected asset name: {filename}\n"
            f"- URL: {url}\n\n"
            "Fix:\n"
            "- Ensure the GitHub Release exists and includes the asset with the exact filename.\n"
            "- Or pass a different --tag.\n\n"
            f"Original error: {e}"
        ) from e

    if not dest.exists() or dest.stat().st_size == 0:
        raise RuntimeError(f"Downloaded file is missing/empty: {dest}")

    print(f"✓ Downloaded: {dest}")
    return dest


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lecture",
        choices=sorted(EXTRACTS_BY_LECTURE.keys()),
        help="Download processed cohort extract for a lecture into --out (default: data/processed).",
    )
    parser.add_argument(
        "--tag",
        default=DEFAULT_EXTRACTS_TAG,
        help=f"GitHub Release tag for processed extracts (default: {DEFAULT_EXTRACTS_TAG})",
    )
    parser.add_argument("--overwrite", action="store_true", help="Re-download even if the output file exists.")

    parser.add_argument("--method", choices=["wget", "python"], default="wget", help="Raw MIMIC-IV Demo download method.")
    parser.add_argument("--version", default="2.2", help="MIMIC-IV Demo version on PhysioNet (default: 2.2)")
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory. Default: data/processed when --lecture is set, otherwise data/raw.",
    )
    args = parser.parse_args(argv)

    out_default = "data/processed" if args.lecture else "data/raw"
    out_dir = Path(args.out or out_default).resolve()

    if args.lecture:
        download_course_extracts(args.lecture, out_dir=out_dir, tag=args.tag, overwrite=args.overwrite)
        return 0

    if args.method == "wget":
        download_with_wget(args.version, out_dir)
    else:
        download_with_python(args.version, out_dir, COURSE_MANIFEST)

    print("\nNext step (recommended): build an SQLite DB from the CSVs for faster querying.")
    print("We provide a separate script in later lectures to build sqlite + derived cohorts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
