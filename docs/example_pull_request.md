# Example Pull Request

A pull request is more than a GitHub button.

It is a way to explain a change before it becomes part of the main branch.

This page shows what a clear pull request can look like.

## What a pull request should answer

A good pull request should answer three questions:

```text
What changed?
Why was it changed?
How was it checked?
```

If a reviewer can answer these questions quickly, the pull request is easier to review.

## Example pull request title

Good title:

```text
docs: explain pytest
```

Why it works:

- it starts with a clear type,
- it says what changed,
- it is short,
- it matches the style used in commit messages.

Avoid titles like:

```text
Update files
Some changes
Fix stuff
Work
```

These titles do not explain the purpose of the pull request.

## Example pull request description

A good pull request description may look like this:

```markdown
## Summary

Adds a guide chapter explaining pytest and the role of tests in the project.

## Why

The project now includes pytest and a first test suite, so the guide should explain how tests fit into the development workflow.

## Changes

- Adds `docs/04_pytest.md`
- Explains why tests matter
- Describes the `tests/` directory
- Explains pytest naming conventions
- Introduces the Arrange, Act, Assert pattern
- Documents how to run tests with `uv run pytest`

## Type of change

- [x] Documentation
- [ ] Project configuration
- [ ] New feature
- [ ] Tests
- [ ] CI/CD
- [ ] Refactoring
- [ ] Bug fix

## Checklist

- [x] The change is small and focused
- [x] The pull request title is clear
- [x] I updated documentation if needed
- [x] I added or updated tests if needed
- [x] I ran local checks if applicable

## Notes

Documentation-only change.
```

This description is useful because it gives the reviewer context.

The reviewer does not need to guess why the change exists.

## Summary

The summary should describe the change in one or two sentences.

Good example:

```text
Adds a quickstart guide for creating a new Python project with uv.
```

Bad example:

```text
Updated docs.
```

The good version explains what was updated.

The bad version forces the reviewer to inspect the diff without context.

## Why

The `Why` section explains the motivation.

Good example:

```text
Readers who already understand the concepts may want a compact command reference instead of searching through the full guide.
```

Bad example:

```text
Because I wanted to.
```

The good version explains the reader or project need.

The bad version does not help the reviewer understand the decision.

## Changes

The `Changes` section should list the concrete modifications.

Good example:

```markdown
- Adds `docs/cheatsheet.md`
- Lists common `uv` commands
- Lists local quality check commands
- Adds a cheatsheet link to the README
```

Bad example:

```markdown
- Changed stuff
- Updated files
```

Concrete bullets make review easier.

## Type of change

The type of change helps classify the pull request.

Examples:

- documentation,
- project configuration,
- feature,
- tests,
- CI/CD,
- refactoring,
- bug fix.

Choose the most relevant option.

If the pull request mixes many types, it may be too large.

## Checklist

The checklist is a small self-review tool.

Before opening a pull request, check:

- is the change small and focused?
- is the title clear?
- did documentation change when needed?
- did tests change when needed?
- did local checks run when applicable?

The checklist should not be treated as decoration.

It should help catch simple mistakes before review.

## Notes

The `Notes` section is optional.

Use it for extra context such as:

- documentation-only change,
- follow-up work,
- intentionally deferred topics,
- known limitations,
- local commands that were run.

Example:

```text
This change intentionally does not add CI yet. CI will be introduced in a separate pull request.
```

## Good pull request example

```text
Title:
docs: add command cheatsheet

Summary:
Adds a command cheatsheet for common project, uv, Ruff, pytest, Git, and CI commands.

Why:
Readers who already understand the concepts may want a compact command reference instead of searching through the full guide and quickstarts.

Changes:
- Adds docs/cheatsheet.md
- Lists project setup commands
- Lists dependency management commands
- Lists local check commands
- Lists Git workflow commands
- Adds a cheatsheet link to the README

Notes:
Documentation-only change.
```

This pull request is clear because:

- the title is specific,
- the scope is small,
- the reason is explained,
- the changed files are predictable,
- the reviewer knows what to expect.

## Bad pull request example

```text
Title:
updates

Summary:
Changed some docs.

Why:
N/A

Changes:
- stuff
- more stuff

Notes:
none
```

This pull request is hard to review because:

- the title is vague,
- the motivation is missing,
- the change list is not useful,
- the reviewer must guess the purpose,
- the scope may be unclear.

## Before opening a pull request

Review your own diff first.

Useful commands:

```bash
git status
git diff
```

If you already staged files:

```bash
git diff --staged
```

For code changes, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Keep pull requests small

A good pull request should usually focus on one idea.

Good examples:

```text
docs: add project glossary
docs: add command cheatsheet
chore: configure ruff
test: add text statistics tests
ci: add GitHub Actions workflow
```

Avoid combining unrelated changes:

```text
Add glossary, configure Ruff, refactor tests, update CI, and add new features.
```

Small pull requests are easier to review and easier to fix.

## When multiple commits are okay

A pull request can contain more than one commit if each commit represents a logical step.

Good example:

```text
docs: add expected results to uv quickstart
docs: add expected results to clone quickstart
```

Both commits support the same pull request goal, but they affect separate files.

Avoid noisy commits such as:

```text
fix
fix again
typo
oops
final
```

The goal is not to have the fewest commits.

The goal is to have meaningful commits.

## Rule of thumb

A pull request should make the reviewer think:

```text
I understand what changed.
I understand why it changed.
I know how it was checked.
```

If the reviewer has to guess, improve the pull request description before asking for review.