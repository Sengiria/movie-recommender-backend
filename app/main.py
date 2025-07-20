from fastapi import FastAPI, HTTPException
from .data_loader import load_movies
from .recommender import recommend_movies
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load movie data on startup
movies, movie_vectors, id_to_index = load_movies()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/movies")
def get_movies():
    return movies

@app.get("/recommend")
def recommend(movie_id: int, limit: int = 5):
    if str(movie_id) not in id_to_index:
        raise HTTPException(status_code=404, detail="Movie not found")
    recommendations = recommend_movies(movie_id, movies, movie_vectors, id_to_index, limit)
    return recommendations
