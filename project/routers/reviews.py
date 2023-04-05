from typing import List
from fastapi import APIRouter, HTTPException
# Importamos los modelos de BD
from ..database import UserReview
from ..database import User
from ..database import Movie
# Importamos los schemas 
from ..schemas import ReviewRequestModel
from ..schemas import ReviewResponseModel



router = APIRouter(prefix='/reviews')



# Endpoint - Agregar reseña
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



# # Endpoint - Listar todas las reseñas 
# @router.get('', response_model=List[ReviewResponseModel])
# async def get_reviews():
#     reviews = UserReview.select()

#     # Creamos un listado de objetos de UserReview, los cuales ya pudieron ser serializados
#     return [ user_review for user_review in reviews ]



# Endpoint - Listar todas las reseñas con paginacion
@router.get('', response_model=List[ReviewResponseModel])
async def pagination_get_reviews(page: int = 1, limit: int =3):
    reviews = UserReview.select().paginate(page, limit)

    # Creamos un listado de objetos de UserReview, los cuales ya pudieron ser serializados
    return [ user_review for user_review in reviews ]



# Endpoint - Listar reseña especifica por id
@router.get('/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None:
        raise HTTPException(status_code=404, detail='Reseña no encontrada')
    
    return user_review

