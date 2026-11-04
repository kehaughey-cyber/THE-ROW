# THE ROW

Marketing research for a neutral trade association serving right-of-way (ROW) infrastructure, starting with a telecom beachhead. The repo holds the research documents and a linter that enforces labeled, sourced findings.

- Spec: [docs/superpowers/specs/2026-11-04-row-association-marketing-design.md](docs/superpowers/specs/2026-11-04-row-association-marketing-design.md)
- Plan: [docs/superpowers/plans/2026-11-04-row-association-marketing.md](docs/superpowers/plans/2026-11-04-row-association-marketing.md)

## Documents

1. [Exit & ARR model](docs/01-exit-arr-model.md)
2. [Market definition & sizing](docs/02-market-sizing.md)
3. [Customer archetypes](docs/03-archetypes.md)
4. [How they buy](docs/04-buying-process.md)
5. [Competitive landscape](docs/05-competitive-landscape.md)
6. [Value proposition & positioning](docs/06-value-proposition.md)
7. [Membership & pricing tiers](docs/07-membership-pricing.md)

Supporting: [sources](docs/sources.md), [assumptions](docs/assumptions.md).

## Check

`py scripts/check_docs.py` (exit 0 when all docs are clean); tests: `py -m pytest`.
