import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

def standardization(data, outcome, exposure, confounders, formula=None):
    """
    Simple parametric g-formula (standardization).
    Hides complexity for students.
    """
    if formula is None:
        formula = f"{outcome} ~ {exposure} + {' + '.join(confounders)}"
    
    # Fit outcome model
    model = smf.ols(formula, data=data).fit()
    
    # Create counterfactual datasets
    df_a1 = data.copy()
    df_a1[exposure] = 1
    
    df_a0 = data.copy()
    df_a0[exposure] = 0
    
    # Predict
    y_a1 = model.predict(df_a1).mean()
    y_a0 = model.predict(df_a0).mean()
    
    return {
        'mean_y_a1': y_a1,
        'mean_y_a0': y_a0,
        'ace': y_a1 - y_a0
    }

def ipw_simple(data, outcome, exposure, confounders):
    """
    Simple IPW estimator.
    """
    # Fit propensity score model
    ps_formula = f"{exposure} ~ {' + '.join(confounders)}"
    ps_model = smf.logit(ps_formula, data=data).fit(disp=0)
    data['ps'] = ps_model.predict(data)
    
    # Calculate weights
    data['w'] = np.where(data[exposure] == 1, 1/data['ps'], 1/(1-data['ps']))
    
    # Weighted mean
    mean_y_a1 = (data[data[exposure] == 1]['Y'] * data[data[exposure] == 1]['w']).sum() / data['w'][data[exposure] == 1].sum()
    mean_y_a0 = (data[data[exposure] == 0]['Y'] * data[data[exposure] == 0]['w']).sum() / data['w'][data[exposure] == 0].sum()
    
    return {
        'mean_y_a1': mean_y_a1,
        'mean_y_a0': mean_y_a0,
        'ace': mean_y_a1 - mean_y_a0
    }

