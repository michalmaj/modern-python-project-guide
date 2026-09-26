# pre-commit Hooks

`pre-commit` hooks run small checks after you ask Git to create a commit but
before Git finishes creating it.

They provide quick feedback while the changed files are still fresh in your
mind. They do not replace the complete local checks or GitHub Actions.

## Why add hooks now?

This guide first introduced each command directly. You already know how to run
Ruff, pytest with coverage, mypy, and the package build yourself.

Adding automation now makes the workflow more convenient without hiding what
the tools do.

## Install the hooks

After `uv sync`, install the Git hook for this clone:

```bash
uv run pre-commit install
```

Expected output:

```text
pre-commit installed at .git/hooks/pre-commit
```

The installation is local to the current clone. The committed configuration is
shared, but every contributor must install the hook after cloning.

## Run every hook manually

A normal commit checks only the files involved in that commit. After adding or
changing hook configuration, check the whole repository once:

```bash
uv run pre-commit run --all-files
```

The first run can take longer because pre-commit creates isolated environments
for the configured hooks.

## Current configuration

The hooks are configured in `.pre-commit-config.yaml`.

The general file checks:

- remove accidental trailing whitespace while preserving intentional Markdown
  line breaks,
- ensure files end with a newline,
- validate YAML and TOML syntax,
- detect unresolved merge conflict markers.

The Ruff hooks:

- apply safe lint fixes,
- format changed Python files.

These checks are deliberately fast. Tests, coverage, mypy, and distribution
builds remain part of the complete local and CI checks.

## When a hook changes a file

A hook may fix a file and stop the commit. This is expected.

Review the result:

```bash
git diff
```

Then stage the corrected file and commit again:

```bash
git add path/to/file
git commit
```

Do not stage changes without reviewing them.

## Hooks and CI have different jobs

Hooks give fast local feedback, but they can be skipped or left uninstalled.
GitHub Actions runs in a clean environment and protects the shared branch.

Use both layers:

- pre-commit hooks for quick feedback on changed files,
- the complete local checks before opening a pull request,
- CI as the required shared verification.

## Remove the installed hook

To stop running the hook in the current clone:

```bash
uv run pre-commit uninstall
```

This does not delete `.pre-commit-config.yaml` or remove the dependency from the
project.

## Rule of thumb

Automate fast, repeatable checks before commits.

Keep the complete quality checks visible and understandable.

## Continue

- [Previous: Test Coverage with pytest-cov](12_test_coverage.md)
- [Next: Project Checklist](09_checklist.md)
- [Back to README](../README.md)
