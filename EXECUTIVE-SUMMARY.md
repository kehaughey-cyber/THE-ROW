# THE ROW: Executive Summary

Status as of 2026-11-04. Repo state: `main` and `build/marketing-workstream` both at commit `849d79f`.

## 1. What this is

A trade association for right-of-way (ROW) infrastructure. Products: a newsletter, semi-annual meetings, and a Bloomberg-style dashboard that adds predictions to current and historical data. Exit target: $300-500M in 5-10 years, from subscriptions, memberships and value-adds. The work is built backwards from that exit.

Agreed decisions:
- Telecom is the beachhead; expand to all ROW infrastructure later.
- Three member sides: operators, contractors and engineering firms, ROW managers.
- ROW managers (municipalities, DOTs, commissions) join free or near-free in exchange for data. They carry zero revenue in the model.
- Approach: an exit/ARR model sets hypotheses, and the research tests them. Every claim is labeled [sourced], [estimated] or [assumption].

## 2. What the research found

- **The exit needs a lot of revenue.** A $300-500M exit at a 5-8x revenue multiple needs roughly $37.5M to $100M of annual recurring revenue (ARR).
- **Telecom alone does not get there.** At the final tiers (blended price about $6,020 per paying member) telecom gives about $5-12M ARR. Across the $5k-$10k price band the range is about $4-21M; the top figure assumes $10k average price and 15% of telecom joining.
- **$37.5M is not shown to be reachable on dues alone.** Even at 15% of the whole ROW market, the final tiers give $26-35M.
- **$100M has no support yet.** It would take about 10,000 paying members at $10k.
- **Nothing has been tested with a real buyer.** The biggest unknown is whether agencies will contribute data.
- **Two selling points are less unique than assumed.** Competitors already offer prediction (CostQuest, Shovels) and a three-sided membership (Common Ground Alliance).

Implication: the case for the exit has to rest on more than membership dues. Data and dashboard subscriptions, expansion beyond telecom, and add-ons are where the research should push next.

## 3. The seven documents

| # | Document | Question it answers |
|---|---|---|
| 1 | `docs/01-exit-arr-model.md` | What must we reach, with how many members at what price? |
| 2 | `docs/02-market-sizing.md` | How big are the telecom beachhead and the wider ROW market? |
| 3 | `docs/03-archetypes.md` | Who are the operator, contractor and ROW-manager buyers? |
| 4 | `docs/04-buying-process.md` | Who decides, what is the budget cycle, what is the procurement path? |
| 5 | `docs/05-competitive-landscape.md` | How do existing associations, data vendors and permit platforms compare? |
| 6 | `docs/06-value-proposition.md` | Why join, why pay, why trust a neutral convener? |
| 7 | `docs/07-membership-pricing.md` | What does each side get and pay? |

Supporting files: `docs/sources.md` (80 sources, headings `## S-NNN`) and `docs/assumptions.md` (open assumptions).

## 4. Where everything is

**Local (Kevin's machine)**
- Repo folder: `C:\Users\Dad\OneDrive\Desktop\Active\THE ROW` (inside OneDrive; other writers should use their own clone, not this folder).
- Spec: `docs/superpowers/specs/2026-11-04-row-association-marketing-design.md`
- Plan: `docs/superpowers/plans/2026-11-04-row-association-marketing.md` (contains personal Gmail addresses and the Drive folder id; fine while the repo is private).
- Model and checks: `model/arr_model.py`, `tests/`, `scripts/check_docs.py`.
- Team rules: `CONTRIBUTING.md`. Orientation: `README.md`.
- Build record (git-ignored, local only): `.superpowers/sdd/2026-11-04-row-association-marketing/progress.md` (ledger and all rulings), plus task briefs and reports. `drafts/` there holds another tool's unreviewed drafts of docs 05-07, kept but not committed.
- Full conversation transcript: `C:\Users\Dad\.claude\projects\C--Users-Dad-OneDrive-Desktop-Active-THE-ROW\43134f4d-9234-4da0-8911-3a7fb61994b9.jsonl`

**GitHub**
- Private repo: https://github.com/kehaughey-cyber/THE-ROW
- Default branch: `main`. Work branch `build/marketing-workstream` is at the same commit.
- Local `master` is a stale leftover holding only the spec and plan.
- Collaborator: Austin (`Austin-IAnderson`), invited; acceptance pending.

**Google Drive** (kehaughey@gmail.com)
- Shared folder "ROW The foundation": https://drive.google.com/drive/folders/1C2Ml7t_Q3Rk-h-srKPbpDFg5wKC-8BaJ
- Readable Word copies, moved into it on 2026-11-04: "THE ROW - doc copies (repo 849d79f)": https://drive.google.com/drive/folders/1FGFGdE_eS1cSQhisDG6g7viyF6b89lup
- That folder holds 10 .docx files (Start Here, docs 01-07, Sources, Assumptions), each stamped with the repo commit. The repo is the source of truth; Drive copies are exports.

## 5. Working rules (from CONTRIBUTING.md)

- One branch per writer, `<name>/<topic>`, branched from `main`, merged by pull request with a review from someone other than the author.
- Each writer uses their own clone, not a shared or cloud-synced folder.
- Before every commit run `py scripts/check_docs.py` and `py -m pytest -q` (use `python3` on Mac or Linux). As of `849d79f` the checker is clean and 21 tests pass.
- Every bullet under `## Findings` is labeled; [sourced] bullets end with a source id like `[S-012]` and state only what that source supports.
- No passwords, tokens, keys or personal data in the repo.

## 6. Open items

1. Austin accepts the GitHub invite; then confirm he shows as a collaborator with write access.
2. A stray test doc, `zz-dollar-test`, is still in the Drive copies folder; trash it by hand.
3. Only 06 and 07 of the 10 Drive copies were opened and checked; the others may have awkward table wrapping.
4. Two wording defects in `docs/05-competitive-landscape.md`: the NATOA conference/webinar/newsletter claim is labeled [sourced] but S-030 does not cover it, and "Shovels self-serve plans from $599" conflicts with S-032, which lists a free plan.
5. Existing clones (including GPT's) need `git fetch` and a switch to `main`.
6. Optional, owner only: GitHub branch protection on `main`, and a separate clone for GPT.
7. Next research step: test the data-contribution assumption with real ROW managers, and look for revenue beyond dues.
