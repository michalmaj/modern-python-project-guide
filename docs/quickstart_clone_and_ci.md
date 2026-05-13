# Clone and CI Quickstart

This quickstart is for people who already have a Python project on GitHub and want to run it locally or configure a simple CI workflow.

It focuses on the practical path:

```text
clone repository → sync environment → run checks → configure CI
```

For a quick guide to creating a new project from scratch, see:

```text
docs/quickstart_uv.md
```

## What this quickstart covers

This chapter shows how to:

- clone a project from GitHub,
- install `uv`,
- synchronize the local environment,
- run tests,
- run Ruff,
- understand `uv sync`,
- understand `uv sync --locked`,
- configure a basic GitHub Actions workflow.

## 1. Clone the repository

Clone the project:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

For this guide, the repository is:

```bash
git clone https://github.com/michalmaj/modern-python-project-guide.git
cd modern-python-project-guide
```

## 2. Install uv

If `uv` is not installed yet, install it first.

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check the installation:

```bash
uv --version
```

## 3. Check important project files

A project managed with `uv` usually contains:

```text
pyproject.toml
uv.lock
.python-version
```

### `pyproject.toml`

This file describes the project.

It may contain:

- project metadata,
- runtime dependencies,
- development dependencies,
- tool configuration.

### `uv.lock`

This file stores exact resolved dependency versions.

It should be committed to Git.

### `.python-version`

This file stores the Python version used by the project.

It helps `uv` install and use the correct Python version.

## 4. Sync the local environment

After cloning a project, run:

```bash
uv sync
```

This creates or updates the local virtual environment.

The environment is usually created in:

```text
.venv/
```

Do not commit `.venv/` to Git.

## 5. What does uv sync do?

`uv sync` synchronizes the local environment with the project.

It uses:

```text
pyproject.toml
uv.lock
```

In practice, this means:

- creating `.venv/` if needed,
- installing project dependencies,
- installing development dependencies included by default,
- making the local environment match the project configuration.

For most local development work, this is the command to run after cloning or pulling new changes:

```bash
uv sync
```

## 6. Run local checks

Run tests:

```bash
uv run pytest
```

Run Ruff linting:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

A useful local check sequence is:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

If formatting fails, run:

```bash
uv run ruff format .
```

Then repeat:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## 7. When to run uv sync again

Run:

```bash
uv sync
```

after:

- cloning the repository,
- pulling changes that modify `pyproject.toml`,
- pulling changes that modify `uv.lock`,
- switching to a branch with different dependencies,
- adding or removing dependencies.

If dependencies did not change, running `uv sync` again is usually harmless.

## 8. Adding a new dependency locally

Add a runtime dependency with:

```bash
uv add package-name
```

Example:

```bash
uv add rich
```

Add a development dependency with:

```bash
uv add --group dev package-name
```

Examples:

```bash
uv add --group dev pytest
uv add --group dev ruff
```

After adding a dependency, commit both:

```text
pyproject.toml
uv.lock
```

## 9. uv sync vs uv sync --locked

Use this locally most of the time:

```bash
uv sync
```

Use this in CI:

```bash
uv sync --locked
```

The difference is important.

### `uv sync`

`uv sync` synchronizes the environment and may update the lockfile if needed.

This is useful during normal development.

### `uv sync --locked`

`uv sync --locked` requires the existing `uv.lock` file to be up to date.

It should fail if the lockfile needs to be changed.

This is useful in CI because CI should not silently update project files.

CI should verify what is already committed.

## 10. Basic GitHub Actions workflow

Create:

```text
.github/workflows/ci.yml
```

Example workflow:

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  quality:
    name: Quality checks
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@v8.1.0

      - name: Set up Python
        run: uv python install

      - name: Install dependencies
        run: uv sync --locked

      - name: Run Ruff linting
        run: uv run ruff check .

      - name: Check formatting
        run: uv run ruff format --check .

      - name: Run tests
        run: uv run pytest
```

This workflow runs on:

- pull requests targeting `main`,
- pushes to `main`.

## 11. Why CI uses the same commands

The CI workflow should run the same checks that developers run locally:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

This makes the workflow easier to understand.

A developer can run the same checks before opening a pull request.

## 12. What green CI means

A green CI check means:

- dependencies installed successfully,
- Ruff linting passed,
- formatting check passed,
- tests passed.

It does not mean the pull request is automatically good.

A human review is still needed for:

- clarity,
- design,
- documentation quality,
- project direction,
- maintainability.

## 13. Common clone problems

### `uv` is not found

Check whether `uv` is installed:

```bash
uv --version
```

If the command fails, install `uv` and restart the terminal.

### Python version is missing

Run:

```bash
uv python install
```

This uses the Python version requested by the project.

### Tests cannot import the package

Check whether `pyproject.toml` contains pytest configuration similar to:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

Then run:

```bash
uv sync
uv run pytest
```

### CI fails but local checks pass

Possible reasons:

- uncommitted local files,
- missing changes in `uv.lock`,
- different Python version,
- platform-specific behavior,
- stale branch.

Check:

```bash
git status
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Quick command summary

For a freshly cloned project:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project

uv sync

uv run ruff check .
uv run ruff format --check .
uv run pytest
```

For CI:

```bash
uv python install
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Rule of thumb

After cloning a project, run:

```bash
uv sync
```

Before opening a pull request, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

In CI, use:

```bash
uv sync --locked
```

Local development may update the environment.

CI should verify the committed project state.
