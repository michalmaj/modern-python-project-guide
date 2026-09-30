# Troubleshooting

This page describes common problems that may happen when setting up or running the project.

The goal is to help you slow down, read the error, and check the most likely cause.

## General rule

When something fails, start with:

```bash
git status
uv --version
uv sync
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

Do not change many things at once.

Read the first error message carefully.

Fix one problem, then run the checks again.

## `uv` command not found

### Problem

You run:

```bash
uv --version
```

and the terminal says that `uv` is not found.

### Possible cause

`uv` is not installed, or the terminal does not see it in `PATH`.

### Fix

Install `uv`.

macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then restart the terminal and check again:

```bash
uv --version
```

## Python version is missing

### Problem

`uv` reports that the requested Python version is not installed.

### Possible cause

The project uses `.python-version`, but that Python version is not available locally yet.

### Fix

Run:

```bash
uv python install
```

Then sync the environment:

```bash
uv sync
```

## Virtual environment was not created

### Problem

You expected a `.venv/` directory, but it does not exist.

### Possible cause

The project environment has not been synchronized yet.

### Fix

Run:

```bash
uv sync
```

Expected result:

```text
.venv/
```

The `.venv/` directory is local.

Do not commit it to Git.

## Tests cannot import the package

### Problem

Running tests fails with an import error, for example:

```text
ModuleNotFoundError: No module named 'text_toolkit'
```

### Possible cause

The project uses a `src/` layout, but it was not installed into the environment.

### Fix

Check that `pyproject.toml` contains a build system:

```toml
[build-system]
requires = ["uv_build>=0.12.19,<0.13"]
build-backend = "uv_build"
```

Then run:

```bash
uv sync
uv run pytest
```

The sync output should show that `text-toolkit` was built and installed from the
local project.

## pytest is not found

### Problem

You run:

```bash
uv run pytest
```

and pytest is not available.

### Possible cause

Development dependencies were not installed or `pytest` is missing from the development dependency group.

### Fix

Check that `pyproject.toml` contains something similar to:

```toml
[dependency-groups]
dev = [
    "pytest>=9.0.3",
    "ruff>=0.15.12",
]
```

Then run:

```bash
uv sync
uv run pytest
```

If `pytest` is missing, add it:

```bash
uv add --group dev pytest
```

Commit both:

```text
pyproject.toml
uv.lock
```

## Ruff is not found

### Problem

You run:

```bash
uv run ruff check .
```

and Ruff is not available.

### Possible cause

Ruff is not installed as a development dependency.

### Fix

Add Ruff:

```bash
uv add --group dev ruff
```

Then run:

```bash
uv run ruff check .
uv run ruff format --check .
```

Commit both:

```text
pyproject.toml
uv.lock
```

## Formatting check fails

### Problem

This command fails:

```bash
uv run ruff format --check .
```

### Possible cause

Some files are not formatted according to Ruff.

### Fix

Run:

```bash
uv run ruff format .
```

Then check again:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

## Ruff linting fails

### Problem

This command fails:

```bash
uv run ruff check .
```

### Possible cause

Ruff found a linting issue.

Examples:

- unused import,
- unsorted imports,
- undefined name,
- outdated syntax,
- suspicious pattern.

### Fix

Read the Ruff message.

If Ruff offers an automatic fix, you can try:

```bash
uv run ruff check . --fix
```

Then run all checks again:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

Do not blindly apply fixes without reviewing the diff.

Check:

```bash
git diff
```

## mypy is missing or type checking fails

### Problem

This command is unavailable or reports a type error:

```bash
uv run mypy
```

### Possible causes

- the local environment is out of sync,
- mypy is missing from the development dependency group,
- code does not match its type annotations.

### Fix

Sync the environment first:

```bash
uv sync
uv run mypy
```

When adding mypy to a different project, record it as a development dependency:

```bash
uv add --group dev mypy
```

For a type error, read the file path, line number, and error code. Fix the code
or its annotation instead of adding a broad ignore without understanding the
problem.

## Tests fail

### Problem

This command fails:

```bash
uv run pytest
```

### Possible cause

The code behavior does not match the expected behavior in tests.

### Fix

Read the failing test name first.

Then read the assertion error.

Useful command:

```bash
uv run pytest -v
```

If needed, run one test file:

```bash
uv run pytest tests/test_text_stats.py
```

Fix the code or the test, depending on what is actually wrong.

Then run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

## Coverage reporting fails

### Problem

Tests may pass without coverage, but this command fails:

```bash
uv run pytest --cov=text_toolkit --cov-report=term-missing
```

### Possible causes

- pytest-cov is missing from the development dependency group,
- the local environment is out of sync,
- the package name passed to `--cov` is incorrect,
- coverage configuration is invalid.

### Fix

Sync dependencies and retry:

```bash
uv sync
uv run pytest --cov=text_toolkit --cov-report=term-missing
```

Check that `pyproject.toml` contains pytest-cov and the `[tool.coverage.run]`
section. A lower percentage by itself does not fail this project because no
`fail_under` threshold is configured.

## Markdown linting fails

### Problem

This command reports one or more rule violations:

```bash
uv run rumdl check .
```

### Possible causes

- a heading level was skipped,
- a list or code fence is missing surrounding blank lines,
- a fenced code block has no language identifier,
- Markdown structure or style is inconsistent,
- a deliberate project pattern needs a narrow exception.

### Fix

Read the rule identifier and inspect the reported line. Fix the structure when
it is genuinely inconsistent.

For automatically fixable issues, you may run:

```bash
uv run rumdl check --fix .
git diff
```

Review every automatic change. Configure an exception only when the existing
Markdown is intentional and the reason can be explained.

## MkDocs build fails

### Problem

The strict documentation build exits with an error:

```bash
uv run mkdocs build --strict
```

### Possible causes

- a page is missing from `mkdocs.yml`,
- a navigation target does not exist,
- a document link or heading anchor is incorrect,
- MkDocs emitted a warning that strict mode treats as an error.

### Fix

Read the first warning, correct the referenced page or navigation entry, and run
the strict build again.

For visual review, start the local server:

```bash
uv run mkdocs serve
```

If port 8000 is already in use, choose another address:

```bash
uv run mkdocs serve --dev-addr 127.0.0.1:8001
```

## A pre-commit hook fails or changes files

### Problem

Git stops a commit because a hook failed or modified a file.

### Possible causes

- a file contains trailing whitespace or invalid YAML or TOML,
- unresolved merge conflict markers remain,
- Ruff found or fixed a Python issue,
- a hook changed a file that must be staged again.

### Fix

Review both the hook output and the resulting diff:

```bash
git diff
uv run pre-commit run --all-files
```

If a hook fixed a file, stage the reviewed change and try the commit again.
Do not bypass the hook merely because it changed a file.

If pre-commit itself is missing, sync the development environment:

```bash
uv sync
uv run pre-commit install
```

## `uv.lock` is out of sync

### Problem

CI fails during:

```bash
uv sync --locked --group dev
```

### Possible cause

`pyproject.toml` changed, but `uv.lock` was not updated.

CI uses `uv sync --locked --group dev` because it should verify the committed
project state and explicitly install the development tools, not silently update
files.

### Fix

Run locally:

```bash
uv sync
```

or:

```bash
uv lock
```

Then commit:

```text
pyproject.toml
uv.lock
```

Run checks again:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

## `.venv/` was committed by mistake

### Problem

The pull request contains many files from:

```text
.venv/
```

### Possible cause

The virtual environment was added to Git accidentally.

### Fix

Make sure `.gitignore` contains:

```gitignore
.venv/
```

Remove `.venv/` from Git tracking:

```bash
git rm -r --cached .venv
```

Then commit the cleanup:

```bash
git add .gitignore
git commit -m "chore: stop tracking virtual environment"
```

The local `.venv/` directory can still exist on your machine.

It should just not be tracked by Git.

## Cache directories were committed

### Problem

The pull request contains files such as:

```text
__pycache__/
.pytest_cache/
.ruff_cache/
.mypy_cache/
```

### Possible cause

Generated cache files were added to Git accidentally.

### Fix

Make sure `.gitignore` contains:

```gitignore
__pycache__/
.pytest_cache/
.ruff_cache/
.mypy_cache/
```

Remove cached files from Git tracking if needed:

```bash
git rm -r --cached __pycache__ .pytest_cache .ruff_cache .mypy_cache
```

Some directories may not exist. That is fine.

Then commit the cleanup.

## Git says working tree is not clean

### Problem

You run:

```bash
git status
```

and see modified or untracked files.

### Possible cause

You changed files locally, generated files appeared, or formatting changed files.

### Fix

Review the changes:

```bash
git diff
```

For staged changes:

```bash
git diff --staged
```

If the changes are correct, commit them.

If a generated file appears, add it to `.gitignore` or remove it from Git tracking.

Do not commit files you do not understand.

## Git branch is behind main

### Problem

Your branch is outdated compared to `main`.

### Possible cause

Other pull requests were merged after you created your branch.

### Fix

Update `main`:

```bash
git switch main
git pull
```

Then update your branch.

For a beginner-friendly workflow, the simplest option is often to create a fresh branch from the updated `main` and reapply a small change.

If the branch contains more work, use Git carefully and ask for help before rewriting history.

## Pull request contains unrelated files

### Problem

The pull request shows files that are not related to the change.

### Possible cause

Files were edited accidentally, generated files were committed, or the branch was used for more than one task.

### Fix

Check:

```bash
git status
git diff
```

Remove unrelated changes before committing.

If unrelated changes are already committed, consider making a new clean branch and copying only the intended changes.

Small pull requests are easier to fix.

## CI fails but local checks pass

### Problem

Local checks pass, but GitHub Actions fails.

### Possible causes

- uncommitted local changes,
- missing `uv.lock` update,
- different Python version,
- platform-specific behavior,
- stale branch,
- CI configuration issue.

### Fix

Start with:

```bash
git status
uv sync
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

