# Bank Customer Churn & Loan Risk Analysis

**Business question:** Which customer segments are most likely to churn, and where should the bank prioritize retention efforts to protect revenue?

A modular, end-to-end Python analytics pipeline built with **Pandas, NumPy, and Seaborn** — cleaning, feature engineering, business-metric derivation, visualization, and automated reporting, all as reusable modules rather than a single notebook.

---

## Key Findings

- **Overall churn rate: 20.37%**
- **Germany has the highest churn rate (32.44%)** vs. Spain (16.67%) and France (16.15%)
- **The 51–60 age band churns at 56.21%** — by far the highest of any segment, more than 4x the 18–30 band
- **Inactive members churn at 26.85%**, nearly double the 14.27% rate for active members
- **723 customers (7.2% of the base)** are flagged **High Risk** by the scoring model in `business_metrics.py` — but they hold less total value at risk than the Medium Risk tier, meaning a purely volume-based retention strategy would miss where the real financial exposure sits

Full report with all segment tables: [`outputs/summary_report.md`](outputs/summary_report.md)

---

## Tech Stack

- **Pandas / NumPy** — cleaning, transformation, feature engineering
- **Seaborn / Matplotlib** — visualization
- **Modular Python (`src/`)** — each pipeline stage is an importable, testable module
- **Jupyter Notebook** — narrative walkthrough (`notebooks/analysis.ipynb`)

---

## Project Structure

```
bank-analytics-project/
├── data/
│   ├── raw/bank_churn.csv           # original dataset (10,000 customers)
│   └── processed/                   # cleaned + engineered output
├── src/
│   ├── data_loader.py               # load + schema validation
│   ├── data_cleaner.py              # nulls, dtypes, dedup, outlier flagging
│   ├── feature_engineer.py          # age bands, tenure groups, balance segments, value proxy
│   ├── business_metrics.py          # churn-by-segment, rule-based risk score, value-at-risk
│   ├── eda.py                       # seaborn chart generation
│   └── report_generator.py          # markdown report assembly
├── notebooks/
│   └── analysis.ipynb               # narrative version, orchestrates the modules
├── outputs/
│   ├── charts/                      # generated PNG charts
│   └── summary_report.md            # auto-generated business report
├── main.py                          # runs the full pipeline end-to-end
└── requirements.txt
```

## Why Modules, Not One Notebook

Each file in `src/` has a single responsibility and is independently importable — `main.py` calls `data_loader.load()` → `data_cleaner.clean_pipeline()` → `feature_engineer.engineer_pipeline()` → `business_metrics` → `eda` → `report_generator`, in sequence. This mirrors how a real reporting pipeline is built: reusable, testable stages instead of one long script.

## Why Rule-Based Risk Scoring, Not ML

The risk score in `business_metrics.py` is a transparent, weighted rule (inactive status + low product engagement + age band + tenure) rather than a trained classifier. Every point in every customer's score is traceable to a specific business reason — which is what makes it defensible in a stakeholder review, and avoids overstating the sophistication of the analysis.

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

This regenerates the processed dataset, all charts in `outputs/charts/`, and the summary report at `outputs/summary_report.md`.

Or open `notebooks/analysis.ipynb` for the narrative walkthrough.

## Dataset

10,000-row bank customer dataset (CreditScore, Geography, Gender, Age, Tenure, Balance, Number of Products, Credit Card status, Active Member status, Estimated Salary, Churn flag) — a widely used public banking churn dataset.
