
from libraryhub.library import borrow_percentile, Library


def test_lowest_borrower_gets_zero_percentile():
    library = Library()

    library.loans = {
        101: ["ISBN-1"],
        102: ["ISBN-1", "ISBN-2"],
        103: ["ISBN-1", "ISBN-2", "ISBN-3"]
    }

    assert borrow_percentile(101, library) == 0.0


def test_more_borrowed_books_gives_higher_percentile():
    library = Library()

    library.loans = {
        101: ["ISBN-1"],
        102: ["ISBN-1", "ISBN-2"],
        103: ["ISBN-1", "ISBN-2", "ISBN-3"]
    }

    assert borrow_percentile(103, library) > borrow_percentile(102, library)
