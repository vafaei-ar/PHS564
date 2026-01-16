"""
Diagnostic utilities for causal inference: overlap, weights, balance checks.
"""

import numpy as np
import pandas as pd
from typing import List, Optional, Tuple


def compute_smd(treated: np.ndarray, control: np.ndarray) -> float:
    """
    Compute standardized mean difference (SMD) between two groups.

    Parameters
    ----------
    treated : array-like
        Values for treated group.
    control : array-like
        Values for control group.

    Returns
    -------
    float
        Standardized mean difference.
    """
    mean_t = np.mean(treated)
    mean_c = np.mean(control)
    var_t = np.var(treated, ddof=1)
    var_c = np.var(control, ddof=1)
    pooled_std = np.sqrt((var_t + var_c) / 2)

    if pooled_std == 0:
        return 0.0

    return (mean_t - mean_c) / pooled_std


def love_plot_data(
    df: pd.DataFrame, treatment: str, covariates: List[str], weights: Optional[np.ndarray] = None
) -> pd.DataFrame:
    """
    Prepare data for a Love plot (balance before/after weighting).

    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    weights : array-like, optional
        IP weights. If provided, computes weighted SMDs.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: covariate, smd_before, smd_after (if weights provided).
    """
    treated = df[df[treatment] == 1]
    control = df[df[treatment] == 0]

    results = []
    for covar in covariates:
        smd_before = compute_smd(treated[covar].values, control[covar].values)

        if weights is not None:
            # Weighted means
            treated_weighted = df[df[treatment] == 1][covar].values
            control_weighted = df[df[treatment] == 0][covar].values
            weights_t = weights[df[treatment] == 1]
            weights_c = weights[df[treatment] == 0]

            mean_t_w = np.average(treated_weighted, weights=weights_t)
            mean_c_w = np.average(control_weighted, weights=weights_c)

            # Weighted variance (simplified)
            var_t_w = np.average((treated_weighted - mean_t_w) ** 2, weights=weights_t)
            var_c_w = np.average((control_weighted - mean_c_w) ** 2, weights=weights_c)
            pooled_std_w = np.sqrt((var_t_w + var_c_w) / 2)

            if pooled_std_w > 0:
                smd_after = (mean_t_w - mean_c_w) / pooled_std_w
            else:
                smd_after = 0.0
        else:
            smd_after = None

        results.append(
            {
                "covariate": covar,
                "smd_before": smd_before,
                "smd_after": smd_after if weights is not None else None,
            }
        )

    return pd.DataFrame(results)


def check_positivity(
    ps: np.ndarray, threshold_min: float = 0.01, threshold_max: float = 0.99
) -> Tuple[bool, int]:
    """
    Check positivity assumption by counting extreme propensity scores.

    Parameters
    ----------
    ps : array-like
        Propensity scores.
    threshold_min : float, default 0.01
        Minimum acceptable propensity score.
    threshold_max : float, default 0.99
        Maximum acceptable propensity score.

    Returns
    -------
    tuple
        (violation_exists, n_violations)
    """
    violations = (ps < threshold_min) | (ps > threshold_max)
    n_violations = np.sum(violations)
    return n_violations > 0, n_violations


def summarize_weights(weights: np.ndarray) -> dict:
    """
    Summarize IP weight distribution.

    Parameters
    ----------
    weights : array-like
        IP weights.

    Returns
    -------
    dict
        Summary statistics: mean, median, min, max, p1, p99.
    """
    return {
        "mean": float(np.mean(weights)),
        "median": float(np.median(weights)),
        "min": float(np.min(weights)),
        "max": float(np.max(weights)),
        "p1": float(np.percentile(weights, 1)),
        "p99": float(np.percentile(weights, 99)),
    }
