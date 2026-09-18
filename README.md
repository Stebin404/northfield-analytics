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