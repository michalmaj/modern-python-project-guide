# pyproject.toml

`pyproject.toml` is the central configuration file for a modern Python project.

It describes the project itself and can also store configuration for development tools.

In this guide, `pyproject.toml` is the main place for project configuration.

## Why this file matters

A Python project should be understandable not only from its source code, but also from its configuration.

The `pyproject.toml` file helps answer questions such as:

- What is the project called?
- Which Python version does it require?
- Which dependencies does it use?
- Which development tools are configured?
- How should tests, linting, and formatting behave?

Instead of spreading configuration across many unrelated files, this guide keeps the basic setup in one place.

## Current configuration

The project configuration is intentionally small.

The current file contains:

```toml
[project]
name = "text-toolkit"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

[build-system]
requires = ["uv_build>=0.12.19,<0.13"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "mypy>=2.3.1",
    "pre-commit>=4.6.2",
    "pytest>=9.0.3",
    "pytest-cov>=7.1.0",
    "ruff>=0.15.12",
]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.mypy]
python_version = "3.12"
files = ["src", "tests"]
strict = true

[tool.coverage.run]
branch = true
source = ["text_toolkit"]

[tool.coverage.report]
show_missing = true

[tool.ruff]
line-length = 88
target-version = "py312"
src = ["src", "tests"]

[tool.ruff.lint]
select = [
    "E",
    "F",
    "I",
    "B",
    "UP",
]
```

This describes the project, its build system, its development dependencies, and
the settings used by pytest, mypy, Coverage.py, and Ruff. `pre-commit` is a
development dependency, but its hooks use the separate
`.pre-commit-config.yaml` file.

## The `[project]` section

The `[project]` section contains basic project metadata.

Example:

```toml
[project]
name = "text-toolkit"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

### `name`

The `name` field defines the package name.

In this guide, the example package is called:

```text
text-toolkit
```

The package name is intentionally simple and neutral.

The purpose of the project is to teach workflow and structure, not a specific application domain.

### `version`

The `version` field describes the current project version.

At the beginning, the version is:

```text
0.1.0
```

This is a common starting point for early-stage projects.

### `requires-python`

The `requires-python` field defines the supported Python version range.

Example:

```toml
requires-python = ">=3.12"
```

This tells users and tools that the project expects Python 3.12 or newer.

### `dependencies`

The `dependencies` list contains packages required by the project at runtime.

At this stage, it is empty:

```toml
dependencies = []
```

This is intentional.

The example package starts with standard library code only.

Development tools such as `pytest`, pytest-cov, mypy, and Ruff are stored
separately in the `dev` dependency group.

## The `[build-system]` section

A build system tells Python tools how to build and install the project.

This project uses:

```toml
[build-system]
requires = ["uv_build>=0.12.19,<0.13"]
build-backend = "uv_build"
```

`uv_build` is a small build backend designed for Python projects managed with
`uv`. It supports this project's pure Python package and its standard `src/`
layout:

```text
src/text_toolkit/
```

The upper version bound protects the project from incompatible future backend
releases. It should move deliberately when the project updates `uv_build`.

When a build system is present, `uv sync` installs the current project into the
environment. By default, the installation is editable: changes inside `src/`
are visible without reinstalling the package.

This is enough to test the package through the same import name its users see.
The [building distributions](10_building_distributions.md) chapter explains how
the same backend creates a wheel and source distribution. Publishing to PyPI
remains a separate topic.

## Runtime dependencies vs development dependencies

Not all dependencies have the same role.

Runtime dependencies are needed when someone uses the project.

Development dependencies are needed only while developing the project.

Examples of development dependencies:

- `pytest`,
- `pytest-cov`,
- `mypy`,
- `ruff`,
- test coverage tools,
- type checkers,
- documentation tools.

The guide introduces development dependencies gradually so that each tool is
understandable before the next one appears.

## Tool configuration

Many Python tools can be configured inside `pyproject.toml`.

The current file also contains sections such as:

```toml
[tool.pytest.ini_options]
```

and:

```toml
[tool.mypy]
```

and:

```toml
[tool.coverage.run]
```

and:

```toml
[tool.ruff]
```

This keeps important project settings close to the project metadata.

## Why configure the project gradually?

It would be possible to add all configuration immediately.

However, that would make the project harder to learn from.

This guide was built using a slower approach:

1. start with minimal project metadata,
2. add source code,
3. add tests,
4. configure pytest,
5. add Ruff,
6. configure linting and formatting,
7. add continuous integration,
8. add a build system and install the project,
9. add static type checking,
10. add test coverage reporting.

Each step should explain one idea clearly.

## Rule of thumb

A good `pyproject.toml` should be boring in the best possible way.

It should be:

- clear,
- minimal,
- readable,
- easy to change,
- easy to explain.

If a configuration option cannot be explained yet, it probably does not belong in the first version.

## Continue

- [Previous: uv](02_uv.md)
- [Next: pytest](04_pytest.md)
- [Back to README](../README.md)