Then check whether these files were committed if they changed:

```text
pyproject.toml
uv.lock
.github/workflows/ci.yml
```

If CI still fails, open the failed GitHub Actions run and read the first failing step.

## Local checks fail after pulling main

### Problem

The project worked before, but after:

```bash
git pull
```

local checks fail.

### Possible cause

New changes modified dependencies, tool configuration, tests, or source code.

### Fix

Run:

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

If dependencies changed, `uv sync` is the important first step.

## Markdown looks wrong on GitHub

### Problem

A Markdown file looks fine locally, but strange on GitHub.

### Possible causes

- broken code fence,
- missing blank line,
- wrong indentation,
- nested code blocks,
- malformed list,
- broken link.

### Fix

Review the rendered Markdown in the pull request.

Also inspect the raw diff.

Common things to check:

- every code fence starts and ends with triple backticks,
- lists have blank lines before code blocks,
- links use correct relative paths,
- headings are in the right order.

## Link in README is broken

### Problem

A README link returns 404 or points to the wrong file.

### Possible cause

The file path is wrong, the file was renamed, or the link uses the wrong relative path.

### Fix

For files inside `docs/`, use paths like:

```markdown
[Glossary](docs/glossary.md)
```

For links from one file inside `docs/` to another file inside `docs/`, use:

```markdown
[Glossary](glossary.md)
```

Check links after opening the pull request.

## A command works in PowerShell but not in Bash

### Problem

A command works in one shell but not another.

### Possible cause

Some commands are shell-specific.

For example:

```bash
mkdir -p src/example_project tests
touch src/example_project/__init__.py
```

works in Bash, but PowerShell may need:

```powershell
New-Item -ItemType Directory -Force src/example_project
New-Item -ItemType Directory -Force tests
New-Item -ItemType File -Force src/example_project/__init__.py
```

### Fix

Use the command version for your shell.

This guide often shows both Bash and PowerShell examples when file creation commands differ.

## When in doubt

Use this sequence:

```bash
git status
uv sync
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
```

Then:

1. read the first error,
2. fix one thing,
3. run the checks again,
4. review the diff,
5. commit only related changes.

## Rule of thumb

Most setup problems are caused by one of these:

- environment not synced,
- missing dependency,
- stale lockfile,
- wrong branch,
- generated files committed by mistake,
- local changes not committed,
- command run from the wrong directory.

Start with the simple checks before changing configuration.
