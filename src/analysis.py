"""
src/analysis.py

Computes the specific summary statistics that back the business narrative
in reports/findings.md. Each number here should be traceable to a claim
in the write-up — this script is the "show your work" layer.
"""

import pandas as pd
from pathlib import Path

df = pd.read_csv("data/processed/master_data_clean.csv", parse_dates=["Date"])

print("=" * 60)
print("1. OVERALL REVENUE SUMMARY")
print("=" * 60)
print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()} ({len(df)} days)")
print(f"Total revenue over period: ${df['Total_Revenue'].sum():,.0f}")
print(f"Avg daily revenue: ${df['Total_Revenue'].mean():,.0f}")

# Year-over-year comparison (only use full comparable periods)
yearly = df.groupby("Year")["Total_Revenue"].agg(["sum", "mean", "count"])
print(f"\nBy year:\n{yearly}")

print("\n" + "=" * 60)
print("2. PROMOTIONAL LEVER LIFT (mean comparison, associational)")
print("=" * 60)
flags = ["Promotion_Discount", "UWG_Mailing", "Offline_Promo", "holiday_list", "BFCM_Promo_Effect"]
lift_summary = []
for flag in flags:
    on = df.loc[df[flag] == 1, "Total_Revenue"]
    off = df.loc[df[flag] == 0, "Total_Revenue"]
    lift_pct = (on.mean() - off.mean()) / off.mean() * 100
    lift_summary.append({
        "lever": flag, "days_on": len(on), "days_off": len(off),
        "avg_revenue_on": on.mean(), "avg_revenue_off": off.mean(),
        "lift_pct": lift_pct,
    })
lift_df = pd.DataFrame(lift_summary).sort_values("lift_pct", ascending=False)
print(lift_df.to_string(index=False))

print("\n" + "=" * 60)
print("3. NEW CUSTOMER ACQUISITION TREND")
print("=" * 60)
yearly_new = df.groupby("Year").apply(
    lambda x: x["Revenue_New_Customer"].sum() / x["Total_Revenue"].sum() * 100
)
print(f"New-customer revenue share by year:\n{yearly_new}")

print("\n" + "=" * 60)
print("4. MEDIA EFFICIENCY")
print("=" * 60)
print(f"Avg media spend as % of revenue: {df['Media_Pct_of_Revenue'].mean():.2f}%")
print(f"Media % on promo days:    {df.loc[df['Promotion_Discount']==1, 'Media_Pct_of_Revenue'].mean():.2f}%")
print(f"Media % on non-promo days: {df.loc[df['Promotion_Discount']==0, 'Media_Pct_of_Revenue'].mean():.2f}%")

channel_totals = df[["spend_Google", "spend_Meta", "microsoft_spend", "criteo_spend",
                      "cost_outbrain", "Awin_spend", "influencer_spend"]].sum().sort_values(ascending=False)
print(f"\nTotal spend by channel (period total):\n{channel_totals}")
print(f"\nChannel share of total paid media:\n{(channel_totals / channel_totals.sum() * 100).round(1)}")

print("\n" + "=" * 60)
print("5. BRAND SEARCH & AFFILIATE - DEMAND CAPTURE QUESTION")
print("=" * 60)
# Does brand search spend correlate with revenue, or does it just track promo days?
brand_promo_corr = df[["spend_Google_Branded", "Awin_spend", "Total_Revenue", "Promotion_Discount"]].corr()
print(f"Correlation matrix:\n{brand_promo_corr}")