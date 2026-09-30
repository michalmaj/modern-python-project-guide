# Publishing with GitHub Pages

A strict MkDocs build proves that the documentation can be generated. GitHub
Pages makes that generated site available to readers on the web.

This project publishes the site at:

<https://michalmaj.github.io/modern-python-project-guide/>

## Build and deployment remain separate

The repository has two workflows with different responsibilities:

- `.github/workflows/ci.yml` validates every pull request and push to `main`,
- `.github/workflows/pages.yml` publishes documentation after relevant changes
  reach `main`.

A pull request therefore cannot update the public site. It must first pass the
normal review and `Quality checks` requirement. The merge commit then starts the
documentation workflow.

## One-time repository setting

The repository owner must enable GitHub Pages once:

1. Open the repository **Settings**.
2. Select **Pages** under **Code, planning, and automation**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.

The workflow does not publish from a `gh-pages` branch and does not commit the
generated `site/` directory.

## When deployment runs

The documentation workflow runs when a push to `main` changes its own workflow,
the Python version, documentation sources, MkDocs configuration, or dependency
files. It can also be started manually from the **Actions** tab.

The path filter avoids redeploying an unchanged site after unrelated source-code
changes. Manual dispatch remains available for recovery or verification.

## Build job

The `build` job recreates the site from a clean checkout:

1. check out the repository,
2. install `uv` and the configured Python version,
3. install locked development dependencies,
4. configure GitHub Pages,
5. run `uv run mkdocs build --strict`,
6. upload `site/` as a GitHub Pages artifact.

The artifact is the boundary between building and deploying. It contains the
generated static site, but it is not committed to the repository.

## Deploy job

The `deploy` job waits for the build job. It deploys the uploaded artifact to
the `github-pages` environment and reports the resulting public URL.

The workflow grants only the permissions it needs:

- `contents: read` reads repository files,
- `pages: write` creates the Pages deployment,
- `id-token: write` lets GitHub verify the deployment with OpenID Connect.

The write permissions belong only to the deploy job. The normal CI workflow
does not receive them.

## Why use an environment?

GitHub Pages deployments use the `github-pages` environment. It records
deployment history and can enforce protection rules.

The workflow also uses a `pages` concurrency group. A running production
deployment is allowed to finish instead of being cancelled by a newer run.

## Verify a deployment

After merging a documentation change:

1. open the repository **Actions** tab,
2. select the **Documentation** workflow,
3. confirm that **Build documentation** and **Deploy documentation** passed,
4. open the deployment URL shown by the deploy job,
5. verify the changed page and navigation.

The existing `Quality checks` status remains the branch-protection requirement.
Deployment happens after merge, so a deployment failure should be fixed with a
new pull request rather than by weakening that requirement.

## Public output and secrets

Everything in the generated site is public. Documentation sources and build
configuration must not contain credentials, private notes, or other sensitive
information.

This workflow needs no repository secrets. GitHub supplies a short-lived token
with the declared permissions.

## Custom domains are separate

This project uses the default `github.io` address. A custom domain would require
additional DNS and repository settings and is intentionally outside this setup.

## Rule of thumb

Validate on pull requests. Publish only from the protected default branch.

Keep generated files out of Git and deploy a reproducible artifact instead.

## Continue

- [Previous: Documentation Site with MkDocs](15_documentation_site_with_mkdocs.md)
- [Next: Project Checklist](09_checklist.md)
- [Back to documentation home](index.md)
