from models import USR, Shelf, Book


def show_users():
    users = USR.select(Shelf)  # we can use a selected (join) table for reduce a hit but the data that coming from the
    # database is heavier
    for user in users:
        # shelves_count = Shelf.select().where(Shelf.user == users) # This line for a counting a id
        shelves_count = user.shelves.count

        shelves = ', '.join([Shelf.name for shelf in user.shelves])
        print(user.username, '\t', shelves, '\t', user.book_shelves.count())


def show_books():
    books = Book.select()
    for book in books:
        authors = ', '.join([book_author.author.name for book_author in book.authors])
        print(f"{book.name}({book.isbn})", '\t', authors)
