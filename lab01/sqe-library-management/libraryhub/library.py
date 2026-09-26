class Book:
    def __init__(self, isbn, available_copies):
        self.isbn = isbn
        self.available_copies = available_copies


def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return "None"

    if 1 <= days_overdue <= 7:
        return "Low"

    if 8 <= days_overdue <= 14:
        return "Medium"

    if 15 <= days_overdue <= 30:
        return "High"

    return "Severe"


class LibraryIOError(Exception):
    """Raised when the library catalog cannot be exported."""


class Library:
    MAX_BOOKS = 5

    def __init__(self):
        self.loans = {}
        self.catalog = []

    def borrow_book(self, member_id, isbn):
        if member_id not in self.loans:
            self.loans[member_id] = []

        if len(self.loans[member_id]) >= self.MAX_BOOKS:
            raise ValueError("Member cannot borrow more than 5 books")

        self.loans[member_id].append(isbn)

    def total_available_copies(self):
        return sum(book.available_copies for book in self.catalog)

    def export_catalog(self, path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                for book in self.catalog:
                    file.write(
                        f"{book.isbn},{book.available_copies}\n"
                    )
        except OSError as exc:
            raise LibraryIOError(
                f"Unable to export catalog to {path}"
            ) from exc


def validate_isbn(isbn):
    if not isinstance(isbn, str):
        return False

    return len(isbn) == 13 and isbn.isdigit()