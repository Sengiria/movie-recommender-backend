import kagglehub
import os
import pandas as pd
import ast

# Download latest version
path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
csv_path = os.path.join(path, "tmdb_5000_movies.csv")

# Load CSV
df = pd.read_csv(csv_path)

# Filter out bad entries
df = df.dropna(subset=["overview"])
df = df[df["overview"].str.len() > 20]
df = df.drop_duplicates(subset=["title"])

#Parse 'genres' JSON string into Python list
def parse_genres(genre_str):
    try:
        genre_list = ast.literal_eval(genre_str)
        return [genre["name"] for genre in genre_list]
    except:
        return []

df["genres"] = df["genres"].apply(parse_genres)

#Select relevant columns
df_clean = df[["id", "title", "overview", "genres", "vote_average", "release_date"]]

# Save to JSON
output_path = "movies.json"
df_clean.to_json(output_path, orient="records", indent=2)

print(f"✅ Cleaned dataset saved to {output_path}")
print(f"🎬 Total movies: {len(df_clean)}")