def get_summary(df):
    """Return high-level expense statistics."""

    total_spending = df["Amount"].sum()
    transactions = len(df)
    average_expense = df["Amount"].mean()
    median_expense = df["Amount"].median()
    maximum_expense = df["Amount"].max()
    minimum_expense = df["Amount"].min()

    return {
        "total_spending": total_spending,
        "transactions": transactions,
        "average_expense": average_expense,
        "median_expense": median_expense,
        "maximum_expense": maximum_expense,
        "minimum_expense": minimum_expense,
    }


def spending_by_item(df):
    """Calculate total spending for each item."""

    return (
        df.groupby("Item")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


def spending_by_category(df):
    """Calculate total spending for each category."""

    return (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


def spending_by_day(df):
    """Calculate spending by day of week."""

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return (
        df.groupby("day")["Amount"]
        .sum()
        .reindex(day_order)
    )


def spending_by_time_period(df):
    """Calculate spending by time period."""

    return (
        df.groupby("Time_Period")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


def daily_spending(df):
    """Calculate total spending for each date."""

    return (
        df.groupby("Date")["Amount"]
        .sum()
        .sort_index()
    )