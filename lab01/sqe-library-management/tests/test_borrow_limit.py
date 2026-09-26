import pytest


def test_borrow_book_allows_fourth_book(library):
    # Arrange
    member_id = 1
    library.loans[member_id] = [
        "ISBN-1",
        "ISBN-2",
        "ISBN-3",
        "ISBN-4",
    ]

    # Act
    library.borrow_book(member_id, "ISBN-NEW")

    # Assert
    assert len(library.loans[member_id]) == 5


def test_borrow_book_rejects_sixth_book(library):
    # Arrange
    member_id = 1
    library.loans[member_id] = [
        "ISBN-1",
        "ISBN-2",
        "ISBN-3",
        "ISBN-4",
        "ISBN-5",
    ]

    # Act + Assert
    with pytest.raises(ValueError, match="more than 5 books"):
        library.borrow_book(member_id, "ISBN-NEW")

    assert len(library.loans[member_id]) == 5


def test_borrow_book_rejects_member_already_over_limit(library):
    # Arrange
    member_id = 1
    library.loans[member_id] = [
        "ISBN-1",
        "ISBN-2",
        "ISBN-3",
        "ISBN-4",
        "ISBN-5",
        "ISBN-6",
    ]

    # Act + Assert
    with pytest.raises(ValueError, match="more than 5 books"):
        library.borrow_book(member_id, "ISBN-NEW")

    assert len(library.loans[member_id]) == 6


def test_populated_library_fixture_has_expected_books(populated_library):
    # Arrange
    member_id = 1

    # Act
    borrowed_books = populated_library.loans[member_id]

    # Assert
    assert len(borrowed_books) == 3
    assert borrowed_books == ["ISBN-1", "ISBN-2", "ISBN-3"]