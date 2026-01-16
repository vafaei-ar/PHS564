"""
Survival analysis utilities for causal inference.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
import statsmodels.api as sm
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.genmod import families


def make_person_period(
    df: pd.DataFrame, id_col: str, time_col: str, event_col: str, t_max: int
) -> pd.DataFrame:
    """
    Convert survival data to person-period (discrete-time) format.

    Parameters
    ----------
    df : pd.DataFrame
        Wide-format survival data with one row per person.
    id_col : str
        Person ID column name.
    time_col : str
        Follow-up time column name.
    event_col : str
        Event indicator column name (1 = event, 0 = censored).
    t_max : int
        Maximum follow-up time.

    Returns
    -------
    pd.DataFrame
        Long-format person-period data with one row per person-period.
    """
    periods = []

    for _, row in df.iterrows():
        person_id = row[id_col]
        follow_time = int(row[time_col])
        event = row[event_col]

        # Create one row for each time period up to follow_time or t_max
        max_t = min(follow_time, t_max)

        for t in range(1, max_t + 1):
            # Event occurs at the last period if event=1
            event_t = 1 if (t == follow_time and event == 1) else 0

            period_row = row.copy()
            period_row["t"] = t
            period_row["E_t"] = event_t
            periods.append(period_row)

    return pd.DataFrame(periods)


def fit_hazard_model(
    df_long: pd.DataFrame, treatment: str, covariates: List[str], time_var: str = "t"
) -> object:
    """
    Fit pooled logistic regression model for discrete-time hazards.

    Parameters
    ----------
    df_long : pd.DataFrame
        Person-period dataset.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    time_var : str, default "t"
        Time period column name.

    Returns
    -------
    object
        Fitted GLM model.
    """
    y = df_long["E_t"].values
    X_vars = [treatment, time_var] + covariates
    X = df_long[X_vars].values
    X = sm.add_constant(X)

    model = GLM(y, X, family=families.Binomial())
    fitted = model.fit()

    return fitted


def predict_survival_curve(
    hazard_model: object,
    df_long: pd.DataFrame,
    treatment: str,
    covariates: List[str],
    treatment_value: int,
    t_max: int,
    time_var: str = "t",
    id_col: Optional[str] = None,
) -> np.ndarray:
    """
    Predict survival curve under a specific treatment value.

    Parameters
    ----------
    hazard_model : object
        Fitted hazard model.
    df_long : pd.DataFrame
        Person-period dataset.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    treatment_value : int
        Treatment value to predict under.
    t_max : int
        Maximum follow-up time.
    time_var : str, default "t"
        Time period column name.

    Returns
    -------
    np.ndarray
        Survival probabilities at each time point.

    Scientific note
    --------------
    This implements a teaching version of the **g-formula for discrete-time hazards**:
    we average predicted hazards across individuals at each time, then form
    S(t) = ∏_{k≤t} (1 - h(k)).
    """
    # Get one row per individual for standardization
    if id_col is None:
        # Best-effort defaults for this course repo
        if "hadm_id" in df_long.columns:
            id_col = "hadm_id"
        elif "stay_id" in df_long.columns:
            id_col = "stay_id"
        else:
            raise ValueError(
                "id_col is required unless df_long contains a recognizable identifier "
                "column (e.g., 'hadm_id' or 'stay_id')."
            )

    unique_ids = df_long.drop_duplicates(subset=[id_col]).copy()

    survival_curve = np.ones(t_max + 1)  # S(0) = 1

    for t in range(1, t_max + 1):
        # Create counterfactual dataset for time t
        df_t = unique_ids.copy()
        df_t[treatment] = treatment_value
        df_t[time_var] = t

        # Predict hazards for all individuals at time t
        X_vars = [treatment, time_var] + covariates
        X_t = df_t[X_vars].values
        X_t = sm.add_constant(X_t)

        hazards_t = hazard_model.predict(X_t)

        # Average hazard across individuals
        mean_hazard_t = np.mean(hazards_t)

        # Update survival: S(t) = S(t-1) * (1 - h(t))
        survival_curve[t] = survival_curve[t - 1] * (1 - mean_hazard_t)

    return survival_curve
