# Exit & ARR model

## Question
What must we reach, with how many members at what price?

## Findings
- [estimated] Required ARR by exit value (rows) and revenue multiple (columns), in $M, computed as exit value divided by multiple:

| Exit value | 5x | 6x | 7x | 8x |
|---|---|---|---|---|
| $300M | 60.0 | 50.0 | 42.9 | 37.5 |
| $400M | 80.0 | 66.7 | 57.1 | 50.0 |
| $500M | 100.0 | 83.3 | 71.4 | 62.5 |

- [estimated] The founder's $300-500M exit target at 5-8x revenue implies roughly $37.5M to $100M of ARR; the table above gives each combination.
- [assumption] Illustrative and superseded by the price research below: members needed at three annual prices ($15k, $30k, $60k) for target ARR of $37.5M (low end), $50M (mid), and $100M (high end), rounded up:

| Target ARR ($M) | $15k | $30k | $60k |
|---|---|---|---|
| 37.5 | 2,500 | 1,250 | 625 |
| 50.0 | 3,334 | 1,667 | 834 |
| 100.0 | 6,667 | 3,334 | 1,667 |

- [assumption] ROW managers are free or near-free and carry zero ARR; a segment that does not pay contributes 0 even if it has a nonzero list price. Only paying members count toward the figures above.
- [assumption] The annual prices of $15k, $30k, and $60k are illustrative, not validated against willingness to pay.
- [estimated] Potential member counts from document 02 (market sizing), replacing the earlier illustrative counts:

| Side | Potential members | Pays? |
|---|---|---|
| Telecom operators (unique) | 2,000-3,000 | yes |
| Telecom contractors and engineering firms | 6,500-10,700 | yes |
| Telecom paying universe | 8,500-13,700 | yes |
| ROW managers (counties, municipalities, townships, DOTs, commissions) | ~38,840 total; 5,000-10,000 active | no (zero ARR) |
| Expansion paying universe (electric, gas, water operators and contractors; build-up in document 02) | 18,500-27,500 | yes |
| All-ROW paying universe (corrected for NAICS 237130 being split across both sides) | 29,000-39,000 | yes |

- [estimated] Illustrative and superseded: share of the paying universe that must join to hit target ARR, computed as members needed (table above) divided by the low and high universe counts:

| Target ARR ($M) | Universe | $15k | $30k | $60k |
|---|---|---|---|---|
| 37.5 | Telecom only | 18-29% | 9-15% | 5-7% |
| 50.0 | Telecom only | 24-39% | 12-20% | 6-10% |
| 100.0 | Telecom only | 49-78% | 24-39% | 12-20% |
| 37.5 | All ROW | 6-9% | 3-4% | 2% |
| 50.0 | All ROW | 9-11% | 4-6% | 2-3% |
| 100.0 | All ROW | 17-23% | 9-11% | 4-6% |

- [estimated] Illustrative and superseded: telecom beachhead ARR, computed as universe x penetration x average price, with penetration of 10-15% (the ceiling assumed below):

| Average price | 8,500 at 10% | 8,500 at 15% | 13,700 at 10% | 13,700 at 15% |
|---|---|---|---|---|
| $15k | $12.8M | $19.1M | $20.6M | $30.8M |
| $30k | $25.5M | $38.3M | $41.1M | $61.7M |

- [estimated] First-pass view, superseded by the price research below: the arithmetic in the three illustrative tables above ($15k, $30k, $60k) is kept only to show how penetration scales with price. At $30k, $37.5M on telecom alone needs 9-15% of the telecom universe, and $100M needs 24-39%, well above the 15% ceiling. With the electric, gas and water expansion, $100M needs 9-11% of a 29,000-39,000 universe at $30k, or 17-23% at $15k. These prices are illustrative, not supported: the price research below finds a blended price of about $5,000-$10,000, not $15,000 or $30,000, and the telecom beachhead is about $4-21M across the $5k-$10k band (the $21M top is the $10k/15% case); about $5-12M at the final $6,020 tiers.
- [estimated] Realistic annual price per paying side, from document 04's published comparables (NTCA, FBA, NATOA dues and a public permit-data price list): operators pay about $1,000-$10,000 for association membership (only the largest ILEC groups pay above $25,000), contractors and engineering firms about $2,000-$6,000; a membership that includes the dashboard is plausibly $8,000-$18,000 for the firms that take it (basis in the next bullet). A blended average across paying members of about $5,000 (membership-led) to $10,000 (dashboard-led) is what the research supports; $15,000 needs most members to buy the dashboard, and $30,000+ applies only to an enterprise tier for the largest carriers and primes. No willingness-to-pay data exists; these are list-price comparables.
- [estimated] Basis of the $8,000-$18,000 figure: it is dues plus a data product, added, with the endpoints chosen by judgment. Low end: about $1,000 of association dues (the bottom of the $1,000-$10,000 dues cluster in document 04) plus the $7,200 Shovels Basic plan, about $8,000. High end: about $6,000 of dues (FBA vendor dues and the top of FBA operator dues) plus the $12,000 Shovels Pro plan, about $18,000. It is a judgment because a membership that bundles a dashboard is not a product anyone sells today, so no price is published for it, and the bundle is assumed to cost about what the two parts cost separately.
- [estimated] Basis of the blend of $5,000 (membership-led) to $10,000 (dashboard-led): judgment, not a computed average. $5,000 is near the middle of the $1,000-$10,000 dues cluster, which is what a base of mostly small members who buy newsletter, meetings and a light view would pay. $10,000 is a base in which about half the members take the dashboard at $8,000-$18,000 and the rest pay dues below $5,000. The final tiers in document 07 give a computed blend of $6,020, inside this band.
- [estimated] Members needed and telecom ARR at the research-supported averages, computed with model/arr_model.py (members_needed, and arr with ROW managers as a zero-ARR segment):

