import pandas as pd
import folium
from dotenv import load_dotenv
from folium.plugins import HeatMap
from datetime import datetime
from branca.element import Element

# === CONFIG ===
CSV_FILE = 'final_data.csv'
LAT_COL = 'latitude'
LNG_COL = 'longitude'
OUTPUT_HTML = 'heatmap.html'
AUTHOR_NAME = 'Adrian Kombe and Abbigail Kinaro'

# === LOAD DATA ===
df = pd.read_csv(CSV_FILE)

# Drop missing lat/lng
df = df.dropna(subset=[LAT_COL, LNG_COL])

# Convert lat/lng to numeric
df[LAT_COL] = pd.to_numeric(df[LAT_COL], errors='coerce')
df[LNG_COL] = pd.to_numeric(df[LNG_COL], errors='coerce')

# Drop any rows still containing NaNs
df = df.dropna(subset=[LAT_COL, LNG_COL])

# === CREATE BASE MAP CENTERED ON MEAN LOCATION ===
map_center = [df[LAT_COL].mean(), df[LNG_COL].mean()]
m = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB dark_matter')

# === PREPARE HEATMAP DATA (NO WEIGHT) ===
heat_data = df[[LAT_COL, LNG_COL]].values.tolist()

# Add heatmap layer
HeatMap(
    heat_data,
    radius=20,
    blur=15,
    min_opacity=0.3,
    gradient={
        "0.2": 'blue',
        "0.4": 'lime',
        "0.6": 'yellow',
        "0.8": 'orange',
        "1.0": 'red'
    }
).add_to(m)

# === ADD PINK SPOTS FROM CENTROID FILE ===
centroids_df = pd.read_csv("cluster_centroids.csv")

# Drop any missing or invalid values
centroids_df = centroids_df.dropna(subset=['latitude', 'longitude'])

# Add pink circle markers for each centroid
for _, row in centroids_df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=7,
        color='deeppink',
        fill=True,
        fill_color='deeppink',
        fill_opacity=0.9,
        popup=f"Centroid: ({row['latitude']:.4f}, {row['longitude']:.4f})"
    ).add_to(m)

# === ADD WHITE DOTS FOR FIRE STATIONS ===
stations_df = pd.read_csv("firestations.csv")

# Drop rows with missing values
stations_df = stations_df.dropna(subset=['latitude', 'longitude'])

# Add white markers for fire stations
for _, row in stations_df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='white',
        fill=True,
        fill_color='white',
        fill_opacity=0.95,
        popup=f"Fire Station: ({row['latitude']:.4f}, {row['longitude']:.4f})"
    ).add_to(m)


# === ADD TOP BANNER ===
today = datetime.today().strftime('%B %d, %Y')
banner_html = f"""
<style>
    .custom-banner {{
        position: fixed;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 8px 20px;
        font-family: Arial, sans-serif;
        font-size: 14px;
        border-radius: 10px;
        z-index: 9999;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }}
</style>
<div class="custom-banner">
    Created by {AUTHOR_NAME} — {2025}
</div>
"""
# === ADD LEGEND ON RIGHT SIDE ===
legend_html = """
<style>
    .custom-legend {
        position: fixed;
        top: 70px;
        right: 20px;
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 10px 15px;
        font-family: Arial, sans-serif;
        font-size: 13px;
        border-radius: 10px;
        z-index: 9998;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        max-width: 220px;
    }
    .legend-item {
        display: flex;
        align-items: center;
        margin-bottom: 6px;
    }
    .legend-color {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
        flex-shrink: 0;
    }
</style>
<div class="custom-legend">
    <div class="legend-item">
        <div class="legend-color" style="background: red;"></div>
        <span>Higher Incident Density</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background: blue;"></div>
        <span>Lower Incident Density</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background: deeppink;"></div>
        <span>Cluster Centroids</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background: white; border: 1px solid #ccc;"></div>
        <span>Fire Stations</span>
    </div>
</div>
"""


m.get_root().html.add_child(Element(legend_html))



m.get_root().html.add_child(Element(banner_html))

# === SAVE HTML ===
m.save(OUTPUT_HTML)
print(f"✅ Heatmap saved to {OUTPUT_HTML}")
