import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.iv import IV2SLS

def wald_estimator(data, outcome, exposure, instrument):
    """
    Calculates the Wald Estimator for a binary instrument.
    (E[Y|Z=1] - E[Y|Z=0]) / (E[A|Z=1] - E[A|Z=0])
    """
    ey_z1 = data[data[instrument] == 1][outcome].mean()
    ey_z0 = data[data[instrument] == 0][outcome].mean()
    
    ea_z1 = data[data[instrument] == 1][exposure].mean()
    ea_z0 = data[data[instrument] == 0][exposure].mean()
    
    return (ey_z1 - ey_z0) / (ea_z1 - ea_z0)

def iv_2sls(data, outcome, exposure, instrument, confounders=None):
    """
    Simple wrapper for 2SLS using linearmodels.
    """
    if confounders is None:
        confounders = []
        
    formula = f"{outcome} ~ 1 "
    if confounders:
        formula += " + " + " + ".join(confounders)
    formula += f" + [{exposure} ~ {instrument}]"
    
    model = IV2SLS.from_formula(formula, data).fit()
    return model

