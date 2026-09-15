# Boundary Value Analysis

## Purpose

Boundary Value Analysis (BVA) focuses on values at and around the boundaries of input ranges. It complements the Equivalence Partitioning (EP) performed in Lab 5 by testing values immediately below, at, and immediately above important boundaries.

The three functions under test are:

* `fine_tier()`
* `Library.borrow_book()`
* `validate_isbn()`

---

## 1. `fine_tier()` Boundary Analysis

### Business Rules

The `fine_tier()` function uses the following overdue-day ranges:

| Input Range  | Expected Result |
| ------------ | --------------- |
| Less than 0  | ValueError      |
| 0            | None            |
| 1–7          | Low             |
| 8–14         | Medium          |
| 15–30        | High            |
| 31 and above | Severe          |

### Boundary Table

| Boundary        | Value - 1 | Expected   | Boundary Value | Expected | Value + 1 | Expected |
| --------------- | --------: | ---------- | -------------: | -------- | --------: | -------- |
| Domain edge / 0 |        -1 | ValueError |              0 | None     |         1 | Low      |
| Low/Medium      |         7 | Low        |              8 | Medium   |         9 | Medium   |
| Medium/High     |        14 | Medium     |             15 | High     |        16 | High     |
| High/Severe     |        30 | High       |             31 | Severe   |        32 | Severe   |

### BVA Test Set

The resulting boundary-focused test values are:

```text
-1, 0, 1,
7, 8, 9,
14, 15, 16,
30, 31, 32
```

These values verify the values immediately below, at, and immediately above each important boundary and help detect off-by-one errors.

---

## 2. `Library.borrow_book()` Boundary Analysis

### Business Rule

A member can have a maximum of 5 books on loan simultaneously.

Therefore:

| Current Books | Next Borrow     | Expected |
| ------------: | --------------- | -------- |
|           0–4 | Borrow one book | Allowed  |
|             5 | Borrow one book | Rejected |
|             6 | Borrow one book | Rejected |

### Boundary Table

| Boundary           | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
| ------------------ | --------: | -------- | -------------: | -------- | --------: | -------- |
| Maximum loan limit |         4 | Allowed  |              5 | Rejected |         6 | Rejected |

The important BVA states are therefore:

```text
4 books → borrowing another book is allowed

5 books → borrowing another book is rejected

6 books → borrowing another book is rejected
```

The 6-book state is not normally reachable through `borrow_book()` because the function correctly rejects attempts once the member already has 5 books. It can nevertheless be used as a defensive-state boundary test by preparing the member's loan list directly.

---

## 3. `validate_isbn()` Boundary Analysis

### Business Rule

An ISBN is valid when it contains exactly 13 numeric digits.

Therefore:

* 12 digits = invalid
* 13 digits = valid
* 14 digits = invalid

The lab additionally requests 11 and 15 digits to verify behavior farther from the boundary.

### Boundary Table

| Boundary      | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
| ------------- | --------: | -------- | -------------: | -------- | --------: | -------- |
| 13-digit ISBN | 12 digits | False    |      13 digits | True     | 14 digits | False    |

### Extended BVA Values

|    Length | Expected |
| --------: | -------- |
| 11 digits | False    |
| 12 digits | False    |
| 13 digits | True     |
| 14 digits | False    |
| 15 digits | False    |

The final ISBN boundary-focused test set is:

```text
11 digits
12 digits
13 digits
14 digits
15 digits
```

---

## 4. EP + BVA Test Strategy

Equivalence Partitioning tests representative values from each input class, while Boundary Value Analysis tests values around the edges of those classes.

For this project:

* EP confirms that each equivalence class behaves correctly.
* BVA confirms that transitions between classes occur at the correct values.
* Together, EP and BVA provide efficient coverage without testing every possible input.

---

## Conclusion

The BVA suite focuses on the values most likely to expose off-by-one errors:

* `fine_tier()`: `-1, 0, 1, 7, 8, 9, 14, 15, 16, 30, 31, 32`
* `borrow_book()`: `4, 5, 6`
* `validate_isbn()`: `11, 12, 13, 14, 15` digits

These tests complement the existing EP tests from Lab 5.
