"""
Main pipeline entry point.
Runs the full flow: load -> clean -> engineer features -> compute business
metrics -> generate charts -> generate report.

Run from the project root:
    python main.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_data, validate_schema
from data_cleaner import clean_pipeline
from feature_engineer import engineer_pipeline
from business_metrics import (
    churn_rate_by_segment,
    compute_risk_score,
    revenue_at_risk,
    top_findings,
)
from eda import run_all_plots
from report_generator import generate_markdown_report

RAW_DATA_PATH = "data/raw/bank_churn.csv"
PROCESSED_DATA_PATH = "data/processed/bank_churn_processed.csv"
CHARTS_DIR = "outputs/charts"
REPORT_PATH = "outputs/summary_report.md"

EXPECTED_COLUMNS = [
    "CustomerId", "Surname", "CreditScore", "Geography", "Gender", "Age",
    "Tenure", "Balance", "Num Of Products", "Has Credit Card",
    "Is Active Member", "Estimated Salary", "Churn",
]


def main():
    print("=" * 60)
    print("BANK CUSTOMER CHURN & RISK ANALYSIS — PIPELINE START")
    print("=" * 60)

    # 1. Load
    df = load_data(RAW_DATA_PATH)
    validate_schema(df, EXPECTED_COLUMNS)

    # 2. Clean
    df = clean_pipeline(df)

    # 3. Feature engineering
    df = engineer_pipeline(df)

    # 4. Business metrics
    df = compute_risk_score(df)
    churn_by_geo = churn_rate_by_segment(df, "geography")
    churn_by_age = churn_rate_by_segment(df, "age_band")
    revenue_risk = revenue_at_risk(df)
    findings = top_findings(df)

    # Save processed dataset
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[main] Processed data saved to {PROCESSED_DATA_PATH}")

    # 5. Charts
    run_all_plots(df, output_dir=CHARTS_DIR)

    # 6. Report
    generate_markdown_report(findings, churn_by_geo, churn_by_age, revenue_risk, REPORT_PATH)

    print("=" * 60)
    print("PIPELINE COMPLETE")
    print(f"Key finding: overall churn rate = {findings['overall_churn_rate_pct']}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
