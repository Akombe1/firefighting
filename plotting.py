import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === SETTINGS ===
INPUT_CSV = 'test_this.csv'
DATE_COLUMN = 'alarm_date'
OUTPUT_IMAGE_BAR = 'incidents_per_year.png'
OUTPUT_IMAGE_PIE = 'incidents_per_season.png'

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

# Descriptive statistics
mean_incidents = year_counts.mean()
median_incidents = year_counts.median()
total_incidents = year_counts.sum()

# --- BAR CHART: Incidents per Year ---
fig, ax = plt.subplots(figsize=(12,7))

# Bar plot
bars = ax.bar(year_counts.index, year_counts.values, width=0.6, color="#4C72B0", edgecolor='none')

# Trendline (linear fit)
z = np.polyfit(year_counts.index, year_counts.values, 1)
p = np.poly1d(z)
ax.plot(year_counts.index, p(year_counts.index), "r--", linewidth=2, label="Trendline")

# Modern styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.8)
ax.spines['bottom'].set_linewidth(0.8)
ax.set_facecolor('#f7f7f7')
fig.patch.set_facecolor('#f7f7f7')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Incidents', fontsize=14)
ax.set_title('Incidents per Year', fontsize=18, weight='bold')
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xticks(year_counts.index)
plt.xticks(rotation=45)

# Add a statistics legend box
stats_text = (f"Mean: {mean_incidents:.1f}\n"
              f"Median: {median_incidents:.1f}\n"
              f"Total: {total_incidents}")
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='gray')
ax.text(1.02, 0.5, stats_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='center', bbox=props)

# Tight layout and save
plt.tight_layout()
plt.savefig(OUTPUT_IMAGE_BAR, dpi=300)
print(f"✅ Saved bar chart to {OUTPUT_IMAGE_BAR}")

# --- PIE CHART: Incidents per Season ---

# Helper function to assign seasons
def get_season(date):
    year = date.year
    spring_start = pd.Timestamp(year=year, month=3, day=20)
    summer_start = pd.Timestamp(year=year, month=6, day=20)
    fall_start   = pd.Timestamp(year=year, month=9, day=22)
    winter_start = pd.Timestamp(year=year, month=12, day=21)
    
    if spring_start <= date < summer_start:
        return 'Spring'
    elif summer_start <= date < fall_start:
        return 'Summer'
    elif fall_start <= date < winter_start:
        return 'Fall'
    else:
        return 'Winter'

# Apply the season categorization
df['season'] = df[DATE_COLUMN].apply(get_season)

# Count incidents per season
season_counts = df['season'].value_counts()

# Pie chart
fig2, ax2 = plt.subplots(figsize=(8,8))
colors = ["#A1D99B", "#FC9272", "#9ECAE1", "#FDD0A2"]  # pastel green, pink, blue, orange
ax2.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 14})
ax2.set_title('Fire Department Calls by Season', fontsize=20, weight='bold')
fig2.patch.set_facecolor('#f7f7f7')

plt.tight_layout()
plt.savefig(OUTPUT_IMAGE_PIE, dpi=300)
print(f"✅ Saved season pie chart to {OUTPUT_IMAGE_PIE}")
