import streamlit as st
import matplotlib.pyplot as plt

from src.datacleaning import load_data, clean_data
from src.analysis import (
    get_summary,
    spending_by_item,
    spending_by_category,
    spending_by_day,
    spending_by_time_period,
    daily_spending
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Personal Expense Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# GREEN + BLACK THEME
# ============================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #0B1F16;
        color: #F0FFF4;
    }

    /* Main content */
    .main {
        background-color: #0B1F16;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #07140E;
        border-right: 1px solid #16A34A;
    }

    [data-testid="stSidebar"] * {
        color: #F0FFF4;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #22C55E !important;
    }

    /* Normal text */
    p, label, span {
        color: #E2FBEA;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #102A1D;
        border: 1px solid #16A34A;
        border-radius: 12px;
        padding: 18px;
        box-shadow: none;
    }

    [data-testid="stMetricLabel"] {
        color: #86EFAC !important;
    }

    [data-testid="stMetricValue"] {
        color: #22C55E !important;
        font-weight: 700;
    }

    [data-testid="stMetricDelta"] {
        color: #86EFAC !important;
    }

    /* Dividers */
    hr {
        border-color: #166534;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #102A1D;
        border: 1px solid #166534;
        color: #F0FFF4;
    }

    /* Multiselect tags */
    span[data-baseweb="tag"] {
        background-color: #166534 !important;
        color: white !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #16A34A;
        color: #06100A;
        border: 1px solid #22C55E;
        border-radius: 8px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #22C55E;
        color: #06100A;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border: 1px solid #166534;
        border-radius: 10px;
    }

    /* Caption */
    .stCaption {
        color: #86EFAC !important;
    }

    /* Markdown links */
    a {
        color: #4ADE80 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """<div style="padding: 10px 0 20px 0; border-bottom: 1px solid #166534; margin-bottom: 25px;">
<h1 style="color: #22C55E; font-size: 42px; margin-bottom: 5px;">Personal Expense Intelligence</h1>
<p style="color: #86EFAC; font-size: 16px; margin-top: 0;">Understand where your money goes.</p>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

df = load_data("data/raw/myExpenses1.csv")
df = clean_data(df)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    """
    <h2 style="color:#22C55E;">Filters</h2>
    """,
    unsafe_allow_html=True
)


# Category filter
categories = (
    df["Category"]
    .dropna()
    .unique()
    .tolist()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)


# Item filter
items = sorted(
    df["Item"]
    .dropna()
    .unique()
    .tolist()
)

selected_items = st.sidebar.multiselect(
    "Item",
    items,
    default=items
)


# Time period filter
time_periods = [
    "Morning",
    "Afternoon",
    "Evening",
    "Night"
]

selected_periods = st.sidebar.multiselect(
    "Time Period",
    time_periods,
    default=time_periods
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    df["Category"].isin(selected_categories)
    & df["Item"].isin(selected_items)
    & df["Time_Period"].isin(selected_periods)
]


# ============================================================
# SUMMARY METRICS
# ============================================================

summary = get_summary(filtered_df)

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Spending",
        f"Rs. {summary['total_spending']:,.0f}"
    )


with col2:
    st.metric(
        "Transactions",
        f"{summary['transactions']:,}"
    )


with col3:
    st.metric(
        "Average Expense",
        f"Rs. {summary['average_expense']:,.2f}"
    )


with col4:
    st.metric(
        "Largest Expense",
        f"Rs. {summary['maximum_expense']:,.0f}"
    )


st.divider()


# ============================================================
# CHART THEME
# ============================================================

def style_chart(ax):
    ax.set_facecolor("#102A1D")

    ax.tick_params(
        colors="#E2FBEA"
    )

    ax.xaxis.label.set_color("#86EFAC")
    ax.yaxis.label.set_color("#86EFAC")

    ax.title.set_color("#22C55E")

    for spine in ax.spines.values():
        spine.set_color("#166534")

    ax.grid(
        axis="y",
        alpha=0.15
    )


# ============================================================
# TOP ITEMS + CATEGORY
# ============================================================

col1, col2 = st.columns(2)


# -------------------- TOP ITEMS ------------------------------

with col1:

    st.subheader("Top Spending Items")

    item_data = (
        spending_by_item(filtered_df)
        .head(10)
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    fig.patch.set_facecolor("#0B1F16")

    item_data.sort_values().plot(
        kind="barh",
        ax=ax,
        color="#22C55E"
    )

    ax.set_xlabel("Amount")
    ax.set_ylabel("Item")
    ax.set_title("Top 10 Items by Spending")

    style_chart(ax)

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# -------------------- CATEGORY ------------------------------

with col2:

    st.subheader("Spending by Category")

    category_data = spending_by_category(
        filtered_df
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    fig.patch.set_facecolor("#0B1F16")

    category_data.plot(
        kind="bar",
        ax=ax,
        color="#16A34A"
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    ax.set_title("Total Spending by Category")

    style_chart(ax)

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# DAILY SPENDING
# ============================================================

st.subheader("Daily Spending")

daily_data = daily_spending(
    filtered_df
)

fig, ax = plt.subplots(
    figsize=(12, 5)
)

fig.patch.set_facecolor("#0B1F16")

daily_data.plot(
    ax=ax,
    color="#22C55E",
    linewidth=2
)

ax.set_xlabel("Date")
ax.set_ylabel("Amount")
ax.set_title("Daily Spending Trend")

style_chart(ax)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# ============================================================
# DAY + TIME ANALYSIS
# ============================================================

col1, col2 = st.columns(2)


# -------------------- DAY -----------------------------------

with col1:

    st.subheader("Spending by Day")

    day_data = spending_by_day(
        filtered_df
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    fig.patch.set_facecolor("#0B1F16")

    day_data.plot(
        kind="bar",
        ax=ax,
        color="#22C55E"
    )

    ax.set_xlabel("Day")
    ax.set_ylabel("Amount")
    ax.set_title("Spending by Day of Week")

    style_chart(ax)

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# -------------------- TIME ----------------------------------

with col2:

    st.subheader("Spending by Time of Day")

    time_data = spending_by_time_period(
        filtered_df
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    fig.patch.set_facecolor("#0B1F16")

    time_data.plot(
        kind="bar",
        ax=ax,
        color="#16A34A"
    )

    ax.set_xlabel("Time Period")
    ax.set_ylabel("Amount")
    ax.set_title("Spending by Time of Day")

    style_chart(ax)

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# TRANSACTION TABLE
# ============================================================

st.subheader("Transactions")

st.dataframe(
    filtered_df.sort_values(
        "Amount",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True
)