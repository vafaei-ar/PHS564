import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_potential_outcomes(df):
    """
    Plots the distribution of potential outcomes.
    Highly simplified for teaching.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['Y_a0'], label='Potential Outcome if Untreated (Y_a0)', fill=True)
    sns.kdeplot(df['Y_a1'], label='Potential Outcome if Treated (Y_a1)', fill=True)
    plt.title("Distribution of Potential Outcomes in the Population")
    plt.xlabel("Outcome Value")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

def plot_observed_association(df):
    """
    Plots the observed association between A and Y.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='A', y='Y', data=df)
    plt.title("Observed Association: Treatment (A) vs Outcome (Y)")
    plt.xlabel("Treatment (0=Untreated, 1=Treated)")
    plt.ylabel("Observed Outcome (Y)")
    plt.show()

