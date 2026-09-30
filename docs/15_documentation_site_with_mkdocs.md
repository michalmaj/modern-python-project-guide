# Documentation Site with MkDocs

The Markdown files in this repository work well on GitHub. MkDocs adds a second
way to read them: a generated site with navigation, search, and a local preview.

The site is an additional view of the same source files. It does not replace the
repository README or require contributors to edit generated HTML.

## Why add a site now?

The guide now contains a complete learning path, quickstarts, troubleshooting,
and several focused references. A site makes those pages easier to explore.

MkDocs was introduced only after the Markdown sources, links, terminology, and
linting rules were already stable. This keeps the generator from hiding weak
source documentation.

## Source and generated files

MkDocs reads configuration from:

```text
mkdocs.yml
```

It reads source pages from:

```text
docs/
```

The site landing page is `docs/index.md`. The repository landing page remains
the root `README.md` because those pages serve different contexts.

The generated HTML is written to:

```text
site/
```

The `site/` directory is ignored by Git. Generated files should be rebuilt, not
committed.

## Install MkDocs

MkDocs is a development dependency, so the normal sync command installs it:

```bash
uv sync
```

No global installation is required.

## Preview the site locally

Start the development server:

```bash
uv run mkdocs serve
```

MkDocs prints the local address, normally `http://127.0.0.1:8000/`. It watches
the source files and rebuilds the preview when documentation changes.

Stop the server with `Ctrl+C`.

## Build the site strictly

Build the same way as CI:

```bash
uv run mkdocs build --strict
```

Strict mode turns warnings into failures. For this project, that includes pages
missing from navigation, invalid navigation targets, missing document links,
and missing heading anchors.

## Configuration choices

The initial setup is intentionally small:

- the built-in `mkdocs` theme,
- one explicit navigation tree,
- the built-in search plugin,
- strict validation in CI,
- no third-party plugins or custom styling.

Every source page is included in the navigation. Adding a page without updating
`mkdocs.yml` causes the strict build to fail, which keeps the site structure
deliberate.

## How this relates to other documentation checks

The documentation checks have separate responsibilities:

- `rumdl` checks Markdown structure and consistency,
- pytest checks local file links and heading anchors,
- MkDocs validates and renders the site,
- human review checks meaning, clarity, and teaching quality.

No single tool replaces the others.

## Build and deployment are separate

The `Quality checks` CI job only proves that the site can be generated. It does
not publish HTML or require deployment permissions.

After a reviewed change reaches `main`, a separate workflow publishes the
generated site. Keeping these operations separate prevents pull requests from
changing the public documentation.

## Rule of thumb

Keep Markdown useful on its own.

Use the generated site to improve navigation, search, and previewing.

## Continue

- [Previous: Markdown Linting with rumdl](14_markdown_linting.md)
- [Next: Publishing with GitHub Pages](16_publishing_with_github_pages.md)
- [Back to documentation home](index.md)
