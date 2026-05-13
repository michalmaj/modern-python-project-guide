# Common Questions

This page answers common questions about the decisions used in this guide.

The goal is not to cover every possible Python workflow.

The goal is to explain why this repository uses a small, practical setup for learning modern Python project structure.

## Why not just use pip?

`pip` is an important Python tool, and many projects still use it.

However, this guide uses `uv` because it provides a compact workflow for:

- creating project environments,
- managing dependencies,
- locking dependency versions,
- running tools inside the project environment,
- working with Python versions.

For beginners moving from scripts to projects, using one consistent tool can make the workflow easier to understand.

This does not mean `pip` is bad.

It means this guide chooses `uv` to keep the project workflow modern and reproducible.

## Why commit uv.lock?

The `uv.lock` file stores the exact dependency versions resolved for the project.

It should be committed because it helps make the project reproducible.

Without a lockfile, different machines may install different dependency versions.

That can lead to confusing situations where:

- tests pass on one machine but fail on another,
- CI uses different versions than local development,
- a dependency update breaks the project unexpectedly.

The `pyproject.toml` file describes dependency requirements.

The `uv.lock` file records the exact resolved versions.

Both files are important.

## Why use a src/ layout?

This guide uses:

```text
src/text_toolkit/
```

instead of placing the package directly in the repository root.

The `src/` layout makes the project structure clearer:

- source code lives in `src/`,
- tests live in `tests/`,
- documentation lives in `docs/`,
- GitHub-specific files live in `.github/`.

It also avoids some import confusion that can happen when Python accidentally imports code directly from the current working directory.

In this guide, `src/` is used to teach clean project structure.

Packaging and publishing are separate topics.

## Is this a complete Python packaging guide?

No.

This guide uses an importable package inside `src/`, but it does not yet cover the full packaging workflow.

It does not currently explain:

- build backends,
- `[build-system]`,
- editable installs,
- wheels,
- source distributions,
- publishing to PyPI.

That is intentional.

The first version focuses on:

- project structure,
- dependency management,
- tests,
- linting,
- formatting,
- CI,
- pull requests.

Packaging can be added later as a separate topic.

## Why does pytest use pythonpath = ["src"]?

The pytest configuration includes:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

The `pythonpath = ["src"]` setting lets tests import the example package from the `src/` directory.

For example:

```python
from text_toolkit import count_words
```

This keeps the guide simple before introducing packaging or editable installs.

In a more complete packaging workflow, the project may instead be installed into the environment as an editable package.

## Why use Ruff?

Ruff provides linting and formatting in one fast tool.

In this guide, Ruff helps check:

- unused imports,
- import ordering,
- common style issues,
- suspicious patterns,
- opportunities to use modern Python syntax.

It also formats code consistently.

The goal is not to satisfy tools blindly.

The goal is to reduce repetitive review comments and keep code easier to maintain.

## Why not enable all Ruff rules?

Ruff supports many rules.

Enabling everything at once can be overwhelming, especially in a beginner-friendly guide.

This project starts with a moderate rule set:

```toml
select = [
    "E",
    "F",
    "I",
    "B",
    "UP",
]
```

More rules can be added later if the project needs them.

A smaller configuration that people understand is better than a strict setup copied without context.

## Is it okay to ignore some Ruff rules?

Yes, if the decision is intentional.

Some rules may be too strict for specific contexts, such as:

- tests,
- UI code,
- educational examples,
- visual demos,
- configuration-heavy code.

For example, strict configurations may complain about magic values in tests.

A small test like this can still be readable:

```python
def test_count_words_handles_repeated_whitespace() -> None:
    text = "Python    project\nworkflow"

    result = count_words(text)

    assert result == 3
```

The value `3` is clear in this context.

If a rule is too strict only for tests, prefer a narrow exception:

```toml
[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "PLR2004",
]
```

The important thing is to know why a rule is disabled.

## Why not add Docker?

Docker is useful in many projects.

However, it would add another layer of tooling to this guide.

This repository focuses on the Python project foundation first:

- project structure,
- dependencies,
- tests,
- linting,
- formatting,
- CI,
- pull requests.

Docker can be introduced later when there is a clear reason for it.

Adding it too early would make the guide heavier without helping the core learning path.

## Why not add pre-commit?

`pre-commit` is useful for running checks before commits.

However, it adds another tool and another configuration file.

This guide first teaches the commands directly:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Once readers understand these commands, adding `pre-commit` later will be easier.

The guide intentionally avoids too much automation too early.

## Why not add type checking yet?

Type checking with tools such as Pyright or mypy can be valuable.

The example code already uses type hints, but this guide does not add a type checker in the first version.

That is intentional.

Before adding type checking, the guide first explains:

- project structure,
- dependency management,
- tests,
- linting,
- formatting,
- CI.

Type checking is a good candidate for a future chapter.

## Why not add coverage yet?

Coverage tools can show which lines are executed by tests.

However, coverage can be misleading if introduced too early.

High coverage does not automatically mean good tests.

This guide first focuses on writing clear tests that check behavior.

Coverage can be added later after the testing basics are clear.

## Why does CI use uv sync --locked?

Local development usually uses:

```bash
uv sync
```

CI uses:

```bash
uv sync --locked
```

The `--locked` option tells `uv` to use the existing `uv.lock` file without updating it.

This matters because CI should verify the committed project state.

CI should not silently change the lockfile.

If `pyproject.toml` and `uv.lock` are out of sync, CI should fail and tell the developer to update the lockfile locally.

## What should I run after cloning the repository?

Run:

```bash
uv sync
```

Then run the local checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

If formatting fails, run:

```bash
uv run ruff format .
```

Then repeat the checks.

## What should I commit?

Commit files that describe the project and its source code, such as:

```text
pyproject.toml
uv.lock
.python-version
src/
tests/
docs/
.github/
README.md
CONTRIBUTING.md
```

Do not commit generated local files such as:

```text
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.coverage
```

These files are local artifacts and should stay ignored.

## Is this repository a template?

Not exactly.

This repository can inspire a project template, but its main purpose is educational.

It explains why each file and tool exists.

The goal is not only to copy the final structure.

The goal is to understand how the structure grows step by step.

## Rule of thumb

If a tool helps you understand, run, test, or maintain the project, it may belong here.

If a tool adds complexity before the basics are clear, it should probably wait.