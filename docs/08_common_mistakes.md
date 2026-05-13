# Common Beginner Mistakes

This chapter describes common mistakes that happen when people move from small Python scripts to maintainable projects.

These mistakes are normal.

The goal is not to shame anyone.

The goal is to notice problems early and replace them with better habits.

## Mistake 1: Keeping everything in one file

Many Python projects start as one file:

```text
main.py
```

That is fine for experiments.

However, as the project grows, one large file becomes harder to understand, test, and reuse.

A better approach is to separate responsibilities.

Example:

```text
src/
└── text_toolkit/
    ├── __init__.py
    └── text_stats.py

tests/
└── test_text_stats.py
```

This makes it clearer where implementation code and tests belong.

## Mistake 2: Installing packages manually without project configuration

A beginner may install packages with:

```bash
pip install package-name
```

This works locally, but it does not explain the project requirements to other people.

A maintainable project should describe its dependencies in a project file.

In this guide, dependencies are managed through:

```text
pyproject.toml
uv.lock
```

This makes the project easier to reproduce on another machine or in CI.

## Mistake 3: Not using a virtual environment

Installing everything globally can create confusing problems.

Different projects may need different dependencies.

A virtual environment keeps dependencies isolated for one project.

In this guide, `uv` manages the environment through:

```text
.venv/
```

The `.venv/` directory is generated locally and should not be committed to Git.

## Mistake 4: Committing generated local files

Some files are created by tools and should stay local.

Examples:

```text
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.coverage
```

These files usually do not belong in Git.

They can make pull requests noisy and repository history messy.

Use `.gitignore` to keep generated files out of the repository.

## Mistake 5: No tests

A project without tests can still work.

The problem is that changes become harder to trust.

Without tests, every change must be checked manually.

A better habit is to add small tests for important behavior.

Example:

```python
def test_count_words_returns_zero_for_empty_text() -> None:
    result = count_words("")

    assert result == 0
```

Tests make it easier to change code without breaking existing behavior.

## Mistake 6: Testing implementation details instead of behavior

Tests should usually check what the code does, not how it does it internally.

A good test describes expected behavior.

Better:

```python
def test_normalize_whitespace_replaces_repeated_spaces() -> None:
    text = "Python    is   fun"

    result = normalize_whitespace(text)

    assert result == "Python is fun"
```

This test checks behavior.

It does not care about the exact internal implementation.

## Mistake 7: Not running checks before opening a pull request

A pull request should be checked locally before it is opened.

For code changes, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

This reduces avoidable CI failures.

CI is still useful, but it should not be the first place where simple issues are discovered.

## Mistake 8: Treating formatting as a personal preference debate

Formatting discussions can waste a lot of time.

A formatter makes formatting consistent automatically.

In this project, formatting is checked with:

```bash
uv run ruff format --check .
```

and fixed with:

```bash
uv run ruff format .
```

The goal is not to make everyone love the same style.

The goal is to remove unnecessary style discussions from code review.

## Mistake 9: Blindly obeying every linting rule

Linting rules are useful, but they are not absolute laws.

Sometimes a rule is too strict for a specific context.

For example, small tests may use expected numeric values directly:

```python
def test_count_words_handles_repeated_whitespace() -> None:
    text = "Python    project\nworkflow"

    result = count_words(text)

    assert result == 3
```

A strict configuration may treat `3` as a magic value.

In this context, the value is readable and meaningful.

A team may decide to ignore such a rule for tests:

```toml
[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "PLR2004",
]
```

The important thing is to ignore rules intentionally, not randomly.

## Mistake 10: Writing unclear commit messages

Commit messages should explain what changed.

Bad examples:

```text
update
fix
changes
final
final2
```

Better examples:

```text
docs: explain pytest
test: add text statistics tests
chore: configure ruff
ci: add GitHub Actions workflow
```

Readable commits make project history more useful.

## Mistake 11: Committing directly to main

Committing directly to `main` may be tempting when working alone.

However, using branches and pull requests has benefits even in solo projects.

It gives every change a place to be reviewed, checked, and explained.

A better workflow is:

```text
create branch → commit → push → pull request → CI → merge
```

This keeps `main` cleaner and safer.

## Mistake 12: Making pull requests too large

Large pull requests are hard to review.

They often mix many unrelated changes.

Example of a poor pull request:

```text
Add tests, configure Ruff, add CI, update README, refactor package, and add new features.
```

Better:

```text
test: add text statistics tests
chore: configure ruff
ci: add GitHub Actions workflow
docs: update README
```

Small pull requests are easier to understand and easier to fix if something goes wrong.

## Mistake 13: Ignoring failing CI

A failing CI check is a signal that something needs attention.

It should not be ignored.

Common causes include:

- failing tests,
- formatting issues,
- linting errors,
- dependency installation problems,
- workflow configuration mistakes.

When CI fails, read the error message carefully.

Then reproduce the problem locally if possible.

## Mistake 14: Copying templates without understanding them

Project templates can be useful.

However, copying a large template without understanding it can create confusion.

A beginner may end up with:

- unused tools,
- unexplained configuration,
- complex CI,
- unnecessary files,
- unclear dependencies.

This guide takes a slower approach.

Each file and tool is introduced only when it becomes useful.

## Mistake 15: Adding advanced tools too early

Tools such as coverage, type checkers, pre-commit hooks, documentation generators, Docker, and release automation can be valuable.

However, adding all of them at the beginning may overwhelm the project.

A better approach is gradual:

1. project structure,
2. dependency management,
3. tests,
4. linting and formatting,
5. CI,
6. documentation,
7. stricter quality tools later.

A project should grow only as fast as its maintainers can understand it.

## Rule of thumb

Most beginner mistakes come from moving too fast.

Slow down.

Make one change at a time.

Run checks.

Open small pull requests.

Explain decisions.

A clean project is not created by one perfect setup command.

It is created by many small, understandable decisions.