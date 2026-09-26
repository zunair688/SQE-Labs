import pytest
from libraryhub.library import Library


@pytest.fixture
def library():
    """Fresh Library for each test to keep tests isolated."""
    return Library()


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