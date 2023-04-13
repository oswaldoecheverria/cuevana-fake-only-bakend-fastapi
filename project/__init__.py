# Llamamos a la clase FastApi
from fastapi import FastAPI, HTTPException
# Centralizamos las urls 
from fastapi import APIRouter
# Importamos Oauth 
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from fastapi import status
from .common import create_access_token
# Llamamos a la BD para su coneccion con la app 
from .database import database as conection
# Importamos los modelos de BD 
from .database import User
from .database import Movie
from .database import UserReview
# Importamos las instancias FASTApi modulos
from .routers import user_router
from .routers import review_router
from .routers import movie_router


# Creamos el servidor instanciando a la clase 
app = FastAPI(
    title = 'Cuevana Fake',
    description = 'En esta web podras realizar reseñas a tus peliculas favoritas',
    version = '1'
)

# Centralizamos la urls 
api_v1 = APIRouter(prefix='/api/v1')


# Incluimos las rutas de los modulos junto al detalle de las url
api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movie_router)


@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    
    user = User.authenticate(data.username, data.password)
    
    # si el user existe por ahora regrese 
    if user:
        return {
            'access_token': create_access_token(user),
            'token_type': 'Bearer'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username  o Password incorrectos',
            headers={'WWW-Autenticate': 'beraer'}
        )



app.include_router(api_v1)


# Evento StartUp 
@app.on_event('startup')
def startup():
    if conection.is_closed():
        conection.connect()

        print('Connecting.....')

    conection.create_tables([User, Movie, UserReview])


# Evento ShutDown
@app.on_event('shutdown')
def shutdown():
    if not conection.is_closed():
        conection.close()

        print('Close...')


# Creamos url index
@app.get('/')
async def index():
    return 'hola mundo desde servidor FastApi'


