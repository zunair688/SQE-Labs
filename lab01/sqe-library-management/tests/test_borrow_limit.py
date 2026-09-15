import pytest
from libraryhub.library import Library


@pytest.mark.parametrize(
    "current_books, should_raise",
    [
        (4, False),
        (5, True),
        (6, True),
    ]
)
def test_borrow_limit_boundaries(current_books, should_raise):
    library = Library()
    member_id = 1

    library.loans[member_id] = [
        f"ISBN-{i}" for i in range(current_books)
    ]

    if should_raise:
        with pytest.raises(ValueError):
            library.borrow_book(member_id, "ISBN-NEW")

        assert len(library.loans[member_id]) == current_books

    else:
        library.borrow_book(member_id, "ISBN-NEW")
        assert len(library.loans[member_id]) == current_books + 1