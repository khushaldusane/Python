"""
Module 5: EDA / Visualization
Generates and saves the seaborn/matplotlib charts used in the
report and README. Each function saves one chart to outputs/charts/.
"""

import matplotlib
matplotlib.use("Agg")  # headless-safe backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

sns.set_style("whitegrid")
PALETTE = "viridis"


def _save(fig, filename, output_dir):
    path = os.path.join(output_dir, filename)
    fig.savefig(path, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(f"[eda] Saved {path}")


def plot_churn_by_geography(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(7, 5))
    order = df.groupby("geography", observed=True)["churn"].mean().sort_values(ascending=False).index
    sns.barplot(data=df, x="geography", y="churn", order=order, estimator="mean",
                errorbar=None, hue="geography", palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Churn Rate by Geography")
    ax.set_ylabel("Churn Rate")
    ax.set_xlabel("Geography")
    _save(fig, "churn_by_geography.png", output_dir)


def plot_churn_by_age_band(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(7, 5))
    order = ["18-30", "31-40", "41-50", "51-60", "60+"]
    sns.barplot(data=df, x="age_band", y="churn", order=order, estimator="mean",
                errorbar=None, hue="age_band", palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Churn Rate by Age Band")
    ax.set_ylabel("Churn Rate")
    ax.set_xlabel("Age Band")
    _save(fig, "churn_by_age_band.png", output_dir)


def plot_active_vs_inactive_churn(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(6, 5))
    plot_df = df.copy()
    plot_df["member_status"] = plot_df["is_active_member"].map({1: "Active", 0: "Inactive"})
    sns.barplot(data=plot_df, x="member_status", y="churn", estimator="mean",
                errorbar=None, hue="member_status", palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Churn Rate: Active vs Inactive Members")
    ax.set_ylabel("Churn Rate")
    ax.set_xlabel("Membership Status")
    _save(fig, "churn_active_vs_inactive.png", output_dir)


def plot_correlation_heatmap(df: pd.DataFrame, output_dir: str):
    numeric_cols = ["creditscore", "age", "tenure", "balance", "num_of_products",
                     "has_credit_card", "is_active_member", "estimated_salary", "churn"]
    numeric_cols = [c for c in numeric_cols if c in df.columns]
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm",
                center=0, ax=ax)
    ax.set_title("Correlation Heatmap — Numeric Features")
    _save(fig, "correlation_heatmap.png", output_dir)


def plot_risk_tier_distribution(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(6, 5))
    order = ["Low Risk", "Medium Risk", "High Risk"]
    sns.countplot(data=df, x="risk_tier", order=order, hue="risk_tier", palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Customer Distribution by Risk Tier")
    ax.set_ylabel("Number of Customers")
    ax.set_xlabel("Risk Tier")
    _save(fig, "risk_tier_distribution.png", output_dir)


def plot_balance_distribution_by_churn(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x="churn", y="balance", hue="churn", palette=PALETTE, legend=False, ax=ax)
    ax.set_title("Account Balance Distribution: Churned vs Retained")
    ax.set_xlabel("Churned (0 = No, 1 = Yes)")
    ax.set_ylabel("Balance")
    _save(fig, "balance_by_churn.png", output_dir)


def run_all_plots(df: pd.DataFrame, output_dir: str = "../outputs/charts"):
    os.makedirs(output_dir, exist_ok=True)
    plot_churn_by_geography(df, output_dir)
    plot_churn_by_age_band(df, output_dir)
    plot_active_vs_inactive_churn(df, output_dir)
    plot_correlation_heatmap(df, output_dir)
    plot_risk_tier_distribution(df, output_dir)
    plot_balance_distribution_by_churn(df, output_dir)
    print("[eda] All charts generated.")
