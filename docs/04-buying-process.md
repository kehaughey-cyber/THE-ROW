# How they buy

## Question
Who decides, what is the budget cycle, what is the procurement path?

## Findings

### How to read this document
- [assumption] Desk research dated 2026-11-04, no buyer interviews. Government budget cycles, purchasing thresholds and records law are sourced where noted. Private-company approval levels, line-item ownership and sales-cycle lengths had no public source and are marked `[estimated]` or `[assumption]`; they are the main weak spot of this document.

### Price benchmarks that frame the purchase
- [sourced] Published operator dues: NTCA general broadband providers $592-$4,036 by employee band and ILECs up to $26,906 (group maximum $67,266) [S-026]
- [sourced] Published operator dues: FBA network operators $1,200-$6,000 by subscriber count [S-027]
- [sourced] FBA Premier (board-voting) membership is $9,500 a year [S-028]
- [sourced] FBA vendor membership is $6,000 a year [S-029]
- [sourced] NATOA agency dues are $925-$2,125 by population and for-profit associate dues $1,970 (2027 schedule) [S-030]
- [sourced] A permit-data vendor publishes self-serve plans at $599 and $999 a month (about $7,200 and $12,000 a year if kept all year) with custom enterprise pricing [S-032]
- [estimated] Association dues for paying members cluster at $1,000-$10,000 a year, with only the largest ILEC groups above $25,000. Self-serve permit data runs about $7,000-$12,000 a year per small team. A membership above roughly $10,000 is therefore likely to be judged as a data/software purchase rather than as dues.

### Side 1: Operators
- [assumption] Decision path (not sourced; to be validated):

| Step | Small operator (O3) | Regional builder (O2) | National carrier / MSO (O1) |
|---|---|---|---|
| Initiates | GM/CEO or operations manager, often after a state or NTCA meeting | VP Construction, Director of Engineering or Permitting Manager | Regional ROW/deployment lead or a corporate strategy/analytics team |
| Decides | GM/CEO | COO or VP Operations | VP Network Deployment with finance partner |
| Signs | GM/CEO; board only if dues are a new budget line | COO/CFO | Procurement under delegated authority after legal, security and vendor onboarding |
| Line item | Association dues or general and administrative | Dues (membership) and engineering/operations opex (data) | Dues held by government affairs; data subscriptions by network planning, IT or procurement |

- [sourced] Dues paid to a 501(c)(6) association are subject to IRC 6033(e) notice rules: the association must tell members what share of dues goes to nondeductible lobbying or pay a proxy tax [S-044]
- [sourced] A NATOA invoice states 80% of its dues may be deductible as a business expense and 20% is non-deductible lobbying under Section 162(e), an example of how members see the split [S-031]
- [estimated] Dues are normally expensed as a business expense, so the split between "dues" and "data subscription" matters mainly for who owns the budget, not tax. Separating membership (dues) from the dashboard (subscription with an invoice and order form) lets each go to the right owner.
- [estimated] Budget timing: most operators and contractors use calendar fiscal years and set capex and opex budgets in Q3-Q4 for the next year; Dycom's fiscal year ends January 31 [S-043] and shows that not all do. Pitch new paid lines in August-October; in-year purchases need discretionary money or a pilot. Not sourced as a general rule.
- [estimated] Approval levels: under about $10,000 a year is often a manager or director card or PO purchase; $10,000-$50,000 needs VP or CFO approval; above about $50,000, or anything needing a data contribution or API, triggers procurement, legal and security review at large firms. These are typical corporate practice, not sourced.
- [estimated] Sales cycle: 1-3 months for small operators (owner decides), 3-6 months for regional builders, 6-12 months or more for national carriers when a data license, security review or vendor onboarding is involved. No public source found.

### Side 2: Contractors and engineering firms
- [assumption] Decision path (not sourced):

| Step | Local contractor (C2) | Engineering / permitting firm (C3) | National prime (C1) |
|---|---|---|---|
| Initiates | Owner or estimator | Permitting practice lead | VP Business Development or preconstruction |
| Decides | Owner | Principal or practice executive | Regional president or COO |
| Signs | Owner | Principal / CFO | CFO or procurement; legal reviews license terms |
| Line item | Dues / overhead | Overhead or billable project cost if the license allows client use | Business development budget (dues); IT/data or estimating (subscription) |

