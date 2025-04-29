import pandas as pd

# === SETTINGS ===
INPUT_CSV = 'confirmed_fires_all_columns.csv'
OUTPUT_CSV = 'final_data.csv'

# === MAIN ===
def combine_address_components(file_path):
    try:
        df = pd.read_csv(file_path)

        # Fill NaNs with empty strings to avoid issues during concatenation
        df = df.fillna('')

        # Combine components into one full address string with fixed city and state
        df['full_address'] = (
            df['street_number'].astype(str).str.strip() + ' ' +
            df['street_name'].str.strip() + ' ' +
            df['street_suffix'].str.strip() + ' ' +
            'Boston, MA ' +
            df['zip'].astype(str).str.strip()
        ).str.replace('  ', ' ').str.replace(', ,', ',').str.strip()

        # Create a new DataFrame with only full_address and alarm_date
        output_df = df[['full_address', 'alarm_date']]

        # Save the result
        output_df.to_csv(OUTPUT_CSV, index=False)
        print(f"✅ Saved combined addresses and dates to '{OUTPUT_CSV}'")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

# === RUN SCRIPT ===
combine_address_components(INPUT_CSV)
