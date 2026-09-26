# Unit Testing Notes

## Task 5 — Coverage Housekeeping and CI Readiness

### Pytest Output Comparison

Two pytest commands were executed to compare verbose and short output formats.

#### Verbose output

Command:

```text
python -m pytest -v tests/
```

The verbose mode displays each individual test name and its result (`PASSED` or `FAILED`). This format is useful when developing or debugging tests because it clearly shows which specific test cases were executed.

Result:

```text
40 passed in 0.20s
```

The complete verbose output is stored in:

```text
docs/pytest-verbose-output.txt
```

#### Short traceback output

Command:

```text
python -m pytest --tb=short
```

The short traceback option provides a more compact test report. Instead of displaying detailed information for every test, it summarizes the test files and results while keeping traceback information concise when a failure occurs.

Result:

```text
40 passed in 0.18s
```

The complete short-output result is stored in:

```text
docs/pytest-short-output.txt
```

### When to Use Each Format

* **`pytest -v`**: Use during development and debugging when individual test names and results need to be clearly identified.
* **`pytest --tb=short`**: Use for a more compact test report, especially when running the complete test suite or reviewing CI output.

## Fixture Scopes

The project uses pytest fixtures in `tests/conftest.py`.

### Function Scope

The `library` fixture uses the default function scope:

```python
@pytest.fixture
def library():
    """Fresh Library for each test to keep tests isolated."""
    return Library()
```

A function-scoped fixture is created separately for each test that uses it. This keeps tests isolated so that changes made by one test do not affect another test.

### Module Scope

The `populated_library` fixture uses module scope:

```python
@pytest.fixture(scope="module")
def populated_library():
    """
    Shared Library for tests that need the same expensive setup.

    Module scope creates this fixture once for the whole test module.
    It is appropriate when setup is expensive and tests do not mutate
    the shared state in a way that could affect other tests.
    """
    library = Library()
    library.loans[1] = ["ISBN-1", "ISBN-2", "ISBN-3"]
    return library
```

A module-scoped fixture is created once for the test module and can be reused by tests in that module. It is suitable when the setup is shared and tests do not modify the shared state in a way that could affect other tests.

## Pytest Configuration

The project uses `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
```

This configuration tells pytest to:

* Search for tests inside the `tests` directory.
* Recognize files following the `test_*.py` naming convention.

The configuration was verified successfully:

```text
configfile: pytest.ini
testpaths: tests
collected 40 items
```

## Final Test Status

The complete test suite currently contains 40 tests, and all tests pass successfully.

```text
40 passed
```
