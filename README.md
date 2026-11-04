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

## Where the research stands

- Universes of paying organizations: telecom 8,500-13,700; telecom plus electric, gas and water expansion 18,500-27,500 more; all ROW 29,000-39,000.
- Supported blended price is $5,000-$10,000 a year; the final tiers in [docs/07](docs/07-membership-pricing.md) blend to $6,020.
- Telecom beachhead: about $5-12M ARR at the final $6,020 tiers, and up to about $21M only in the $10k price, 15% penetration case ([docs/01](docs/01-exit-arr-model.md)).
- Dues alone do not reach $37.5M on telecom; $100M has no support in the research.
- Nothing has been validated with a buyer. The single biggest unknown is whether agencies (ROW managers) will contribute permit data.

## Check

Install test tools once with `pip install -r requirements-dev.txt`. Then `py scripts/check_docs.py` (exit 0 when all docs are clean); tests: `py -m pytest`.
