
from peewee import *
from datetime import datetime
# Libreria para la encriptacion md5
import hashlib

database = MySQLDatabase(
    'reviews_app',
    user = 'root',
    password = 'abc123....',
    host = 'localhost',
    port = 3306
)

# Modelos de BD 

class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    create_at = DateField(default=datetime.now)

    def __str__(self):
        return self.username
    
    class Meta:
        database = database
        table_name = 'users'
    
    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()
 

 
class Movie(Model):
    title = CharField(max_length=50, unique=True)
    create_at = DateField(default=datetime.now)

    def __str__(self):
        return self.title
    
    class Meta:
        database = database
        table_name = 'movies'



class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie)
    review = TextField()
    score = IntegerField()
    create_at = DateField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
    
    class Meta:
        database = database
        table_name = 'user_reviews'

    

