import pandas as pd

# === SETTINGS ===
INPUT_CSV = 'confirmedFires_fixed.csv'        # Change this to your input file
OUTPUT_CSV = 'rounded_file.csv'     # Output file after rounding
LAT_COLUMN = 'latitude'
LON_COLUMN = 'longitude'
DECIMALS = 5

# === MAIN SCRIPT ===

def main():
    # Load the CSV
    df = pd.read_csv(INPUT_CSV)

    # Round latitude and longitude to 5 decimal places
    df[LAT_COLUMN] = df[LAT_COLUMN].round(DECIMALS)
    df[LON_COLUMN] = df[LON_COLUMN].round(DECIMALS)

    # Save the updated CSV
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ Done! Saved rounded coordinates to '{OUTPUT_CSV}'.")

if __name__ == '__main__':
    main()
