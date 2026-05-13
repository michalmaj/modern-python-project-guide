# pyproject.toml

`pyproject.toml` is the central configuration file for a modern Python project.

It describes the project itself and can also store configuration for development tools.

In this guide, `pyproject.toml` will gradually become the main place for project configuration.

## Why this file matters

A Python project should be understandable not only from its source code, but also from its configuration.

The `pyproject.toml` file helps answer questions such as:

- What is the project called?
- Which Python version does it require?
- Which dependencies does it use?
- Which development tools are configured?
- How should tests, linting, and formatting behave?

Instead of spreading configuration across many unrelated files, this guide keeps the basic setup in one place.

## Current minimal version

At this stage, the project configuration is intentionally small.

The file may look similar to this:

```toml
[project]
name = "text-toolkit"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

This is enough to describe a minimal Python project.

More configuration will be added later, but only when it becomes useful.

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

Development tools such as `pytest` and `ruff` will be added later as development dependencies.

## Runtime dependencies vs development dependencies

Not all dependencies have the same role.

Runtime dependencies are needed when someone uses the project.

Development dependencies are needed only while developing the project.

Examples of development dependencies:

- `pytest`,
- `ruff`,
- test coverage tools,
- type checkers,
- documentation tools.

This guide will add development dependencies gradually.

The goal is to make each tool understandable before adding the next one.

## Tool configuration

Many Python tools can be configured inside `pyproject.toml`.

Later in this guide, this file will also contain sections such as:

```toml
[tool.pytest.ini_options]
```

and:

```toml
[tool.ruff]
```

This keeps important project settings close to the project metadata.

## Why not configure everything now?

It would be possible to add all configuration immediately.

However, that would make the project harder to learn from.

This guide follows a slower approach:

1. start with minimal project metadata,
2. add source code,
3. add tests,
4. configure pytest,
5. add Ruff,
6. configure linting and formatting,
7. add continuous integration.

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
