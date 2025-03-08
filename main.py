from peewee import fn
from models import db, USR, Book, Author, BookAuthor, BookShelf, UserRelation, UserAutherRelation, Shelf
from admin import UserImporter, BookImporter, AuthorImporter, BookAutherImportent, ShelfImpoerter, BookShelfImporter


def Load_data():
    Importent_classes = [
        UserImporter, BookImporter, AuthorImporter,
        BookAutherImportent, ShelfImpoerter, BookShelfImporter
    ]
    for _class in Importent_classes:
        print(_class.load())


def create_table():
    """
    This function is used to create the database tables
    return: a (--USR, Book, Author, BookAuthor, UserRelation, UserAutherRelation, Shelf--) BookShelf tables in database
    """
    db.create_tables(
        [
            USR, Book, Author, BookAuthor, UserRelation,
            UserAutherRelation, Shelf, BookShelf
        ]
    )


def show_user_data(username=None, password=None):
    user = USR.authenticate(username=username, password=password)
    if user is None:
        print("User not found")
        return
    print(f"username: {USR.username}")
    print("bookshelves")
    for Shelf in user.shelves:
        print(f"\t{Shelf.name}({Shelf.book_shelves.count()})")

    print("Books")
    for book_shelf_instance in user.book_shelves:
        print(f"\t{book_shelf_instance.book.name}")


def show_book_shelves():
    query = BookShelf.select(
        BookShelf.user,
        BookShelf.shelf,
        fn.COUNT(BookShelf.book).alias('books_count')  # alias for name a group
    ).group_by(BookShelf.shelf)

    for q in query:
        print(q.user.username, q.shelf.name, q.books_count)


def show_Book_shelves():  # suggestion: for this part we most be use in DATABASE side
    query = BookShelf.select(
        BookShelf.book,
        BookShelf.shelf,
        fn.COUNT(BookShelf.book)
    ).group_by(BookShelf.shelf)

    for q in query:
        print(q.user.username, q.shelf.name, q.books_count)


if __name__ == '__main__':
    # create_table()
    # Load_data()
    # show_data()
    # test = input()
    # show_user_data(username=test)
    # show_book_rates()
    # show_Book_shelves()
    print("It's Done")
