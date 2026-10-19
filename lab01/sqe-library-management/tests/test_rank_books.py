
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



def test_rank_books_equal_popularity_sorted_alphabetically_by_title():
    library = Library()

    book_z = Book("9780000000003", 2, title="Zebra")
    book_a = Book("9780000000004", 2, title="Apple")

    library.catalog.extend([book_z, book_a])

    library.loans = {
        1: ["9780000000003", "9780000000004"],
    }

    assert rank_books_by_popularity(library) == [book_a, book_z]



def test_rank_books_unborrowed_books_come_after_borrowed_books():
    library = Library()

    book_z = Book("9780000000005", 2, title="Zebra")
    book_a = Book("9780000000006", 2, title="Apple")
    book_m = Book("9780000000007", 2, title="Moon")

    library.catalog.extend([book_z, book_a, book_m])
    library.loans = {
        1: ["9780000000005", "9780000000005"],
    }

    assert rank_books_by_popularity(library) == [
        book_z,
        book_a,
        book_m,
    ]
