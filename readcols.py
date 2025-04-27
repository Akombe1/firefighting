import pandas as pd

def list_csv_columns(file_path):
    try:
        df = pd.read_csv(file_path, nrows=0)  # Only read header row
        columns = df.columns.tolist()
        print("📄 Columns in CSV:")
        for col in columns:
            print(f" - {col}")
        return columns
    except Exception as e:
        print(f"❌ Failed to read CSV: {e}")
        return []

# Call the function AFTER it's defined, and use quotes around the path
list_csv_columns("new_fire_data.csv")
