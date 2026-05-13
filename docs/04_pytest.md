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
def test_count_words_returns_zero_for_empty_text() -> None:
    result = count_words("")

    assert result == 0
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
def test_normalize_whitespace_replaces_repeated_spaces() -> None:
    text = "Python    is   fun"

    result = normalize_whitespace(text)

    assert result == "Python is fun"
```

This style makes tests easier to read and review.

## pytest configuration

The project configures pytest in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

The `testpaths` option tells pytest where tests are located.

The `pythonpath` option allows tests to import the package from the `src/` directory.

This keeps the project structure clean while still making imports straightforward.

### Why `pythonpath = ["src"]` is used here

The project currently uses:

```toml
pythonpath = ["src"]
```

This lets pytest import the example package from the `src/` directory.

For example, tests can import:

```python
from text_toolkit import count_words
```

This is an educational simplification.

It keeps the guide focused on tests and project structure before introducing packaging, build systems, or editable installs.

In a more complete packaging workflow, the project may instead be installed into the environment as an editable package.

That topic is intentionally left for a later stage.

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