import pandas as pd
import numpy as np
import statsmodels.api as sm

def calculate_smd(data, exposure, confounders):
    """
    Calculates Standardized Mean Differences (SMD) for confounders.
    Simple version for teaching.
    """
    smds = {}
    treated = data[data[exposure] == 1]
    untreated = data[data[exposure] == 0]
    
    for c in confounders:
        m1 = treated[c].mean()
        m0 = untreated[c].mean()
        v1 = treated[c].var()
        v0 = untreated[c].var()
        
        pooled_sd = np.sqrt((v1 + v0) / 2)
        smds[c] = (m1 - m0) / pooled_sd
        
    return pd.Series(smds)

