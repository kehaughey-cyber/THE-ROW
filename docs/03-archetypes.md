# Customer archetypes

## Question
Who are the operator, contractor, and ROW-manager buyers?

## Findings

### How to read this document
- [assumption] This is desk research dated 2026-11-04 with no customer interviews. Sourced bullets give the public evidence (pain reports, job descriptions, published dues). The archetype tables are hypotheses built on that evidence: titles, budget owners, information sources and willingness to pay must be validated in interviews before they are used for pricing or sales targets.
- [assumption] Weak spots: no source was found that ranks operator or contractor pains by frequency or cost, gives buyer titles for association or data purchases, or shows what ROW data subscriptions sell for outside a single public price list (S-032). Pain evidence comes mostly from operator trade groups with a policy agenda (S-038, S-039).

### Evidence on pains shared across sides
- [sourced] USTelecom told the FCC (July 2025) that permit approvals range from a few days to more than a year, 8 weeks to 6 months in New York, and that timelines vary between reviewers in the same community and among neighboring jurisdictions [S-038]
- [sourced] The same filing reports permitting fees of $30,000-$50,000 per project in some municipalities for one large provider, gross-revenue ROW fees in Utah and Montana, and survey costs above $40,000 in one Florida city [S-038]
- [sourced] The Fiber Broadband Association describes permitting across states as complex and inconsistent, with weak communication between applicants and agencies and paper-based processes (September 2025) [S-039]
- [sourced] Federal small-cell rules upheld in City of Portland v. FCC set 60-day and 90-day shot clocks and fee safe harbors of $500 for up to five facilities, $1,000 per new pole and $270 per facility per year [S-040]
- [estimated] ROW managers work inside these federal limits, which cap the fees and time they can set for small cells.
- [estimated] The cross-side pain is variance and opacity: operators and contractors cannot predict how long or how much a permit will take, and jurisdictions cannot see what is coming. This is the strongest public evidence for a dashboard with historical and predicted permit timing, but it is advocacy-sourced and needs interview confirmation.

### Side 1: Operators (pay)
- [sourced] Existing association dues for operators scale with size: NTCA charges ILECs $5.28 per in-area broadband subscription (minimum $538, maximum $26,906) and general broadband providers $592-$4,036 by employee band [S-026]
- [sourced] Fiber Broadband Association network-operator dues are $1,200, $2,250 or $6,000 a year by subscriber count in North America [S-027]
- [sourced] FBA Premier membership, which carries board voting, is $9,500 a year in North America [S-028]
- [assumption] Operator archetypes (hypotheses; titles and budget owners not sourced):

| Archetype | Role / titles | Organization | Top pains (ROW, permitting, build planning, data) | Information used today | Would pay for | Red flags / objections to a neutral association |
|---|---|---|---|---|---|---|
| O1 National carrier or large MSO deployment lead | VP/Director Network Deployment, Director ROW and Permitting, Regional Engineering Director | ~20 national carriers and cable MSOs; thousands of employees; in-house ROW teams | Permit-time variance across hundreds of jurisdictions; non-cost-based fees; forecasting crews and capex timing | Internal permit-tracking and project systems, consultants, contractor reports, carrier trade groups | Portfolio-level permit-time and fee benchmarks by jurisdiction, predicted approval dates, API feed into planning tools | Already in USTelecom, CTIA, NCTA, WIA; will not share build plans with competitors; legal/security review of any data contribution; sees "neutral" body that includes cities as a lobbying risk |
| O2 Regional or competitive fiber builder | COO, VP Construction, Director of Engineering/OSP, Permitting Manager | Hundreds of competitive fiber, co-op and municipal builders; tens to a few hundred staff | Sequencing builds across unfamiliar jurisdictions; BEAD and grant deadlines vs slow approvals; restoration rules | Spreadsheets, contractor and engineering-firm knowledge, calls to permit offices, FBA events | Regional permit-time history and predictions, jurisdiction requirement library, alerts on rule changes, peer meetings with ROW managers | Price vs FBA ($1,200-$9,500) and state association dues; doubts the data covers its region; fear that contributed data helps rivals |
| O3 Small rural telco, co-op, WISP or municipal network | General Manager/CEO, Operations Manager, Outside Plant Manager | ~850 NTCA members, ~500 ACA Connects members, ~2,000 WISPs, 400+ municipal networks (document 02); often under 50 staff | Few staff to handle state DOT and county permits; grant-funded deadlines; pole and railroad crossings | NTCA, state associations, consultants, the engineering firm that designs the build | Newsletter, meetings, a low-cost regional view of permit times; little appetite for an analytics seat | Already pays NTCA/WISPA/state dues; budget is small and owner-approved; national dashboard has little value outside its footprint |

