"""Tests for basic text statistics utilities."""

import pytest

from text_toolkit import (
    count_characters,
    count_words,
    normalize_whitespace,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Python    is   fun", "Python is fun"),
        ("Python\tis\nfun", "Python is fun"),
        (" \t\n ", ""),
        ("  Python project  ", "Python project"),
    ],
)
def test_normalize_whitespace_handles_common_inputs(text: str, expected: str) -> None:
    result = normalize_whitespace(text)

    assert result == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        (" \t\n ", 0),
        ("  Python project  ", 2),
        ("Python    project\nworkflow", 3),
    ],
)
def test_count_words_handles_common_whitespace(text: str, expected: int) -> None:
    result = count_words(text)

    assert result == expected


def test_count_characters_includes_whitespace_by_default() -> None:
    result = count_characters("hello world")

    assert result == 11


def test_count_characters_can_ignore_whitespace() -> None:
    result = count_characters("hello world", include_whitespace=False)

    assert result == 10


def test_count_characters_ignores_tabs_and_newlines_when_requested() -> None:
    text = "hello\tworld\nagain"

    result = count_characters(text, include_whitespace=False)

    assert result == 15
