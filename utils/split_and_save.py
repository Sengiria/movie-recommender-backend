# scripts/split_and_save.py
import json
import numpy as np

with open("data/movies_with_embeddings.json", "r", encoding="utf-8") as f:
    full_data = json.load(f)

# Separate metadata and vectors
metadata = []
vectors = []

for movie in full_data:
    vectors.append(movie["embedding"])
    del movie["embedding"]
    metadata.append(movie)

# Save outputs
with open("data/movies.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

np.save("data/movie_vectors.npy", np.array(vectors))

print("✅ Split complete.")
