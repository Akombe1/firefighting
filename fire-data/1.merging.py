import pandas as pd
import os

def merge_fire_datasets(save_path='fireData.csv'):
    # Load datasets
    file1 = pd.read_csv(file1_path)
    file2 = pd.read_csv(file2_path)
    file3 = pd.read_csv(file3_path)

    # Standardize column names (lowercase, no spaces)
    def standardize_columns(df):
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        return df

    file1 = standardize_columns('tmpxj6igizd.csv')
    file2 = standardize_columns('76771c63-2d95-4095-bf3d-5f22844350d8.csv')
    file3 = standardize_columns('2012-bostonfireincidentopendata.csv')

    # Drop '_id' column from file3 if exists
    if '_id' in file3.columns:
        file3 = file3.drop(columns=['_id'])

    # Concatenate all three files
    fireData = pd.concat([file1, file2, file3], ignore_index=True)

    # Standardize 'alarm_date' column to YYYY-MM-DD
    fireData['alarm_date'] = pd.to_datetime(fireData['alarm_date'], errors='coerce')
    fireData['alarm_date'] = fireData['alarm_date'].dt.strftime('%Y-%m-%d')

    # Save merged dataset
    fireData.to_csv(save_path, index=False)
    print(f"🔥 fireData saved successfully to {save_path}!")

    return fireData