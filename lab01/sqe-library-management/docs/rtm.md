# LibraryHub Requirements Traceability Matrix

## 1. Purpose

This Requirements Traceability Matrix (RTM) maps each LibraryHub functional requirement to the test cases that verify it. The purpose of the RTM is to ensure that every identified requirement has corresponding test coverage. It also helps identify any requirement that has no linked test case.

## 2. Requirements Traceability Matrix

| Requirement ID | Requirement                    | Description                                                                                                                                                          | Test Case IDs       | Coverage Status |
| -------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------- |
| **R1**         | Book Registration              | The system shall allow a book to be added when valid book information and a new ISBN are provided.                                                                   | TC-01               | **Covered**     |
| **R2**         | ISBN Validation and Uniqueness | The system shall reject malformed ISBN values and prevent duplicate ISBN values from being registered.                                                               | TC-02, TC-03        | **Covered**     |
| **R3**         | Book Borrowing                 | The system shall allow an eligible member to borrow a book when at least one copy is available.                                                                      | TC-04               | **Covered**     |
| **R4**         | Book Availability              | The system shall prevent a member from borrowing a book when no copies are available.                                                                                | TC-05               | **Covered**     |
| **R5**         | Book Return                    | The system shall allow a member to return a book currently on loan and reject an invalid return for a book not borrowed by that member.                              | TC-06, TC-07        | **Covered**     |
| **R6**         | Member Borrowing Limit         | The system shall allow borrowing up to the configured maximum and reject borrowing beyond that limit. The current implementation uses a maximum of 3 borrowed books. | TC-08, TC-09        | **Covered**     |
| **R7**         | Fine Calculation               | The system shall calculate overdue fines correctly for zero overdue days, a mid-range overdue period, and an overdue-tier boundary.                                  | TC-10, TC-11, TC-12 | **Covered**     |

## 3. Coverage Analysis

All seven identified requirements have at least one linked test case. Therefore, no requirement currently has zero test-case coverage.

| Metric                                   |   Result |
| ---------------------------------------- | -------: |
| Total Requirements                       |        7 |
| Requirements with at least one test case |        7 |
| Requirements with zero test cases        |        0 |
| Requirement Coverage                     | **100%** |
| Total Test Cases                         |       12 |

### Requirement Coverage Calculation

**Requirement Coverage = (Requirements with at least one linked test / Total Requirements) × 100**

**= (7 / 7) × 100 = 100%**

## 4. Zero-Coverage Requirement Check

The RTM was reviewed to identify requirements with zero linked test cases. No zero-coverage requirement was found because all seven requirements are mapped to one or more test cases.

The complete mapping is:

* **R1 → TC-01**
* **R2 → TC-02, TC-03**
* **R3 → TC-04**
* **R4 → TC-05**
* **R5 → TC-06, TC-07**
* **R6 → TC-08, TC-09**
* **R7 → TC-10, TC-11, TC-12**

Therefore, no additional test case is required to close a coverage gap.

## 5. Traceability Summary

The RTM provides complete requirement-level traceability for the LibraryHub test suite. All seven requirements are linked to at least one test case, resulting in 100% requirement coverage. Multiple test cases are used for requirements involving negative, boundary, and limit conditions to provide broader functional coverage.

