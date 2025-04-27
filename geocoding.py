import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# === SETTINGS ===
CSV_FILE = 'dated_fires.csv'  # Same file for reading and writing
WAIT_BETWEEN_CALLS = 1  # seconds, to respect API usage limits

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

    for i, row in df.iterrows():
        if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
            continue  # Skip if already geocoded

        lat, lng = geocode_address(row['full_address'])  # Using the full_address column
        df.at[i, 'latitude'] = lat
        df.at[i, 'longitude'] = lng
        time.sleep(WAIT_BETWEEN_CALLS)

        print(f"✅ Row {i} — {row['full_address']} → ({lat}, {lng})")

    # Save back to the SAME FILE
    df.to_csv(CSV_FILE, index=False)
    print(f"\n🎉 Done! Updated '{CSV_FILE}' with geocoded coordinates!")

if __name__ == '__main__':
    main()
    