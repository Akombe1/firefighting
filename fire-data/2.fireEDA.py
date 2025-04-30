# firePredictions_cleaned.py (or inside Jupyter Notebook)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Fire Theme Style
sns.set(style="whitegrid", palette="rocket")

# Create a folder to save plots if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

fireData = pd.read_csv('fireData.csv')

# Clean Date columns
fireData['alarm_date'] = pd.to_datetime(fireData['alarm_date'], errors='coerce')
fireData['alarm_time'] = pd.to_datetime(fireData['alarm_time'], errors='coerce')

# Extract year, month, hour
fireData['year'] = fireData['alarm_date'].dt.year
fireData['month'] = fireData['alarm_date'].dt.month
fireData['day_of_week'] = fireData['alarm_date'].dt.day_name()
fireData['alarm_hour'] = fireData['alarm_time'].dt.hour

# -----------------------------------------------------------
# 1. Monthly Incident Trends
plt.figure(figsize=(10,6))
sns.countplot(x='month', data=fireData, palette="flare", order=range(1,13))
plt.title('Number of Fire Incidents per Month', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.savefig('plots/incidents_per_month.png', dpi=300)
plt.close()

# -----------------------------------------------------------
# 2. Top 10 Fire Incident Types
top_incidents = fireData['incident_description'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_incidents.values, y=top_incidents.index, palette="rocket")
plt.title('Top 10 Fire Incident Types', fontsize=16)
plt.xlabel('Number of Incidents')
plt.ylabel('Incident Type')
plt.tight_layout()
plt.savefig('plots/top_incident_types.png', dpi=300)
plt.close()

# -----------------------------------------------------------
# 3. Top 10 Neighborhoods
top_neighborhoods = fireData['neighborhood'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_neighborhoods.values, y=top_neighborhoods.index, palette="magma")
plt.title('Top 10 Neighborhoods with Most Incidents', fontsize=16)
plt.xlabel('Number of Incidents')
plt.ylabel('Neighborhood')
plt.tight_layout()
plt.savefig('plots/top_neighborhoods.png', dpi=300)
plt.close()

# -----------------------------------------------------------
# 4. Heatmap: Day of Week vs Hour
heatmap_data = fireData.pivot_table(index='day_of_week', columns='alarm_hour', aggfunc='size', fill_value=0)
# Order the days correctly
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data.reindex(ordered_days)

plt.figure(figsize=(14,8))
sns.heatmap(heatmap_data, cmap="YlOrRd")
plt.title('Heatmap of Incidents by Day and Hour', fontsize=18)
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week')
plt.tight_layout()
plt.savefig('plots/heatmap_day_hour.png', dpi=300)
plt.close()

# -----------------------------------------------------------
# 5. Property Loss by Incident Type
loss_by_type = (fireData.groupby('incident_description')['estimated_property_loss']
                .sum()
                .sort_values(ascending=False)
                .head(10))

plt.figure(figsize=(12,6))
sns.barplot(x=loss_by_type.values, y=loss_by_type.index, palette="flare")
plt.title('Top 10 Incident Types by Total Property Loss', fontsize=16)
plt.xlabel('Total Property Loss ($)')
plt.ylabel('Incident Type')
plt.tight_layout()
plt.savefig('plots/property_loss_by_type.png', dpi=300)
plt.close()

# -----------------------------------------------------------
# 6. Yearly Trends
plt.figure(figsize=(10,6))
sns.countplot(x='year', data=fireData, palette="coolwarm")
plt.title('Number of Fire Incidents by Year', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/incidents_by_year.png', dpi=300)
plt.close()

# -----------------------------------------------------------

print("🔥 All plots created and saved inside 'plots/' folder successfully!")