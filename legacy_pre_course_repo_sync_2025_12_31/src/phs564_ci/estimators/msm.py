import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

def fit_msm_pooled_logistic(data, outcome, exposure, weights, time_col=None):
    """
    Fits a simple Marginal Structural Model (MSM) using pooled logistic regression.
    Often used for discrete-time hazard models.
    """
    formula = f"{outcome} ~ {exposure}"
    if time_col:
        formula += f" + {time_col}"
        
    # Fit weighted model
    model = smf.glm(formula, data=data, family=sm.families.Binomial(), freq_weights=data[weights]).fit()
    return model

