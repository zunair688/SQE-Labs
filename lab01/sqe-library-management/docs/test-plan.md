# LibraryHub Test Plan

## 1. Test Plan Identifier

**Test Plan ID:** TP-LH-001
**Project:** LibraryHub – Library Management System
**Version:** 1.0
**Test Level:** Functional/System Testing
**Test Environment:** Java-based LibraryHub implementation in the `lab01/sqe-library-management` repository.

This test plan defines the testing activities for the core LibraryHub library-management functionality. The plan is based on the current repository implementation and the functional requirements specified for the LibraryHub testing exercise.

---

## 2. Introduction

The purpose of this test plan is to verify the functional correctness and reliability of LibraryHub's core library-management operations. The testing scope focuses on book management, member management, book borrowing and returning, borrowing limits, and overdue fine calculation. The plan also defines the test approach, pass/fail criteria, test environment, responsibilities, risks, and required test deliverables.

The current repository is implemented in Java and contains domain-level library-management classes and an existing test program. Testing will therefore focus primarily on the observable behavior of the Java implementation rather than on a graphical user interface.

---

## 3. Test Items

The primary test items are the LibraryHub Java components located under `lab01/sqe-library-management/src`. The relevant domain functionality includes book-related and member-related behavior implemented by the `Book` and `Member` classes.

The repository also contains existing tests under the `tests` directory. These tests provide an existing baseline for member registration, duplicate member IDs, case-insensitive member-name matching, and borrowing-limit behavior.

The requested LibraryHub test scope additionally includes book registration, ISBN validation, borrowing and returning operations, copy availability, and fine calculation. These requested operations will be tested against the current implementation where the corresponding functionality is available.

---

## 4. Features to be Tested

The following LibraryHub features are included in the test scope:

* **Book registration:** Adding a book using a valid new ISBN.
* **ISBN validation:** Rejecting duplicate or malformed ISBN values.
* **Book borrowing:** Allowing a member to borrow a book when copies are available.
* **Book availability:** Preventing borrowing when no copies are available.
* **Book return:** Successfully returning a book currently borrowed by the member.
* **Invalid return handling:** Rejecting a return when the specified book is not currently borrowed by that member.
* **Member borrowing limit:** Allowing borrowing up to the configured limit and rejecting borrowing beyond that limit.
* **Fine calculation:** Verifying zero-overdue, mid-range overdue, and overdue-tier boundary calculations.
* **Existing member behavior:** Verifying relevant member-management validation already represented in the repository's test code.

---

## 5. Features Not to be Tested

The graphical user interface is excluded from this test plan because the scope of this exercise is functional testing of the LibraryHub domain logic rather than UI testing. The relevant repository implementation and existing tests are focused on Java classes and their behavior, so testing visual layouts, buttons, forms, colors, or screen navigation would not provide meaningful coverage for this test scope.

Database integration, network/API integration, authentication, deployment infrastructure, and performance/load testing are also excluded because these components are not part of the current LibraryHub testing baseline.

This exclusion keeps the test effort focused on the functional requirements being evaluated in this exercise.

---

## 6. Test Approach

Testing will use primarily functional black-box testing based on the expected behavior of the LibraryHub operations. Test cases will include positive tests, negative/error-path tests, boundary-value tests, and limit tests.

The tester will first inspect the current Java implementation to establish the available functionality and then execute the defined test cases against that baseline. Existing repository tests will also be considered when evaluating member-management behavior.

If a requested operation is not implemented in the current baseline and therefore cannot be executed, the corresponding test will be recorded as **Blocked** rather than being incorrectly marked as Pass or Fail.

---

## 7. Item Pass/Fail Criteria

An individual test case will be marked **PASS** when the actual result exactly matches the expected result. A test case will be marked **FAIL** when the implemented functionality can be executed but produces behavior different from the expected result. A test case will be marked **BLOCKED** when it cannot be executed because the required functionality, dependency, or precondition is unavailable in the current baseline.

The overall test cycle will be considered successful when **at least 95% of the planned test cases pass and zero Critical-severity defects remain open**.

Because the planned execution contains 12 test cases, achieving at least 95% requires all 12 cases to pass in practice:

**12/12 = 100%**
**11/12 = 91.67%**

Therefore, for this 12-test execution cycle, the practical acceptance criterion is **12 passed tests and zero open Critical defects**.

---

## 8. Suspension Criteria and Resumption Requirements

Testing will be suspended if the LibraryHub source code cannot be compiled, the test environment is unavailable, or a major environment problem prevents meaningful execution of the test suite.

