\# Automated Test Coverage — LibraryHub



\## Task 1: Baseline Coverage



Baseline generated using:



```bash

python -m pytest --cov=libraryhub --cov-branch --cov-report=term-missing --cov-report=html

```



\### Baseline Results



| Metric | Result |

|---|---:|

| Overall coverage | 95% |

| Line coverage | 96% |

| Branch coverage | 92% |

| Total statements | 56 |

| Missing statements | 2 |

| Total branches | 24 |

| Partial branches | 2 |

| Tests passed | 47 |



\### Per-file Results



| File | Line Coverage | Branch Coverage | Total |

|---|---:|---:|---:|

| libraryhub/\_\_init\_\_.py | 100% | 100% | 100% |

| libraryhub/library.py | 96% | 92% | 95% |



The baseline report shows two missing lines and two partial branches in `libraryhub/library.py`.



HTML report generated in the `htmlcov/` directory.



\## Task 2: Coverage Gaps



Pending detailed inspection of the HTML report to identify the exact uncovered lines and branches.



\## Task 3: Additional Tests



Pending.



\## Task 4: Coverage vs. Quality



Pending selection and strengthening of an existing weak assertion.



\## Task 5: Coverage Threshold



Pending.



\## Final Coverage



Pending final test execution.







\## Task 2: Identify Coverage Gaps



The Functions report identified two functions with incomplete coverage:



1\. `Library.borrow\_book()` — 78% total coverage.

&#x20;  - Missing line: 41.

&#x20;  - Partial branch: the new-member condition at line 40.



2\. `validate\_isbn()` — 60% total coverage.

&#x20;  - Missing line: 66.

&#x20;  - Partial branch: the non-string input condition at line 65.



All other reported functions had 100% coverage. Therefore, only two functions had actual uncovered paths in the baseline report.



\## Task 3: Close the Gaps



Added the following tests:



\- `test\_borrow\_book\_creates\_loan\_list\_for\_new\_member`

\- `test\_validate\_isbn\_rejects\_none`

\- `test\_validate\_isbn\_rejects\_integer`



After adding these tests, all previously uncovered lines and partial branches were executed.



\### Final Coverage Results



| Metric | Baseline | Final |

|---|---:|---:|

| Line coverage | 96% | 100% |

| Branch coverage | 92% | 100% |

| Total coverage | 95% | 100% |

| Missing lines | 2 | 0 |

| Partial branches | 2 | 0 |

| Tests passed | 47 | 50 |


## Task 4: Coverage vs. Quality Discussion

### Weak Assertion Identified

The existing test `test_more_borrowed_books_gives_higher_percentile()` only checked whether member 103 had a higher percentile than member 102.

Original assertion:

```python
assert borrow_percentile(103, library) > borrow_percentile(102, library)
```

### Why It Was a Coverage Trap

The test executed the percentile calculation and contributed to code coverage, but it did not verify the exact expected results. An incorrect implementation could still return two different but incorrect values and pass the test.

### Improvement

The assertion was strengthened to check exact expected percentile values:

```python
assert borrow_percentile(102, library) == pytest.approx(100 / 3)
assert borrow_percentile(103, library) == pytest.approx(200 / 3)
```

This verifies the actual calculation instead of only checking the relative order.

**Lesson:** High code coverage does not guarantee correct behavior. Assertions must verify meaningful expected results.



## Task 5: Enforce Coverage Threshold

The pytest configuration was updated with the following options:

```ini
addopts = --cov=libraryhub --cov-branch --cov-report=term-missing --cov-report=html --cov-fail-under=85
```

The minimum required coverage is 85%.

### Threshold Verification

The new-member borrowing test was temporarily disabled and the threshold was temporarily raised to 100%.

Pytest exited with a non-zero status because coverage fell below the temporary threshold.

The original test was restored and the configured threshold was returned to 85%.

### Final Verification

- All 50 tests passed.
- Line coverage: 100%.
- Branch coverage: 100%.
- Configured minimum threshold: 85%.


