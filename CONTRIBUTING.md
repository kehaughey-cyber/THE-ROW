# Contributing to THE ROW

Several people and AI tools work on this repo. These rules keep us from overwriting each other.

## Branches and pull requests
- Each writer works on their own branch: `<name>/<short-topic>` (for example `austin/review-doc-02`). Branch from and open pull requests against `main`; do not commit directly to it. Until `main` exists (it will be created from `build/marketing-workstream` at merge), use `build/marketing-workstream` as the base.
- Use your own clone, not a shared folder. Do not have two tools editing the same working copy, and do not keep a clone inside a cloud-synced folder (OneDrive, Dropbox), because sync conflicts with git.
- Commit small and often, then open a pull request. A pull request needs the checks below to pass and a review from someone other than its author.
- AI tools follow the same rules. Any AI-assisted change names the tool in the commit message.

## Document rules (the checker enforces these)
- Every bullet under `## Findings` starts with `[sourced]`, `[estimated]` or `[assumption]`.
- A `[sourced]` bullet ends with its source id in square brackets as the last characters, for example `[S-012]`, with no period after the bracket.
- A `[sourced]` bullet states only what its source's Supports line (in `docs/sources.md`) says; put any inference in a separate `[estimated]` bullet.
- The checker reads only bullets under `## Findings`. It does not check table rows or numbered lists, so put the label on a bullet above each table (the bullet introducing the table carries the label for it).
- Each source is a heading exactly `## S-NNN` in `docs/sources.md`, followed by title, publisher, URL, `Accessed: <date>`, and one line on what it supports. Only cite pages you actually opened. Never invent a source.
- Each document keeps the three headings `## Question`, `## Findings`, `## Assumptions`. No `TBD` or `TODO`.
- ROW managers (municipalities, DOTs, commissions) are free or near-free members and carry zero revenue in the model.
- If a claim has no source, label it `[estimated]` or `[assumption]` and add it to `docs/assumptions.md`.

## Before every commit
```
py scripts/check_docs.py
py -m pytest -q
```
Use `python3` instead of `py` on Mac or Linux. Both must pass.

## What to keep out of the repo
Passwords, tokens, API keys, and personal data. Scratch work goes in a local folder that is not committed.

## Drive copies
The shared Drive folder holds readable copies of the documents. The repo is the source of truth, and each Drive copy states the repo commit it came from.
