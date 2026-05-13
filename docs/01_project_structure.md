# Project Structure

A clean project structure helps people understand where things belong.

When a project is small, it may be tempting to put everything in one file. That can work for experiments, but it usually becomes difficult to maintain as the project grows.

This guide uses a simple structure that can grow gradually.

## The planned structure

The project will eventually use this structure:

```text
modern-python-project-guide/
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
├── docs/
│   ├── 00_why_this_guide.md
│   ├── 01_project_structure.md
│   └── ...
├── src/
│   └── text_toolkit/
│       ├── __init__.py
│       └── text_stats.py
├── tests/
│   └── test_text_stats.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── uv.lock
```

Not every file exists yet.

The repository is built step by step, so each part will be introduced when it becomes useful.

## Why use separate directories?

Different files have different responsibilities.

A clear structure makes those responsibilities visible.

## `docs/`

The `docs/` directory contains guide chapters and explanations.

It is used for human-readable documentation, not Python source code.

Examples:

```text
docs/00_why_this_guide.md
docs/01_project_structure.md
docs/02_uv.md
```

## src/

The `src/` directory contains the actual Python package code.

This guide will use the `src/` layout:

```text
src/text_toolkit/
```

The `src/` layout helps separate project source code from configuration files, tests, documentation, and other repository files.

It also makes imports more realistic, because the package has to be discovered properly instead of being accidentally imported from the current working directory.

## tests/

The `tests/` directory contains automated tests.

Tests should be separate from the implementation code.

Example:

```text
tests/test_text_stats.py
```

Keeping tests in a dedicated directory makes them easier to find and run.

## .github/

The `.github/` directory contains GitHub-specific files.

This may include:

- pull request templates,
- GitHub Actions workflows,
- issue templates.

Example:

```text
.github/pull_request_template.md
.github/workflows/ci.yml
```

## pyproject.toml

The `pyproject.toml` file is the central configuration file for a modern Python project.

In this guide, it will eventually contain:

- project metadata,
- Python version requirements,
- dependency configuration,
- pytest configuration,
- Ruff configuration.

This file will be added in a later step.

## uv.lock

The `uv.lock` file records exact dependency versions.

It helps make installations reproducible across machines and continuous integration environments.

This file will be generated after introducing `uv`.

## Why not start with everything?

A common beginner mistake is copying a large project template without understanding it.

This guide avoids that.

Each file and directory should appear for a reason.

The goal is not to create the biggest possible project structure.

The goal is to create a structure that is simple, useful, and understandable.

Rule of thumb

A good project structure should help answer these questions:

- Where does the application code live?
- Where do the tests live?
- Where is the documentation?
- Where is the project configuration?
- How can another person run and check the project?

If the structure answers these questions clearly, it is doing its job.
