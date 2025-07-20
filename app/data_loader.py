import json
import numpy as np

def load_movies(path="data/movies_with_embeddings.json"):
    with open(path, "r", encoding="utf-8") as f:
        movies = json.load(f)

    # Extract vectors
    movie_vectors = np.array([movie["embedding"] for movie in movies])

    # Map movie ID to index in the list
    id_to_index = {str(movie["id"]): idx for idx, movie in enumerate(movies)}

    return movies, movie_vectors, id_to_index
