import pandas as pd
import time
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# === SETTINGS ===
CSV_FILE = 'confirmedFires_fixed.csv'  # Same file for reading and writing
WAIT_BETWEEN_CALLS = 0.05  # seconds, to respect API usage limits

load_dotenv("pass.env")
api_key = os.getenv("API_KEY")

# === INITIALIZE GEOCODER ===
geolocator = Nominatim(user_agent="open-geocoder-script")

def geocode_address(address):
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"⚠️ Address not found: {address}")
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"⏳ Geocoding error for '{address}': {e}")
        return None, None

# === MAIN ===

def main():
    df = pd.read_csv(CSV_FILE)

    # Create latitude and longitude columns if they don't exist
    if 'latitude' not in df.columns:
        df['latitude'] = None
    if 'longitude' not in df.columns:
        df['longitude'] = None

    start_index = 9403  # 👈 Start at row 9403

    for i, row in df.iloc[start_index:].iterrows():
        if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
            continue  # Skip if already geocoded

        lat, lng = geocode_address(row['full_address'])  # Using the full_address column
        df.at[i, 'latitude'] = lat
        df.at[i, 'longitude'] = lng
        time.sleep(WAIT_BETWEEN_CALLS)

        print(f"✅ Row {i} — {row['full_address']} → ({lat}, {lng})")

        # 🔥 Save progress every 100 rows
        if i % 100 == 0 and i != 0:
            df.to_csv(CSV_FILE, index=False)
            print(f"💾 Auto-saved after {i} rows...")

    # Final save after all rows are done
    df.to_csv(CSV_FILE, index=False)
    print(f"\n🎉 Done! Updated '{CSV_FILE}' with geocoded coordinates!")
if __name__ == '__main__':
    main()