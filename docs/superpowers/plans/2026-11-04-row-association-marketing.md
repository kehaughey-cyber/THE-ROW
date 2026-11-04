# THE ROW Marketing Workstream Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the shared repo and Drive folder, then produce the seven marketing documents with every claim labeled and an exit/ARR model that is revised as research lands.

**Architecture:** A markdown repo is the source of truth. A small Python ARR model (`model/arr_model.py`) holds the exit math, and a small linter (`scripts/check_docs.py`) enforces the spec's claim-labeling rule. Drive holds readable copies, exported from the repo.

**Tech Stack:** Git/GitHub (`gh`), Python 3 + pytest, markdown, Google Drive (via Chrome, because the Drive connector cannot see the folder).

**Spec:** `docs/superpowers/specs/2026-11-04-row-association-marketing-design.md`

## Global Constraints

- Exit target: $300-500M valuation in 5-10 years, driven by subscriptions, memberships, and value-adds.
- Revenue multiple range under test: 5-8x, implying roughly $40-100M ARR (placeholder until the model tests it).
- Market: ROW infrastructure; telecom is the beachhead (fiber, cable, wireless/small cell, towers); electric, gas, water, and other ROW occupants are the expansion.
- Three member sides from launch: operators, contractors and engineering firms, ROW managers (municipalities, DOTs, utility commissions).
- Commercial model: ROW managers join free or near-free in exchange for data; operators and contractors pay.
- The association is a neutral convener.
- Every claim is labeled `[sourced]`, `[estimated]`, or `[assumption]`. Sourced claims point to an entry in `docs/sources.md` with a date accessed.
- Repo is private on GitHub. Drive copies are exports; the repo is the source of truth.
- Out of scope: five-pillars and 7S frameworks, product build, legal entity formation.

## Review Focus

1. A member count for ROW managers reaching the revenue total: they are free or near-free, so the model must count them as zero ARR.
2. A revenue multiple of zero or negative, or an exit value of zero: the model must reject it, not return infinity or a negative ARR.
3. A finding with no label, or a `[sourced]` claim with no source entry: the linter must flag it.
4. Placeholder text (`TBD`, `TODO`) left in a finished document: the linter must flag it.
5. Drive copies drifting from the repo: each Drive copy states the repo commit it was exported from.

## File Structure

```
README.md
.gitignore
docs/01-exit-arr-model.md ... docs/07-membership-pricing.md
docs/sources.md
docs/assumptions.md
model/arr_model.py
scripts/check_docs.py
tests/test_arr_model.py
tests/test_check_docs.py
```

---

### Task 1: Doc linter and repo scaffold

**Files:**
- Create: `scripts/check_docs.py`, `tests/test_check_docs.py`, `README.md`, `.gitignore`, `docs/sources.md`, `docs/assumptions.md`, `docs/01-exit-arr-model.md` through `docs/07-membership-pricing.md`

**Interfaces:**
- Produces: `check_doc(text: str, source_ids: set[str]) -> list[str]` returning one problem string per violation (empty list means clean). A document must contain `## Question`, `## Findings`, `## Assumptions`. Every bullet under `## Findings` must start with `[sourced]`, `[estimated]`, or `[assumption]`. A `[sourced]` bullet must end with a source id in square brackets, such as `[S-003]`, that is in `source_ids`. The words `TBD` and `TODO` are problems anywhere.
- Produces: `python scripts/check_docs.py` checks every `docs/0*.md` file and exits non-zero if any problem is found. `source_ids` come from the headings in `docs/sources.md` that look like `## S-003`.

