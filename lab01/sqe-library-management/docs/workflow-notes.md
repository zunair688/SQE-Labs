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