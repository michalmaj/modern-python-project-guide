# Command Cheatsheet

This page is a quick command reference.

It does not explain every concept in detail.

For explanations, use the full guide and quickstarts.

## Project setup

Create a new project:

```bash
mkdir example-python-project
cd example-python-project
uv init --bare --name example-python-project --python 3.12
uv python pin 3.12
```

Create a basic `src/` layout:

```bash
mkdir -p src/example_project tests
touch src/example_project/__init__.py
touch src/example_project/calculator.py
touch tests/test_calculator.py
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force src/example_project
New-Item -ItemType Directory -Force tests
New-Item -ItemType File -Force src/example_project/__init__.py
New-Item -ItemType File -Force src/example_project/calculator.py
New-Item -ItemType File -Force tests/test_calculator.py
```

## Dependencies

Add a runtime dependency:

```bash
uv add package-name
```

Example:

```bash
uv add rich
```

Add a development dependency:

```bash
uv add --group dev package-name
```

Examples:

```bash
uv add --group dev pytest
uv add --group dev ruff
```

Sync the local environment:

```bash
uv sync
```

Lock dependencies explicitly:

```bash
uv lock
```

## Running tools

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

Format files:

```bash
uv run ruff format .
```

Run all local checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Fix formatting and recheck

If formatting fails:

```bash
uv run ruff format .
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Clone an existing project

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
uv sync
```

Then run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Git workflow

Update `main`:

```bash
git switch main
git pull
```

Create a branch:

```bash
git switch -c docs/example-change
```

Check changed files:

```bash
git status
```

Stage a file:

```bash
git add path/to/file.md
```

Commit:

```bash
git commit -m "docs: describe example change"
```

Push the branch:

```bash
git push -u origin docs/example-change
```

After the pull request is merged:

```bash
git switch main
git pull
git branch -d docs/example-change
```

## Useful commit message examples

Documentation:

```text
docs: add project glossary
docs: explain pytest
docs: update README quickstarts
```

Project configuration:

```text
chore: initialize uv project
chore: configure ruff
chore: add editorconfig
```

Tests:

```text
test: add text statistics tests
```

CI:

```text
ci: add GitHub Actions workflow
```

Feature code:

```text
feat: add text toolkit package
```

## GitHub Actions CI

Minimal CI workflow commands:

```bash
uv python install
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

CI should use:

```bash
uv sync --locked
```

Local development usually uses:

```bash
uv sync
```

## Files to commit

Usually commit:

```text
README.md
CONTRIBUTING.md
LICENSE
pyproject.toml
uv.lock
.python-version
.github/
docs/
src/
tests/
```

Do not commit:

```text
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.coverage
htmlcov/
```

## Quick local checklist

Before opening a pull request with code changes:

```bash
git status
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Before merging:

```text
CI is green
PR title is clear
PR description explains what changed and why
Diff has been reviewed
No unrelated files are included
```