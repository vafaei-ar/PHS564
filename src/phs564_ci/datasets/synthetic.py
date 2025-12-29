import numpy as np
import pandas as pd

def generate_l01_data(n=1000, seed=2025):
    """Potential outcomes for Lecture 01."""
    rng = np.random.default_rng(seed)
    L = rng.binomial(1, 0.4, n)
    Y_a0 = rng.normal(0.5 + 0.2 * L, 0.1)
    Y_a1 = Y_a0 + 0.1
    prob_A = 0.2 + 0.5 * L
    A = rng.binomial(1, prob_A)
    Y = A * Y_a1 + (1 - A) * Y_a0
    return pd.DataFrame({'L': L, 'Y_a0': Y_a0, 'Y_a1': Y_a1, 'A': A, 'Y': Y})

def generate_l02_data(n=1000, seed=2025):
    """Stratified RCT data for Lecture 02."""
    rng = np.random.default_rng(seed)
    L = rng.binomial(1, 0.5, n)
    prob_A = np.where(L == 1, 0.7, 0.3)
    A = rng.binomial(1, prob_A)
    Y = rng.binomial(1, 0.2 + 0.1 * A + 0.2 * L)
    return pd.DataFrame({'L': L, 'A': A, 'Y': Y})

def generate_l03_data(n=1000, seed=2025):
    """Confounded observational data for Lecture 03."""
    rng = np.random.default_rng(seed)
    L = rng.normal(0, 1, n)
    prob_A = 1 / (1 + np.exp(-(0.5 * L)))
    A = rng.binomial(1, prob_A)
    Y = rng.normal(10 + 2 * A + 5 * L, 1)
    return pd.DataFrame({'L': L, 'A': A, 'Y': Y})

def generate_l04_data(n=1000, seed=2025):
    """Effect modification data for Lecture 04."""
    rng = np.random.default_rng(seed)
    M = rng.binomial(1, 0.5, n)
    A = rng.binomial(1, 0.5, n)
    Y_prob = 0.1 + (0.05 * A) + (0.1 * M) + (0.15 * A * M)
    Y = rng.binomial(1, Y_prob)
    return pd.DataFrame({'M': M, 'A': A, 'Y': Y})

def generate_l05_data(n=1000, seed=2025):
    """Collider bias data for Lecture 05."""
    rng = np.random.default_rng(seed)
    A = rng.binomial(1, 0.5, n)
    Y = rng.binomial(1, 0.3, n)
    prob_C = 0.1 + 0.4 * A + 0.4 * Y
    C = rng.binomial(1, prob_C)
    return pd.DataFrame({'A': A, 'Y': Y, 'C': C})

def generate_l06_data(n=1000, seed=2025):
    """Multiple confounders and a mediator for Lecture 06."""
    rng = np.random.default_rng(seed)
    L1 = rng.normal(50, 10, n)
    L2 = rng.binomial(1, 0.3, n)
    prob_A = 1 / (1 + np.exp(-( (L1 - 50)/10 + 2*L2 - 1 )))
    A = rng.binomial(1, prob_A)
    M = rng.normal(2 * A + 0.5 * L1, 1)
    Y = 10 + 5 * A + 0.2 * L1 + 3 * L2 + 1.5 * M + rng.normal(0, 2, n)
    return pd.DataFrame({'L1': L1, 'L2': L2, 'A': A, 'M': M, 'Y': Y})

def generate_l07_data(n=1000, seed=2025):
    """Selection bias (censoring) for Lecture 07."""
    rng = np.random.default_rng(seed)
    L = rng.normal(0, 1, n)
    prob_A = 1 / (1 + np.exp(-(L)))
    A = rng.binomial(1, prob_A)
    Y = 10 + 2 * A + 2 * L + rng.normal(0, 1, n)
    prob_C = 1 / (1 + np.exp(-( -1 + 0.5 * A + L )))
    C = rng.binomial(1, prob_C)
    Y_obs = np.where(C == 0, Y, np.nan)
    return pd.DataFrame({'L': L, 'A': A, 'Y': Y, 'C': C, 'Y_obs': Y_obs})

def generate_l08_l09_data(n=1000, seed=2025):
    """High-dimensional confounding for parametric models (L08/L09)."""
    rng = np.random.default_rng(seed)
    L1 = rng.normal(0, 1, n)
    L2 = rng.binomial(1, 0.5, n)
    L3 = rng.normal(10, 2, n)
    L4 = rng.binomial(1, 0.2, n)
    prob_A = 1 / (1 + np.exp(-(0.5*L1 + L2 - 0.2*L3 + 1.5*L4)))
    A = rng.binomial(1, prob_A)
    Y = 5 + 3.5*A + 2*L1 + 5*L2 + 0.5*L3 - 4*L4 + rng.normal(0, 1, n)
    return pd.DataFrame({'L1': L1, 'L2': L2, 'L3': L3, 'L4': L4, 'A': A, 'Y': Y})

def generate_l10_data(n=2000, seed=2025):
    """Instrumental variables data for Lecture 10."""
    rng = np.random.default_rng(seed)
    U = rng.normal(0, 1, n)
    Z = rng.binomial(1, 0.5, n)
    prob_A = 1 / (1 + np.exp(-( -1 + 2*Z + 1.5*U )))
    A = rng.binomial(1, prob_A)
    Y = 10 + 2.0 * A + 2.0 * U + rng.normal(0, 0.5, n)
    return pd.DataFrame({'Z': Z, 'A': A, 'Y': Y, 'U': U})

def generate_l11_data(n=1000, seed=2025):
    """Data for IPW and balance diagnostics (Lecture 11)."""
    return generate_l08_l09_data(n, seed)

def generate_l12_survival_data(n=1000, seed=2025):
    """Discrete-time survival data for Lecture 12."""
    rng = np.random.default_rng(seed)
    L = rng.binomial(1, 0.4, n)
    A = rng.binomial(1, 0.5, n)
    
    data = []
    for i in range(n):
        for t in range(1, 6):
            # FIXED: Use scalar indexing for A and L
            hazard = 1 / (1 + np.exp(-( -3 + 0.5*t - 1.0*A[i] + 0.8*L[i] )))
            event = rng.binomial(1, hazard)
            
            data.append({'id': i, 't': t, 'A': A[i], 'L': L[i], 'Y': event})
            if event == 1:
                break
                
    return pd.DataFrame(data)
