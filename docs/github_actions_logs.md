# Reading GitHub Actions Logs

GitHub Actions logs can look intimidating at first.

A failed CI run may show many lines of output, but usually only one step contains the important error.

This page explains how to read CI logs slowly and find the useful information.

## When to use this guide

Use this guide when:

- a pull request has a red CI check,
- a workflow failed after pushing to `main`,
- local checks pass but GitHub Actions fails,
- you do not know which command failed,
- the logs look too long to understand.

## The most important idea

Do not read the whole log from top to bottom immediately.

Start by finding:

```text
Which job failed?
Which step failed?
What was the first useful error message?
```

The first useful error is usually more important than the last line of the log.

## Where to find CI logs

When a pull request has a failing check:

1. Open the pull request on GitHub.
2. Scroll to the checks section.
3. Click the failed check.
4. Open the failed job.
5. Open the failed step.

In this project, the job is called:

```text
Quality checks
```

The workflow is called:

```text
CI
```

## Understand the workflow structure

This project uses a workflow similar to:

```yaml
name: CI

jobs:
  quality:
    name: Quality checks
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
      - name: Install uv
      - name: Set up Python
      - name: Install dependencies
      - name: Run Ruff linting
      - name: Check formatting
      - name: Run tests
```

When CI fails, one of these steps usually failed.

Do not debug everything at once.

Start with the failed step.

## Step: Checkout repository

### What it does

This step downloads the repository files into the GitHub Actions runner.

Example:

```yaml
- name: Checkout repository
  uses: actions/checkout@v6
```

### If it fails

This is uncommon.

Possible causes include:

- GitHub service issue,
- invalid workflow syntax,
- repository access problem.

Usually, this is not caused by Python code.

## Step: Install uv

### What it does

This step installs `uv` in the CI environment.

Example:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v8.1.0
```

### If it fails

Possible causes include:

- wrong action name,
- invalid action version,
- temporary network issue,
- GitHub Actions service issue.

Check whether the `uses:` line is correct.

## Step: Set up Python

### What it does

This step installs the Python version requested by the project.

Example:

```yaml
- name: Set up Python
  run: uv python install
```

The project uses:

```text
.python-version
```

to define the selected Python version.

### If it fails

Possible causes include:

- invalid Python version in `.python-version`,
- Python version not available,
- `uv` was not installed correctly in the previous step.

Check:

```text
.python-version
```

For this guide, it should contain something like:

```text
3.12
```

## Step: Install dependencies

### What it does

This step installs project dependencies in CI.

Example:

```yaml
- name: Install dependencies
  run: uv sync --locked
```

CI uses:

```bash
uv sync --locked
```

because it should verify the committed lockfile, not silently update it.

### If it fails

A common cause is that `pyproject.toml` and `uv.lock` are out of sync.

This may happen after adding or removing a dependency without committing the updated lockfile.

### How to fix it

Run locally:

```bash
uv sync
```

or:

```bash
uv lock
```

Then check:

```bash
git status
```

If `uv.lock` changed, commit it:

```bash
git add pyproject.toml uv.lock
git commit -m "chore: update dependency lockfile"
```

Then push again.

## Step: Run Ruff linting

### What it does

This step runs:

```bash
uv run ruff check .
```

It checks the project for selected linting issues.

### If it fails

The log usually shows:

- file path,
- line number,
- rule code,
- message.

Example:

```text
src/example_project/module.py:1:1: F401 `os` imported but unused
```

This means:

```text
file: src/example_project/module.py
line: 1
column: 1
rule: F401
problem: os was imported but not used
```

### How to fix it

Open the file and fix the issue.

Some Ruff issues can be fixed automatically:

```bash
uv run ruff check . --fix
```

Then review the diff:

```bash
git diff
```

Do not apply fixes blindly without reading the changes.

After fixing, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Step: Check formatting

### What it does

This step runs:

```bash
uv run ruff format --check .
```

It checks whether files are formatted correctly.

It does not modify files in CI.

### If it fails

The log may say that files would be reformatted.

That means formatting is different from Ruff's expected format.

### How to fix it

Run locally:

```bash
uv run ruff format .
```

Then run all checks again:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Commit the formatting changes:

```bash
git add .
git commit -m "style: format files"
```

If the formatting change is part of another small documentation or code PR, it may be better to amend the existing commit instead of adding a separate formatting-only commit.

## Step: Run tests

### What it does

This step runs:

```bash
uv run pytest
```

It checks whether the code behaves as expected.

### If it fails

Pytest usually shows:

- failing test file,
- failing test name,
- assertion error,
- expected value,
- actual value.

Example:

```text
FAILED tests/test_text_stats.py::test_count_words_handles_repeated_whitespace
```

This tells you which test failed.

### How to fix it

Start by reading:

```text
test file
test name
assertion error
```

Then run tests locally:

```bash
uv run pytest
```

For more detail:

```bash
uv run pytest -v
```

To run one test file:

```bash
uv run pytest tests/test_text_stats.py
```

Fix the code or the test depending on what is actually wrong.

Then run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Local checks pass, but CI fails

This can happen.

Common causes:

- uncommitted local files,
- missing `uv.lock` update,
- different Python version,
- branch is stale,
- workflow file changed,
- platform-specific behavior.

Start locally:

```bash
git status
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

