
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


def test_rank_books_most_borrowed_book_comes_first():
    library = Library()
    book_a = Book("9780000000001", 2)
    book_b = Book("9780000000002", 3)

    library.catalog.extend([book_a, book_b])

    library.loans = {
        1: ["9780000000002", "9780000000001"],
        2: ["9780000000002"],
        3: ["9780000000002"],
    }

    assert rank_books_by_popularity(library) == [book_b, book_a]
