# Git, Commits, Branches, and Pull Requests

This repository is built using a branch-based workflow.

The goal is not only to create a clean Python project, but also to show how a project can grow through small, understandable changes.

## Why workflow matters

Writing code is only one part of software development.

A maintainable project also needs a clear workflow for:

- making changes,
- reviewing changes,
- understanding project history,
- protecting the main branch,
- collaborating with other people.

Even when working alone, a good workflow helps keep the project organized.

## The basic workflow

This repository uses the following workflow:

```text
update main
create a branch
make a small change
commit the change
push the branch
open a pull request
review the pull request
merge into main
delete the branch
```

In command form:

```bash
git switch main
git pull
git switch -c docs/example-change

# edit files

git status
git add path/to/file.md
git commit -m "docs: describe example change"
git push -u origin docs/example-change
```

After the pull request is merged:

```bash
git switch main
git pull
git branch -d docs/example-change
```

## The main branch

The `main` branch should represent the current stable version of the project.

Do not commit directly to `main`.

Every meaningful change should go through a pull request.

This keeps the project history easier to understand and gives CI a chance to check changes before they are merged.

## Branches

A branch is an isolated place for one change.

Good branches are small and focused.

Recommended branch name format:

```text
<type>/<short-description>
```

Examples:

```text
docs/add-pytest-guide
docs/add-git-workflow-guide
chore/configure-ruff
test/add-text-statistics-tests
ci/add-github-actions-workflow
feat/add-text-toolkit-package
```

The branch name should describe the purpose of the change.

## Good branch names

Good branch names are clear and specific:

```text
docs/add-ruff-guide
test/add-text-stats-tests
ci/add-github-actions-workflow
chore/initialize-uv-project
```

These names make it easy to understand what the branch is about.

## Bad branch names

Avoid vague names:

```text
changes
updates
work
stuff
fixes
new-version
final
```

These names do not explain the purpose of the branch.

They may be understandable for a few minutes, but they become confusing later.

## Commits

A commit should represent one logical change.

Good commits make project history readable.

This repository uses commit messages in this format:

```text
<type>: <short description>
```

Examples:

```text
docs: add project roadmap
docs: explain pytest
chore: configure ruff
test: add text statistics tests
ci: add GitHub Actions workflow
feat: add text toolkit package
```

## Common commit types

Useful commit types include:

```text
docs      documentation changes
chore     configuration, setup, maintenance
feat      new functionality
test      tests
fix       bug fixes
ci        continuous integration changes
refactor  code changes that do not change behavior
```

The goal is not to follow a complicated standard perfectly.

The goal is to make the project history easy to scan.

## Good commit messages

Good commit messages are specific:

```text
docs: explain github actions
test: add text statistics tests
chore: initialize uv project
ci: add GitHub Actions workflow
```

A person reading the history can understand what happened.

## Bad commit messages

Avoid unclear messages:

```text
update
fix
changes
work
final
final fix
really final
```

These messages do not explain the change.

They make history harder to understand.

## Small changes

Small changes are easier to review.

A pull request should usually focus on one idea.

Good examples:

```text
Add pytest configuration and first tests.
Add Ruff configuration.
Add GitHub Actions workflow.
Explain project structure.
```

Poor examples:

```text
Add tests, CI, Ruff, documentation, refactoring, and new features at once.
```

Large pull requests are harder to review because many decisions are mixed together.

Small pull requests make it easier to discuss one thing at a time.

## Pull requests

A pull request is a proposal to merge a branch into `main`.

A good pull request should answer three questions:

```text
What changed?
Why was it changed?
How was it checked?
```

The pull request description should be helpful to the reviewer.

It should not force the reviewer to guess the intention of the change.

## Pull request title

The pull request title should use the same style as commit messages.

Examples:

```text
docs: explain ruff
test: add text statistics tests
ci: add GitHub Actions workflow
```

Avoid vague titles:

```text
Update files
New changes
Some fixes
```

## Pull request description

A good pull request description may include:

- summary,
- motivation,
- list of changes,
- type of change,
- local checks,
- notes for reviewers.

Example:

```markdown
## Summary

Adds tests for the text statistics utilities.

## Why

The project now contains a small example package, so it should include automated tests that verify its behavior.

## Changes

- Adds pytest as a development dependency
- Adds tests for whitespace normalization
- Adds tests for word counting
- Adds tests for character counting

## Notes

Local check:

```bash
uv run pytest
```
```

## Review mindset

A pull request is not only a technical step.

It is also a communication tool.

When preparing a pull request, think about the person who will review it.

A good pull request should make the reviewer's job easier.

That means:

- avoid unrelated changes,
- keep the diff small,
- explain non-obvious decisions,
- include checks that were run,
- mention follow-up work when needed.

## Reviewing your own pull request

Before asking someone else to review a pull request, review it yourself.

Useful questions:

- Is the pull request focused?
- Is the title clear?
- Does the description explain the change?
- Are unrelated files included by accident?
- Did local checks pass?
- Is the diff easy to read?

Self-review catches many simple mistakes.

## Local checks before opening a pull request

For code changes, run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

For documentation-only changes, code checks may not be necessary.

However, it is still useful to review the rendered Markdown on GitHub after opening the pull request.

## CI checks

After opening a pull request, GitHub Actions runs automated checks.

A green CI check means:

- linting passed,
- formatting check passed,
- tests passed.

A green CI check does not mean the pull request is perfect.

It only means the automated checks passed.

Human review is still needed for clarity, design, documentation quality, and project direction.

## After merging

After the pull request is merged, update the local `main` branch:

```bash
git switch main
git pull
```

Then delete the local branch:

```bash
git branch -d docs/example-change
```

The remote branch can usually be deleted from GitHub after merging.

Deleting merged branches keeps the repository clean.

## Common beginner mistakes

Common mistakes include:

- committing directly to `main`,
- making one huge pull request,
- using unclear commit messages,
- mixing unrelated changes,
- forgetting to pull the latest `main`,
- ignoring failing CI,
- not reading the diff before opening a pull request,
- using branches with vague names.

These mistakes are normal when learning.

The purpose of this workflow is to avoid them gradually.

## Rule of thumb

A good workflow should make the project easier to understand.

Use branches to isolate work.

Use commits to record meaningful steps.

Use pull requests to explain and review changes.

Use CI to check repetitive things automatically.

The goal is not bureaucracy.

The goal is clarity.
