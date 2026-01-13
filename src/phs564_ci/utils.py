"""
General utility functions.
"""

import numpy as np
import pandas as pd
from typing import Optional, Callable
from scipy import stats


def bootstrap_ci(
    data: np.ndarray,
    statistic: Callable,
    n_bootstrap: int = 1000,
    confidence: float = 0.95,
    random_state: Optional[int] = None
) -> tuple:
    """
    Compute bootstrap confidence interval for a statistic.
    
    Parameters
    ----------
    data : array-like
        Original data.
    statistic : callable
        Function that computes the statistic from data.
    n_bootstrap : int, default 1000
        Number of bootstrap replicates.
    confidence : float, default 0.95
        Confidence level.
    random_state : int, optional
        Random seed.
    
    Returns
    -------
    tuple
        (point_estimate, lower_bound, upper_bound, bootstrap_distribution)
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    n = len(data)
    bootstrap_stats = []
    
    for _ in range(n_bootstrap):
        # Resample with replacement
        bootstrap_sample = np.random.choice(data, size=n, replace=True)
        stat = statistic(bootstrap_sample)
        bootstrap_stats.append(stat)
    
    bootstrap_stats = np.array(bootstrap_stats)
    
    # Point estimate from original data
    point_estimate = statistic(data)
    
    # Percentile-based CI
    alpha = 1 - confidence
    lower_bound = np.percentile(bootstrap_stats, 100 * alpha / 2)
    upper_bound = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))
    
    return point_estimate, lower_bound, upper_bound, bootstrap_stats


def set_seed(seed: int = 564) -> None:
    """
    Set random seed for reproducibility.
    
    Parameters
    ----------
    seed : int, default 564
        Random seed.
    """
    np.random.seed(seed)
    import random
    random.seed(seed)
