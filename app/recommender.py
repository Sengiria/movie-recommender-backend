import numpy as np

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot / (norm1 * norm2)

def recommend_movies(movie_id, movies, movie_vectors, id_to_index, limit=5):
    index = id_to_index[str(movie_id)]
    query_vector = movie_vectors[index]

    # Compute similarity with all other movies
    similarities = []
    for i, vector in enumerate(movie_vectors):
        if i == index:
            continue  # skip itself
        sim = cosine_similarity(query_vector, vector)
        similarities.append((i, sim))

    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Get top N
    recommended = []
    for idx, score in similarities[:limit]:
        movie = movies[idx].copy()
        movie["similarity"] = round(score, 4)
        recommended.append(movie)

    return recommended