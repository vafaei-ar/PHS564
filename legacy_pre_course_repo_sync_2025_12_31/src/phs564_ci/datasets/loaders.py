import pandas as pd
import os
from pathlib import Path

def get_data_dir():
    """Returns the absolute path to the data directory."""
    # This assumes the package is installed in editable mode or 
    # the script is running from the repo root.
    # For a more robust approach in a real package, we'd use importlib.resources
    # But for this course repo, we'll keep it simple.
    
    # Try to find the root by looking for pyproject.toml
    current_path = Path(os.getcwd())
    for parent in [current_path] + list(current_path.parents):
        if (parent / "pyproject.toml").exists():
            data_dir = parent / "data"
            if data_dir.exists():
                return data_dir
    
    # Fallback to current directory / data
    return Path("./data")

def load_data(filename):
    """Loads a CSV file from the central data directory."""
    data_path = get_data_dir() / filename
    if not data_path.exists():
        raise FileNotFoundError(f"Data file {filename} not found in {get_data_dir()}")
    return pd.read_csv(data_path)

def load_nhefs():
    """Loads the NHEFS smoking cessation dataset."""
    return load_data("nhefs.csv")

