from fastapi import APIRouter, HTTPException
# Importamos los modelos de BD
from ..database import UserReview
from ..database import User
from ..database import Movie
# Importamos los schemas 
from ..schemas import ReviewRequestModel
from ..schemas import ReviewResponseModel



router = APIRouter(prefix='/reviews')


@router.post('', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):

    
    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail='El usurio no se ha encontrado')

    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')


    user_review = UserReview.create(
        # Las siguinetes variables son las creadas en el modelo 
        # de validacion ReviewRequestModel
        user_id=user_review.user_id,
        movie_id=user_review.movie_id,
        review=user_review.review,
        score=user_review.score
    )

    return user_review