- [ ] **Step 1: Write failing tests in `tests/test_check_docs.py`.** Cases: a clean doc returns `[]`; an unlabeled finding returns one problem; a `[sourced]` finding citing `[S-999]` not in `source_ids` returns one problem; a doc containing `TBD` returns one problem; a doc missing `## Assumptions` returns one problem.
- [ ] **Step 2: Run** `python -m pytest tests/test_check_docs.py -v`. Expected: FAIL (module not found).
- [ ] **Step 3: Implement `check_doc` and the CLI in `scripts/check_docs.py`.** Plain string and regex handling, standard library only.
- [ ] **Step 4: Run the tests.** Expected: all PASS.
- [ ] **Step 5: Create the scaffold.** `README.md` states the concept, links the spec and plan, and lists the seven documents. Each of the seven docs holds the three required headings with the question from the spec's deliverables table under `## Question` and a single `[assumption]` bullet saying the research has not been done. `docs/sources.md` and `docs/assumptions.md` hold a header and nothing else. `.gitignore` covers `__pycache__/`, `.pytest_cache/`, `.venv/`.
- [ ] **Step 6: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 7: Commit** `scaffold repo and doc linter`.

### Task 2: ARR model (document 01, first pass)

**Files:**
- Create: `model/arr_model.py`, `tests/test_arr_model.py`
- Modify: `docs/01-exit-arr-model.md`

**Interfaces:**
- Produces: `required_arr(exit_value: float, revenue_multiple: float) -> float`; raises `ValueError` if either argument is `<= 0`.
- Produces: `Segment(name: str, members: int, annual_price: float, pays: bool)` as a dataclass.
- Produces: `arr(segments: list[Segment]) -> float`, the sum of `members * annual_price` for segments where `pays` is true.
- Produces: `members_needed(target_arr: float, annual_price: float) -> int`, rounded up; raises `ValueError` if `annual_price <= 0`.

- [ ] **Step 1: Write failing tests.** `required_arr(300e6, 8) == 37.5e6`; `required_arr(500e6, 5) == 100e6`; `required_arr(300e6, 0)` raises `ValueError`; `required_arr(0, 5)` raises `ValueError`; `arr` of `[Segment("ROW managers", 2000, 0.0, False), Segment("Operators", 100, 50_000.0, True)]` equals `5_000_000.0`; a free segment with a nonzero price and `pays=False` still contributes `0`; `members_needed(1_000_000, 30_000) == 34`.
- [ ] **Step 2: Run** `python -m pytest tests/test_arr_model.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement the four interfaces in `model/arr_model.py`.**
- [ ] **Step 4: Run the tests.** Expected: all PASS.
- [ ] **Step 5: Fill `docs/01-exit-arr-model.md`.** A table of required ARR at multiples 5, 6, 7, and 8 against exit values $300M, $400M, and $500M, computed with `required_arr`. Each cell is `[estimated]`. A second table of members needed at three illustrative annual prices ($15k, $30k, $60k), each marked `[assumption]`. State that ROW managers carry zero ARR.
- [ ] **Step 4b: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 5b: Commit** `first-pass exit and ARR model`.

### Task 3: Private GitHub repo and contributor access

**Files:** none (remote setup).

**Interfaces:** Consumes the committed local repo from Tasks 1-2.

- [ ] **Step 1: Confirm with the user before creating anything on GitHub.** Ask for the repo name (default `the-row`) and confirm the account to create it under.
- [ ] **Step 2: Check** `gh auth status`. If not logged in, stop and ask the user to run `gh auth login`; do not enter credentials.
- [ ] **Step 3: Run** `gh repo create <name> --private --source . --push`. Expected: repo created, `main` pushed.
- [ ] **Step 4: Verify** `gh repo view --json visibility`. Expected: `PRIVATE`.
- [ ] **Step 5: Add the contributor, once the user has supplied their GitHub username:** `gh api -X PUT repos/<owner>/<name>/collaborators/<username> -f permission=push`. Confirm with the user before sending the invite. Until the username arrives, skip this step and say so in the status note.

### Task 4: Drive folder: Start Here doc and sharing

**Files:** none in the repo.

**Interfaces:** Consumes the README text. The Drive connector cannot see the folder, so this runs in the user's Chrome (Claude in Chrome), in the folder `https://drive.google.com/drive/folders/1C2Ml7t_Q3Rk-h-srKPbpDFg5wKC-8BaJ` ("ROW The foundation", owned by kehaughey@gmail.com).

