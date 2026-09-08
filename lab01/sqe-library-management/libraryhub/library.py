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


class Library:
    MAX_BOOKS = 5

    def __init__(self):
        self.loans = {}

    def borrow_book(self, member_id, isbn):
        if member_id not in self.loans:
            self.loans[member_id] = []

        if len(self.loans[member_id]) >= self.MAX_BOOKS:
            raise ValueError("Member cannot borrow more than 5 books")

        self.loans[member_id].append(isbn)
