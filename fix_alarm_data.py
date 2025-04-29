import pandas as pd

# === SETTINGS ===
INPUT_CSV = 'confirmed_fires_all_columns.csv'
DATE_COLUMN = 'alarm_date'

# === MAIN SCRIPT ===
df = pd.read_csv(INPUT_CSV, low_memory=False)  # Avoid dtype warning

# Initial cleanup for empty or NaN
df[DATE_COLUMN] = df[DATE_COLUMN].astype(str).str.strip()

# Initialize an empty Series of the same length as df
parsed_dates = pd.Series([pd.NaT] * len(df), index=df.index)

# Try a range of common formats
formats_to_try = [
    "%Y-%m-%d",    # ISO format
    "%d/%m/%y",    # e.g. 11/12/20
    "%d/%m/%Y",    # e.g. 03/03/2021
]

# Try parsing with each format and fill in the blanks as we go
for fmt in formats_to_try:
    mask_unparsed = parsed_dates.isna()
    try_parse = pd.to_datetime(df.loc[mask_unparsed, DATE_COLUMN], format=fmt, errors='coerce')
    parsed_dates.loc[mask_unparsed] = try_parse

# Update dataframe with cleaned dates
df[DATE_COLUMN] = parsed_dates

# Drop rows where parsing failed
before_drop = len
