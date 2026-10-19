# TDD Log — Rank Books by Popularity

## Feature Objective

Implement `rank_books_by_popularity(library)` to return books sorted by total borrowing frequency in descending order. When two books have the same borrowing frequency, sort them alphabetically by title, ignoring case.

## TDD Cycles

### Cycle 1 — Empty Catalog

- **RED:** Commit `b7d91bf` — Added a test expecting an empty list for an empty catalog. The test initially failed because the function was not implemented.
- **GREEN:** Commit `69299de` — Added a minimal implementation returning an empty list.
- **Result:** The empty-catalog test passed.

### Cycle 2 — One Book

- **RED:** Commit `9435e1f` — Added a test expecting one catalog book to be returned. The test failed because the function returned an empty list.
- **GREEN:** Commit `a3336e6` — Updated the function to return the catalog as a list.
- **Result:** Both existing feature tests passed.

### Cycle 3 — Borrowing Frequency

- **RED:** Commit `17b7af3` — Added a test requiring the most-borrowed book to rank first. The test failed because the catalog was returned in its original order.
- **GREEN:** Commit `872ef5b` — Implemented sorting by borrowing frequency in descending order.
- **Result:** All three feature tests passed.

### Cycle 4 — Alphabetical Tie-Breaking

- **RED:** Commit `9b4df75` — Added a test requiring books with equal borrowing counts to be sorted alphabetically by title. The test failed because the `Book` constructor did not accept a title.
- **GREEN:** Commit `1e4825e` — Added optional title support to `Book` and implemented case-insensitive alphabetical tie-breaking.
- **Result:** All four feature tests passed.

### Cycle 5 — Books Without Borrowing History

- **Regression test:** Commit `8b1da75` — Added a test verifying that borrowed books rank ahead of unborrowed books and that unborrowed books are alphabetized.
- **Result:** The test passed with the existing sorting implementation. This was an additional regression test, rather than a separate failing RED/GREEN cycle.

## Final Verification

- Feature tests: 5 passed.
- Complete regression suite: 45 passed.
- Working tree: clean at the time of verification.

## Reflection

Test-driven development helped me understand how tests guide implementation. I first wrote tests for simple cases and then added more complex sorting requirements. The failing tests showed which behavior was missing, while the passing tests confirmed that the changes worked. I also learned how to preserve existing functionality while extending a class with an optional field. Finally, running the complete test suite helped verify that the new feature did not break existing functionality.