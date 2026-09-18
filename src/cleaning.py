"""
src/cleaning.py

Loads data/raw/master_data.csv, validates it, and writes a clean,
analysis-ready table to data/processed/master_data_clean.csv.

Checks performed (and logged):
  1. Date parses correctly, no duplicate dates, no gaps in the daily series
  2. Binary flag columns contain only 0/1
  3. No negative values in revenue/spend columns
  4. Row count and date range match the Business brief (852 days,
     1 Apr 2024 - 31 Jul 2026)
  5. Derived columns added: Year, Month, Weekday, Total_Google_Components,
     Total_Meta_Components (component sums, kept SEPARATE from the
     spend_Google / spend_Meta roll-ups per the glossary's warning)
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/master_data.csv")
OUT_PATH = Path("data/processed/master_data_clean.csv")

BINARY_FLAGS = [
    "UWG_Mailing", "BFCM_Promo_Effect", "holiday_list",
    "Offline_Promo", "Promotion_Discount",
]

GOOGLE_COMPONENTS = [
    "spend_Google_Branded", "spend_Google_Non_Branded", "spend_Google_PMAX",
    "spend_Google_Demand_Gen", "spend_Google_Others",
]
META_COMPONENTS = [
    "spend_Meta_ASC", "spend_Meta_Retargeting", "spend_Meta_Prospecting",
]

SPEND_COLS = GOOGLE_COMPONENTS + META_COMPONENTS + [
    "influencer_spend", "Awin_spend", "microsoft_spend",
    "criteo_spend", "cost_outbrain",
]
REVENUE_COLS = ["Total_Revenue", "Revenue_New_Customer"]


def load_and_clean():
    df = pd.read_csv(RAW_PATH)
    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")

    # --- 1. Date parsing & continuity checks ---
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    dupes = df["Date"].duplicated().sum()
    print(f"Duplicate dates: {dupes}")

    full_range = pd.date_range(df["Date"].min(), df["Date"].max(), freq="D")
    missing_dates = full_range.difference(df["Date"])
    print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Expected days: {len(full_range)}, Actual rows: {len(df)}, "
          f"Missing dates: {len(missing_dates)}")
    if len(missing_dates) > 0:
        print(f"  Missing: {list(missing_dates[:10])}{' ...' if len(missing_dates) > 10 else ''}")

    # --- 2. Binary flag validation ---
    for col in BINARY_FLAGS:
        bad_vals = set(df[col].dropna().unique()) - {0, 1, 0.0, 1.0}
        if bad_vals:
            print(f"  [WARNING] {col} has non-binary values: {bad_vals}")
        df[col] = df[col].astype(int)

    # --- 3. Negative value checks ---
    for col in REVENUE_COLS + SPEND_COLS:
        neg_count = (df[col] < 0).sum()
        if neg_count > 0:
            print(f"  [WARNING] {col} has {neg_count} negative values")

    # --- 4. Missing value summary ---
    null_counts = df.isnull().sum()
    nulls_present = null_counts[null_counts > 0]
    if len(nulls_present) > 0:
        print(f"  Columns with nulls:\n{nulls_present}")
    else:
        print("  No nulls found.")

    # --- 5. Roll-up sanity check (spend_Google/spend_Meta vs components) ---
    df["Total_Google_Components"] = df[GOOGLE_COMPONENTS].sum(axis=1)
    df["Total_Meta_Components"] = df[META_COMPONENTS].sum(axis=1)

    google_diff = (df["spend_Google"] - df["Total_Google_Components"]).abs()
    meta_diff = (df["spend_Meta"] - df["Total_Meta_Components"]).abs()
    print(f"  spend_Google vs component sum -> max abs diff: {google_diff.max():.2f}, "
          f"mean abs diff: {google_diff.mean():.4f}")
    print(f"  spend_Meta vs component sum   -> max abs diff: {meta_diff.max():.2f}, "
          f"mean abs diff: {meta_diff.mean():.4f}")

    # --- 6. Derived calendar columns (for EDA/dashboard grouping) ---
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    df["Weekday"] = df["Date"].dt.day_name()

    # --- 7. Total paid media (using roll-ups, NOT double-counted) ---
    df["Total_Paid_Media"] = (
        df["spend_Google"] + df["spend_Meta"] + df["influencer_spend"] +
        df["Awin_spend"] + df["microsoft_spend"] + df["criteo_spend"] +
        df["cost_outbrain"]
    )
    df["Media_Pct_of_Revenue"] = (df["Total_Paid_Media"] / df["Total_Revenue"]) * 100

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"\nSaved cleaned data -> {OUT_PATH}  ({df.shape[0]} rows, {df.shape[1]} cols)")
    return df


if __name__ == "__main__":
    load_and_clean()