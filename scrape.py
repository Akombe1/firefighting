import pandas as pd
import requests
import time

# === SETTINGS ===
API_KEY = 'AIzaSyAD4JYQV0uGRwQYmOkz1WJBS_95sjc2SNo'
INPUT_CSV = 'addresses.csv'
OUTPUT_CSV = 'addresses_with_coordinates.csv'
WAIT_BETWEEN_CALLS = 0.1  # seconds
SAVE_INTERVAL = 50        # Save progress every N rows

def geocode_address(address, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={requests.utils.quote(address)}&key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Geocoding failed for '{address}' with status: {data['status']}")
        return None, None

# === MAIN ===
df = pd.read_csv(INPUT_CSV)
if 'latitude' not in df.columns:
    df['latitude'] = None
    df['longitude'] = None

for i, row in df.iterrows():
    if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
        continue  # Skip already processed rows
    
    lat, lng = geocode_address(row['address'], API_KEY)
    df.at[i, 'latitude'] = lat
    df.at[i, 'longitude'] = lng
    time.sleep(WAIT_BETWEEN_CALLS)

    if i % SAVE_INTERVAL == 0:
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"[Checkpoint] Saved progress at row {i}")

# Final save
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Done. Final output written to {OUTPUT_CSV}")
