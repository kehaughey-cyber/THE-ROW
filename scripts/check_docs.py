"""Lint the research docs: required headings, labeled findings, valid sources."""
import re
import sys
from pathlib import Path

REQUIRED = ("## Question", "## Findings", "## Assumptions")
LABELS = ("[sourced]", "[estimated]", "[assumption]")
TRAILING_ID = re.compile(r"\[(S-\d+)\]\s*$")


def _findings_bullets(text):
    bullets = []
    in_findings = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_findings = line.strip() == "## Findings"
            continue
        if in_findings and line.lstrip().startswith(("- ", "* ")):
            bullets.append(line.lstrip()[2:].strip())
    return bullets


def check_doc(text, source_ids):
    problems = []
    lines = {line.strip() for line in text.splitlines()}
    for heading in REQUIRED:
        if heading not in lines:
            problems.append(f"missing heading: {heading}")
    for word in ("TBD", "TODO"):
        if re.search(rf"\b{word}\b", text):
            problems.append(f"contains {word}")
    for bullet in _findings_bullets(text):
        if not bullet.startswith(LABELS):
            problems.append(f"unlabeled finding: {bullet}")
        elif bullet.startswith("[sourced]"):
            m = TRAILING_ID.search(bullet)
            if not m:
                problems.append(f"sourced finding lacks source id: {bullet}")
            elif m.group(1) not in source_ids:
                problems.append(f"unknown source id {m.group(1)}: {bullet}")
    return problems


def load_source_ids(path):
    if not path.exists():
        return set()
    return set(re.findall(r"^## (S-\d+)\s*$", path.read_text(encoding="utf-8"), re.M))


def main():
    docs = Path(__file__).resolve().parent.parent / "docs"
    ids = load_source_ids(docs / "sources.md")
    failed = False
    for path in sorted(docs.glob("0*.md")):
        for problem in check_doc(path.read_text(encoding="utf-8"), ids):
            print(f"{path.name}: {problem}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
