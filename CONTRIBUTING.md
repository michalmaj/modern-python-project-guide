# Contributing Guide

Thank you for your interest in this project.

This repository is built step by step as a practical guide to modern Python project development. The goal is not only to show the final project structure, but also to demonstrate a clean and realistic development workflow.

## Main idea

Every meaningful change should be small, focused, and easy to review.

This project uses a simple workflow:

```text
create a branch → make a small change → commit → push → open a pull request → review → merge
```

## Branches

Do not commit directly to `main`.
Create a separate branch for each meaningful change.
Recommended branch name format:

```text
<type>/<short-description>
```

Examples:

```text
docs/add-project-roadmap
docs/add-contributing-guide
chore/configure-uv
test/add-text-statistics-tests
ci/add-github-actions-workflow
```

Use short, descriptive names.

Good branch names:

```text
docs/add-pull-request-guide
chore/configure-ruff
test/add-basic-tests
```

Avoid vague branch names:

```text
changes
updates
stuff
fixes
new-files
```

## Commits

Use small, readable commits.

Recommended commit message format:

```text
<type>: <short description>
```

Examples:

```text
docs: add project roadmap
docs: add contributing guide
chore: configure uv project
test: add tests for text statistics
ci: add GitHub Actions workflow
```

Common commit types:

```text
docs     - documentation changes
chore    - project setup, configuration, maintenance
feat     - new functionality
test     - tests
fix      - bug fixes
ci       - continuous integration changes
refactor - code changes without changing behavior
```

Good commit messages:

```text
docs: add contributing guide
chore: configure ruff
test: add whitespace normalization tests
```

Avoid unclear commit messages:

```text
update
fix
changes
work
final
final2
```

## Pull requests

Every meaningful change should be introduced through a pull request.

A good pull request should:

- have a clear title,
- describe what changed,
- explain why the change was made,
- be small enough to review comfortably,
- include tests or documentation when needed.

Good pull request title examples:

```text
docs: add contributing guide
chore: configure uv project
ci: add GitHub Actions workflow
```

Avoid vague pull request titles:

```text
Update files
Some changes
Work in progress
```

## Review mindset

A pull request is not only a technical step.

It is also a communication tool.

When opening a pull request, try to make the reviewer’s job easy:

- keep the change focused,
- avoid unrelated edits,
- explain non-obvious decisions,
- mention follow-up work if needed.

## Local checks

Before opening a pull request with code changes, run the local quality checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

If formatting fails, run:

```bash
uv run ruff format .
```

Then repeat the checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

For documentation-only changes, code checks may not always be necessary.

However, review the rendered Markdown on GitHub after opening the pull request.

The goal is to catch simple issues locally before CI runs on GitHub.

## Project philosophy

This repository should stay beginner-friendly, but not careless.

The goal is to teach professional habits without overwhelming the reader.

That means:

- simple examples,
- clear explanations,
- small changes,
- readable history,
- realistic development practices.

Advanced tools should be introduced only when the basic workflow is already clear.
