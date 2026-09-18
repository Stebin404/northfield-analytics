@"
# Northfield & Co. — Analytics Case Study

Business dashboard and analysis for Northfield & Co., a US mass-market
casual apparel e-commerce brand. Built from 852 days (Apr 2024-Jul 2026)
of daily revenue and marketing spend data.

## Structure
- ``data/raw/`` - extracted source data (CSV, one file per original sheet)
- ``data/processed/`` - cleaned, analysis-ready data
- ``notebooks/`` - exploratory data analysis
- ``src/`` - ingestion, cleaning, and analysis scripts
- ``dashboard/`` - Streamlit app
- ``reports/`` - findings & recommendations write-up
- ``powerbi/`` - Power BI dashboard (optional)

## Setup
``````bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
``````

## Run the dashboard
``````bash
streamlit run dashboard/app.py
``````
"@ | Out-File -Encoding utf8 README.md

## Power BI Dashboard

Open `powerbi/northfield_dashboard.pbix` in Power BI Desktop (free download
from Microsoft). The report has 4 pages:
1. Revenue Overview — headline KPIs and daily revenue trend
2. Promo & Mailing Impact — lift analysis by promotional lever
3. Media Mix — channel spend breakdown and efficiency
4. Findings & Recommendations — narrative summary

A static PDF export is also available at `powerbi/northfield_dashboard.pdf`
for reviewers without Power BI installed.

Data source: `data/processed/master_data_clean.csv` (see `src/cleaning.py`
for how it was derived from the raw workbook).