"""
G-formula / Standardization utilities.
"""

import numpy as np
import pandas as pd
from typing import List, Optional
import statsmodels.api as sm
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.genmod import families


def fit_outcome_model(
    df: pd.DataFrame,
    outcome: str,
    treatment: str,
    covariates: List[str],
    family: str = "gaussian"
) -> object:
    """
    Fit outcome regression model E[Y|A,L].
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    outcome : str
        Outcome column name.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    family : str, default "gaussian"
        Model family: "gaussian" (linear) or "binomial" (logistic).
    
    Returns
    -------
    object
        Fitted model.
    """
    y = df[outcome].values
    X = df[[treatment] + covariates].values
    X = sm.add_constant(X)
    
    if family == "binomial":
        model = GLM(y, X, family=families.Binomial())
    else:
        model = sm.OLS(y, X)
    
    fitted = model.fit()
    return fitted


def standardize(
    df: pd.DataFrame,
    outcome_model: object,
    treatment: str,
    covariates: List[str],
    treatment_value: int = 1
) -> float:
    """
    Compute standardized mean under a specific treatment value.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    outcome_model : object
        Fitted outcome regression model.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    treatment_value : int, default 1
        Treatment value to standardize to.
    
    Returns
    -------
    float
        Standardized mean outcome.
    """
    # Create counterfactual dataset with A = treatment_value
    df_cf = df.copy()
    df_cf[treatment] = treatment_value
    
    # Predict outcomes
    X_cf = df_cf[[treatment] + covariates].values
    X_cf = sm.add_constant(X_cf)
    
    if hasattr(outcome_model, "predict"):
        predictions = outcome_model.predict(X_cf)
    else:
        # For GLM
        predictions = outcome_model.fittedvalues
    
    # Average over all individuals
    standardized_mean = np.mean(predictions)
    
    return standardized_mean


def gformula_effect(
    df: pd.DataFrame,
    outcome: str,
    treatment: str,
    covariates: List[str],
    family: str = "gaussian"
) -> dict:
    """
    Compute causal effect using g-formula/standardization.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset.
    outcome : str
        Outcome column name.
    treatment : str
        Treatment column name.
    covariates : list of str
        Covariate column names.
    family : str, default "gaussian"
        Model family: "gaussian" or "binomial".
    
    Returns
    -------
    dict
        Dictionary with keys: effect, mean_treated, mean_control, model
    """
    # Fit outcome model
    model = fit_outcome_model(df, outcome, treatment, covariates, family)
    
    # Standardize to A=1
    mean_treated = standardize(df, model, treatment, covariates, treatment_value=1)
    
    # Standardize to A=0
    mean_control = standardize(df, model, treatment, covariates, treatment_value=0)
    
    # Causal effect
    effect = mean_treated - mean_control
    
    return {
        "effect": effect,
        "mean_treated": mean_treated,
        "mean_control": mean_control,
        "model": model
    }
