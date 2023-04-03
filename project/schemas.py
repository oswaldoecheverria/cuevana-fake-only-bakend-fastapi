# Convierten  los datos en diccionario 
from pydantic import BaseModel
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect
# Permite validar con el decorador validator 
from pydantic import validator


# Convierte el objeto UserModel de BD a diccionario 
class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)

        if isinstance(res, ModelSelect): 
            return list(res)  
        
        return res
    

# Abstraccion - Refactor
# clase que usamos en todos los clases ResponseModel
class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# -------------  USER  ------------------

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 20:
            raise ValueError ('La longitud debe ser entre 3 y 20 caracteres.')
        
        return username
    
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 5 or len(password) > 15:
            raise ValueError ('La longitud debe ser entre 3 y 15 caracteres.')
        
        return password

# Valida los datos de respuesta al cliente, los serializa 
class UserResponseModel(ResponseModel):
    id: int
    username: str


# -------------  MOVIE  ------------------

class MovieRequestModel(BaseModel):
    title: str

    @validator('title')
    def movie_validator(cls, title):
        if len(title) < 2 or len (title) > 100:
            raise ValueError ('La longitud debe ser entre 2 y 100 letras')
        
        return title
    
class MovieResponseModel(ResponseModel):
    id: int
    title: str




