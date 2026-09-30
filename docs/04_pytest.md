# pytest

`pytest` is the testing framework used in this guide.

Tests help verify that the project behaves as expected.

They are also an important part of a clean development workflow.

## Why tests matter

A project without tests can still work.

The problem is that every change becomes riskier.

Without tests, it is harder to answer questions such as:

- Did this change break existing behavior?
- Does this function handle edge cases?
- Can another person safely modify this code?
- Can this project be checked automatically in CI?

Tests do not make a project perfect, but they make it easier to trust.

## What we test in this project

The example package is intentionally small.

It contains simple text utilities such as:

- whitespace normalization,
- word counting,
- character counting.

These functions are simple enough to understand quickly, but still useful for demonstrating testing.

The goal is not to build an advanced text processing library.

The goal is to show how tests fit into a maintainable Python project.

## Test directory

Tests are stored in the `tests/` directory:

```text
tests/
└── test_text_stats.py
```

Keeping tests separate from source code makes the project easier to navigate.

The source code lives in:

```text
src/text_toolkit/
```

The tests live in:

```text
tests/
```

This separation makes it clear which files implement behavior and which files verify it.

## Test file naming

The test file is named:

```text
test_text_stats.py
```

This name follows a common pytest convention.

By default, pytest discovers files whose names start with `test_` or end with `_test.py`.

Inside those files, test functions usually start with `test_`.

Example:

```python
def test_count_characters_includes_whitespace_by_default() -> None:
    result = count_characters("hello world")

    assert result == 11
```

The function name describes the expected behavior.

Good test names should be readable.

A person should be able to understand what is being tested without reading the whole implementation first.

## Arrange, Act, Assert

Many tests in this guide follow a simple structure:

```text
Arrange → Act → Assert
```

This means:

1. prepare the input,
2. call the function,
3. check the result.

Example:

```python
def test_count_characters_can_ignore_whitespace() -> None:
    result = count_characters("hello world", include_whitespace=False)

    assert result == 10
```

This style makes tests easier to read and review.

## Parametrizing related cases

Sometimes several inputs should follow the same behavior. Copying the entire
test for each input would make the test file repetitive.

pytest can run one test function with several sets of values:

```python
import pytest


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
```

The names `text` and `expected` match the two values in every tuple. pytest
runs the function once for each tuple and reports every case separately.

This example covers repeated spaces, tabs and newlines, whitespace-only text,
and leading or trailing spaces without duplicating the test logic.

Parametrization is useful when the action and assertion stay the same. Use
separate tests when cases describe different behavior or need different setup.

## pytest configuration

The project configures pytest in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

The `testpaths` option tells pytest where tests are located.

### How tests import the package

The project defines a build system in `pyproject.toml`. When you run:

```bash
uv sync
```

`uv` installs the project into its environment in editable mode.

For example, tests can import:

```python
from text_toolkit import count_words
```

No pytest-specific `pythonpath` shortcut is needed. Tests use the installed
package, while editable installation keeps changes in `src/` immediately
available during development.

## Running tests

Tests can be run with:

```bash
uv run pytest
```

This command runs pytest inside the project environment managed by `uv`.

Using `uv run` is important because it makes sure the command uses the dependencies installed for this project.

## What good tests should do

Good tests should be:

- small,
- readable,
- focused on behavior,
- easy to run,
- independent from each other.

A test should usually check one idea.

If a test checks many unrelated things at once, it becomes harder to understand what failed.

## What tests should avoid

Tests should avoid:

- depending on execution order,
- requiring manual steps,
- testing too many things at once,
- duplicating implementation details,
- using unclear names.

Tests should describe expected behavior, not simply repeat how the function is implemented.

## Local workflow

Before opening a pull request with code changes, run:

```bash
uv run pytest
```

If tests fail, fix the problem before pushing the branch.

Later, the same command will also run automatically in GitHub Actions.

This means tests will become part of both:

- the local development workflow,
- the pull request review workflow.

## Rule of thumb

Tests are not something added at the end of a project.

They are part of how the project grows.

A small project with a few clear tests is better than a large project that nobody can safely change.

## Continue

- [Previous: pyproject.toml](03_pyproject_toml.md)
- [Next: Ruff](05_ruff.md)
- [Back to documentation home](index.md)
