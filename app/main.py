from fastapi import FastAPI, HTTPException
from fastapi_cache2 import FastAPICache
from fastapi_cache2.backends.inmemory import InMemoryBackend
from fastapi_cache2.decorator import cache
from .data_loader import load_movies
from .recommender import recommend_movies
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI(default_response_class=ORJSONResponse)

# Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Load movie data on startup
movies, movie_vectors, id_to_index = load_movies()

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/movies")
@cache(expire=60 * 5)
def get_movies():
    return movies

@app.get("/recommend")
def recommend(movie_id: int, limit: int = 5):
    if str(movie_id) not in id_to_index:
        raise HTTPException(status_code=404, detail="Movie not found")
    recommendations = recommend_movies(movie_id, movies, movie_vectors, id_to_index, limit)
    return recommendations
