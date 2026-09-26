# Modern Python Project Guide

[![CI](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/michalmaj/modern-python-project-guide/actions/workflows/ci.yml)

A practical, beginner-friendly guide to building a clean Python project with
`uv`, `pytest`, Ruff, `pyproject.toml`, GitHub Actions, and a pull request based
workflow.

This repository is both a tutorial and a working example. It introduces each
tool gradually and shows how the pieces fit together in a maintainable project.

## Choose your path

- **Create a new project:** follow the [uv quickstart](docs/quickstart_uv.md).
- **Run this repository locally:** follow the
  [clone and CI quickstart](docs/quickstart_clone_and_ci.md).
- **Learn the complete workflow:** start with
  [Why This Guide Exists](docs/00_why_this_guide.md) and follow the main learning
  path below.
- **Find a command or solve a problem:** jump to the
  [reference material](#reference-material).

## What you will learn

By following the guide, you will learn how to:

- structure a Python project with the `src/` layout,
- manage Python and dependencies with `uv`,
- configure the project in `pyproject.toml`,
- install a package in editable mode and build distributions,
- test code with `pytest`,
- lint and format code with Ruff,
- run the same checks in GitHub Actions,
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
11. [Project checklist](docs/09_checklist.md)

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
│   └── workflows/
├── docs/
├── src/
│   └── text_toolkit/
├── tests/
├── CONTRIBUTING.md
├── README.md
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
uv run pytest
uv build --no-sources
```

For explanations and expected results, use the
[clone and CI quickstart](docs/quickstart_clone_and_ci.md).

## Contributing

Small, focused improvements are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).
