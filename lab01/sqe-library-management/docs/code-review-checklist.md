# Code Review Checklist

This checklist is used to review code changes in the SQE Library Management System. It focuses on correctness, testing, readability, design, and risk.

## 1. Correctness

- [ ] Does the function produce the expected output for normal inputs?
- [ ] Are boundary conditions and edge cases handled correctly?
- [ ] Are calculations and logical conditions correct?

## 2. Testing

- [ ] Are appropriate test cases included for the new functionality?
- [ ] Do tests cover normal, boundary, and invalid inputs?
- [ ] Do tests verify actual expected behavior rather than simply copying the implementation?

## 3. Readability

- [ ] Are function and variable names meaningful?
- [ ] Does the code follow consistent indentation and formatting?
- [ ] Are docstrings or comments provided where necessary?

## 4. Design

- [ ] Does the implementation follow the existing project architecture?
- [ ] Is unnecessary code duplication avoided?
- [ ] Is the function small, understandable, and easy to maintain?

## 5. Risk

- [ ] Could the changes break existing functionality?
- [ ] Are invalid inputs and unexpected states handled safely?
- [ ] Could the implementation introduce performance or compatibility problems?

---

## Lessons Learned

### Most Valuable Checklist Item

The most valuable checklist item was **Correctness - Verify boundary conditions and edge cases**.

During the code review of the `fine_tier()` function, we identified an off-by-one error. The function incorrectly classified 8 overdue days as Low instead of Medium because the condition included 8 in both ranges.

The review helped identify this issue before approval. After correcting the condition and verifying the boundary tests, all tests passed successfully.

### Checklist Item to Add for Next Time

For future code reviews, I would add the following checkpoint:

* **Boundary Value Testing:** Verify values immediately below, at, and above every important threshold. Ensure that each boundary has a corresponding automated test.

### Overall Reflection

This lab demonstrated that structured code reviews improve software quality by identifying logic errors, missing edge cases, and weaknesses in test coverage. Actionable inline comments and reviewer feedback also made the correction process more effective.
