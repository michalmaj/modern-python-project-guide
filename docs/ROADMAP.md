# Project Roadmap

This roadmap describes how the repository is built and how it may grow.

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

## Current foundation

The first foundation is now in place.

The repository already includes:

- a clear README landing page,
- quickstart guides,
- a step-by-step guide,
- a small example package,
- the `src/` layout,
- pytest tests,
- Ruff linting and formatting,
- GitHub Actions CI,
- a pull request template,
- contributing guidelines,
- a glossary,
- a command cheatsheet,
- common questions,
- an example pull request guide,
- a from-script-to-project guide,
- a Markdown review guide,
- a GitHub Actions logs guide,
- a troubleshooting guide,
- a guide to building distributions,
- EditorConfig.

## Done

These parts are already included in the repository.

### Repository foundation

- [x] Bootstrap the repository
- [x] Add a project roadmap
- [x] Add contribution guidelines
- [x] Add a pull request template
- [x] Add a README landing page
- [x] Add GitHub metadata guidance
- [x] Protect `main` with pull request and CI requirements
- [x] Enable automatic deletion of merged branches
- [x] Choose and document the merge commit strategy

### Python project setup

- [x] Initialize the project with `uv`
- [x] Add `pyproject.toml`
- [x] Add `.python-version`
- [x] Add `uv.lock`
- [x] Use the `src/` layout
- [x] Create a small example package
- [x] Clarify the difference between project structure and packaging
- [x] Add the `uv_build` build backend
- [x] Install the project in editable mode with `uv sync`
- [x] Remove the pytest `pythonpath` shortcut

### Tests and quality tools

- [x] Add `pytest`
- [x] Add a minimal test suite
- [x] Configure pytest in `pyproject.toml`
- [x] Add Ruff
- [x] Configure Ruff in `pyproject.toml`
- [x] Explain linting and formatting
- [x] Explain when ignoring linting rules may be reasonable
- [x] Check internal Markdown links with pytest
- [x] Add whitespace edge cases to the example test suite
- [x] Demonstrate pytest parametrization with related inputs
- [x] Add mypy as a development dependency
- [x] Configure strict local type checking
- [x] Run type checks against source code and tests
- [x] Add pytest-cov and local branch coverage reporting

### Continuous integration

- [x] Add a GitHub Actions workflow
- [x] Run linting in CI
- [x] Run formatting checks in CI
- [x] Run tests in CI
- [x] Run coverage reporting in CI
- [x] Run type checking in CI
- [x] Build distributions in CI
- [x] Add a CI badge to the README
- [x] Explain how CI supports pull requests

### Learning materials

- [x] Explain why the guide exists
- [x] Explain project structure
- [x] Explain `uv`
- [x] Explain `pyproject.toml`
- [x] Explain pytest
- [x] Explain Ruff
- [x] Explain GitHub Actions and CI
- [x] Explain Git, commits, branches, and pull requests
- [x] Add common beginner mistakes
- [x] Add a project checklist
- [x] Add quickstarts
- [x] Add expected results to quickstarts
- [x] Add common questions
- [x] Add a glossary
- [x] Add a command cheatsheet
- [x] Add an example pull request guide
- [x] Add a from-script-to-project guide
- [x] Add a short guide for reviewing Markdown changes
- [x] Add a guide for reading GitHub Actions logs
- [x] Add a troubleshooting guide for common setup problems
- [x] Review internal documentation links
- [x] Explain how to build wheels and source distributions
- [x] Keep the README focused as a landing page
- [x] Separate the main learning path from reference material
- [x] Add previous and next navigation to the core chapters
- [x] Review commit history and self-review coverage in the existing guides
- [x] Standardize terminology and dependency examples across the documentation
- [x] Explain type hints and static type checking with mypy
- [x] Explain what coverage does and does not measure
- [x] Avoid treating coverage percentage as a quality guarantee
- [x] Add fast `pre-commit` hooks
- [x] Explain how local hooks complement complete checks and CI

## Next

These are good candidates for upcoming small pull requests.

### Repository polish

- [ ] Add issue templates only if the repository starts receiving external feedback

### Optional convenience

- [ ] Consider a task runner chapter
- [ ] Consider `Makefile` as an optional convenience layer
- [ ] Consider `just` as an alternative task runner

Task runners should not replace the basic commands in the main learning path.

They should be introduced only as convenience wrappers after the underlying commands are clear.

## Later

These topics are intentionally not part of the first foundation.

They may be added later as separate chapters.

### Packaging

- [ ] Explain publishing to PyPI

### Documentation site

- [ ] Consider MkDocs or another documentation site generator
- [ ] Keep Markdown files readable without requiring a generated site

### Release automation

- [ ] Explain versioning
- [ ] Add release notes
- [ ] Add GitHub releases
- [ ] Consider automated release workflows

### Docker

- [ ] Explain when Docker is useful
- [ ] Add Docker only if it solves a real problem for the guide

## Not part of the original foundation

These topics were deliberately excluded from the original foundation:

- Docker,
- publishing to PyPI,
- release automation,
- documentation site generation,
- pre-commit hooks,
- coverage gates,
- complex multi-job CI,
- template generation.

These tools can be useful, but adding them too early would make the foundation harder to understand.

## Rule of thumb

The project should grow only when a new addition teaches something useful.

A smaller setup that readers understand is better than a large template copied without context.
