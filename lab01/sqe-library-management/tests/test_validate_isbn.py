import pytest
from libraryhub.library import validate_isbn


@pytest.mark.parametrize(
    "isbn, expected",
    [
        ("9781234567890", True),   # Exactly 13 numeric digits
        ("", False),               # Empty
        ("978123456", False),      # Fewer than 13 digits
        ("97812345678A0", False),  # Contains letter
        ("97812345678-0", False),  # Contains symbol
    ]
)
def test_validate_isbn_classes(isbn, expected):
    assert validate_isbn(isbn) == expected
