# Llamamos a la clase FastApi
from fastapi import FastAPI
# Llamamos a la BD para su coneccion con la app 
from .database import database as conection


# Creamos el servidor instanciando a la clase 
app = FastAPI(
    title = 'Cuevana Fake',
    description = 'En esta web podras realizar reseñas a tus peliculas favoritas',
    version = '1'
)

# Evento StartUp 
@app.on_event('startup')
def startup():
    if conection.is_closed():
        conection.connect()

        print('Connecting.....')

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


