import json
from models import USR, Book, Author, Shelf, BookAuthor, BookShelf

class BaseModelAdmin:
    filename = None
    model = None

    @classmethod
    def load(cls):
        with open(f'fixtures/{cls.filename}.json') as q:
            data = json.loads(q.read())

        instances = list()
        for instance in data:
            instances.append(cls.model.create(**instance))

        return instances

class UserImporter(BaseModelAdmin):
    filename = 'users'
    model = USR


class BookImporter(BaseModelAdmin):
    filename = 'books'
    model = Book


class AuthorImporter(BaseModelAdmin):
    filename = 'authors'
    model = Author


class ShelfImpoerter(BaseModelAdmin):
    filename = None
    model = Shelf
    default_shelves = ['read', 'currently reading', 'want to read']

    @classmethod
    def load(cls):
        instances = list()
        for user in USR.select():
            for shelf in cls.default_shelves:
                instances.append(cls.model.create(user=user, name=shelf))

        return instances


class BookAutherImportent(BaseModelAdmin):
    filename = 'books-authors'
    model = BookAuthor


class BookShelfImporter(BaseModelAdmin):
    filename = 'book-shelves'
    model = BookShelf

