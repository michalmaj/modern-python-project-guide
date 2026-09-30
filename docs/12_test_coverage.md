# Test Coverage with pytest-cov

Test coverage measures which parts of the source code run while the test suite
is executing.

It can reveal code that no test reaches, but it cannot prove that the tests make
the right assertions.

## Coverage is a diagnostic tool

A coverage report helps answer questions such as:

- Which source lines ran during the tests?
- Which branches of a condition were exercised?
- Is there production code that the test suite never reaches?

It does not answer:

- Are the assertions correct?
- Are important requirements missing?
- Are the tests readable and maintainable?
- Is the program design good?

Coverage provides evidence about test execution, not a complete quality score.

## Add pytest-cov

This project uses pytest-cov to collect coverage while pytest runs. It is a
development dependency:

```bash
uv add --group dev pytest-cov
```

The package is not needed by users of `text-toolkit`.

## Configure coverage

Coverage.py reads its settings from `pyproject.toml`:

```toml
[tool.coverage.run]
branch = true
source = ["text_toolkit"]

[tool.coverage.report]
show_missing = true
```

The settings mean:

- `source` limits measurement to the example package,
- `branch` records possible paths through conditions,
- `show_missing` lists source lines that did not run.

Tests themselves are not included in the percentage. The report measures the
package behavior that the tests exercise.

## Statement and branch coverage

Statement coverage checks whether executable statements ran.

Branch coverage also checks different paths through decisions. For example, an
`if` statement may execute both its true and false branches. Running the line
with the `if` is not enough to prove that both paths were exercised.

The example package has a condition in `count_words`. Tests cover both an empty
input and text containing words, so both outcomes are represented.

## Run the coverage report

Run:

```bash
uv run pytest --cov=text_toolkit --cov-report=term-missing
```

pytest still runs the same tests. pytest-cov additionally records execution and
prints a table similar to:

```text
Name                             Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------
src/text_toolkit/__init__.py         2      0      0      0   100%
src/text_toolkit/text_stats.py      11      0      4      0   100%
----------------------------------------------------------------------------
TOTAL                               13      0      4      0   100%
```

The important columns are:

- `Stmts`: executable statements found,
- `Miss`: statements that did not run,
- `Branch`: branch destinations found,
- `BrPart`: partially covered branches,
- `Missing`: source line numbers that did not run.

The exact counts will change when the package changes.

## Coverage in CI

The `Quality checks` job runs the same command:

```bash
uv run pytest --cov=text_toolkit --cov-report=term-missing
```

The report is visible in the GitHub Actions log. CI fails when tests or coverage
collection fail, but it does not fail because the percentage decreases.

## Why there is no percentage gate

This project intentionally does not configure `fail_under`.

A fixed threshold can encourage tests written only to increase a number. A
suite can reach 100% coverage while using weak assertions or missing important
requirements.

The current report happens to show 100%, but that is a property of a very small
example package. It is not a promise that every future change must preserve a
perfect score.

When coverage decreases, inspect the missing lines and decide whether they
represent meaningful untested behavior. Do not add a test merely to satisfy a
percentage.

## Generated data

Coverage.py stores local measurement data in:

```text
.coverage
```

This file is generated and listed in `.gitignore`. Do not commit it.

## Rule of thumb

Use coverage to find questions worth asking about the test suite.

Do not use the percentage as a substitute for those questions.

## Continue

- [Previous: Static Type Checking with mypy](11_type_checking_with_mypy.md)
- [Next: `pre-commit` Hooks](13_pre_commit_hooks.md)
- [Back to documentation home](index.md)
