"""
I/O utilities for loading cohort extracts and managing paths.
"""

from pathlib import Path
from typing import Optional
import pandas as pd


def find_repo_root(start_path: Optional[Path] = None) -> Path:
    """
    Find the repository root by walking up from start_path until finding README.md or requirements.txt.

    Parameters
    ----------
    start_path : Path, optional
        Starting directory. Defaults to current working directory.

    Returns
    -------
    Path
        Repository root directory.

    Raises
    ------
    FileNotFoundError
        If repository root cannot be found.
    """
    if start_path is None:
        start_path = Path.cwd()

    current = Path(start_path).resolve()
    for _ in range(10):  # Limit search depth
        if (current / "README.md").exists() or (current / "requirements.txt").exists():
            return current
        if current.parent == current:  # Reached filesystem root
            break
        current = current.parent

    raise FileNotFoundError("Could not find repository root (README.md or requirements.txt)")


def get_data_dir(repo_root: Optional[Path] = None) -> Path:
    """
    Get the data directory path.

    Parameters
    ----------
    repo_root : Path, optional
        Repository root. If None, will be found automatically.

    Returns
    -------
    Path
        Path to data/ directory.
    """
    if repo_root is None:
        repo_root = find_repo_root()
    return repo_root / "data"


def get_processed_dir(repo_root: Optional[Path] = None) -> Path:
    """
    Get the processed data directory path.

    Parameters
    ----------
    repo_root : Path, optional
        Repository root. If None, will be found automatically.

    Returns
    -------
    Path
        Path to data/processed/ directory.
    """
    return get_data_dir(repo_root) / "processed"


def load_cohort_extract(
    lecture: str, repo_root: Optional[Path] = None, prefer_parquet: bool = True
) -> pd.DataFrame:
    """
    Load a cohort extract for a specific lecture.

    Parameters
    ----------
    lecture : str
        Lecture identifier (e.g., "L08", "L10").
    repo_root : Path, optional
        Repository root. If None, will be found automatically.
    prefer_parquet : bool, default True
        If True, try Parquet first, then CSV. If False, try CSV first.

    Returns
    -------
    pd.DataFrame
        Loaded cohort extract.

    Raises
    ------
    FileNotFoundError
        If neither Parquet nor CSV file is found.
    """
    processed_dir = get_processed_dir(repo_root)

    # Map lecture to expected filename
    filename_map = {
        "L08": "cohort_L08_ps_ipw",
        "L09": "cohort_L09_gformula",
        "L10": "cohort_L10_survival",
        "L11": "cohort_L11_msm_longitudinal",
        "L12": "cohort_L12_capstone",
        "L13": "cohort_L13_workshop",
    }

    base_name = filename_map.get(lecture, f"cohort_{lecture}")

    if prefer_parquet:
        parquet_path = processed_dir / f"{base_name}.parquet"
        csv_path = processed_dir / f"{base_name}.csv"

        if parquet_path.exists():
            return pd.read_parquet(parquet_path)
        elif csv_path.exists():
            return pd.read_csv(csv_path)
    else:
        csv_path = processed_dir / f"{base_name}.csv"
        parquet_path = processed_dir / f"{base_name}.parquet"

        if csv_path.exists():
            return pd.read_csv(csv_path)
        elif parquet_path.exists():
            return pd.read_parquet(parquet_path)

    raise FileNotFoundError(
        f"Could not find cohort extract for {lecture}. "
        f"Expected files: {processed_dir / f'{base_name}.parquet'} or "
        f"{processed_dir / f'{base_name}.csv'}. "
        f"Run: python data/build_processed_extracts_demo.py"
    )
