import pandas as pd
import matplotlib.pyplot as plt

# === SETTINGS ===
INPUT_CSV = 'confirmed_fires_all_columns.csv'    # Change to your actual CSV file name
TIME_COLUMN = 'alarm_time'
PLOT_TITLE = 'Fire Incidents by Hour of the Day'
OUTPUT_IMAGE = '24hourday.png'

# === MAIN SCRIPT ===

# Load the CSV
df = pd.read_csv(INPUT_CSV)

# Parse the time column
df[TIME_COLUMN] = pd.to_datetime(df[TIME_COLUMN], format='%H:%M:%S', errors='coerce')

# Drop rows with invalid times
df = df.dropna(subset=[TIME_COLUMN])

# Extract hour from time
df['hour'] = df[TIME_COLUMN].dt.hour

# Count incidents by hour
hour_counts = df['hour'].value_counts().sort_index()

# === PLOTTING ===
plt.style.use('seaborn-v0_8-deep')  # Modern, clean style

plt.figure(figsize=(12, 6))
plt.bar(hour_counts.index, hour_counts.values, width=0.8)

plt.xticks(range(0, 24))
plt.xlabel('Hour of Day')
plt.ylabel('Number of Incidents')
plt.title(PLOT_TITLE)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot
plt.tight_layout()
plt.savefig(OUTPUT_IMAGE, dpi=300)
