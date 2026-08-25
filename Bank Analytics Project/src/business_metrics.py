"""
Module 4: Business Metrics
This is the analytical core of the project: turns cleaned, engineered
data into business answers — churn rate by segment, a transparent
rule-based risk score, and revenue-at-risk estimates.
"""

import pandas as pd
import numpy as np


def churn_rate_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """Return churn rate (%) for each value in a given segment column."""
    result = (
        df.groupby(segment_col, observed=True)["churn"]
        .agg(customers="count", churned="sum")
        .assign(churn_rate_pct=lambda x: round(x["churned"] / x["customers"] * 100, 2))
        .sort_values("churn_rate_pct", ascending=False)
        .reset_index()
    )
    return result


def compute_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    A simple, transparent, weighted risk score (0-100) built from
    known churn drivers in this dataset:
      - inactive members
      - single-product customers (low engagement)
      - customers in the 51-60 / 60+ age bands (historically higher churn)
      - low tenure

    This is a scoring RULE, not a trained model — every point is traceable
    to a specific business reason, which is the point.
    """
    df = df.copy()
    score = pd.Series(0, index=df.index, dtype=float)

    score += np.where(df["is_active_member"] == 0, 30, 0)
    score += np.where(df["low_engagement"], 25, 0)
    score += np.where(df["age_band"].isin(["51-60", "60+"]), 25, 0)
    score += np.where(df["tenure_group"] == "New (0-1 yrs)", 20, 0)

    df["risk_score"] = score.clip(upper=100)

    def tier(s):
        if s >= 60:
            return "High Risk"
        elif s >= 30:
            return "Medium Risk"
        else:
            return "Low Risk"

    df["risk_tier"] = df["risk_score"].apply(tier)
    return df


def revenue_at_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estimate revenue/value exposure by risk tier, using the value_proxy
    computed in feature_engineer. Gives a rupee-figure impact statement
    rather than just customer counts — this is what makes a finding
    'business-relevant' instead of just statistical.
    """
    result = (
        df.groupby("risk_tier", observed=True)["value_proxy"]
        .agg(customers="count", total_value_at_risk="sum")
        .sort_values("total_value_at_risk", ascending=False)
        .reset_index()
    )
    result["total_value_at_risk"] = result["total_value_at_risk"].round(0).apply(lambda x: f"{x:,.0f}")
    return result


def top_findings(df: pd.DataFrame) -> dict:
    """
    Pulls together the headline numbers used in the README / report.
    Centralizing this avoids re-deriving the same numbers in multiple places.
    """
    findings = {}

    overall_churn = round(df["churn"].mean() * 100, 2)
    findings["overall_churn_rate_pct"] = overall_churn

    geo = churn_rate_by_segment(df, "geography")
    findings["highest_churn_geography"] = geo.iloc[0].to_dict()

    age = churn_rate_by_segment(df, "age_band")
    findings["highest_churn_age_band"] = age.iloc[0].to_dict()

    inactive_churn = df[df["is_active_member"] == 0]["churn"].mean() * 100
    active_churn = df[df["is_active_member"] == 1]["churn"].mean() * 100
    findings["inactive_member_churn_pct"] = round(inactive_churn, 2)
    findings["active_member_churn_pct"] = round(active_churn, 2)

    high_risk_count = (df["risk_tier"] == "High Risk").sum()
    findings["high_risk_customer_count"] = int(high_risk_count)
    findings["high_risk_pct_of_base"] = round(high_risk_count / len(df) * 100, 2)

    return findings
