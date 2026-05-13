"""Basic text statistics utilities.

This module is intentionally small and simple.

The goal of this project is not to build an advanced text processing library.
The goal is to show how a Python project can be structured, tested, checked,
and maintained step by step.
"""


def normalize_whitespace(text: str) -> str:
    """Return text with repeated whitespace replaced by single spaces."""
    return " ".join(text.split())


def count_words(text: str) -> int:
    """Count words in a text after whitespace normalization."""
    normalized_text = normalize_whitespace(text)

    if not normalized_text:
        return 0

    return len(normalized_text.split(" "))


def count_characters(text: str, include_whitespace: bool = True) -> int:
    """Count characters in a text.

    Args:
        text: Input text.
        include_whitespace: If True, count all characters. If False, ignore
            whitespace characters such as spaces, tabs, and newlines.

    Returns:
        The number of characters.
    """
    if include_whitespace:
        return len(text)

    return len("".join(text.split()))