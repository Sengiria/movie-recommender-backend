# AI Movie Recommender – Backend

This is the backend for the AI-powered movie recommendation system. It is built using **FastAPI** and provides endpoints to fetch movie data and generate content-based recommendations using precomputed sentence embeddings.

---

## Tech Stack

- **Python 3**
- **FastAPI**
- **NumPy**
- **Uvicorn** (ASGI server)
- **CORS Middleware**
- **JSON** (for data storage)

---

## Project Structure

<pre>backend/
├── app/
│ ├── main.py
│ ├── data_loader.py
│ ├── recommender.py
├── data/
│ ├── movies.json
│ ├── movies_with_embeddings.json
├── scripts/
│ ├── movies-cleanup.py
│ ├── embed_movies.py
├── .gitignore
├── README.md
</pre>

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-movie-recommender-backend.git
cd ai-movie-recommender-backend
```

### 2. Create a virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3.  Start the server

```bash
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs for interactive Swagger UI.

## API Endpoints

| Method    | Endpoint | Description |
| -------- | ------- | ------- |
| GET  | /ping    | Health check |
| GET | /movies     | Returns all movie data |
| GET    | /recommend?movie_id={ID}?limit={limit}    | Get similar movies by ID |

Example:

```bash
 /recommend?movie_id=12&limit=5
```

---

## Notes

- Recommendations are content-based using cosine similarity between sentence embeddings of movie descriptions.
- Embeddings are precomputed using Sentence-BERT and stored in movies_with_embeddings.json.

## License
MIT – feel free to use and modify for your own projects!