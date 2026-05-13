# Why This Guide Exists

Many people learn Python by writing small scripts.

That is a good start.

However, a script is not the same thing as a maintainable project.

A maintainable project should be easy to:

- understand,
- run,
- test,
- format,
- review,
- change,
- share with others.

This guide shows how to move from a simple Python script to a clean, modern Python project.

## The problem

Beginners often know how to write Python code, but they may not know how to organize a project around that code.

Common problems include:

- keeping all code in one large file,
- installing dependencies manually without a clear project file,
- not knowing where tests should go,
- not using automated formatting,
- not checking code before pushing it,
- committing directly to `main`,
- writing unclear commit messages,
- opening large pull requests that are hard to review.

These problems are normal at the beginning.

The goal of this guide is to introduce better habits step by step.

## The main idea

This repository is both a tutorial and a working example.

It teaches a practical workflow based on:

- `uv` for project and dependency management,
- `pyproject.toml` for project configuration,
- `pytest` for testing,
- `ruff` for linting and formatting,
- GitHub Actions for continuous integration,
- branches for isolated work,
- pull requests for review,
- readable commits for project history.

The project starts small on purpose.

Advanced tools are useful, but they should not be introduced too early.

A simple, understandable foundation is more valuable than a complicated setup that nobody understands.

## What this guide is not

This guide is not a complete Python packaging course.

It does not start with advanced topics such as:

- publishing packages to PyPI,
- Docker,
- pre-commit hooks,
- static type checking,
- documentation generators,
- release automation.

These topics may be added later.

The first goal is to understand the basic workflow.

## Who this guide is for

This guide is for people who know basic Python and want to learn how to build projects in a more professional way.

It may be useful for:

- students,
- self-taught developers,
- junior Python developers,
- teachers,
- people preparing portfolio projects,
- anyone moving from scripts to maintainable projects.

## The philosophy

This project should stay simple, but not careless.

It should be beginner-friendly, but still realistic.

Every part of the repository should answer one question:

> Would this help someone understand how a clean Python project is built?

If the answer is yes, it belongs here.

If the answer is no, it should probably wait.