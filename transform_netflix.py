import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/sindhu/netflix-shows/netflix_titles.csv")

# 1. Drop rows with missing 'director'
df = df.dropna(subset=['director'])

# 2. Create a new column for content age
df['content_age'] = 2025 - df['release_year']

# 3. Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df = df.dropna(subset=['date_added'])

# 4. Extract year from 'date_added' and add as a new column
df['added_year'] = df['date_added'].dt.year

# 5. Filter only TV Shows from the dataset
df_tv = df[df['type'] == 'TV Show']

# Save transformed data
df_tv.to_csv("C:/Users/sindhu/netflix-shows/netflix_transformed.csv", index=False)

print("✅ Transformations complete. Transformed file saved.")
