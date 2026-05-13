# Project Checklist

This checklist helps verify whether a small Python project has a clean and maintainable foundation.

It is not a strict certification.

It is a practical self-review tool.

## Repository basics

A good project should have basic repository files:

- [ ] `README.md`
- [ ] `.gitignore`
- [ ] `LICENSE`
- [ ] `CONTRIBUTING.md`
- [ ] pull request template
- [ ] clear project roadmap or development notes

These files help people understand what the project is, how to work with it, and how it may grow.

## Project structure

The project should have a clear structure:

- [ ] source code is separated from repository metadata
- [ ] tests are separated from source code
- [ ] documentation has a dedicated place
- [ ] GitHub-specific files are stored in `.github/`
- [ ] generated local files are ignored

Example:

```text
modern-python-project-guide/
├── .github/
├── docs/
├── src/
├── tests/
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

The exact structure may differ between projects.

The important part is that the structure is understandable.

## Python project configuration

The project should clearly define how Python and dependencies are managed:

- [ ] `pyproject.toml` exists
- [ ] project name is defined
- [ ] project version is defined
- [ ] supported Python version is defined
- [ ] runtime dependencies are listed
- [ ] development dependencies are separated from runtime dependencies
- [ ] `uv.lock` is committed
- [ ] `.venv/` is ignored

This makes the project easier to reproduce on another machine.

## Source code

The source code should be easy to find and understand:

- [ ] package code is inside `src/`
- [ ] package name is clear
- [ ] modules have focused responsibilities
- [ ] public functions have readable names
- [ ] simple docstrings explain non-obvious modules or functions
- [ ] code avoids unnecessary complexity

The goal is not to make the code clever.

The goal is to make it readable and maintainable.

## Tests

The project should include automated tests:

- [ ] tests are stored in `tests/`
- [ ] test files use clear names
- [ ] test functions use clear names
- [ ] tests check behavior, not implementation details
- [ ] tests include important edge cases
- [ ] tests can be run with one command

In this guide, tests are run with:

```bash
uv run pytest
```

Good tests make future changes safer.

## Linting and formatting

The project should use automated code quality tools:

- [ ] Ruff is installed as a development dependency
- [ ] Ruff is configured in `pyproject.toml`
- [ ] linting can be run locally
- [ ] formatting can be checked locally
- [ ] formatting can be fixed automatically
- [ ] ignored rules are intentional and documented when needed

In this guide, the local commands are:

```bash
uv run ruff check .
uv run ruff format --check .
uv run ruff format .
```

The goal is not to satisfy tools blindly.

The goal is to keep the project clean and consistent.

## Continuous integration

The project should run checks automatically in CI:

- [ ] GitHub Actions workflow exists
- [ ] CI runs on pull requests
- [ ] CI runs on pushes to `main`
- [ ] CI installs dependencies from the lockfile
- [ ] CI runs linting
- [ ] CI checks formatting
- [ ] CI runs tests
- [ ] CI status is visible in the README

CI helps protect the main branch from broken changes.

## Git workflow

The project should use a clear Git workflow:

- [ ] changes are made on branches
- [ ] branch names are descriptive
- [ ] commits are small and focused
- [ ] commit messages are readable
- [ ] meaningful changes go through pull requests
- [ ] pull requests explain what changed and why
- [ ] pull requests include information about checks
- [ ] merged branches are deleted

A good workflow keeps history understandable.

## Pull requests

A good pull request should answer:

- [ ] What changed?
- [ ] Why was it changed?
- [ ] How was it checked?

Before opening a pull request, review:

- [ ] the changed files
- [ ] the diff
- [ ] the pull request title
- [ ] the pull request description
- [ ] local check results
- [ ] whether the change is small enough

Small pull requests are easier to review and safer to merge.

## Local command checklist

For code changes, run:

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

For documentation-only changes, code checks may not always be necessary.

However, review the rendered Markdown on GitHub.

## Red flags

The project may need cleanup if:

- [ ] many unrelated changes appear in one pull request
- [ ] commit messages are vague
- [ ] tests are missing
- [ ] CI is failing
- [ ] generated files are committed
- [ ] dependencies are installed manually but not recorded
- [ ] configuration files are copied without being understood
- [ ] the project cannot be set up from a clean clone

These are not reasons to panic.

They are signals that the workflow needs attention.

## Minimal healthy project

A small healthy Python project should answer these questions:

```text
What is this project?
How do I install it?
Where is the code?
Where are the tests?
How do I run the tests?
How do I check formatting and linting?
What happens before code is merged?
```

If the repository answers these questions clearly, it has a strong foundation.

## Rule of thumb

A clean project is not necessarily a large project.

A clean project is one where another person can understand the structure, run the checks, and make a small change safely.

Start simple.

Keep changes small.

Explain decisions.

Let the project grow gradually.