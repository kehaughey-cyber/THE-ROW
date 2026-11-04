import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_docs import check_doc

IDS = {"S-001", "S-003"}

CLEAN = """# Doc

## Question
What?

## Findings
- [sourced] A fact. [S-003]
- [estimated] A guess.
- [assumption] A premise.

## Assumptions
- None.
"""


def test_clean_doc():
    assert check_doc(CLEAN, IDS) == []


def test_unlabeled_finding():
    text = CLEAN.replace("- [estimated] A guess.", "- A guess with no label.")
    assert len(check_doc(text, IDS)) == 1


def test_unknown_source_id():
    text = CLEAN.replace("[S-003]", "[S-999]")
    assert len(check_doc(text, IDS)) == 1


def test_tbd_word():
    text = CLEAN.replace("What?", "What is TBD?")
    assert len(check_doc(text, IDS)) == 1


def test_missing_assumptions_heading():
    text = CLEAN.replace("## Assumptions\n- None.\n", "")
    assert len(check_doc(text, IDS)) == 1


def test_main_fails_when_sources_missing(tmp_path, monkeypatch, capsys):
    import check_docs
    (tmp_path / "scripts").mkdir()
    (tmp_path / "docs").mkdir()
    monkeypatch.setattr(check_docs, "__file__", str(tmp_path / "scripts" / "check_docs.py"))
    assert check_docs.main() != 0
    assert "sources.md" in capsys.readouterr().out
