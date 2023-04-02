# Llamamos a la clase FastApi
from fastapi import FastAPI
# Centralizamos las urls 
from fastapi import APIRouter
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
api_v1.app.include_router(user_router)
api_v1.app.include_router(review_router)
api_v1.app.include_router(movie_router)



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
    return'hola mundo desde servidor FastApi'


