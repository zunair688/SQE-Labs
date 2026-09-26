import pytest


@pytest.mark.parametrize(
    "current_books, should_raise, expected_count",
    [
        pytest.param(
            0,
            False,
            1,
            id="new-member-borrows-first-book",
        ),
        pytest.param(
            3,
            False,
            4,
            id="member-with-three-borrows-gets-fourth-book",
        ),
        pytest.param(
            4,
            False,
            5,
            id="member-at-four-books-gets-fifth-book",
        ),
        pytest.param(
            5,
            True,
            5,
            id="member-at-limit-rejects-sixth-book",
        ),
        pytest.param(
            6,
            True,
            6,
            id="member-already-over-limit-stays-unchanged",
        ),
        pytest.param(
            10,
            True,
            10,
            id="member-far-over-limit-stays-unchanged",
        ),
    ],
)
def test_borrow_book_edge_cases(
    library,
    current_books,
    should_raise,
    expected_count,
):
    # Arrange
    member_id = 1
    library.loans[member_id] = [
        f"ISBN-{i}" for i in range(current_books)
    ]

    # Act + Assert
    if should_raise:
        with pytest.raises(
            ValueError,
            match="more than 5 books",
        ):
            library.borrow_book(member_id, "ISBN-NEW")
    else:
        library.borrow_book(member_id, "ISBN-NEW")

    assert len(library.loans[member_id]) == expected_count


def test_populated_library_fixture_has_expected_books(populated_library):
    # Arrange
    member_id = 1

    # Act
    borrowed_books = populated_library.loans[member_id]

    # Assert
    assert len(borrowed_books) == 3
    assert borrowed_books == ["ISBN-1", "ISBN-2", "ISBN-3"]