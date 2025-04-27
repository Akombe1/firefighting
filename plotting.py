import pandas as pd
import matplotlib.pyplot as plt

# === SETTINGS ===
INPUT_CSV = 'test_this.csv'    # Change this to your actual file name
DATE_COLUMN = 'alarm_date'           # Change this to the actual name of your date column
OUTPUT_IMAGE = 'incidents_per_year.png'

# === MAIN SCRIPT ===

# Load the CSV
df = pd.read_csv(INPUT_CSV)

# Parse the date column
df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN], format='%d/%m/%Y', errors='coerce')

# Drop rows where date parsing failed
df = df.dropna(subset=[DATE_COLUMN])

# Extract the year
df['year'] = df[DATE_COLUMN].dt.year

# Count incidents per year
year_counts = df['year'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10,6))
plt.bar(year_counts.index, year_counts.values)
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.title('Incidents per Year')
plt.xticks(year_counts.index, rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig(OUTPUT_IMAGE)

print(f"Saved bar chart to {OUTPUT_IMAGE}")
