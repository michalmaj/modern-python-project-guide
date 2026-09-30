# Building Distributions

The project can now be installed into its development environment.

The next step is to build files that could be installed on another machine.
These files are called distributions.

This chapter explains how to build them. It does not publish anything to PyPI.

## Prerequisites

The project defines a build system in `pyproject.toml`:

```toml
[build-system]
requires = ["uv_build>=0.12.19,<0.13"]
build-backend = "uv_build"
```

The build backend reads the project metadata and the package under:

```text
src/text_toolkit/
```

It then creates standard Python distribution files.

## Build the project

Run:

```bash
uv build --no-sources
```

The `--no-sources` option tells `uv` to ignore any uv-specific dependency
sources while resolving build requirements. This helps verify that the project
can be built from its standard package metadata.

This project does not currently define custom sources, but using the option
makes the build check suitable for a future publishing workflow.

## Expected result

The command creates a `dist/` directory containing two files similar to:

```text
dist/
├── text_toolkit-0.1.0-py3-none-any.whl
└── text_toolkit-0.1.0.tar.gz
```

The exact filenames depend on the project name and version.

The `dist/` directory contains generated artifacts. It is excluded by
`.gitignore` and should not be committed.

## Wheel

A wheel is a built distribution.

This project's wheel is:

```text
text_toolkit-0.1.0-py3-none-any.whl
```

The filename communicates several facts:

- `text_toolkit` is the normalized distribution name,
- `0.1.0` is the project version,
- `py3` means it supports Python 3,
- `none-any` means it contains pure Python code and is not tied to one operating
  system or processor architecture.

Installing a compatible wheel usually does not require running the build backend
again.

## Source distribution

A source distribution is often shortened to `sdist`.

This project's source distribution is:

```text
text_toolkit-0.1.0.tar.gz
```

It contains the source files and metadata needed to build the project. Tools can
use the source distribution to create a wheel.

By default, `uv build` builds the source distribution first and then builds the
wheel from that source distribution. This helps verify that the source archive
contains everything required for a successful build.

## Why build both files?

The two formats serve different purposes:

- a wheel is ready to install on a compatible Python environment,
- a source distribution preserves the source package in a standard archive,
- building the wheel from the source distribution checks that the archive is
  complete.

For a pure Python project, producing both files is a useful packaging check.

## Build in CI

The GitHub Actions workflow runs:

```yaml
- name: Build distributions
  run: uv build --no-sources
```

This means every pull request verifies that the project can still produce a
wheel and source distribution.

The workflow does not upload the files or publish a release. It only checks that
the build succeeds.

## Run the packaging check locally

Run the same command before opening a pull request that changes:

- `pyproject.toml`,
- package metadata,
- the build backend,
- files included in the package,
- package structure under `src/`.

```bash
uv build --no-sources
```

After the command succeeds, `git status` should stay clean because `dist/` is
ignored.

## What this chapter does not cover

Building files locally is different from publishing them.

This chapter does not cover:

- creating a PyPI project,
- configuring trusted publishing,
- uploading distributions,
- versioning releases,
- release automation.

Those steps should be introduced separately because they affect external
systems and released artifacts.

## Rule of thumb

Install the project with `uv sync` while developing it.

Build distribution files with `uv build --no-sources` when checking whether the
project is ready to be packaged.

Treat publishing as a separate, deliberate operation.

## Continue

- [Previous: Common Beginner Mistakes](08_common_mistakes.md)
- [Next: Static Type Checking with mypy](11_type_checking_with_mypy.md)
- [Back to documentation home](index.md)