### Side 2: Contractors and engineering firms (pay)
- [sourced] Dycom, a large telecom contractor, reports that a significant portion of revenue comes from multi-year master service agreements and that AT&T, Verizon and Lumen accounted for 25.4%, 14.0% and 10.8% of fiscal 2026 contract revenue [S-043]
- [sourced] Dycom also states that customers' capital budgets, the timing of their approvals and seasonal spending drive its results [S-043]
- [sourced] FBA charges vendors $6,000 a year (North America), the nearest published comparable for contractor and engineering-firm dues in a fiber association [S-029]
- [sourced] NTCA associate dues for suppliers and service firms run $750 (1-10 employees) to $5,000 (101+ employees) [S-026]
- [estimated] For large contractors the buying signal is customer capex timing rather than permits alone, so a dashboard that predicts where operators will build is likely worth more to them than permit benchmarks. This is inferred from the Dycom disclosures, not stated by a contractor.
- [assumption] Contractor and engineering archetypes (hypotheses; titles and budget owners not sourced):

| Archetype | Role / titles | Organization | Top pains | Information used today | Would pay for | Red flags / objections |
|---|---|---|---|---|---|---|
| C1 National or multi-region prime | VP Business Development, Regional President, VP Preconstruction/Estimating | Dycom-, MasTec-, Quanta-class firms and large regionals; MSA-driven; revenue concentrated in a few carriers | Forecasting which customers build where and when; crew mobilization vs permit dates; remobilization cost | Customer forecasts under MSAs, bid boards, Dodge-type lead services, internal history | Market-wide build and spend projections by region, permit-time predictions for bid pricing, customer capex tracking | Gets forecasts from its carrier customers already; will not share bid or margin data; wary of a body that also represents those customers |
| C2 Regional or local OSP / civil contractor | Owner/President, Operations Manager, Estimator | Most of the 4,500-6,700 telecom-relevant line-construction firms (document 02); small to mid-size, often family-owned | Finding work early; idle crews while permits wait; restoration and inspection rules that vary by town | Relationships with operators and primes, local permit office contacts, state contractor associations | Local opportunity alerts, jurisdiction requirement library, networking with operators at meetings | Low overhead budget; owner decides alone; national data has little value; skeptical of "association" dues without leads |
| C3 OSP engineering and permitting firm | Principal, Permitting Practice Lead, Project Director | 2,000-4,000 telecom/ROW engineering firms (document 02); consultancies serving operators | Researching each jurisdiction's requirements repeatedly; changing application rules; client pressure on timelines | Internal knowledge bases, jurisdiction websites, phone calls, prior applications | Maintained jurisdiction requirements and fee database, historical approval times to quote clients, exportable reports | Its jurisdiction knowledge is its product, so a shared database can look like a competitor; license must allow client deliverables |

