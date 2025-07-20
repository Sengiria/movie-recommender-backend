import json
import numpy as np

def load_movies(
    metadata_path="data/movies.json",
    vectors_path="data/movie_vectors.npy"
):
    with open(metadata_path, "r", encoding="utf-8") as f:
        movies = json.load(f)

    movie_vectors = np.load(vectors_path)

    # Map movie ID to index in the list
    id_to_index = {str(movie["id"]): idx for idx, movie in enumerate(movies)}

    return movies, movie_vectors, id_to_index
