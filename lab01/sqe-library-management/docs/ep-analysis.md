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
