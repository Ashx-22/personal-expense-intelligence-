# Personal Expense Analysis

## Overview

A Python-based data analysis project that explores personal
expense transactions to identify spending patterns, major
expenses, category behavior, and time-based spending trends.

## Objective

The project aims to answer questions such as:

- How much was spent overall?
- What items are purchased most frequently?
- Which items account for the highest spending?
- How does spending differ by category?
- Which days have the highest spending?
- What time of day has the highest spending?
- Are there unusually high-value transactions?

## Dataset

The dataset contains 145 expense transactions recorded
during March 2023.

### Columns

- Date
- Item
- Amount
- Category
- Time
- day

## Key Findings

- Total spending: ₹4,609
- Transactions: 145
- Average transaction: ₹31.79
- Median transaction: ₹17
- Largest transaction: ₹500
- Highest-spending item: Chai with snacks
- Top 5 items account for approximately 61.7% of total spending

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
personal-expense-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_expense_exploration.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore

## App
https://ashx-22-personal-expense-intelligence--app-vl0rag.streamlit.app/
