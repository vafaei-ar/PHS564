import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

def ipcw_simple(data, outcome, exposure, confounders, censoring):
    """
    Simple Inverse Probability of Censoring Weighting (IPCW).
    data: DataFrame
    outcome: string (observed outcome with NaNs)
    exposure: string
    confounders: list of strings
    censoring: string (binary, 1 if censored/missing)
    """
    # 1. Fit censoring model (prob of NOT being censored)
    # We want P(C=0 | A, L)
    formula = f"1 - {censoring} ~ {exposure} + {' + '.join(confounders)}"
    model = smf.logit(formula, data=data).fit(disp=0)
    
    # 2. Calculate weights for the uncensored people
    data['prob_uncensored'] = model.predict(data)
    data['w_c'] = 1 / data['prob_uncensored']
    
    # 3. Weighted mean among the uncensored (C=0)
    uncensored = data[data[censoring] == 0].copy()
    
    mean_y_a1 = (uncensored[uncensored[exposure] == 1][outcome] * uncensored[uncensored[exposure] == 1]['w_c']).sum() / uncensored[uncensored[exposure] == 1]['w_c'].sum()
    mean_y_a0 = (uncensored[uncensored[exposure] == 0][outcome] * uncensored[uncensored[exposure] == 0]['w_c']).sum() / uncensored[uncensored[exposure] == 0]['w_c'].sum()
    
    return {
        'mean_y_a1': mean_y_a1,
        'mean_y_a0': mean_y_a0,
        'ace': mean_y_a1 - mean_y_a0
    }

