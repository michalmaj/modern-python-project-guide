"""Checks for local links in the project's Markdown documentation."""

import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

PROJECT_ROOT = Path(__file__).resolve().parents[1]

FENCE_PATTERN = re.compile(r"^\s*(?P<marker>`{3,}|~{3,})")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*#*\s*$")
LINK_PATTERN = re.compile(r"!?\[[^]]*\]\(\s*(?P<target><[^>]+>|[^)\s]+)")
EXTERNAL_TARGET_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def markdown_files() -> list[Path]:
    """Return public Markdown files maintained by the project."""
    files = [*PROJECT_ROOT.glob("*.md")]
    files.extend((PROJECT_ROOT / "docs").rglob("*.md"))
    files.extend((PROJECT_ROOT / ".github").rglob("*.md"))
    return sorted(files)


def active_markdown_lines(path: Path) -> list[tuple[int, str]]:
    """Return lines outside fenced code blocks with their line numbers."""
    active_lines: list[tuple[int, str]] = []
    fence: tuple[str, int] | None = None

    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        match = FENCE_PATTERN.match(line)

        if match:
            marker = match.group("marker")
            marker_type = marker[0]

            if fence is None:
                fence = (marker_type, len(marker))
            elif marker_type == fence[0] and len(marker) >= fence[1]:
                fence = None

            continue

        if fence is None:
            active_lines.append((line_number, line))

    return active_lines


def github_heading_slug(title: str) -> str:
    """Return the GitHub-style anchor used for a Markdown heading."""
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"[`*_~]", "", title).casefold()
    title = "".join(
        character
        for character in title
        if character.isalnum() or character in {" ", "-", "_"}
    )
    return re.sub(r"\s+", "-", title.strip())


def heading_anchors(path: Path) -> set[str]:
    """Return all heading anchors available in a Markdown file."""
    anchors: set[str] = set()
    occurrences: defaultdict[str, int] = defaultdict(int)

    for _, line in active_markdown_lines(path):
        match = HEADING_PATTERN.match(line)

        if not match:
            continue

        base_anchor = github_heading_slug(match.group("title"))
        occurrence = occurrences[base_anchor]
        occurrences[base_anchor] += 1
        anchor = base_anchor if occurrence == 0 else f"{base_anchor}-{occurrence}"
        anchors.add(anchor)

    return anchors


def test_internal_markdown_links_resolve() -> None:
    files = markdown_files()
    anchors_by_file = {path.resolve(): heading_anchors(path) for path in files}
    problems: list[str] = []

    for source in files:
        for line_number, line in active_markdown_lines(source):
            for match in LINK_PATTERN.finditer(line):
                target = match.group("target").strip("<>")

                if target.startswith("//") or EXTERNAL_TARGET_PATTERN.match(target):
                    continue

                path_text, _, fragment = target.partition("#")
                path_text = unquote(path_text.split("?", maxsplit=1)[0])
                destination = (
                    (source.parent / path_text).resolve()
                    if path_text
                    else source.resolve()
                )
                location = f"{source.relative_to(PROJECT_ROOT)}:{line_number}"

                if path_text and not destination.exists():
                    problems.append(f"{location}: missing file in {target!r}")
                    continue

                if (
                    fragment
                    and destination.suffix.lower() == ".md"
                    and unquote(fragment) not in anchors_by_file.get(destination, set())
                ):
                    problems.append(f"{location}: missing anchor in {target!r}")

    assert not problems, "Broken internal Markdown links:\n" + "\n".join(problems)