- [ ] **Step 1: Open the folder in a new tab and create a Google Doc named `THE ROW - Start Here`.** Its content is the README's concept summary plus the line `Exported from repo commit <short hash>`. Do not touch the existing `Ping.docx`.
- [ ] **Step 2: Share the folder with austin.anderson216@gmail.com as Editor.** Confirm with the user in chat before clicking Share; the email is already confirmed by the user.
- [ ] **Step 3: Verify** by reading the folder's sharing panel. Expected: the contributor is listed as Editor.
- [ ] **Step 4: Close the tab you opened.**

### Task 5: Market definition and sizing (document 02)

**Files:**
- Modify: `docs/02-market-sizing.md`, `docs/sources.md`, `docs/assumptions.md`, `docs/01-exit-arr-model.md`

- [ ] **Step 1: Research** the telecom ROW beachhead (counts of operators, contractors, and ROW-managing jurisdictions in the US; annual build and permit activity; ROW-related spend) and the expansion segments (electric, gas, water). Use the deep-research skill. Each fact gets a source entry (`## S-00N`, title, URL, date accessed).
- [ ] **Step 2: Write `docs/02-market-sizing.md`.** Include a bottom-up count of potential members per side and a rough annual spend pool addressable by the dashboard. Every finding bullet carries a label; `[sourced]` bullets cite `[S-00N]`.
- [ ] **Step 3: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 4: Update document 01.** Replace the illustrative member counts with the counts from document 02, and state whether the required ARR looks reachable.
- [ ] **Step 5: Commit** `market sizing and model update`.

### Task 6: Customer archetypes and buying process (documents 03 and 04)

**Files:**
- Modify: `docs/03-archetypes.md`, `docs/04-buying-process.md`, `docs/sources.md`, `docs/assumptions.md`, `docs/01-exit-arr-model.md`

- [ ] **Step 1: Research** the operator, contractor, and ROW-manager buyers: typical titles, who holds budget, how association memberships and data subscriptions are approved, budget cycles, and procurement rules for government members (including what lets a government agency join free).
- [ ] **Step 2: Write document 03:** two to four archetypes per side, each with role, pain, and what they would pay for. Write document 04: the decision path for each side.
- [ ] **Step 3: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 4: Update document 01** with a realistic annual price per paying side if the research supports one.
- [ ] **Step 5: Commit** `archetypes and buying process`.

### Task 7: Competitive landscape (document 05)

**Files:**
- Modify: `docs/05-competitive-landscape.md`, `docs/sources.md`, `docs/assumptions.md`

- [ ] **Step 1: Research** existing trade associations, data vendors, and permit or ROW-management platforms serving these three sides. Record membership models, pricing where public, and what each does not do (especially prediction).
- [ ] **Step 2: Write document 05** as a comparison table plus a short statement of the gap. All claims labeled.
- [ ] **Step 3: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 4: Commit** `competitive landscape`.

### Task 8: Value proposition and positioning (document 06)

**Files:**
- Modify: `docs/06-value-proposition.md`, `docs/assumptions.md`

- [ ] **Step 1: Write document 06** from documents 03-05: one value proposition per member side, the neutral-convener positioning statement, and why a member would pay for predictions. Each claim traces to a finding in an earlier document.
- [ ] **Step 2: Run** `python scripts/check_docs.py`. Expected: exit 0.
- [ ] **Step 3: Commit** `value proposition and positioning`.

### Task 9: Membership and pricing tiers (document 07) and final model revision

**Files:**
- Modify: `docs/07-membership-pricing.md`, `docs/01-exit-arr-model.md`

- [ ] **Step 1: Write document 07:** tiers per side. ROW managers free or near-free in exchange for data contribution; operator and contractor tiers priced using documents 03-06.
- [ ] **Step 2: Re-run the model with the final tiers.** State how many paying members the exit target requires and whether the research says that is achievable. List which assumptions in `docs/assumptions.md` are still unvalidated.
- [ ] **Step 3: Run** `python scripts/check_docs.py` and `python -m pytest`. Expected: exit 0 and all tests PASS.
- [ ] **Step 4: Commit and push.** Export each document into the Drive folder as a Google Doc stamped with the commit hash, following Task 4's method.
