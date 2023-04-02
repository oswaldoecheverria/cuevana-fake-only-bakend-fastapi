from fastapi import APIRouter
from fastapi import HTTPException
# Importamos el modelos BD User
from ..database import User
# Llamamos a los modelos de validacion schemas 
from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

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


