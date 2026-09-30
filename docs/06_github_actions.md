# GitHub Actions and CI

GitHub Actions is used in this project to run automated checks.

These checks are part of continuous integration, often shortened to CI.

## What is CI?

Continuous integration means that important project checks run automatically when changes are pushed or proposed in a pull request.

In this guide, CI runs:

- linting,
- formatting checks,
- tests,
- distribution builds.

The goal is simple:

> A pull request should not be merged if the basic project checks are failing.

## Why CI matters

Running checks locally is important.

However, local checks depend on the developer remembering to run them.

CI gives the project an additional safety net.

It helps answer questions such as:

- Does the project work on a clean machine?
- Did the tests pass outside the developer's local environment?
- Is the formatting still consistent?
- Did the pull request break the main branch expectations?

CI does not replace careful review.

It supports review by checking repetitive things automatically.

## Local checks and CI checks

The CI workflow should run the same checks that developers run locally.

In this project, the local checks are:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
uv build --no-sources
```

The GitHub Actions workflow runs the same commands.

This is important because local development and CI should not behave like two unrelated systems.

A developer should be able to run the same checks locally before opening a pull request.

## Workflow file

GitHub Actions workflows are stored in:

```text
.github/workflows/
```

This project uses:

```text
.github/workflows/ci.yml
```

The workflow is named:

```yaml
name: CI
```

This name appears in the GitHub Actions interface and in pull request checks.

## When the workflow runs

The workflow runs on:

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

This means CI runs when:

- code is pushed to `main`,
- a pull request targets `main`.

Running CI on pull requests helps catch problems before merging.

Running CI on `main` helps confirm that the main branch remains healthy after merges.

## The job

The workflow defines one job:

```yaml
jobs:
  quality:
    name: Quality checks
    runs-on: ubuntu-latest
```

The job runs on a GitHub-hosted Ubuntu runner.

This gives the project a clean environment for every CI run.

## Checkout step

The first step checks out the repository:

```yaml
- name: Checkout repository
  uses: actions/checkout@v6
```

Without this step, the workflow would not have access to the project files.

## Installing uv

The workflow installs `uv`:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v8.1.0
```

This makes the `uv` command available in the CI environment.

The project uses `uv` locally, so CI should use it too.

## Setting up Python

The workflow installs Python:

```yaml
- name: Set up Python
  run: uv python install
```

The project contains a `.python-version` file, so `uv` knows which Python version should be used.

This keeps local development and CI aligned.

## Installing dependencies

The workflow installs dependencies with:

```yaml
- name: Install dependencies
  run: uv sync --locked --group dev
```

The `--locked` option tells `uv` to use the existing lockfile.

This is important in CI because the workflow should check the project using the dependency versions recorded in `uv.lock`.

The `--group dev` option installs development dependencies such as:

- `pytest`,
- `pytest-cov`,
- `mkdocs`,
- `mypy`,
- `ruff`,
- `rumdl`.

These tools are needed for checks, but they are not runtime dependencies of the package.

## Ruff linting

The workflow runs Ruff linting:

```yaml
- name: Run Ruff linting
  run: uv run ruff check .
```

This checks the project for selected linting issues.

Examples include:

- unused imports,
- import ordering,
- suspicious code patterns,
- syntax modernization suggestions.

## Formatting check

The workflow checks formatting:

```yaml
- name: Check formatting
  run: uv run ruff format --check .
```

This does not modify files.

It only verifies whether files are already formatted correctly.

If formatting is wrong, the command fails.

The developer can fix formatting locally with:

```bash
uv run ruff format .
```

## Markdown linting

The workflow checks Markdown structure and consistency:

```yaml
- name: Lint Markdown
  run: uv run rumdl check .
```

The command uses the `[tool.rumdl]` configuration in `pyproject.toml`. It does
not replace the pytest check for local documentation links or human review.

## Documentation site build

The workflow builds the MkDocs site with strict validation:

```yaml
- name: Build documentation site
  run: uv run mkdocs build --strict
```

The step validates navigation and rendering without publishing the generated
site. The `site/` output directory remains an ignored local artifact.

## Tests and coverage

The workflow runs tests and prints a coverage report:

```yaml
- name: Run tests with coverage
  run: uv run pytest --cov=text_toolkit --cov-report=term-missing
```

This verifies the behavior of the example package while measuring statement and
branch coverage. The terminal report shows missing source lines, but the project
does not fail the workflow based on a coverage percentage.

At this stage, the tests check:

- whitespace normalization,
- word counting,
- character counting.

## Type checking

The workflow runs mypy after the tests:

```yaml
- name: Run type checking
  run: uv run mypy
```

The command reads `[tool.mypy]` from `pyproject.toml` and checks the configured
`src/` and `tests/` directories in strict mode.

Running the same command locally and in CI prevents type-checking results from
depending on a developer remembering an extra manual step.

## Distribution build

The workflow builds the package distributions:

```yaml
- name: Build distributions
  run: uv build --no-sources
```

This creates a wheel and source distribution. The command verifies that the
package metadata and included files are sufficient for a standard build.

The workflow does not publish or upload the generated files.

## Why one job?

This project currently uses one job called `quality`.

That is enough for the current stage.

The job is simple and readable.

Later, a larger project might split checks into separate jobs, for example:

- linting,
- type checking,
- tests,
- documentation,
- packaging.

However, splitting too early would make the workflow more complex without much benefit.

## Why no cache yet?

Caching can make CI faster.

However, this guide starts with a minimal workflow.

A beginner should first understand:

- what the workflow does,
- when it runs,
- how dependencies are installed,
- how checks are executed.

Caching can be added later as an optimization.

The first version should prioritize clarity.

## Green checks

A green CI check means that the automated checks passed.

It does not mean the pull request is automatically good.

It means the pull request passed the basic mechanical checks.

For this project, that also means the documentation site, wheel, and source
distribution were built successfully.

A human review is still needed for questions such as:

- Is the change useful?
- Is the design clear?
- Is the documentation understandable?
- Is the code easy to maintain?
- Does the change fit the project direction?

## Rule of thumb

CI should protect the main branch.

A good CI workflow should be:

- easy to understand,
- easy to run locally in similar form,
- strict enough to catch common mistakes,
- simple enough that beginners can read it.

The goal is not to create a complicated automation system.

The goal is to make every pull request safer.

## Continue

- [Previous: Ruff](05_ruff.md)
- [Next: Git, Commits, Branches, and Pull Requests](07_git_commits_branches_prs.md)
- [Back to documentation home](index.md)
