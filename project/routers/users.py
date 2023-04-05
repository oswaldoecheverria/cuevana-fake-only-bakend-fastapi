from fastapi import APIRouter
from fastapi import HTTPException
# Importamos el modelos BD User
from ..database import User
# Llamamos a los modelos de validacion schemas 
from ..schemas import UserRequestModel
from ..schemas import UserResponseModel
# Importamos librerias para login 
from fastapi.security import HTTPBasicCredentials


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
async def login(credentials: HTTPBasicCredentials):

    #Buscamos en la BD el primer registro que cumpla con la condicion 
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    
    #Comparamos las contrasenias
    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=404, detail='Error de password')
   

    return user




