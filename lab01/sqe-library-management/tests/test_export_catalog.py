from unittest.mock import mock_open, patch

import pytest

from libraryhub.library import Book, Library, LibraryIOError


def test_export_catalog_writes_expected_content(library):
    library.catalog.extend(
        [
            Book("9780000000001", 3),
            Book("9780000000002", 5),
        ]
    )

    mocked_file = mock_open()

    with patch("builtins.open", mocked_file):
        library.export_catalog("catalog.txt")

    mocked_file.assert_called_once_with(
        "catalog.txt",
        "w",
        encoding="utf-8",
    )

    handle = mocked_file()
    assert handle.write.call_count == 2
    handle.write.assert_any_call("9780000000001,3\n")
    handle.write.assert_any_call("9780000000002,5\n")


def test_export_catalog_translates_os_error(library):
    with patch(
        "builtins.open",
        side_effect=OSError("disk error"),
    ):
        with pytest.raises(LibraryIOError, match="Unable to export catalog"):
            library.export_catalog("catalog.txt")