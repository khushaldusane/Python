# 👥 HR Analytics

A statistical analysis project aimed at examining workforce data to uncover insights around employee retention, performance and organisational behaviour.

---

## 📌 Project Overview

This project implements an end-to-end statistical workflow: gathering employee data (demographics, work history, engagement metrics, etc.), conducting exploratory analysis to identify patterns, performing hypothesis testing and regression modelling to understand factors influencing outcomes like attrition or performance. The goal is to derive actionable HR insights to support decision-making in talent management.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scipy, statsmodels
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes employee attributes such as age, gender, tenure, job satisfaction, number of projects, average hours, promotion history, and target outcome variables (e.g., attrition, performance rating).

### 2. Exploratory Data Analysis (EDA)

* Distribution of attrition/performance across employee groups
* Visualisations of tenure vs satisfaction, number of projects vs attrition
* Heatmap of feature correlations
* Identification of missing values, outliers, skewed distributions

### 3. Hypothesis Testing & Feature Engineering

* Define hypotheses (e.g., “Higher job satisfaction reduces attrition risk”)
* Conduct statistical tests (t-tests, chi-square tests) to validate differences between groups
* Create derived features such as project load per year, hours per project, promotion rate
* Encode categorical variables (job role, department) and scale numeric features

### 4. Regression Modelling & Analysis

* Fit regression or logistic regression models to understand relationships (e.g., what predicts attrition)
* Interpret model coefficients, p-values, R² or odds ratios
* Use model insights to identify key drivers and quantify their effect on outcome

### 5. Insights & Business Application

* Provide HR recommendations: e.g., manage high workload employees, improve satisfaction surveys, design retention programmes
* Present findings in dashboards or reports for stakeholder consumption

---

## 📁 Project Structure

```
HR-Analytics/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Variables such as job satisfaction, project load, and promotion history were materially associated with attrition/performance
* Derived features and proper encoding improved analysis clarity
* The regression model enabled quantification of risk factors, allowing HR teams to prioritise interventions
* The project demonstrates how statistical analysis supports strategic HR decision-making

---

## 🚀 Future Improvements

* Expand dataset to include broader organisational segments, longitudinal tracking of employees
* Use advanced modelling (e.g., survival analysis for attrition, multilevel models for nested organisational data)
* Deploy interactive dashboards (e.g., Power BI, Tableau) for real-time monitoring of key HR metrics
* Incorporate external indicators (industry benchmarks, labour market trends) to enrich analysis

---

## 🧑‍💻 Author

**[Khushal Dusane](https://www.linkedin.com/in/khushaldusane29/) – Data Analyst**