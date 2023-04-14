import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from .database import User
from fastapi import status



SECRET_KEY = 'desoxirribonucleico2023'

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')

# Funcion encargada de crear el access token y codificarlo 
def create_access_token(user, days=7):
     
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


# Funcion que decodifica el token 
def decode_access_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as err:
        return None

# Funcion que reibe el access token 
def get_current_user(token: str = Depends(oauth2_schema)) -> User:
    data = decode_access_token(token)

    if data:
        return User.select().where(User.id == data['user_id']).first()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access Token No valido',
            headers={'WWW-Autenticate': 'beraer'}
        )

