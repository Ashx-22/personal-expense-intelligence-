import pandas as pd


def load_data(file_path="data/raw/myExpenses1.csv"):
    """Load the raw expense dataset."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean and prepare the expense dataset."""

    df = df.copy()

    # Convert Date to datetime
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Convert Amount to numeric
    df["Amount"] = pd.to_numeric(
        df["Amount"],
        errors="coerce"
    )

    # Convert Time to datetime
    df["Time"] = pd.to_datetime(
        df["Time"],
        format="%H:%M",
        errors="coerce"
    )

    # Standardize text columns
    text_columns = ["Item", "Category", "day"]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Create Hour column
    df["Hour"] = df["Time"].dt.hour

    # Create Time Period
    def get_time_period(hour):
        if pd.isna(hour):
            return "Unknown"
        elif hour < 12:
            return "Morning"
        elif hour < 17:
            return "Afternoon"
        elif hour < 21:
            return "Evening"
        else:
            return "Night"

    df["Time_Period"] = df["Hour"].apply(get_time_period)

    return df
