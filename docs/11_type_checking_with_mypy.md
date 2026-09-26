# Static Type Checking with mypy

Python does not require type annotations to run a program.

This project still uses annotations because they document what values functions
accept and return:

```python
def count_words(text: str) -> int:
    ...
```

The annotation says that `text` should be a string and the result should be an
integer.

## Type hints do not check themselves

Python normally does not reject a call just because it conflicts with an
annotation. Type hints are metadata that tools can inspect.

A static type checker reads the code without running it and reports operations
that are inconsistent with the annotations. This project uses mypy for that
job.

Tests and type checking answer different questions:

- pytest runs code and checks observed behavior,
- mypy analyzes possible value types before the code runs.

Both are useful, and neither replaces the other.

## Add mypy as a development dependency

mypy is needed while developing the project, not while using `text-toolkit` as
a library. Add it to the `dev` dependency group:

```bash
uv add --group dev mypy
```

After cloning this repository, `uv sync` installs mypy with the other
development dependencies.

## Configure mypy

The project keeps its mypy settings in `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.12"
files = ["src", "tests"]
strict = true
```

These options mean:

- `python_version` checks code using Python 3.12 language rules,
- `files` defines the directories checked when no paths are passed,
- `strict` enables mypy's optional strictness checks.

Strict mode works well here because this is a small project whose functions and
tests already have annotations. Adding strict mode to a larger existing project
may require a gradual approach.

The exact checks included in strict mode can change between mypy releases. The
project therefore runs mypy after dependency updates instead of assuming that a
previous result will always stay valid.

## Run the type checker

Run:

```bash
uv run mypy
```

The `files` setting means that no paths are needed in the command. A successful
check reports output similar to:

```text
Success: no issues found in 4 source files
```

## What an error looks like

Consider code that assigns the integer returned by `count_words` to a variable
declared as a string:

```python
word_count: str = count_words("clean Python project")
```

mypy reports an incompatible assignment because the annotation and return type
do not agree. The program does not need to run for mypy to find that mismatch.

Read the file path, line number, and error code in the message. Fix the type or
the code rather than silencing the warning without understanding it.

## What mypy does not prove

A successful mypy check does not mean that the program is correct.

mypy does not replace:

- tests for runtime behavior,
- Ruff checks for linting and formatting,
- code review,
- clear program design.

Type checking is one layer of feedback in the project workflow.

## Rule of thumb

Use type hints to describe interfaces.

Use mypy to check whether the code follows those descriptions.

Use pytest to check what the code actually does when it runs.

## Continue

- [Previous: Building Distributions](10_building_distributions.md)
- [Next: Project Checklist](09_checklist.md)
- [Back to README](../README.md)
