# Modern Python Project Guide

[![CI](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml)

A practical guide to building a clean, modern Python project with `uv`, `pytest`, `ruff`, `pyproject.toml`, GitHub Actions, and a pull request based workflow.

This repository is both a tutorial and a working example.

It shows how to turn a small Python idea into a maintainable project with:

- a clear project structure,
- dependency management with `uv`,
- tests with `pytest`,
- linting and formatting with `ruff`,
- configuration in `pyproject.toml`,
- continuous integration with GitHub Actions,
- readable commits,
- branches,
- pull requests.

## Quick starts

In a hurry? Start here:

- [uv quickstart](docs/quickstart_uv.md)
- [Clone and CI quickstart](docs/quickstart_clone_and_ci.md)

## Full guide

The full guide is organized as a step-by-step path.

Start from the beginning if you want to understand why each tool and file is introduced.

1. [Why this guide exists](docs/00_why_this_guide.md)
2. [Project structure](docs/01_project_structure.md)
3. [uv](docs/02_uv.md)
4. [pyproject.toml](docs/03_pyproject_toml.md)
5. [pytest](docs/04_pytest.md)
6. [Ruff](docs/05_ruff.md)
7. [GitHub Actions and CI](docs/06_github_actions.md)
8. [Git, commits, branches, and pull requests](docs/07_git_commits_branches_prs.md)
9. [Common beginner mistakes](docs/08_common_mistakes.md)
10. [Project checklist](docs/09_checklist.md)

## Example package

The repository contains a small example package:

```text
src/text_toolkit/
```

The package is intentionally simple.

It is used to demonstrate project structure, tests, linting, formatting, and CI without adding unnecessary domain complexity.

Current utilities include:

- whitespace normalization,
- word counting,
- character counting.

## Repository structure

```text
modern-python-project-guide/
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
├── docs/
│   ├── quickstart_uv.md
│   ├── quickstart_clone_and_ci.md
│   ├── 00_why_this_guide.md
│   └── ...
├── src/
│   └── text_toolkit/
├── tests/
├── .gitignore
├── .python-version
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

## Local setup

Clone the repository:

```bash
git clone https://github.com/michalmaj/modern-python-project-guide.git
cd modern-python-project-guide
```

Sync the environment:

```bash
uv sync
```

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

## Local quality checks

Before opening a pull request with code changes, run:

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

## Development workflow

This repository is built using small branches and pull requests.

Recommended workflow:

```text
update main
create a branch
make a small change
commit the change
push the branch
open a pull request
wait for CI
review the change
merge into main
delete the branch
```

Example:

```bash
git switch main
git pull
git switch -c docs/example-change

# edit files

git status
git add path/to/file.md
git commit -m "docs: describe example change"
git push -u origin docs/example-change
```

After merge:

```bash
git switch main
git pull
git branch -d docs/example-change
```

## Who is this for?

This guide is for people who know basic Python and want to learn how to organize Python projects in a more professional way.

It is especially useful for:

- students,
- self-taught developers,
- junior Python developers,
- teachers preparing programming classes,
- anyone moving from scripts to maintainable projects.

## What this guide is not

This is not a complete Python packaging course.

It does not start with advanced topics such as:

- publishing packages to PyPI,
- Docker,
- pre-commit hooks,
- static type checking,
- documentation generators,
- release automation.

Those topics may be added later.

The goal here is to build a clean foundation first.

## Current status

This repository is built step by step.

Each meaningful change should be introduced through a small branch and a pull request.