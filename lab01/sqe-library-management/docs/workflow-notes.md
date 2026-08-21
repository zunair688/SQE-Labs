## Task 3 — Deliberate Merge Conflict

A deliberate merge conflict was created between
feature/rename-field-a and feature/rename-field-b.

Both branches modified the same field in Book.java differently.
Branch A renamed the field from id to bookId, while Branch B renamed
the field from id to accessionNumber.

After Branch A was merged into main, main was merged into
feature/rename-field-b locally. Git could not automatically merge
the changes because both branches modified the same line differently.

The conflict was resolved locally by keeping bookId as the final
field name. The conflict markers were removed, the resolved file
was staged, and a merge-resolution commit was created and pushed.


## Task 4 — Commit Hygiene Audit

### Last 10 Commits

4605bbc (HEAD -> feature/rename-field-b, origin/feature/rename-field-b) docs: document merge conflict resolution
a48c077 fix(book): resolve field rename conflict
5809432 refactor(book): rename id to accessionNumber
0f7abe5 (origin/main, origin/HEAD, main) Merge pull request #6 from zunair688/feature/rename-field-a
540fee3 (origin/feature/rename-field-a, feature/rename-field-a) refactor(book): rename id to bookId
e2a0e62 Merge pull request #5 from zunair688/feature/add-book-to-member
8499293 (origin/feature/add-book-to-member, feature/add-book-to-member) fix(member): address code review feedback
09127c6 feat(book): validate book details
c4916d6 feat(member): add book removal
76f4fa9 feat(member): add book assignment with validation

Two Weak Commit Messages
1. Original: docs: document merge conflict resolution

Rewritten: docs(workflow): document deliberate merge conflict resolution

Why it is better: The rewritten message identifies the specific documentation area affected (workflow) and clearly describes what was documented.

2. Original: fix(book): resolve field rename conflict

Rewritten: fix(book): resolve id field rename conflict

Why it is better: The rewritten message is more specific because it identifies the exact field involved in the conflict.