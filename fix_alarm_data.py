import pandas as pd

# === SETTINGS ===
INPUT_CSV = 'test_this.csv'    # Change this to your actual CSV filename
DATE_COLUMN = 'alarm_date'     # Your date column

# === MAIN SCRIPT ===

# Load the CSV
df = pd.read_csv(INPUT_CSV)

# Try parsing the alarm_date column with multiple formats
df[DATE_COLUMN] = pd.to_datetime(
    df[DATE_COLUMN],
    format='%d/%m/%y', 
    errors='coerce'
)

# Find rows that failed parsing (NaT) and try parsing them again with ISO format
mask_failed = df[DATE_COLUMN].isna()
df.loc[mask_failed, DATE_COLUMN] = pd.to_datetime(
    df.loc[mask_failed, DATE_COLUMN],
    format='%Y-%m-%d',
    errors='coerce'
)

# Final check: drop any remaining bad rows or handle as needed
df = df.dropna(subset=[DATE_COLUMN])

# Save dates in consistent dd/mm/yyyy format
df[DATE_COLUMN] = df[DATE_COLUMN].dt.strftime('%d/%m/%Y')

# Write back to the same CSV
df.to_csv(INPUT_CSV, index=False)

print(f"✅ Cleaned dates and saved back to {INPUT_CSV}")
