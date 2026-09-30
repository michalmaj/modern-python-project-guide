# Modern Python Project Guide

[![CI](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml)
[![Documentation](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/pages.yml/badge.svg)](https://michalmaj.github.io/modern-python-project-guide/)
[![GitHub release](https://img.shields.io/github/v/release/michalmaj/modern-python-project-guide?display_name=tag&sort=semver)](https://github.com/michalmaj/modern-python-project-guide/releases)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9)](https://docs.astral.sh/uv/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Ruff](https://img.shields.io/badge/lint%20%26%20format-Ruff-D7FF64)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/type%20checked-mypy-2A6DB2)](https://mypy.readthedocs.io/)
[![MkDocs](https://img.shields.io/badge/docs-MkDocs-526CFE)](https://www.mkdocs.org/)
[![pre-commit](https://img.shields.io/badge/hooks-pre--commit-FAB040?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License: MIT](https://img.shields.io/github/license/michalmaj/modern-python-project-guide)](LICENSE)
[![Open issues](https://img.shields.io/github/issues/michalmaj/modern-python-project-guide)](https://github.com/michalmaj/modern-python-project-guide/issues)
[![Student feedback welcome](https://img.shields.io/badge/student%20feedback-welcome-brightgreen)](https://github.com/michalmaj/modern-python-project-guide/issues/new/choose)

A practical, beginner-friendly guide to building a clean Python project with
`uv`, `pytest`, Ruff, mypy, `rumdl`, MkDocs, `pyproject.toml`, GitHub Actions,
and a pull-request-based workflow with `pre-commit` hooks.

This repository is both a tutorial and a working example. It introduces each
tool gradually and shows how the pieces fit together in a maintainable project.

## Choose your path

- **Create a new project:** follow the [uv quickstart](docs/quickstart_uv.md).
- **Run this repository locally:** follow the
  [clone and CI quickstart](docs/quickstart_clone_and_ci.md).
- **Learn the complete workflow:** start with
  [Why This Guide Exists](docs/00_why_this_guide.md) and follow the main learning
  path below.
- **Browse the published guide:** open the
  [documentation site](https://michalmaj.github.io/modern-python-project-guide/).
- **Find a command or solve a problem:** jump to the
  [reference material](#reference-material).

## What you will learn

By following the guide, you will learn how to:

- structure a Python project with the `src/` layout,
- manage Python and dependencies with `uv`,
- configure the project in `pyproject.toml`,
- install a package in editable mode and build distributions,
- test code with `pytest`,
- inspect statement and branch coverage with pytest-cov,
- lint and format code with Ruff,
- check type annotations with mypy,
- lint Markdown documentation with `rumdl`,
- preview and validate a documentation site with MkDocs,
- publish documentation safely with GitHub Pages,
- automate fast checks with `pre-commit` hooks,
- run automated quality checks in GitHub Actions,
- work with branches, commits, and pull requests.

You should already know basic Python, terminal usage, Git, and GitHub. Packaging,
continuous integration, and project structure are explained from the beginning.

## Main learning path

The chapters form one step-by-step path. Start from the beginning if you want to
understand why each tool and file is introduced.

1. [Why this guide exists](docs/00_why_this_guide.md)
2. [Project structure](docs/01_project_structure.md)
3. [uv and dependency management](docs/02_uv.md)
4. [pyproject.toml](docs/03_pyproject_toml.md)
5. [Testing with pytest](docs/04_pytest.md)
6. [Code quality with Ruff](docs/05_ruff.md)
7. [GitHub Actions and CI](docs/06_github_actions.md)
8. [Git, commits, branches, and pull requests](docs/07_git_commits_branches_prs.md)
9. [Common beginner mistakes](docs/08_common_mistakes.md)
10. [Building distributions](docs/10_building_distributions.md)
11. [Static type checking with mypy](docs/11_type_checking_with_mypy.md)
12. [Test coverage with pytest-cov](docs/12_test_coverage.md)
13. [`pre-commit` hooks](docs/13_pre_commit_hooks.md)
14. [Markdown linting with rumdl](docs/14_markdown_linting.md)
15. [Documentation site with MkDocs](docs/15_documentation_site_with_mkdocs.md)
16. [Publishing with GitHub Pages](docs/16_publishing_with_github_pages.md)
17. [Project checklist](docs/09_checklist.md)

## Reference material

Use these guides when you need a focused answer rather than the complete
learning path.

### Starting and adapting a project

- [uv quickstart](docs/quickstart_uv.md)
- [Clone and CI quickstart](docs/quickstart_clone_and_ci.md)
- [From script to project](docs/from_script_to_project.md)

### Commands, concepts, and troubleshooting

- [Command cheatsheet](docs/cheatsheet.md)
- [Glossary](docs/glossary.md)
- [Common questions](docs/common_questions.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Reading GitHub Actions logs](docs/github_actions_logs.md)

### Collaboration and review

- [Contributing guidelines](CONTRIBUTING.md)
- [Example pull request](docs/example_pull_request.md)
- [Reviewing Markdown changes](docs/markdown_review.md)

### Project direction

- [Project roadmap](docs/ROADMAP.md)

## The example project

The repository contains a deliberately small package in `src/text_toolkit/`.
It keeps the domain simple so the guide can focus on project structure,
tooling, tests, packaging, and CI.

```text
modern-python-project-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── .pre-commit-config.yaml
├── docs/
│   ├── index.md
│   └── ...
├── src/
│   └── text_toolkit/
├── tests/
├── CONTRIBUTING.md
├── README.md
├── mkdocs.yml
├── pyproject.toml
└── uv.lock
```

## Try it locally

Clone the repository and install the project environment:

```bash
git clone https://github.com/michalmaj/modern-python-project-guide.git
cd modern-python-project-guide
uv sync
```

Run the same quality checks used by CI:

```bash
uv run ruff check .
uv run ruff format --check .
uv run rumdl check .
uv run mkdocs build --strict
uv run pytest --cov=text_toolkit --cov-report=term-missing
uv run mypy
uv build --no-sources
```

Preview the documentation site separately with:

```bash
uv run mkdocs serve
```

For explanations and expected results, use the
[clone and CI quickstart](docs/quickstart_clone_and_ci.md).

## Share feedback

This guide is ready to be tested with students and other learners. You do not
need to propose a solution or write code to help improve it.

- Share your learning experience with the
  [learning feedback form](https://github.com/michalmaj/modern-python-project-guide/issues/new?template=learning_feedback.yml).
- Report an incorrect instruction, broken command, or site problem with the
  [problem report form](https://github.com/michalmaj/modern-python-project-guide/issues/new?template=problem_report.yml).
- Browse [existing issues](https://github.com/michalmaj/modern-python-project-guide/issues)
  before reporting the same problem again.

## Contributing

Small, focused improvements are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).
