from sentence_transformers import SentenceTransformer
import json

# Load cleaned movie data
with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# Load pre-trained Sentence-BERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Extract overviews
overviews = [movie["overview"] for movie in movies]

# Create embeddings
print("Generating embeddings...")
embeddings = model.encode(overviews, show_progress_bar=True)

# Attach embeddings to movies
for movie, vector in zip(movies, embeddings):
    movie["embedding"] = vector.tolist()  # Convert numpy to regular list

# Save to new file
with open("movies_with_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=2)

print("Embeddings generated and saved to movies_with_embeddings.json")

