"""
Marginal Structural Model (MSM) utilities for time-varying treatments.

Scientific note
--------------
These helpers are intended for **teaching and prototyping**. They implement a
standard workflow for **stabilized inverse probability of treatment weights**
in a person-period (long) dataset.

If you are producing publishable results, you should:
- justify numerator/denominator models carefully,
- handle censoring/competing risks as appropriate,
- use robust variance / bootstrap,
- and validate assumptions/diagnostics thoroughly.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.genmod import families


def compute_msm_weights(
    df_long: pd.DataFrame,
    id_col: str,
    time_col: str,
    treatment: str,
    covariates_time_varying: List[str],
    covariates_baseline: List[str],
    censoring: Optional[str] = None
) -> Tuple[pd.DataFrame, dict]:
    """
    Compute stabilized weights for MSM (treatment weights and optionally censoring weights).
    
    Parameters
    ----------
    df_long : pd.DataFrame
        Person-period dataset.
    id_col : str
        Person ID column name.
    time_col : str
        Time period column name.
    treatment : str
        Time-varying treatment column name.
    covariates_time_varying : list of str
        Time-varying covariate column names.
    covariates_baseline : list of str
        Baseline covariate column names.
    censoring : str, optional
        Censoring indicator column name (1 = censored). If None, no censoring weights.
    
    Returns
    -------
    tuple
        (df_with_weights, weight_info)
        df_with_weights includes columns: wA (treatment weights), wC (censoring weights, if applicable), W (combined)
    """
    if censoring is not None:
        raise NotImplementedError(
            "Censoring weights are not implemented in this teaching helper yet. "
            "For L11, focus on treatment weights wA/W_A unless you explicitly model censoring."
        )

    df = df_long.copy().sort_values([id_col, time_col]).reset_index(drop=True)

    # Add lagged treatment to capture treatment history (minimal feature for time-varying A_t)
    df["_A_lag1"] = df.groupby(id_col)[treatment].shift(1).fillna(0).astype(int)

    # Denominator model: P(A_t = 1 | L0, L_t, A_{t-1}, t)
    denom_covars = covariates_baseline + covariates_time_varying + ["_A_lag1", time_col]
    X_denom = sm.add_constant(df[denom_covars], has_constant="add")
    y = df[treatment].astype(int).values
    denom_fit = GLM(y, X_denom, family=families.Binomial()).fit()

    # Numerator model (stabilization): P(A_t = 1 | L0, A_{t-1}, t)
    num_covars = covariates_baseline + ["_A_lag1", time_col]
    X_num = sm.add_constant(df[num_covars], has_constant="add")
    num_fit = GLM(y, X_num, family=families.Binomial()).fit()

    p_denom = np.clip(denom_fit.predict(X_denom), 1e-6, 1 - 1e-6)
    p_num = np.clip(num_fit.predict(X_num), 1e-6, 1 - 1e-6)

    A = df[treatment].astype(int).values
    # Period-specific stabilized weight contribution
    wA = np.where(A == 1, p_num / p_denom, (1 - p_num) / (1 - p_denom))

    df["pA_denom"] = p_denom
    df["pA_num"] = p_num
    df["wA"] = wA

    # Cumulative treatment weight per person: W_A(t) = ∏_{k<=t} wA_k
    df["W_A"] = df.groupby(id_col)["wA"].cumprod()
    df["W"] = df["W_A"]
    df["wC"] = 1.0

    weight_info = {
        "mean_wA": float(np.mean(wA)),
        "median_wA": float(np.median(wA)),
        "min_wA": float(np.min(wA)),
        "max_wA": float(np.max(wA)),
        "mean_W_A": float(df["W_A"].mean()),
        "median_W_A": float(df["W_A"].median()),
        "min_W_A": float(df["W_A"].min()),
        "max_W_A": float(df["W_A"].max()),
    }

    # Clean internal column
    df = df.drop(columns=["_A_lag1"])
    return df, weight_info


def fit_msm(
    df_long: pd.DataFrame,
    outcome: str,
    treatment: str,
    weights: np.ndarray,
    time_col: str = "t"
) -> object:
    """
    Fit a marginal structural model (weighted pooled logistic/GLM).
    
    Parameters
    ----------
    df_long : pd.DataFrame
        Person-period dataset.
    outcome : str
        Outcome column name.
    treatment : str
        Treatment column name.
    weights : array-like
        MSM weights.
    time_col : str, default "t"
        Time period column name.
    
    Returns
    -------
    object
        Fitted weighted model.
    """
    y = df_long[outcome].values
    X = df_long[[treatment, time_col]].values
    X = sm.add_constant(X)
    
    # Weighted GLM
    model = GLM(y, X, family=families.Binomial(), freq_weights=weights)
    fitted = model.fit()
    
    return fitted
