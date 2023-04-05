from typing import List
from fastapi import APIRouter, HTTPException
# Importamos el modelos BD Movie
from ..database import Movie
# Llamamos a los modelos de validacion schemas 
from ..schemas import MovieRequestModel
from ..schemas import MovieResponseModel


router = APIRouter(prefix='/movies')

@router.post('', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):

    if Movie.select().where(Movie.title == movie.title).exists():
        raise HTTPException(status_code=409, detail='El titulo ya se encuentra registrado')
    
    movie = Movie.create(
        title = movie.title
    )

    return movie



# Endpoint - Listar peliculas
@router.get('', response_model=List[MovieResponseModel])
async def get_reviews():
    movies = Movie.select()

    return [ list_movie for list_movie in movies ]

