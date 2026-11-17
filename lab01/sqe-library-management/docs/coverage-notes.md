# Automated Test Coverage — LibraryHub

## Task 1: Baseline Coverage

The baseline test coverage was generated using the following command:

```bash
python -m pytest --cov=libraryhub --cov-branch --cov-report=term-missing --cov-report=html
```

### Baseline Results

| Metric | Result |
|---|---:|
| Overall Coverage | 95% |
| Line Coverage | 96% |
| Branch Coverage | 92% |
| Total Statements | 56 |
| Missing Statements | 2 |
| Total Branches | 24 |
| Partial Branches | 2 |
| Tests Passed | 47 |

### Per-File Coverage

| File | Line Coverage | Branch Coverage | Total Coverage |
|---|---:|---:|---:|
| `libraryhub/__init__.py` | 100% | 100% | 100% |
| `libraryhub/library.py` | 96% | 92% | 95% |

### Baseline Summary

The baseline coverage report identified two missing lines and two partially covered branches in `libraryhub/library.py`.

An HTML coverage report was also generated in the `htmlcov/` directory for detailed inspection.

---

## Task 2: Identify Coverage Gaps

After inspecting the HTML coverage report, two functions were identified as having incomplete coverage.

### 1. `Library.borrow_book()`

- **Total Coverage:** 78%
- **Missing Line:** 41
- **Partial Branch:** New-member condition at line 40.

### 2. `validate_isbn()`

- **Total Coverage:** 60%
- **Missing Line:** 66
- **Partial Branch:** Non-string input condition at line 65.

### Summary

All other reported functions had 100% coverage. Therefore, only these two functions contained uncovered execution paths in the baseline report.

---

## Task 3: Close the Coverage Gaps

To cover the missing lines and partially covered branches, the following three tests were added:

1. `test_borrow_book_creates_loan_list_for_new_member`
2. `test_validate_isbn_rejects_none`
3. `test_validate_isbn_rejects_integer`

These additional tests covered the previously uncovered execution paths.

### Final Coverage Results

| Metric | Baseline | Final |
|---|---:|---:|
| Line Coverage | 96% | 100% |
| Branch Coverage | 92% | 100% |
| Overall Coverage | 95% | 100% |
| Missing Lines | 2 | 0 |
| Partial Branches | 2 | 0 |
| Tests Passed | 47 | 50 |

### Result

All previously uncovered lines and partial branches were successfully covered. Both line and branch coverage reached 100%.

---

## Task 4: Coverage vs. Quality Discussion

### Weak Assertion Identified

The existing test `test_more_borrowed_books_gives_higher_percentile()` only checked whether member 103 had a higher percentile than member 102.

**Original Assertion:**

```python
assert borrow_percentile(103, library) > borrow_percentile(102, library)
```

### Why Was It a Coverage Trap?

Although the test executed the percentile calculation and contributed to code coverage, it did not verify the exact expected results.

An incorrect implementation could still return two different but incorrect values and pass the test.

### Improvement

The assertion was strengthened to verify the exact expected percentile values:

```python
assert borrow_percentile(102, library) == pytest.approx(100 / 3)
assert borrow_percentile(103, library) == pytest.approx(200 / 3)
```

This improvement ensures that the actual calculation is correct rather than simply checking the relative order of the results.

### Key Lesson

High code coverage does not guarantee correct behavior. Tests should contain meaningful assertions that verify expected results, not just execute code.

---

## Task 5: Enforce Coverage Threshold

The `pytest.ini` configuration was updated to enforce a minimum coverage threshold of **85%**.

The following configuration was added:

```ini
[pytest]
addopts = --cov=libraryhub --cov-branch --cov-report=term-missing --cov-report=html --cov-fail-under=85
```

### Threshold Verification

To verify that the coverage threshold was working correctly:

1. The new-member borrowing test was temporarily disabled.
2. The coverage threshold was temporarily increased to 100%.
3. Pytest was executed again.
4. Pytest exited with a non-zero status because coverage fell below the temporary threshold.
5. The original test was restored.
6. The configured coverage threshold was returned to 85%.

### Result

The coverage threshold was successfully verified.

---

## Final Coverage Summary

The final test execution confirmed that all tests passed and the project achieved complete line and branch coverage.

| Final Metric | Result |
|---|---:|
| Total Tests Passed | 50 |
| Line Coverage | 100% |
| Branch Coverage | 100% |
| Overall Coverage | 100% |
| Required Coverage Threshold | 85% |
| Missing Lines | 0 |
| Partial Branches | 0 |

---

## Final Conclusion

The LibraryHub project successfully achieved **100% overall code coverage**, including 100% line coverage and 100% branch coverage.

The uncovered execution paths were addressed by adding three targeted tests. An existing weak assertion was also strengthened to improve test quality and verify exact expected results.

Finally, an 85% minimum coverage threshold was configured and successfully tested to prevent future reductions in test coverage.

**Final Result: All 50 tests passed successfully, and the project achieved 100% line and branch coverage, exceeding the required 85% coverage threshold.**
