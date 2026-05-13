# Project Roadmap

This roadmap describes how the repository will be built step by step.

The goal is to keep every change small, understandable, and easy to review.

## Guiding principles

This project should be developed using a clean and realistic workflow:

- small branches,
- focused commits,
- pull requests for meaningful changes,
- readable documentation,
- automated checks,
- gradual project growth.

The repository should be useful both as a tutorial and as an example of a modern Python project.

## Phase 1: Repository foundation

The first phase focuses on the basic repository structure.

Planned steps:

- bootstrap the repository,
- add the project roadmap,
- add contribution guidelines,
- add a pull request template,
- explain the intended development workflow.

## Phase 2: Python project setup

The second phase introduces the actual Python project.

Planned steps:

- initialize the project with `uv`,
- add `pyproject.toml`,
- use the `src/` layout,
- create a small example package,
- add a minimal test suite.

## Phase 3: Code quality tools

The third phase adds tools for maintaining code quality.

Planned steps:

- add `ruff` for linting,
- add `ruff` for formatting,
- document local quality checks,
- keep tool configuration inside `pyproject.toml`.

## Phase 4: Continuous integration

The fourth phase adds automated checks on GitHub.

Planned steps:

- add a GitHub Actions workflow,
- run linting in CI,
- run formatting checks in CI,
- run tests in CI,
- explain how CI supports pull requests.

## Phase 5: Git and pull request workflow

The fifth phase documents the development process.

Planned steps:

- describe branch naming,
- describe commit message conventions,
- describe pull request structure,
- explain how to review a pull request,
- show common beginner mistakes.

## Future ideas

These topics are intentionally not part of the first version.

They may be added later:

- test coverage,
- pre-commit hooks,
- static type checking,
- command-line interfaces,
- documentation sites,
- packaging and releases,
- publishing to PyPI.

## Current focus

The current focus is the project foundation.

Advanced tooling should be added only after the basic workflow is clear.