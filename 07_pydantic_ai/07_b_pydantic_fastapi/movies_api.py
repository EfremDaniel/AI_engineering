from fastapi import FastAPI
from agent import movie_agent
from data_models import Prompt
from utils import querry_duckdb

app = FastAPI()

@app.get("/movies")
async def read_movies():
    movies = querry_duckdb("FROM movies;")
    return movies.to_dict(orient="records")

@app.post("/movies/create_movie")
async def create_movies(query:Prompt):
    result = await movie_agent.run(query.prompt)
    movie = result.output

    querry_duckdb(""" 
    INSERT INTO movies VALUES (?,?,?,?)""", parameters=[movie.title, movie.year, movie.genre, movie.rating]
    )

    return movie