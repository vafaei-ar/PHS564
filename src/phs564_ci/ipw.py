"""
Inverse Probability Weighting (IPW) utilities.
"""

import numpy as np
import pandas as pd
from typing import Optional, Tuple
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm


def compute_ipw_weights(
    df: pd.DataFrame,
    treatment: str,
    covariates: list,
    stabilized: bool = True,
    ps_model: Optional[object] = None
) -> Tuple[np.ndarray, np.ndarray, object]:
    """
    Compute IPW weights from propensity scores.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names for propensity score model.
    stabilized : bool, default True
        If True, compute stabilized weights.
    ps_model : object, optional
        Fitted propensity score model. If None, fits a logistic regression.
    
    Returns
    -------
    tuple
        (weights, propensity_scores, fitted_model)
    """
    A = df[treatment].values
    X = df[covariates].values
    
    # Fit propensity score model if not provided
    if ps_model is None:
        ps_model = LogisticRegression(max_iter=1000, random_state=564)
        ps_model.fit(X, A)
    
    # Predict propensity scores
    ps = ps_model.predict_proba(X)[:, 1]
    
    # Compute weights
    if stabilized:
        # Stabilized weights: f(A) / f(A|L)
        # f(A) = marginal probability of observed treatment
        p_a = np.mean(A)
        weights = np.where(A == 1, p_a / ps, (1 - p_a) / (1 - ps))
    else:
        # Unstabilized weights: 1 / f(A|L)
        weights = np.where(A == 1, 1 / ps, 1 / (1 - ps))
    
    return weights, ps, ps_model


def truncate_weights(
    weights: np.ndarray,
    lower: float = 0.01,
    upper: float = 0.99
) -> np.ndarray:
    """
    Truncate weights at specified percentiles.
    
    Parameters
    ----------
    weights : array-like
        IP weights.
    lower : float, default 0.01
        Lower percentile for truncation.
    upper : float, default 0.99
        Upper percentile for truncation.
    
    Returns
    -------
    np.ndarray
        Truncated weights.
    """
    lower_bound = np.percentile(weights, lower * 100)
    upper_bound = np.percentile(weights, upper * 100)
    return np.clip(weights, lower_bound, upper_bound)


def weighted_mean_difference(
    df: pd.DataFrame,
    treatment: str,
    outcome: str,
    weights: np.ndarray
) -> Tuple[float, float]:
    """
    Compute weighted mean difference (causal effect estimate).
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    treatment : str
        Treatment column name.
    outcome : str
        Outcome column name.
    weights : array-like
        IP weights.
    
    Returns
    -------
    tuple
        (effect_estimate, se)

    Scientific note
    --------------
    The returned standard error is a **naïve** (unweighted, model-free) approximation
    and is **not** a valid uncertainty estimate for IPW in general.
    For teaching and basic diagnostics, the point estimate is the main output.
    For inference, prefer a bootstrap or a robust/sandwich variance appropriate to
    the full estimation procedure.
    """
    treated = df[df[treatment] == 1]
    control = df[df[treatment] == 0]
    weights_t = weights[df[treatment] == 1]
    weights_c = weights[df[treatment] == 0]
    
    mean_t = np.average(treated[outcome].values, weights=weights_t)
    mean_c = np.average(control[outcome].values, weights=weights_c)
    
    effect = mean_t - mean_c
    
    # Naïve SE (does not account for weighting or PS estimation)
    se = np.sqrt(
        np.var(treated[outcome].values) / len(treated) +
        np.var(control[outcome].values) / len(control)
    )
    
    return effect, se
