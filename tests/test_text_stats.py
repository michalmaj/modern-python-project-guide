"""Tests for basic text statistics utilities."""

from text_toolkit import (
    count_characters,
    count_words,
    normalize_whitespace,
)


def test_normalize_whitespace_replaces_repeated_spaces() -> None:
    text = "Python    is   fun"

    result = normalize_whitespace(text)

    assert result == "Python is fun"


def test_normalize_whitespace_handles_tabs_and_newlines() -> None:
    text = "Python\tis\nfun"

    result = normalize_whitespace(text)

    assert result == "Python is fun"


def test_count_words_returns_zero_for_empty_text() -> None:
    result = count_words("")

    assert result == 0


def test_count_words_handles_repeated_whitespace() -> None:
    text = "Python    project\nworkflow"

    result = count_words(text)

    assert result == 3


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
