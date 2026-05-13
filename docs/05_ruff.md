# Ruff

`ruff` is the linting and formatting tool used in this guide.

It helps keep Python code clean, consistent, and easier to review.

In this project, Ruff is used for two related but different tasks:

- linting,
- formatting.

## Why use Ruff?

Python projects become easier to maintain when code style and common issues are checked automatically.

Without an automated tool, reviewers may spend too much time commenting on things such as:

- unused imports,
- inconsistent import order,
- outdated syntax,
- formatting differences,
- small bug-prone patterns.

Ruff helps move many of these checks from manual review to automated tooling.

This makes pull requests easier to review because people can focus more on design, behavior, and clarity.

## Linting vs formatting

Linting and formatting are related, but they are not the same thing.

## Linting

Linting checks code for potential problems.

Examples:

- unused imports,
- undefined names,
- suspicious code patterns,
- unnecessary complexity,
- outdated syntax that can be modernized.

In this project, linting is run with:

```bash
uv run ruff check .
```

## Formatting

Formatting changes how code looks.

It focuses on consistent layout rather than program behavior.

Examples:

- line wrapping,
- spacing,
- blank lines,
- quote style where applicable.

In this project, formatting can be checked with:

```bash
uv run ruff format --check .
```

To automatically format files, run:

```bash
uv run ruff format .
```

## Ruff configuration

Ruff is configured in `pyproject.toml`.

The current configuration looks like this:

```toml
[tool.ruff]
line-length = 88
target-version = "py312"
src = ["src", "tests"]

[tool.ruff.lint]
select = [
    "E",
    "F",
    "I",
    "B",
    "UP",
]
```

## `line-length`

The `line-length` option defines the preferred maximum line length.

This project uses:

```toml
line-length = 88
```

This is a common default also used by popular Python formatting tools.

The exact number is less important than consistency.

## `target-version`

The `target-version` option tells Ruff which Python version the project targets.

This project uses:

```toml
target-version = "py312"
```

This matches the project requirement:

```toml
requires-python = ">=3.12"
```

Knowing the target Python version allows Ruff to suggest modern syntax safely.

## `src`

The `src` option tells Ruff where the source code and tests are located.

```toml
src = ["src", "tests"]
```

This helps Ruff understand the project layout.

## Selected rule groups

The current configuration selects these rule groups:

```toml
select = [
    "E",
    "F",
    "I",
    "B",
    "UP",
]
```

These groups provide a useful starting point without overwhelming the project.

## `E`

The `E` rules come from pycodestyle-style checks.

They catch common style issues.

## `F`

The `F` rules come from Pyflakes-style checks.

They catch important problems such as unused imports and undefined names.

## `I`

The `I` rules check import sorting.

This helps keep imports consistent and readable.

## `B`

The `B` rules come from flake8-bugbear-style checks.

They detect patterns that are often suspicious or bug-prone.

## `UP`

The `UP` rules come from pyupgrade-style checks.

They suggest modern Python syntax when the target Python version allows it.

## Why not select all rules?

Ruff supports many rules, but enabling everything at once can be too much for a beginner-friendly project.

A strict configuration can be useful in mature codebases.

However, in a learning project, too many warnings can distract from the main goal.

This guide starts with a practical, moderate configuration.

More rules can be added later when the project needs them.

## When it is okay to ignore rules

Linting rules are useful, but they are not absolute laws.

Sometimes a rule is helpful in most files, but too strict in a specific context.

For example, educational, visual, UI, configuration, or demo code may sometimes need exceptions.

A project may choose to ignore selected rules intentionally:

```toml
[tool.ruff.lint]
select = [
    "E",
    "F",
    "I",
    "B",
    "UP",
    "PL",
]

ignore = [
    "PLR0913", # Too many arguments; sometimes acceptable in UI/config code.
    "PLR2004", # Magic values may be acceptable in small visual/demo code.
]
```

This does not mean that linting is ignored completely.

It means that the project team made a conscious decision.

The important part is to know why a rule is disabled.

## Example: magic values in tests

Some strict rule sets warn about magic values.

For example, a test like this may contain numeric values directly in the assertion:

```python
def test_count_words_handles_repeated_whitespace() -> None:
    text = "Python    project\nworkflow"

    result = count_words(text)

    assert result == 3
```

The value `3` is technically a magic number.

However, in a small test, this can be perfectly readable.

Replacing it with a named constant could make the test longer without making it clearer.

In such cases, the team may decide that the rule is too strict for tests.

## Prefer narrow exceptions

When possible, prefer narrow exceptions instead of disabling a rule everywhere.

For example, if a rule is too strict only for tests, use a per-file ignore:

```toml
[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "PLR2004",
]
```

This keeps the rule active for source code while relaxing it for test files.

## Good reasons to ignore a rule

Ignoring a rule may be reasonable when:

- the rule makes educational examples harder to read,
- the rule is too strict for tests,
- the rule does not fit the project style,
- the warning is technically correct but not useful in context,
- the code becomes less clear after satisfying the rule.

## Bad reasons to ignore a rule

Ignoring a rule is usually a bad idea when:

- nobody understands why it was disabled,
- the rule points to a real bug,
- the team wants to avoid fixing messy code,
- the ignore list grows without discussion,
- the project disables rules before learning what they mean.

## Rule of thumb

Start with a simple Ruff configuration.

Add stricter rules gradually.

Ignore rules only when there is a clear reason.

A good linting configuration should help the project stay clean without making the code harder to understand.

The goal is not to satisfy the tool.

The goal is to make the project easier to maintain.
