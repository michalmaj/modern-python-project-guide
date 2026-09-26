# Markdown Linting with rumdl

Documentation benefits from automated checks just like Python code does.

This project uses `rumdl` to find structural and consistency problems in
Markdown files without turning documentation review into a formatting exercise.

## What a Markdown linter checks

A Markdown linter can find issues such as:

- skipped heading levels,
- missing blank lines around lists and code fences,
- code fences without language identifiers,
- inconsistent list markers,
- malformed links and images,
- trailing punctuation or spacing patterns covered by configured rules.

These checks make documents easier to maintain and render consistently.

## Install the tool

`rumdl` is a development dependency, so the normal project sync installs it:

```bash
uv sync
```

No separate Node.js environment is required.

## Run the check

Lint all Markdown files in the repository:

```bash
uv run rumdl check .
```

A successful run prints a summary with no reported issues and exits with status
code zero.

## Configuration

The project keeps its `rumdl` settings in `pyproject.toml`:

```toml
[tool.rumdl]
disable = ["MD013"]

[tool.rumdl.per-file-ignores]
".github/pull_request_template.md" = ["MD041"]
"docs/markdown_review.md" = ["MD014"]
```

The line-length rule `MD013` is disabled. Long URLs, commands, and examples can
make a strict limit noisy, while the repository's writing conventions already
encourage short, readable paragraphs.

The pull request template intentionally starts with a level-two heading because
GitHub inserts it into the pull request form. The Markdown review guide also
contains an intentional shell-prompt anti-example. These focused exceptions are
recorded instead of weakening the rules for every file.

## Fixing reported issues

Read the rule identifier and inspect the reported line before editing it.

Some issues can be fixed automatically:

```bash
uv run rumdl check --fix .
```

Always review the resulting diff. A technically valid rewrite may still make an
explanation less clear.

## How it fits with existing checks

The pre-commit hook runs `rumdl` on changed Markdown files for fast feedback.
The `Quality checks` job runs it across the whole repository so the check cannot
be bypassed before merging.

The existing pytest link test has a different responsibility: it verifies local
file paths and heading anchors. `rumdl` does not replace that test.

Neither tool can confirm that an explanation is accurate, complete, or helpful.
Human review remains necessary.

## Why not add a documentation site yet?

Linting improves the Markdown files directly and keeps them readable on GitHub.
A generated site would add navigation, themes, deployment, and another layer of
configuration. That should be introduced only when the project needs it.

## Rule of thumb

Use automation for structural mistakes.

Use human review for meaning, teaching quality, and tone.

## Continue

- [Previous: `pre-commit` Hooks](13_pre_commit_hooks.md)
- [Next: Project Checklist](09_checklist.md)
- [Back to README](../README.md)
