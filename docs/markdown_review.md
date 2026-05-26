# Reviewing Markdown Changes

This repository contains many documentation files.

That means many pull requests will change Markdown.

Reviewing Markdown is not only about spelling.

A good Markdown review should check whether the document is clear, readable, correctly linked, and rendered properly on GitHub.

## When to use this guide

Use this guide when reviewing changes to files such as:

```text
README.md
CONTRIBUTING.md
docs/*.md
.github/pull_request_template.md
```

## Start with the rendered view

Markdown is written as plain text, but readers usually see the rendered version on GitHub.

When reviewing a documentation pull request:

1. Open the changed Markdown file on GitHub.
2. Switch to the rendered view if needed.
3. Read it as a reader, not only as a reviewer.
4. Check whether headings, lists, code blocks, and links look correct.

The raw diff is useful, but the rendered view shows how the document will actually appear.

## Check the purpose of the change

Before reviewing details, ask:

```text
What is this document trying to help the reader do?
```

A documentation change should have a clear purpose.

Examples:

- explain a concept,
- show a command,
- answer a common question,
- help with troubleshooting,
- guide a beginner through a workflow.

If the purpose is unclear, the document may need a better introduction.

## Check the title and headings

Headings should make the document easy to scan.

Good headings:

```markdown
## Run local checks
## Fix formatting problems
## Why CI uses uv sync --locked
```

Weak headings:

```markdown
## Stuff
## More info
## Important
```

A reader should be able to skim the headings and understand the structure of the page.

## Check heading order

Avoid jumping randomly between heading levels.

Good:

```markdown
# Page title

## Main section

### Subsection
```

Avoid:

```markdown
# Page title

### Subsection without a parent section

## Main section
```

Consistent heading order makes the document easier to navigate.

## Check links

Markdown links should point to existing files.

From the repository root, links usually look like:

```markdown
[Glossary](docs/glossary.md)
```

From one file inside `docs/` to another file inside `docs/`, links usually look like:

```markdown
[Glossary](glossary.md)
```

Check links after opening the pull request.

Broken links make the guide frustrating to use.

## Check code fences

Every code block should start and end correctly.

Example:

````markdown
```bash
uv run pytest
```
````

A missing closing fence can break the rest of the document.

Also check whether the language label is useful.

Good examples:

````markdown
```bash
uv sync
```

```python
def add(left: int, right: int) -> int:
    return left + right
```

```toml
[project]
name = "example"
```

```yaml
name: CI
```
````

Language labels improve readability and syntax highlighting.

## Check commands

Commands should be copy-paste friendly.

Good:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Avoid mixing shell prompts into commands:

```bash
$ uv run pytest
```

The `$` prompt can be confusing when copied.

Use plain commands unless the prompt is important to the explanation.

## Check Bash and PowerShell differences

Some commands work in Bash but not in PowerShell.

For example:

```bash
mkdir -p src/example_project tests
touch src/example_project/__init__.py
```

PowerShell may need:

```PowerShell
New-Item -ItemType Directory -Force src/example_project
New-Item -ItemType Directory -Force tests
New-Item -ItemType File -Force src/example_project/__init__.py
```

If a guide includes file creation commands, consider whether Windows users need an alternative.

## Check lists

Lists should be easy to scan.

Good:

```markdown
- source code lives in `src/`,
- tests live in `tests/`,
- documentation lives in `docs/`.
```

Avoid very long bullets that contain multiple unrelated ideas.

If a bullet becomes too long, consider splitting it into a paragraph or smaller list.

## Check expected results

Quickstarts and troubleshooting guides should tell readers what success looks like.

Useful phrases:

```markdown
Expected result:

- `pyproject.toml` exists,
- `uv.lock` exists,
- `uv run pytest` passes.
```

This helps readers confirm that they are on the right path.

## Check consistency

Use the same names consistently.

Examples used in this repository:

```text
uv
pytest
Ruff
GitHub Actions
CI
pyproject.toml
uv.lock
src/
tests/
pull request
```

Avoid switching between names without a reason.

For example, do not randomly alternate between:

```text
CI
continuous integration
GitHub Actions
workflow
```

unless the distinction matters.

## Check technical accuracy

Documentation should not only sound good.

It should be technically correct.

When reviewing, check whether:

- commands match the current project setup,
- file names are correct,
- paths exist,
- tool names are capitalized correctly,
- examples match the repository structure,
- explanations do not promise behavior that the project does not support.

For example, this guide intentionally does not cover full Python packaging yet.

Do not describe the project as a complete PyPI packaging tutorial.

## Check whether the document is too broad

A good documentation page should usually focus on one topic.

Good topic:

```text
How to read GitHub Actions logs
```

Too broad:

```text
Everything about GitHub, CI, testing, Ruff, and Python packaging
```

If a page grows too large, consider splitting it into smaller documents.

## Check whether the reader is guided

Good documentation should reduce uncertainty.

Useful reader-friendly signals include:

- what this page covers,
- when to use this page,
- what to run,
- what the expected result is,
- what to do when something fails,
- what is intentionally not covered.

Documentation should not make the reader guess the next step.

## Check for overengineering

This guide intentionally starts small.

When reviewing documentation, watch for unnecessary complexity.

Examples of topics that should not be pushed into the foundation too early:

- Docker,
- pre-commit hooks,
- coverage gates,
- full packaging and PyPI publishing,
- release automation,
- complex CI matrices.

These topics may be useful later.

They should not distract from the first learning path.

## Check tone

The tone should be clear, practical, and beginner-friendly.

Good tone:

```text
This is common when learning.
Here is how to fix it.
```

Avoid tone like:

```text
Obviously, you should never do this.
```

The goal is to help readers build better habits, not make them feel bad.

## Self-review checklist

Before asking for review, check:

- [ ] The document has a clear purpose
- [ ] Headings are readable
- [ ] Code fences are closed
- [ ] Commands are copy-paste friendly
- [ ] Links work
- [ ] File paths are correct
- [ ] The rendered Markdown looks good on GitHub
- [ ] The change is focused
- [ ] No unrelated files are included
- [ ] The PR description explains what changed and why

Useful local checks

For documentation-only changes, code checks may not always be necessary.

However, if the repository has existing quality checks, it is still fine to run:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

At minimum, review:

```bash
git status
git diff
```

If files are staged:

```bash
git diff --staged
```

## Rule of thumb

Review Markdown as both a maintainer and a reader.

The maintainer checks correctness.

The reader checks clarity.

A good documentation change should satisfy both.