Testing may also be temporarily suspended if a blocking infrastructure problem prevents execution of multiple test cases. Testing will resume after the compilation, environment, or blocking condition has been corrected and the affected tests can be executed reliably.

A single missing or unimplemented feature will not automatically suspend the complete test cycle; the affected test will instead be recorded as **Blocked** with an appropriate explanation.

---

## 9. Test Deliverables

The following deliverables will be produced for this testing exercise:

* `docs/test-plan.md` — IEEE 829-based test plan.
* `docs/test-cases.md` — Detailed LibraryHub test cases and execution results.
* `docs/rtm.md` — Requirements Traceability Matrix.
* GitHub Issues — Defect reports for executable test cases that fail.
* Test execution results — Pass, Fail, or Blocked status with a brief execution note.

These deliverables provide traceability from requirements through test design, execution, and defect reporting.

---

## 10. Testing Tasks

The testing activities will be performed in the following sequence:

1. Review the LibraryHub source code and existing tests.
2. Identify and document the functional requirements.
3. Prepare the IEEE 829 test plan.
4. Design the required 12 functional test cases.
5. Build the Requirements Traceability Matrix.
6. Manually execute all 12 test cases against the current implementation.
7. Record Pass, Fail, or Blocked results with execution notes.
8. Create a GitHub Issue for each reproducible failed test case.
9. Link applicable GitHub Issue numbers to the corresponding test cases.
10. Review the final documentation for completeness and traceability.

---

## 11. Environmental Needs

Testing requires a Java development environment capable of compiling and executing the LibraryHub source code and existing tests. The repository should be checked out at the version being evaluated so that the test results correspond to a known source baseline.

The test environment should contain the required Java Development Kit and a command-line or IDE-based Java execution environment. No external database or network service is required for the domain-level testing covered by this plan unless such a dependency is introduced by the implementation under test.

The tester will use the repository's current source and test files as the primary test baseline.

---

## 12. Responsibilities

The tester is responsible for reviewing the implementation, preparing the test plan and test cases, executing the tests, recording objective results, and reporting reproducible defects.

The developer or repository maintainer is responsible for investigating and correcting confirmed defects identified through failed test cases.

The reviewer or instructor is responsible for evaluating whether the test documentation, execution evidence, traceability, and defect reports satisfy the requirements of the testing exercise.

---

## 13. Staffing and Training Needs

The testing activity requires one tester with basic knowledge of Java, object-oriented programming, functional software testing, Markdown, Git, and GitHub Issues.

The tester should understand the LibraryHub domain, including books, members, borrowing, returning, borrowing limits, and overdue fines. No specialized testing tools or formal certification are required for this exercise.

---

## 14. Schedule

The planned activities follow the time allocation specified in the laboratory task:

| Activity                         | Planned Time |
| -------------------------------- | -----------: |
| Test Plan Preparation            |   60 minutes |
| Test Case Design                 |   75 minutes |
| Requirements Traceability Matrix |   30 minutes |
| Manual Test Execution            |   35 minutes |

Additional time may be required for documenting failed tests, creating GitHub Issues, and performing any required re-testing after defect fixes.

---

## 15. Risks and Contingencies

A major testing risk is a mismatch between the requested LibraryHub requirements and the functionality currently implemented in the repository. Some operations specified by the testing exercise may not be available in the current implementation, which can prevent direct execution of the corresponding test cases.

The contingency for an unavailable feature is to record the affected test as **Blocked** with a clear explanation rather than fabricating an execution result. If an implemented feature produces an incorrect result, the tester will record it as **Fail** and create a corresponding GitHub Issue.

Another risk is that changes to the source code during testing could make results inconsistent with the evaluated baseline. Therefore, the tested commit/version should be recorded before execution.

---

## 16. Approvals

**Test Plan ID:** TP-LH-001
**Project:** LibraryHub – Library Management System
**Prepared By:** SQE Lab Tester
**Version:** 1.0
**Status:** Submitted for Review

The test plan requires review and approval by the responsible instructor or project reviewer before it is considered formally approved.

---

## Test Plan Acceptance Summary

This test plan covers the required IEEE 829 test-plan areas for the LibraryHub testing exercise and defines a focused functional testing scope. It explicitly excludes UI and unrelated infrastructure testing, defines measurable pass/fail criteria, and establishes procedures for handling both failed and blocked tests.

The plan provides the baseline for the subsequent **12 Test Cases**, **Requirements Traceability Matrix**, and **Manual Execution Pass** required by the laboratory task.
