# Triage Meeting Log

## Purpose

This triage meeting ranks the five student-related library management
defects according to severity, priority, user impact, and sprint scope.

## Issue Ranking

| Rank | Issue | Severity | Priority | Sprint Decision |
|------|-------|----------|----------|-----------------|
| 1 | Duplicate Student ID is accepted | High | Critical | Fix |
| 2 | Student can borrow books beyond the allowed limit | High | High | Fix |
| 3 | Student search fails with different letter casing | Medium | High | Fix |
| 4 | Student registration accepts an empty name | Medium | Medium | Won't Fix |
| 5 | Student registration accepts negative member ID | Low | Low | Won't Fix |

## Triage Decisions

### 1. Duplicate Student ID

This is ranked first because duplicate student IDs can cause incorrect
identification of students and make borrowing records ambiguous. It has
High severity and Critical priority because correct student identification
is fundamental to the library management system.

### 2. Borrowing Limit Not Enforced

This issue is ranked second because students can borrow more books than
allowed by library policy. It has High severity and High priority because
it directly affects book availability and normal library operations.

### 3. Case-Sensitive Student Search

This issue is ranked third. Its severity is Medium because it does not
destroy existing student data, but its priority is High because student
search is frequently required during library transactions.

### 4. Blank Student Name

This issue is ranked fourth and will not be fixed in this sprint. Although
it creates incomplete student records, its impact is limited and staff can
work around the problem. It will be considered in a future validation
cleanup.

### 5. Negative Student ID

This issue is ranked fifth and will not be fixed in this sprint. Negative
IDs are an edge-case input and have low impact during normal library
operations. The team will prioritize defects that affect common student
transactions.

## Severity vs Priority Trade-offs

The case-sensitive search defect demonstrates that severity and priority
are not always the same. Its severity is Medium because the underlying
student data is not lost or corrupted, but its priority is High because
student lookup is an important and frequently used operation.

The blank student name defect also shows this trade-off. Its severity is
Medium because it creates invalid student data, but its priority is Medium
because it has limited immediate operational impact and can be deferred
while more important defects are fixed.

The negative student ID defect has both Low severity and Low priority
because it affects an unusual input case and does not significantly affect
normal library usage.

## Sprint Decision

The team will fix the three highest-priority issues:

1. Duplicate Student ID
2. Borrowing Limit Not Enforced
3. Case-Sensitive Student Search

The two lower-priority issues will be marked as `status:wontfix` for this
sprint and considered for future improvement.
