# Equivalence Partitioning Analysis

## Task 1 — Partition Two More Inputs

Equivalence Partitioning (EP) divides the possible input values into
equivalence classes where the system is expected to behave in the same way.
One representative value is selected from each class for testing.

---

## 1. Number of Books on Loan

### Business Rule

A library member can have a maximum of 5 books on loan simultaneously.

Therefore:

- 0 to 5 books = valid
- 6 or more books = invalid

### Equivalence Classes

| Class ID | Input Condition | Range | Valid/Invalid | Representative |
|---|---|---|---|---|
| EC-B1 | Allowed number of books | 0–5 | Valid | 3 |
| EC-B2 | More than allowed limit | 6+ | Invalid | 6 |

### Explanation

**EC-B1 — Valid class (0–5):**  
Any member having between 0 and 5 books on loan should be accepted.
The representative value `3` is selected because it is a normal value
inside the valid range.

**EC-B2 — Invalid class (6+):**  
A member having 6 or more books exceeds the maximum allowed limit.
The representative value `6` is selected because it is the first value
outside the valid range.

---

## 2. ISBN

### Business Rule

An ISBN must contain exactly 13 numeric digits.

Therefore, an ISBN is valid only when:

- It contains exactly 13 characters.
- Every character is a numeric digit.
- It is not empty.

### Equivalence Classes

| Class ID | Input Condition | Valid/Invalid | Representative |
|---|---|---|---|
| EC-I1 | Exactly 13 numeric digits | Valid | `9781234567890` |
| EC-I2 | Empty input | Invalid | `""` |
| EC-I3 | Fewer than 13 numeric digits | Invalid | `978123456` |
| EC-I4 | Contains letters or symbols | Invalid | `97812345678A0` |

### Explanation

**EC-I1 — Valid ISBN:**  
The input contains exactly 13 numeric digits, so it satisfies the ISBN
validation rule. The representative is `9781234567890`.

**EC-I2 — Empty ISBN:**  
An empty string does not contain an ISBN and must therefore be rejected.
The representative is `""`.

**EC-I3 — Too-short ISBN:**  
The input contains numeric characters but fewer than 13 digits. It must
be rejected because the ISBN must contain exactly 13 digits.
The representative is `978123456`.

**EC-I4 — Letters or symbols:**  
The input contains a non-numeric character. It must be rejected even
if the total length is 13. The representative is `97812345678A0`.

---

## Equivalence Partitioning Summary

| Input | Valid Classes | Invalid Classes |
|---|---|---|
| Number of books on loan | EC-B1: 0–5 | EC-B2: 6+ |
| ISBN | EC-I1: exactly 13 numeric digits | EC-I2: empty, EC-I3: fewer than 13 digits, EC-I4: letters/symbols |

---

## EP Boundary Blind Spot

Equivalence Partitioning reduces the number of test cases by grouping
inputs that are expected to behave similarly. However, EP can miss
defects at boundaries.

For example, the borrowing rule has a boundary between 5 and 6 books.
Testing only the representative value 3 from the valid class and 6 from
the invalid class may not fully test the behavior around the boundary.

Similarly, ISBN validation has a boundary at exactly 13 digits. A test
using a normal 13-digit ISBN may not detect defects involving 12 or 14
digits.

Therefore, Boundary Value Analysis (BVA) should be used together with
Equivalence Partitioning to test important boundary values.


## 3. Fine Tier — Worked Example

The `fine_tier(days_overdue)` function partitions overdue days into the
following equivalence classes:

| Class ID | Range | Valid/Invalid | Representative | Expected Result |
|---|---:|---|---:|---|
| EC-F1 | < 0 | Invalid | -3 | ValueError |
| EC-F2 | 0 | Valid | 0 | None |
| EC-F3 | 1–7 | Valid | 4 | Low |
| EC-F4 | 8–14 | Valid | 10 | Medium |
| EC-F5 | 15–30 | Valid | 20 | High |
| EC-F6 | 31+ | Valid | 45 | Severe |

### Test Implementation

The equivalence classes are implemented in
`tests/test_fine_tier.py`. Five valid classes are tested using
`pytest.mark.parametrize`, while the invalid negative-days class is
tested separately using `pytest.raises(ValueError)`.

### Test Execution Result

Run:

```text
pytest tests/test_fine_tier.py

Result:

================================================ test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: E:\semester5th\SQE-Labs\lab01\sqe-library-management


collected 6 items                                                                                                     

tests\test_fine_tier.py ......                                                                                  [100%]

================================================= 6 passed in 0.04s ==================================================

```
## Task 3 — Borrow-Limit Tests
Business Rule

A library member can borrow a maximum of 5 books simultaneously.

Therefore:

0 to 5 books = valid
More than 5 books = invalid
Attempting to borrow a 6th book must raise a ValueError
Test Design

The borrow-limit behavior was tested using representative values from
the equivalence classes.

Test Case	Current Books	Action	Expected Result
TC-BL1	3	Borrow one additional book	Successful; total becomes 4
TC-BL2	5	Borrow one additional book	ValueError is raised

The test was implemented using pytest.mark.parametrize so that the
same test function could be executed for both representative cases.

For the invalid case, pytest.raises(ValueError) was used to verify
that the required exception is raised.

Test Implementation

The test was added in:

tests/test_borrow_limit.py

The implementation creates a Library object, adds the required number
of existing books, and then attempts to borrow one more book.

Test Execution

The following command was used:
``` text

python -m pytest tests/test_borrow_limit.py

Actual Test Result
================================================ test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: E:\semester5th\SQE-Labs\lab01\sqe-library-management
collected 2 items

tests\test_borrow_limit.py ..                                                                                   [100%]

================================================= 2 passed in 0.02s ==================================================
```

##Result

Both representative test cases passed successfully.

3 books → 4th book: Passed. The member was allowed to borrow another book.
5 books → 6th book: Passed. The system correctly raised ValueError.

Therefore, the maximum borrowing limit of 5 books is correctly enforced.

## Conclusion

## Task 3 — Borrow-Limit Tests is PASS.

The test suite confirms both the valid and invalid equivalence classes
for the maximum number of books a member can borrow.
