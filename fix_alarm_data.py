import pandas as pd

# === SETTINGS ===
INPUT_CSV = 'final_data.csv'
OUTPUT_CSV = 'final_data_cleaned.csv'
DATE_COLUMN = 'alarm_date'

# === LOAD DATA ===
df = pd.read_csv(INPUT_CSV, low_memory=False)
df[DATE_COLUMN] = df[DATE_COLUMN].astype(str).str.strip()

# === TRY MULTIPLE DATE FORMATS ===
parsed_dates = pd.Series(pd.NaT, index=df.index)

formats_to_try = [
    "%Y-%m-%d",    # ISO format
    "%d/%m/%y",    # e.g. 11/12/20
    "%d/%m/%Y",    # e.g. 03/03/2021
    "%m/%d/%y",    # US-style
    "%m/%d/%Y"     # US-style full year
]

for fmt in formats_to_try:
    mask = parsed_dates.isna()
    parsed = pd.to_datetime(df.loc[mask, DATE_COLUMN], format=fmt, errors='coerce')
    parsed_dates.loc[mask] = parsed

# Assign cleaned date column back
df[DATE_COLUMN] = parsed_dates

# Drop rows with unparsed dates
before = len(df)
df = df.dropna(subset=[DATE_COLUMN])
after = len(df)
print(f"✅ Parsed dates. Dropped {before - after} rows with unrecognized dates.")

# === SAVE CLEANED CSV ===
df.to_csv(OUTPUT_CSV, index=False)
print(f"📁 Cleaned file saved as '{OUTPUT_CSV}'")
