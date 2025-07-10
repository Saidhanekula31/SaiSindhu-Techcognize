import pandas as pd

df = pd.read_csv("C:/Users/sindhu/netflix-shows/netflix_titles.csv")


df = df.dropna(subset=['director'])


df['content_age'] = 2025 - df['release_year']


df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df = df.dropna(subset=['date_added'])


df['added_year'] = df['date_added'].dt.year


df_tv = df[df['type'] == 'TV Show']

# Save the transformed data
df_tv.to_csv("C:/Users/sindhu/netflix-shows/netflix_transformed.csv", index=False)

print("✅ Transformations complete. Transformed file saved.")
