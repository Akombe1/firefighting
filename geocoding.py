import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# === SETTINGS ===
INPUT_CSV = 'concatenated_address.csv'  # CSV must have a column named 'address'
OUTPUT_CSV = 'geocoded_addresses.csv'
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
    df = pd.read_csv(INPUT_CSV)

    # Ensure columns for lat/lng
    if 'latitude' not in df.columns:
        df['latitude'] = None
    if 'longitude' not in df.columns:
        df['longitude'] = None

    for i, row in df.iterrows():
        if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
            continue  # Skip if already geocoded

        lat, lng = geocode_address(row['full_address'])  # <- FIXED HERE
        df.at[i, 'latitude'] = lat
        df.at[i, 'longitude'] = lng
        time.sleep(WAIT_BETWEEN_CALLS)

        print(f"✅ Row {i} — {row['full_address']} → ({lat}, {lng})")


    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n🎉 Done! Saved results to {OUTPUT_CSV}")

if __name__ == '__main__':
    main()