| Target ARR ($M) | $5k | $10k | $15k |
|---|---|---|---|
| 37.5 | 7,500 | 3,750 | 2,500 |
| 50.0 | 10,000 | 5,000 | 3,334 |
| 100.0 | 20,000 | 10,000 | 6,667 |

| Average price | 8,500 at 10% | 8,500 at 15% | 13,700 at 10% | 13,700 at 15% |
|---|---|---|---|---|
| $5k | $4.3M | $6.4M | $6.9M | $10.3M |
| $10k | $8.5M | $12.8M | $13.7M | $20.6M |

- [estimated] At research-supported prices the telecom beachhead is about $4-21M across the $5k-$10k band (the $21M top is the $10k/15% case); about $5-12M at the final $6,020 tiers, and $37.5M needs 3,750 members at $10k (27-44% of the telecom universe, 10-13% of the all-ROW universe). The $300-500M exit therefore depends on the electric, gas and water expansion and on an enterprise data tier well above association-dues levels; membership dues alone do not get there.

### Final model with the tiers from document 07
- [estimated] Blended price from the final tiers, computed with model/arr_model.py (arr over 1,000 paying members, ROW managers as a zero-ARR segment): $6,020 per paying member. The comparison prices are $10,000 and $5,000.
- [estimated] Members and penetration needed, computed with members_needed, penetration being members divided by the universe high and low counts (all ROW 29,000-39,000; telecom only 8,500-13,700):

| Target ARR ($M) | Price | Members needed | Penetration, all ROW | Penetration, telecom only |
|---|---|---|---|---|
| 100.0 | $10,000 | 10,000 | 26-34% | 73-118% |
| 100.0 | $6,020 (final tiers) | 16,612 | 43-57% | 121-195% |
| 100.0 | $5,000 | 20,000 | 51-69% | 146-235% |
| 37.5 | $10,000 | 3,750 | 10-13% | 27-44% |
| 37.5 | $6,020 (final tiers) | 6,230 | 16-21% | 45-73% |
| 37.5 | $5,000 | 7,500 | 19-26% | 55-88% |

- [estimated] The 15% ceiling from the assumptions is the comparison line. Only $37.5M at $10,000 on the all-ROW universe (10-13%) is under it. $37.5M at the final blend on all-ROW is 16-21%, just over it. $100M is over the ceiling on every row, and on telecom only a penetration above 100% means the target cannot be reached from that universe at that price at all.
- [estimated] ARR at the 15% ceiling and the final $6,020 blend: telecom only $7.7M (8,500) to $12.4M (13,700); all ROW $26.2M (29,000) to $35.2M (39,000). At 10% penetration: telecom $5.1M-$8.2M, all ROW $17.5M-$23.5M. Even the all-ROW universe at the ceiling is below $37.5M with these tiers.
- [estimated] Blended price that would be needed at 15% penetration, from target ARR divided by 15% of the universe: $37.5M needs $18,248-$29,412 on telecom only and $6,410-$8,621 on all ROW; $100M needs $48,662-$78,431 on telecom only and $17,094-$22,989 on all ROW.
- [estimated] What must be true for each exit case, stated plainly: dues-only does not reach $37.5M on telecom alone. At any price the research supports ($5,000-$10,000) that case needs 27-88% of the telecom universe, against a 15% ceiling and a telecom beachhead of about $4-21M across the $5k-$10k band (the $21M top is the $10k/15% case); about $5-12M at the final $6,020 tiers. The $37.5M case (a $300M exit at 8x) needs the electric, gas and water expansion and a blended price of about $6,400-$8,600 at 15% of 29,000-39,000 members, which means more enterprise accounts or a larger predictive take rate than document 07 assumes. The $100M case (a $500M exit at 5x) needs a blended price of about $17,000-$23,000 on the all-ROW universe at the ceiling, which only holds if data subscriptions, licensing and enterprise accounts, not dues, are most of the revenue; the research found no evidence that buyers pay that.
- [estimated] Does the research say this is achievable? Not from dues. It says the telecom beachhead is about $4-21M across the $5k-$10k band (the $21M top is the $10k/15% case); about $5-12M at the final $6,020 tiers, plausible against published comparables. $37.5M is not shown to be reachable: it needs the expansion and a blend of about $6,400-$8,600 (above the $6,020 the document 07 tiers give), and it fits under the 15% ceiling only at a $10k blend. It has no support for $100M. All price and mix inputs are unvalidated.
- [assumption] The assumptions still unvalidated are listed in docs/assumptions.md; none of them has been tested with a buyer, and the willingness-to-pay, enterprise-tier and data-contribution assumptions (the sections for documents 03, 06 and 07) matter most to these figures.

## Assumptions
- Exit value range is $300M to $500M and the revenue multiple range is 5x to 8x, per the founder's target.
- ARR is all subscription revenue from paying members; ROW managers are excluded.
- The first two price tables use illustrative prices; the final model section uses the tiers in document 07, which are proposals and not validated willingness to pay.
- Member counts come from document 02 and rest on its assumptions (establishment-to-firm ratio, telecom share of NAICS 237130, overlap between associations).
- Penetration above roughly 15% of a paying universe is treated as unrealistic for a new association; this has not been benchmarked.
