import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the Excel file
file_path = "trial_wordmap.xlsx"  # Change this to your file path
sheet_name = None  # Set to None to read the first sheet, or specify the sheet name

# Read all sheets
df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")

# If the Excel file has multiple sheets, merge them into one DataFrame
if isinstance(df, dict):
    df = pd.concat(df.values(), ignore_index=True)

# Convert all cells to strings and flatten the DataFrame
text_data = " ".join(df.astype(str).values.flatten())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
