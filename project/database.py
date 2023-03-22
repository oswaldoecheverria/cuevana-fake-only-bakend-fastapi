
from peewee import *
from datetime import datetime

database = MySQLDatabase(
    'reviews_app',
    user = 'root',
    password = 'abc123....',
    host = 'localhost',
    port = 3306
)



