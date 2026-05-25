# Glossary

This glossary explains common terms used in this guide.

It is intentionally short and practical.

The goal is to help readers understand project tooling vocabulary without needing to leave the repository.

## Branch

A branch is an isolated line of work in Git.

In this guide, every meaningful change should happen on a separate branch.

Example:

```bash
git switch -c docs/add-glossary
```

Branches help keep changes focused and make pull requests easier to review.

## Build system

A build system tells Python tools how to build and install a project as a distribution.

Build systems are usually configured through a `[build-system]` section in `pyproject.toml`.

This guide does not introduce a build system in the first version.

That is intentional.

The first version focuses on project structure, tests, linting, formatting, CI, and pull requests.

## CI

CI means continuous integration.

In this guide, CI runs automated checks on GitHub using GitHub Actions.

The CI workflow runs:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

CI helps protect the `main` branch from broken changes.

## Commit

A commit is a saved change in Git history.

Good commits should be small, focused, and readable.

Example:

```text
docs: add project glossary
```

Avoid vague commit messages such as:

```text
update
fix
changes
```

## Dependency

A dependency is an external package needed by a project.

Dependencies are listed in `pyproject.toml`.

This guide separates dependencies into:

- runtime dependencies,
- development dependencies.

## Development dependency

A development dependency is needed while developing the project, but not necessarily when using the project as a library.

Examples:

- `pytest`,
- Ruff,
- coverage tools,
- type checkers,
- documentation tools.

In this guide, development dependencies are added with:

```bash
uv add --group dev pytest
uv add --group dev ruff
```

## Formatting

Formatting controls how code looks.

It includes things such as spacing, line wrapping, and blank lines.

In this guide, formatting is checked with:

```bash
uv run ruff format --check .
```

Files can be formatted automatically with:

```bash
uv run ruff format .
```

## GitHub Actions

GitHub Actions is GitHub's automation system.

This guide uses GitHub Actions to run CI.

The workflow file is stored in:

```text
.github/workflows/ci.yml
```

## Linting

Linting checks code for common issues.

Examples include:

- unused imports,
- undefined names,
- import ordering problems,
- suspicious patterns,
- outdated syntax.

In this guide, linting is run with:

```bash
uv run ruff check .
```

## Lockfile

A lockfile records exact dependency versions.

In this guide, the lockfile is:

```text
uv.lock
```

The lockfile should be committed to Git.

It helps make installs reproducible across machines and CI environments.

## Main branch

The `main` branch is the primary branch of the repository.

It should represent the current stable state of the project.

In this guide, meaningful changes should not be committed directly to `main`.

They should go through branches and pull requests.

## Package

The word “package” can mean different things in Python.

In this guide, “package” means an importable Python package inside `src/`.

Example:

```text
src/text_toolkit/
```

This guide does not yet cover building and publishing installable Python distributions.

That is a separate topic.

## Pull request

A pull request is a proposal to merge changes from one branch into another branch.

In this guide, pull requests are used to:

- explain what changed,
- run CI checks,
- review changes before merging,
- keep `main` protected.

A good pull request should answer:

```text
What changed?
Why was it changed?
How was it checked?
```

## pyproject.toml

`pyproject.toml` is the central configuration file for a modern Python project.

In this guide, it contains:

- project metadata,
- Python version requirements,
- dependencies,
- development dependencies,
- pytest configuration,
- Ruff configuration.

## pytest

`pytest` is the testing framework used in this guide.

Tests are run with:

```bash
uv run pytest
```

The tests live in:

```text
tests/
```

## Runtime dependency

A runtime dependency is needed by the project when the project code runs.

Example:

```bash
uv add rich
```

Runtime dependencies belong in the `[project]` dependencies section of `pyproject.toml`.

Development tools such as `pytest` and Ruff should not be runtime dependencies.

## Ruff

Ruff is the linting and formatting tool used in this guide.

It runs linting with:

```bash
uv run ruff check .
```

It checks formatting with:

```bash
uv run ruff format --check .
```

It formats files with:

```bash
uv run ruff format .
```

## src layout

The `src/` layout means that Python source code lives inside the `src/` directory.

Example:

```text
src/text_toolkit/
```

This separates source code from:

- tests,
- documentation,
- repository metadata,
- GitHub configuration.

## Test

A test checks whether code behaves as expected.

Example:

```python
def test_count_words_returns_zero_for_empty_text() -> None:
    result = count_words("")

    assert result == 0
```

Tests in this guide live in:

```text
tests/
```

and are run with:

```bash
uv run pytest
```

## uv

`uv` is the Python project and dependency management tool used in this guide.

It is used to:

- initialize the project,
- pin the Python version,
- manage dependencies,
- create or update the virtual environment,
- run project tools,
- generate and use the lockfile.

Common commands:

```bash
uv sync
uv add package-name
uv add --group dev package-name
uv run pytest
```

## uv sync

`uv sync` synchronizes the local environment with the project configuration.

It uses:

```text
pyproject.toml
uv.lock
```

For local development, run:

```bash
uv sync
```

In CI, this guide uses:

```bash
uv sync --locked
```

## Virtual environment

A virtual environment is an isolated Python environment for one project.

In this guide, `uv` creates the local virtual environment in:

```text
.venv/
```

The `.venv/` directory should not be committed to Git.

It is generated locally.