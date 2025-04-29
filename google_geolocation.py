import pandas as pd
import time
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import os
from dotenv import load_dotenv


# === SETTINGS ===
CSV_FILE = 'final_data.csv'
ADDRESS_COLUMN = 'full_address'
LAT_COLUMN = 'latitude'
LON_COLUMN = 'longitude'
load_dotenv("pass.env")
api_key = os.getenv("GOOGLE_API_KEY")

# === INITIALIZE GEOCODER ===
geolocator = GoogleV3(api_key=GOOGLE_API_KEY, timeout=10)

def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"⚠️ Not found: {address}")
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"⏳ Geocoding error for '{address}': {e}")
        return None, None

def main():
    df = pd.read_csv(CSV_FILE)

    # Ensure lat/lon columns exist
    if LAT_COLUMN not in df.columns:
        df[LAT_COLUMN] = None
    if LON_COLUMN not in df.columns:
        df[LON_COLUMN] = None

    # Step 1: Get unique addresses that still need geocoding
    mask_missing = df[LAT_COLUMN].isna() | df[LON_COLUMN].isna()
    unique_addresses = df.loc[mask_missing, ADDRESS_COLUMN].dropna().unique()

    print(f"🌍 {len(unique_addresses)} unique addresses to geocode...")

    coords_dict = {}
    for i, address in enumerate(unique_addresses):
        lat, lon = geocode_address(address)
        coords_dict[address] = (lat, lon)

        print(f"✅ [{i+1}/{len(unique_addresses)}] {address} → ({lat}, {lon})")
        time.sleep(0.01)  # Keep it light (optional, Google allows decent throughput)

        if (i + 1) % 100 == 0:
            print("💾 Saving progress...")
            df[LAT_COLUMN] = df[ADDRESS_COLUMN].map(lambda x: coords_dict.get(x, (None, None))[0])
            df[LON_COLUMN] = df[ADDRESS_COLUMN].map(lambda x: coords_dict.get(x, (None, None))[1])
            df.to_csv(CSV_FILE, index=False)

    # Final assignment and save
    df[LAT_COLUMN] = df[ADDRESS_COLUMN].map(lambda x: coords_dict.get(x, (None, None))[0])
    df[LON_COLUMN] = df[ADDRESS_COLUMN].map(lambda x: coords_dict.get(x, (None, None))[1])
    df.to_csv(CSV_FILE, index=False)

    print(f"\n🎉 Done! Geocoded data saved to {CSV_FILE}")

if __name__ == '__main__':
    main()
