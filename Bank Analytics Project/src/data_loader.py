"""
Module 1: Data Loader
Responsible for loading the raw dataset and doing basic validation
before it's handed off to the cleaning module.
"""

import pandas as pd
import os


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the raw bank customer dataset from CSV.
    Parameters
    ----------
    filepath : str
        Path to the raw CSV file.
    Returns
    -------
    pd.DataFrame
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Could not find data file at {filepath}")

    df = pd.read_csv(filepath)
    print(f"[data_loader] Loaded {df.shape[0]} rows, {df.shape[1]} columns from {filepath}")
    return df


def validate_schema(df: pd.DataFrame, expected_columns: list) -> bool:
    """
    Confirm the dataframe has the columns we expect before proceeding.
    Raises a clear error instead of failing downstream with a confusing KeyError.
    """
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        raise ValueError(f"[data_loader] Missing expected columns: {missing}")
    print("[data_loader] Schema validated successfully.")
    return True


if __name__ == "__main__":
    df = load_data("../data/raw/bank_churn.csv")
    print(df.head())
    print(df.info())
