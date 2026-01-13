"""
Plotting utilities for causal inference diagnostics and results.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Optional, List, Tuple


def plot_ps_overlap(
    ps_treated: np.ndarray,
    ps_control: np.ndarray,
    bins: int = 30,
    alpha: float = 0.6,
    ax: Optional[plt.Axes] = None,
    title: str = "Propensity Score Overlap"
) -> plt.Axes:
    """
    Plot propensity score distributions for treated and control groups.
    
    Parameters
    ----------
    ps_treated : array-like
        Propensity scores for treated group.
    ps_control : array-like
        Propensity scores for control group.
    bins : int, default 30
        Number of histogram bins.
    alpha : float, default 0.6
        Transparency for histograms.
    ax : matplotlib.Axes, optional
        Axes to plot on. If None, creates new figure.
    title : str, default "Propensity Score Overlap"
        Plot title.
    
    Returns
    -------
    matplotlib.Axes
        The axes object.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.hist(ps_control, bins=bins, alpha=alpha, label="Control (A=0)", color="blue", density=True)
    ax.hist(ps_treated, bins=bins, alpha=alpha, label="Treated (A=1)", color="red", density=True)
    ax.set_xlabel("Propensity Score")
    ax.set_ylabel("Density")
    ax.set_title(title)
    ax.legend()
    ax.grid(alpha=0.3)
    
    return ax


def plot_weights_distribution(
    weights: np.ndarray,
    bins: int = 50,
    log_scale: bool = False,
    ax: Optional[plt.Axes] = None,
    title: str = "Weight Distribution"
) -> plt.Axes:
    """
    Plot distribution of IP weights.
    
    Parameters
    ----------
    weights : array-like
        IP weights.
    bins : int, default 50
        Number of histogram bins.
    log_scale : bool, default False
        If True, use log scale for x-axis.
    ax : matplotlib.Axes, optional
        Axes to plot on. If None, creates new figure.
    title : str, default "Weight Distribution"
        Plot title.
    
    Returns
    -------
    matplotlib.Axes
        The axes object.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.hist(weights, bins=bins, alpha=0.7, edgecolor="black")
    ax.set_xlabel("Weight" + (" (log scale)" if log_scale else ""))
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    if log_scale:
        ax.set_xscale("log")
    ax.grid(alpha=0.3)
    
    # Add summary statistics
    mean_w = np.mean(weights)
    median_w = np.median(weights)
    ax.axvline(mean_w, color="red", linestyle="--", label=f"Mean: {mean_w:.2f}")
    ax.axvline(median_w, color="blue", linestyle="--", label=f"Median: {median_w:.2f}")
    ax.legend()
    
    return ax


def plot_survival_curves(
    time_points: np.ndarray,
    survival_treated: np.ndarray,
    survival_control: np.ndarray,
    ax: Optional[plt.Axes] = None,
    title: str = "Causal Survival Curves"
) -> plt.Axes:
    """
    Plot survival curves for treated and control groups.
    
    Parameters
    ----------
    time_points : array-like
        Time points for survival curves.
    survival_treated : array-like
        Survival probabilities for treated group.
    survival_control : array-like
        Survival probabilities for control group.
    ax : matplotlib.Axes, optional
        Axes to plot on. If None, creates new figure.
    title : str, default "Causal Survival Curves"
        Plot title.
    
    Returns
    -------
    matplotlib.Axes
        The axes object.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.plot(time_points, survival_control, label="Control (A=0)", color="blue", linewidth=2)
    ax.plot(time_points, survival_treated, label="Treated (A=1)", color="red", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Survival Probability")
    ax.set_title(title)
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 1)
    
    return ax
