"""
Module 3: Feature Engineer
Creates derived, business-friendly features from raw columns.
These are the fields that make segmentation and business_metrics possible.
"""

import pandas as pd
import numpy as np


def add_age_band(df: pd.DataFrame) -> pd.DataFrame:
    """Bucket customers into age bands used for segment reporting."""
    df = df.copy()
    bins = [17, 30, 40, 50, 60, 100]
    labels = ["18-30", "31-40", "41-50", "51-60", "60+"]
    df["age_band"] = pd.cut(df["age"], bins=bins, labels=labels)
    return df


def add_tenure_group(df: pd.DataFrame) -> pd.DataFrame:
    """Group tenure (years with bank) into new / established / loyal customers."""
    df = df.copy()

    def bucket(t):
        if t <= 1:
            return "New (0-1 yrs)"
        elif t <= 4:
            return "Established (2-4 yrs)"
        else:
            return "Loyal (5+ yrs)"

    df["tenure_group"] = df["tenure"].apply(bucket)
    return df


def add_balance_segment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Segment customers by account balance.
    Zero-balance customers are treated as their own segment since,
    in real banking data, they behave very differently (often near-dormant accounts).
    """
    df = df.copy()

    def bucket(b):
        if b == 0:
            return "Zero Balance"
        elif b < 50000:
            return "Low (<50K)"
        elif b < 120000:
            return "Mid (50K-120K)"
        else:
            return "High (120K+)"

    df["balance_segment"] = df["balance"].apply(bucket)
    return df


def add_product_engagement(df: pd.DataFrame) -> pd.DataFrame:
    """Flag customers using only a single product as lower-engagement."""
    df = df.copy()
    df["low_engagement"] = df["num_of_products"] == 1
    return df


def add_estimated_clv_proxy(df: pd.DataFrame) -> pd.DataFrame:
    """
    A simple, transparent proxy for customer value (NOT a real CLV model) —
    balance + estimated_salary, scaled. Useful for ranking, not for financial reporting.
    Kept intentionally simple and explainable rather than a black-box formula.
    """
    df = df.copy()
    df["value_proxy"] = (df["balance"] * 0.6) + (df["estimated_salary"] * 0.4)
    return df


def engineer_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Run all feature engineering steps in order."""
    df = add_age_band(df)
    df = add_tenure_group(df)
    df = add_balance_segment(df)
    df = add_product_engagement(df)
    df = add_estimated_clv_proxy(df)
    return df
