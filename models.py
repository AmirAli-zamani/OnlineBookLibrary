from datetime import datetime

from peewee import MySQLDatabase, Model, CharField, DateTimeField, ForeignKeyField, IntegerField, \
    DateField, SmallIntegerField, TextField

db = MySQLDatabase('OnlineBookLibrary', user='', password='', host='127.0.0.1', port=3306)

class BaseModel(Model):

    class Meta:
        database = db

class PositiveIntegerField(IntegerField):
    def db_value(self, value):
        if value < 0:
            raise ValueError("Value must be positive!")
        return super().db_value(value)

class MyModel(BaseModel):
    positive_field = PositiveIntegerField()


class USR(BaseModel):
    username = CharField(max_length=16)
    password = PositiveIntegerField()

    @classmethod
    def authenticate(cls, username, password):
        return cls.select().where(
            cls.username == username, cls.password == password
        ).first()

class Book(BaseModel):
    isbn = CharField(max_length=32, null=False, unique=True)
    name = CharField(max_length=32, default='Unknown Book')
    created_time = DateTimeField(default=datetime.now)

class Author(BaseModel):
    name = CharField(default='Unknown', null=False, unique=True)

class Shelf(BaseModel):
    READ = 'read'
    CURRENTLY_READING = 'currently reading'
    WANT_TO_READ = 'want to read'

    name = CharField()
    user = ForeignKeyField(USR.username, backref='shelves')
    created_time = DateTimeField(default=datetime.now)

class BookShelf(BaseModel):
    user = ForeignKeyField(USR.username, backref='book_shelves')
    book = ForeignKeyField(Book.name, backref='book_shelves')
    shelf = ForeignKeyField(Shelf.name, backref='book_shelves')
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    rate = SmallIntegerField()
    comment = TextField()
    created_time = DateTimeField(default=datetime.now)

class BookAuthor(BaseModel):
    book = ForeignKeyField(Book.name, backref='authers')
    author = ForeignKeyField(book, backref='books')

class UserAutherRelation(BaseModel):
    user = ForeignKeyField(USR.username, backref='followed_authers')
    author = ForeignKeyField(Author.name, backref='following_users')

class UserRelation(BaseModel):
    following = ForeignKeyField(USR, backref='following')
    follower = ForeignKeyField(USR, backref='followe')