### Side 3: ROW managers (free or near-free, zero ARR)
- [sourced] Mesa, AZ describes an Assistant Right of Way Manager who coordinates utilities so conflicts do not disrupt the critical path of capital projects, reviews ROW use and excavation permits for utilities and contractors, enforces licensing agreements and keeps a report of active utility conflicts [S-041]
- [sourced] Phoenix's Utility Coordination section reviews dry-utility plans, issues ROW permits, coordinates relocations on capital projects and manages telecommunications licenses, with a separate small-cell permitting contact [S-042]
- [sourced] Georgia DOT runs utility encroachment permits through GPAS, an online system to submit, manage and review permits, with a separate tool (GUPS) for locating permitted work [S-046]
- [sourced] NATOA, the local-government telecom association, lists staff "managing poles, conduits or rights-of-way" among its members and charges agencies $925-$2,125 a year by population (2027 schedule) [S-030]
- [sourced] Hidalgo County, TX was invoiced $1,630 for NATOA agency dues covering three staff seats (October 2023), showing that local governments do pay modest association dues [S-031]
- [estimated] Because agencies already pay roughly $1,000-$2,000 for NATOA and individual memberships, "near-free" for ROW managers can plausibly mean a nominal fee in that range for large jurisdictions, with free participation for those that contribute data. Inferred from S-030 and S-031; not tested.
- [assumption] ROW-manager archetypes (hypotheses; titles from S-041, S-042, S-046, the rest unsourced):

| Archetype | Role / titles | Organization | Top pains | Information used today | Would want (free or nominal) | Red flags / objections |
|---|---|---|---|---|---|---|
| R1 Municipal or county ROW manager / utility coordinator | ROW Manager, Assistant ROW Manager, Utility Coordinator, City Engineer; sponsor is Public Works or Transportation Director | 5,000-10,000 actively permitting jurisdictions (document 02); larger cities have dedicated ROW sections | Volume of telecom permits vs small staff; shot clocks; conflicts with capital projects; street cuts and restoration | Permit software, GIS, utility coordination meetings, NATOA and APWA peers | Advance view of planned builds in its area, peer benchmarks on fees and timelines, model ordinances, training | Fear the association is industry lobbying in disguise (fees, shot clocks); staff time to export data; legal review; open-records exposure |
| R2 State DOT utility accommodation / permits office | State Utility Engineer, District Utility/Permit Coordinator | 52 state DOTs (document 02); district offices handle permits | Coordinating utility work with highway projects across districts; long-range highway plans vs utility builds | Statewide permit systems such as GPAS, AASHTO peers | Statewide view of upcoming utility builds, consistent definitions, benchmarking against other DOTs | Data release needs central office and legal approval; a district cannot commit the state; preference for AASHTO channels |
| R3 GIS, open-data or IT steward | GIS Manager, Data Officer, IT Director | Larger cities, counties and DOTs | Repeated data requests; inconsistent fields; security of infrastructure locations | Open-data portals, GIS layers | A standard export spec and data dictionary, one place to send data instead of many requests | Security concerns over fiber and utility location data; no staff time; records-law questions |
| R4 Utility commission staff | Telecom or Safety Division staff | 53 state commissions (document 02) | Pole attachment and make-ready disputes in some states; broadband program oversight | Commission dockets, utility filings | Market data for proceedings and broadband programs | Must stay neutral in contested cases; unclear ROW authority in many states, so not a primary data partner |

### Cross-side tensions the archetypes reveal
- [estimated] O1 and O2 want shorter, cheaper permits; R1 and R2 want fewer street cuts and full cost recovery; C1-C3 want early visibility of both. The fee and shot-clock evidence (S-038, S-040) shows these interests conflict in public proceedings, which is the main objection each side will raise to a "neutral" association.
- [assumption] The proposed answer to that objection is governance (each side seated, no lobbying on contested fee or shot-clock issues, published data rules); this is untested and belongs in document 06.

## Assumptions
- All archetype titles, budget owners, information sources and willingness to pay are hypotheses until interviews are done; aim for at least four interviews per side.
- Permit-time variance is the shared pain worth paying for; current evidence is operator advocacy (S-038, S-039).
- Large contractors value build and capex forecasts more than permit benchmarks; inferred from Dycom disclosures.
- Large jurisdictions will pay a nominal fee in the NATOA range ($925-$2,125) or join free in exchange for data.
- Utility commissions are a secondary audience, not primary data partners, because many do not control local ROW records.