If `git status` shows changes, check whether they should be committed.

If `uv.lock` changed, commit it.

If local checks still pass, inspect the failed CI step carefully.

## CI fails on main after merge

If CI fails on `main`, do not ignore it.

The `main` branch should stay healthy.

Recommended response:

1. Open the failed workflow run.
2. Identify the failed job and step.
3. Read the first useful error.
4. Reproduce locally if possible.
5. Create a small fix branch.
6. Open a pull request with the fix.

Example branch:

```bash
git switch main
git pull
git switch -c fix/ci-failure
```

Example commit:

```bash
git commit -m "fix: resolve CI failure"
```

## How to read a long log

Long logs are easier to read if you search for keywords.

Useful words to search for:

```text
error
failed
FAILED
Traceback
ModuleNotFoundError
AssertionError
would be reformatted
out of date
```

But be careful.

Some logs contain warnings or internal messages that are not the actual cause.

Focus on the failed step first.

## First error vs last error

The last line of a log may only say:

```text
Error: Process completed with exit code 1.
```

That line tells you that the command failed.

It does not explain why.

The useful error is usually above it.

Look for the first message that explains the real problem.

## Do not fix everything at once

When CI fails, avoid changing many unrelated things.

Bad approach:

```text
format files, update dependencies, rewrite tests, change CI, and refactor code
```

Better approach:

```text
fix the one issue that caused CI to fail
```

Then run checks and push again.

Small fixes are easier to review.

## Useful local commands

Check repository state:

```bash
git status
```

Review unstaged changes:

```bash
git diff
```

Review staged changes:

```bash
git diff --staged
```

Sync dependencies:

```bash
uv sync
```

Run quality checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Format files:

```bash
uv run ruff format .
```

Run tests with more detail:

```bash
uv run pytest -v
```

## Common CI failure examples

### Lockfile is stale

Symptom:

```text
uv sync --locked
```

fails.

Likely fix:

```bash
uv lock
git add pyproject.toml uv.lock
git commit -m "chore: update lockfile"
```

### Formatting failed

Symptom:

```text
would be reformatted
```

Likely fix:

```bash
uv run ruff format .
git add .
git commit -m "style: format files"
```

### Unused import

Symptom:

```text
F401 imported but unused
```

Likely fix:

Remove the unused import.

### Test assertion failed

Symptom:

```text
AssertionError
```

Likely fix:

Check whether the implementation or the test expectation is wrong.

### Package import failed

Symptom:

```text
ModuleNotFoundError
```

Likely fix:

Check project structure and pytest configuration:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

## What green CI means

A green CI run means:

- dependencies installed,
- Ruff linting passed,
- formatting check passed,
- tests passed.

It does not mean:

- the design is perfect,
- the documentation is clear,
- the change is useful,
- the pull request should be merged without review.

CI checks repetitive things.

Humans still review meaning and quality.

## Rule of thumb

When CI fails, ask:

```text
Which step failed?
What command did that step run?
Can I run the same command locally?
What is the first useful error message?
```

Do not panic.

CI is not judging you.

It is giving feedback.