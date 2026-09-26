from libraryhub.library import Book, Library


def test_total_available_copies_empty_catalog(library):
    assert library.total_available_copies() == 0


def test_total_available_copies_single_book(library):
    library.catalog.append(Book("9780000000001", 4))

    assert library.total_available_copies() == 4


def test_total_available_copies_multiple_books(library):
    library.catalog.extend(
        [
            Book("9780000000001", 3),
            Book("9780000000002", 5),
            Book("9780000000003", 2),
        ]
    )

    assert library.total_available_copies() == 10