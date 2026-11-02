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

*To be completed after the code review.*

### Most Valuable Checklist Item

To be added after identifying which checklist item caught the most important defect.

### Additional Checklist Item for Next Time

To be added after completing the review retrospective.