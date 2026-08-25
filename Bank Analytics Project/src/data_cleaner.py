"""
Module 2: Data Cleaner
Handles missing values, duplicate records, column renaming,
data type fixes, and outlier flags.
"""

import pandas as pd
import numpy as np


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rename columns to a consistent snake_case format."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def drop_irrelevant_columns(df: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:
    """Drop columns that carry no analytical value (e.g. surname, row id)."""
    existing = [c for c in cols_to_drop if c in df.columns]
    df = df.drop(columns=existing)
    print(f"[data_cleaner] Dropped columns: {existing}")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Report and handle missing values.
    Numeric -> median fill. Categorical -> mode fill.
    (This dataset is largely clean, but the logic is here for real-world reuse.)
    """
    df = df.copy()
    missing_summary = df.isnull().sum()
    missing_summary = missing_summary[missing_summary > 0]

    if missing_summary.empty:
        print("[data_cleaner] No missing values found.")
        return df

    print(f"[data_cleaner] Missing values found:\n{missing_summary}")

    for col in missing_summary.index:
        if df[col].dtype in ["float64", "int64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df


def drop_duplicates(df: pd.DataFrame, subset_col: str = "customerid") -> pd.DataFrame:
    """Remove duplicate customer records based on a unique ID column."""
    before = len(df)
    if subset_col in df.columns:
        df = df.drop_duplicates(subset=subset_col)
    else:
        df = df.drop_duplicates()
    after = len(df)
    print(f"[data_cleaner] Removed {before - after} duplicate rows.")
    return df


def flag_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Flag outliers in a numeric column using the IQR method.
    Adds a boolean column '<column>_outlier' rather than silently dropping rows,
    since in banking data, an "outlier" balance might be a legitimate high-value customer.
    """
    df = df.copy()
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df[f"{column}_outlier"] = ~df[column].between(lower_bound, upper_bound)
    n_outliers = df[f"{column}_outlier"].sum()
    print(f"[data_cleaner] Flagged {n_outliers} outliers in '{column}' (IQR method).")
    return df


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full cleaning sequence in order."""
    df = standardize_columns(df)
    df = drop_irrelevant_columns(df, cols_to_drop=["surname",''])
    df = handle_missing_values(df)
    df = drop_duplicates(df, subset_col="customerid")
    df = flag_outliers_iqr(df, column="balance")
    df = flag_outliers_iqr(df, column="creditscore")
    return df
