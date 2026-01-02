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
from typing import Optional, Sequence
from urllib.request import urlopen

BASE_URL = "https://physionet.org/files/mimic-iv-demo/{version}/"


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
    out_dir: str | Path = "data/raw",
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


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", choices=["wget", "python"], default="wget")
    parser.add_argument("--version", default="2.2", help="MIMIC-IV Demo version on PhysioNet (default: 2.2)")
    parser.add_argument("--out", default="data/raw", help="Output directory (default: data/raw)")
    args = parser.parse_args(argv)

    out_dir = Path(args.out).resolve()

    if args.method == "wget":
        download_with_wget(args.version, out_dir)
    else:
        download_with_python(args.version, out_dir, COURSE_MANIFEST)

    print("\nNext step (recommended): build an SQLite DB from the CSVs for faster querying.")
    print("We provide a separate script in later lectures to build sqlite + derived cohorts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
