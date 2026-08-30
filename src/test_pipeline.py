from src.datacleaning import load_data, clean_data
from src.analysis import (
    get_summary,
    spending_by_item,
    spending_by_category,
    spending_by_day,
    spending_by_time_period,
    daily_spending
)


# Load data
df = load_data("data/raw/expenses.csv")

# Clean data
df = clean_data(df)


# Summary
summary = get_summary(df)

print("\nSUMMARY")
print("=" * 40)

for key, value in summary.items():
    print(f"{key}: {value}")


# Item analysis
print("\nSPENDING BY ITEM")
print("=" * 40)
print(spending_by_item(df))


# Category analysis
print("\nSPENDING BY CATEGORY")
print("=" * 40)
print(spending_by_category(df))


# Day analysis
print("\nSPENDING BY DAY")
print("=" * 40)
print(spending_by_day(df))


# Time analysis
print("\nSPENDING BY TIME PERIOD")
print("=" * 40)
print(spending_by_time_period(df))


# Daily spending
print("\nDAILY SPENDING")
print("=" * 40)
print(daily_spending(df))
