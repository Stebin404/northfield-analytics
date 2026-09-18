"""
src/ingestion.py

Extracts each sheet of the raw Northfield & Co. workbook into its own
CSV file under data/raw/. This is the RAW layer: an exact, untouched
copy of the source data in a version-controllable format. No cleaning
or transformation happens here — that's the job of src/cleaning.py.
"""

import pandas as pd
from pathlib import Path

RAW_XLSX = Path("data/raw/Northfield_Co_Case_Study.xlsx")
OUTPUT_DIR = Path("data/raw")

# sheet name -> output CSV filename
SHEET_FILENAMES = {
    "Your project": "project_brief.csv",
    "Business brief": "business_brief.csv",
    "Glossary": "glossary.csv",
    "Master data": "master_data.csv",   # the core dataset for analysis
}


def extract_sheets():
    if not RAW_XLSX.exists():
        raise FileNotFoundError(
            f"Expected the source workbook at {RAW_XLSX} — copy it there first."
        )

    xls = pd.ExcelFile(RAW_XLSX)
    print(f"Found sheets: {xls.sheet_names}\n")

    for sheet_name, filename in SHEET_FILENAMES.items():
        if sheet_name not in xls.sheet_names:
            print(f"  [skip] sheet not found: {sheet_name}")
            continue
        df = xls.parse(sheet_name)
        out_path = OUTPUT_DIR / filename
        df.to_csv(out_path, index=False)
        print(f"  {sheet_name!r:20s} -> {out_path}  ({df.shape[0]} rows, {df.shape[1]} cols)")


if __name__ == "__main__":
    extract_sheets()