import pandas as pd
import folium
from folium.plugins import HeatMap
from datetime import datetime
from branca.element import Element

# === CONFIG ===
CSV_FILE = 'final_data.csv'
LAT_COL = 'latitude'
LNG_COL = 'longitude'
OUTPUT_HTML = 'heatmap.html'
AUTHOR_NAME = 'Adrian Kombe'

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
    Created by {AUTHOR_NAME} — {today}
</div>
"""

m.get_root().html.add_child(Element(banner_html))

# === SAVE HTML ===
m.save(OUTPUT_HTML)
print(f"✅ Heatmap saved to {OUTPUT_HTML}")
