from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
# Importamos el modelos BD User
from ..database import User
# Llamamos a los modelos de validacion schemas 
from ..schemas import UserRequestModel
from ..schemas import UserResponseModel
from ..schemas import ReviewResponseModel
# Importamos librerias para login 
from fastapi.security import HTTPBasicCredentials
# Importamos libreria que permite el uso de cookies para autenticacion
from fastapi import Cookie
# OAuth2 
from fastapi import Depends
from ..common import oauth2_schema
from ..common import get_current_user



router = APIRouter(prefix='/users')


@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    # Validacion de usuarios duplicados 
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(status_code=409, detail='El username ya se encuentra en uso.')
   
    hash_password = User.create_password(user.password)

    user = User.create(
        username = user.username,
        # Reemplazamos el texto plano por el hash 
        password = hash_password
    )
    
    return user




# Login 
@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):

    #Buscamos en la BD el primer registro que cumpla con la condicion 
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    
    #Comparamos las contrasenias
    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=404, detail='Error de password')
   

    response.set_cookie(key='user_id', value=user.id) #token
    return user


# Codigo Get reviews con cookies 
"""
# Listado de resñas de un usurio autenticado
@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_userauth_reviews(page: int = 1, limit: int = 2, user_id: int = Cookie(None)):
    
    # Obtenemos el usuario que esta autenticado haciendo consulta 
    user = User.select().where(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    

    # el reviews del user.reviews es del atributo backref del modelo de BD
    return [ user_review for user_review in user.reviews.paginate(page,limit) ]

"""


# Listado de reseñas de un usurio autenticado con OAuth2
@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_oauth_reviews( page: int = 1, limit: int = 2, user: User = Depends(get_current_user)):
    
    return [ user_review for user_review in user.reviews.paginate(page,limit) ]