- [sourced] Large contractors earn much of their revenue under multi-year MSAs and are concentrated on a few carriers (AT&T 25.4%, Verizon 14.0%, Lumen 10.8% for Dycom in fiscal 2026) [S-043]
- [estimated] Because of that concentration, primes will ask whether their main carrier customers belong and how data is shared before joining; the operator side should be signed first in each region. Inferred, not stated by a contractor.
- [estimated] Sales cycle: under 1 month to 3 months for owner-run contractors; 2-6 months for engineering firms (license terms for client deliverables); 3-9 months for national primes. No public source found.

### Side 3: ROW managers (government)
- [sourced] 46 states begin their fiscal year on July 1; New York starts April 1, Texas September 1, and Alabama and Michigan October 1 [S-034]
- [sourced] GFOA's local budget process ends with a budget adopted by elected officials, and many local governments must hold a public hearing to approve it [S-045]
- [estimated] Local fiscal years commonly follow the state (often July 1, with October 1 and January 1 also common), so a request that needs money must be in the department's budget request several months before adoption, typically in winter or spring for a July 1 year. Local timing was not sourced.
- [sourced] Federal micro-purchase and simplified acquisition thresholds rose to $15,000 and $350,000 on October 1, 2025 (FAR 2.101), relevant to federal land agencies and to grant-funded local purchases that follow federal rules [S-033]
- [sourced] Texas raised the municipal threshold for competitive procurement from contracts over $50,000 to contracts over $100,000, effective September 1, 2025 (enrolled bill; governor action not shown in the copy reviewed) [S-035]
- [estimated] State and local thresholds vary by state and by charter; a nominal fee of about $1,000-$2,500 sits well under every threshold seen and fits the NATOA pattern, where a county paid $1,630 in dues (S-030, S-031). A free membership is not a purchase, so purchasing thresholds should not apply to it.
- [sourced] The NATOA invoice was filed in Hidalgo County's public meeting-document archive, showing that even small dues payments can appear in a governing body's public packet [S-031]
- [assumption] How a free, data-sharing membership gets approved (no public template found): (1) a ROW manager or public-works director sponsors it; (2) the city or county attorney reviews the terms of participation and any data-sharing agreement or MOU (data fields, permitted use, attribution, no exclusivity, no indemnity by the agency, termination); (3) the GIS/IT or records office approves the export method and security of location data; (4) the city or county manager signs under delegated authority, or the governing body approves it on a consent agenda if the agreement exceeds that authority or is an interlocal-style agreement; (5) a named staff owner keeps the feed current.
- [assumption] To keep approval light, the first agreement should ask only for data the agency already publishes or would release under a records request (permit type, location at street level, application and issue dates, status, fees), with no fee and no obligations beyond a periodic export.
- [sourced] Washington's Public Records Act defines a public record as any writing relating to the conduct of government, regardless of physical form, so permit data an agency holds or exchanges is generally disclosable [S-037]
- [sourced] Florida exempts the location and capacity of communications network facilities and network maps from public records, but only for information held by the state broadband office under its grant programs [S-036]
- [estimated] Records implications: (a) anything an agency sends to the association, and probably the agreement itself, is a public record the agency may have to release; (b) operator data the association shares back with an agency can become a public record once the agency holds it, unless a narrow exemption like Florida's applies; (c) the association should therefore give agencies aggregated views and avoid sending operator-identifiable build plans to government members. This is a reading of S-036 and S-037, not legal advice; each state's law differs and should be reviewed by counsel.
- [estimated] Sales cycle: 2-4 months for a large city with a ROW section and delegated signing authority; 4-12 months when a governing-body vote, a state DOT legal review or a records/security review is needed. No public source found.

### Implications for sequencing
- [estimated] Sign operators in a region first, then contractors who serve them, and ROW managers in the same region last but before the dashboard launches there; this follows from contractors' customer concentration (S-043) and the long government approval path.
- [estimated] Time paid-side proposals for August-October budget planning and government data agreements for the months before a July 1 fiscal year (S-034); a free agreement can be signed any time.

## Assumptions
- Private-company approval levels ($10k and $50k breakpoints), line-item ownership and sales-cycle lengths are typical practice, not sourced; validate in interviews.
- Membership above about $10,000 a year will be treated as a data/software purchase with procurement review.
- A free membership is not a purchase and does not trigger government purchasing thresholds; a nominal fee under about $2,500 stays below all thresholds seen.
- Free data-sharing memberships can be approved administratively (manager signature) in most large jurisdictions; some will need a governing-body vote.
- Data an agency contributes is likely a public record; the association should request only already-public fields and keep operator-identifiable data away from agencies.
- Operators should be signed before contractors in each region.
