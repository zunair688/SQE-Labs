
from libraryhub.library import (
    Book,
    Library,
    rank_books_by_popularity,
)


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()

    assert rank_books_by_popularity(library) == []


def test_rank_books_with_one_book_returns_that_book():
    library = Library()
    book = Book("9780000000001", 2)
    library.catalog.append(book)

    assert rank_books_by_popularity(library) == [book]
