###### \# Northfield \& Co. — Analytics Findings \& Recommendations

###### 

###### \## 1. Business Understanding

###### 

###### Northfield \& Co. generated \*\*$52.9M in net online revenue\*\* over the 852-day

###### period (1 Apr 2024 – 31 Jul 2026), averaging \*\*$62,091/day\*\*. Daily averages

###### by year were $60,054 (2024, partial), $61,927 (2025, full year), and $65,017

###### (2026, partial through July) — directionally upward, though 2024 and 2026 are

###### partial years and not directly comparable to the full 2025 figure.

###### 

###### The business runs on a \*\*high-frequency promotional model\*\*: a site-wide

###### discount was live on 572 of 852 days (67%). Paid media is a genuinely

###### low-intensity channel — \*\*8.83% of revenue on average\*\* — confirming the

###### brief's characterization of a brand that runs primarily on organic demand,

###### CRM/loyalty mailings, and promotional cadence rather than paid acquisition.

###### 

###### \## 2. Key Findings

###### 

###### \- \*\*BFCM is by far the single largest revenue lever.\*\* The 17 Black

###### &#x20; Friday/Cyber Monday days averaged $170,906/day vs. $59,876/day on all

###### &#x20; other days — a \*\*+185% lift\*\*. This one 17-day window is disproportionately

###### &#x20; important to annual revenue.

###### 

###### \- \*\*UWG mailings show the second-largest lift (+105%)\*\*, averaging

###### &#x20; $116,441/day vs. $56,768/day on non-mailing days, across 76 mailing days.

###### &#x20; This is the brand's most efficient lever outside of BFCM — a zero-marginal-media-cost

###### &#x20; channel (email/direct mail to an existing loyalty file) producing a larger

###### &#x20; relative lift than paid promotion or even in-store events.

###### 

###### \- \*\*Site-wide discounts and in-store promotions show smaller, but still

###### &#x20; material, lifts\*\* — Offline\_Promo +42%, Promotion\_Discount +36%. Since

###### &#x20; Promotion\_Discount is live two-thirds of the time, its "off" days are the

###### &#x20; unusual case (likely full-price periods outside major campaigns), so this

###### &#x20; 36% is a meaningful floor-to-ceiling comparison, not a rare-event spike.

###### 

###### \- \*\*Promotions are more media-efficient, not less.\*\* Media spend as a share

###### &#x20; of revenue is \*lower\* on promo days (7.97%) than non-promo days (10.59%).

###### &#x20; Revenue rises faster than media spend during promotions — consistent with

###### &#x20; promos converting existing demand (CRM, loyalty, organic) rather than

###### &#x20; being paid-media-driven events.

###### 

###### \- \*\*New-customer revenue share is essentially flat\*\*, hovering in the

###### &#x20; 30.8%–33.9% range across all three years with no clear upward trend. The

###### &#x20; brand is not visibly growing its acquisition base faster than its existing

###### &#x20; customer revenue — worth flagging as a strategic question rather than

###### &#x20; treating current growth as new-customer-driven.

###### 

###### \- \*\*Google and Meta dominate paid media\*\* (56.2% and 28.9% of total spend,

###### &#x20; 85% combined), with affiliates, Criteo, Outbrain, Microsoft, and influencer

###### &#x20; making up the remaining \~15% combined.

###### 

###### \- \*\*Brand search spend shows only a weak link to the promo calendar\*\*

###### &#x20; (correlation with Promotion\_Discount ≈ -0.04) despite a moderate

###### &#x20; correlation with revenue (≈0.45) — consistent with it being an "always-on"

###### &#x20; channel rather than one that flexes with promotions. Awin (affiliate) shows

###### &#x20; a weaker revenue correlation (≈0.28) but a mild positive link to promo days

###### &#x20; (≈0.14), a pattern worth investigating further as a possible sign of

###### &#x20; demand-capture around promotional periods rather than incremental demand

###### &#x20; generation — this dataset alone cannot confirm causality here.

###### 

###### \## 3. Recommendations

###### 

###### \- \*\*Protect and plan around BFCM and UWG mailing cadence\*\* — these are the

###### &#x20; two highest-lift levers in the business. Any resourcing, inventory, or

###### &#x20; stock-out risk planning should prioritize these windows first.

###### \- \*\*Investigate scaling UWG-style mailing frequency\*\*, since it delivers a

###### &#x20; large lift with (relatively) low incremental media cost — test a modest

###### &#x20; increase in mailing frequency and measure incremental lift on non-mailing

###### &#x20; control days.

###### \- \*\*Re-examine whether new-customer acquisition needs a dedicated push.\*\*

###### &#x20; A flat \~30-34% new-customer share over 2+ years suggests the brand may be

###### &#x20; increasingly dependent on repeat/loyalty revenue; this is worth a

###### &#x20; deliberate strategic conversation, not just an operational fix.

###### \- \*\*Audit brand search and affiliate spend for incrementality.\*\* Given the

###### &#x20; brief's own concern about "capturing demand created elsewhere," a holdout

###### &#x20; or geo-based incrementality test on brand search and Awin spend would

###### &#x20; directly answer whether this spend is additive or simply harvesting

###### &#x20; already-occurring conversions.

###### 

###### \## 4. Data Checks \& Assumptions

###### 

###### \- Date range validated as continuous with no gaps across all 852 days

###### &#x20; (1 Apr 2024 – 31 Jul 2026); no duplicate dates.

###### \- All five binary control columns (UWG\_Mailing, BFCM\_Promo\_Effect,

###### &#x20; holiday\_list, Offline\_Promo, Promotion\_Discount) confirmed to contain only

###### &#x20; 0/1 values.

###### \- No negative values found in revenue or spend columns.

###### \- `spend\_Google` and `spend\_Meta` roll-ups were checked against the sum of

###### &#x20; their component columns; small rounding differences only, consistent with

###### &#x20; the brief's note that these are "as reported" platform totals, not

###### &#x20; recomputed sums. `Total\_Paid\_Media` in this analysis uses the roll-up

###### &#x20; columns to avoid double-counting.

###### \- 2024 and 2026 are partial calendar years in this dataset (275 and 212 days

###### &#x20; respectively, vs. 365 for 2025) — all year-over-year comparisons account

###### &#x20; for this and avoid treating raw annual sums as like-for-like.

###### 

###### \## 5. Limitations

###### 

###### \- All lift figures (Section 2) are \*\*simple mean comparisons between "on"

###### &#x20; and "off" days\*\*, not controlled or model-based estimates. Promotional

###### &#x20; levers overlap heavily in this dataset (e.g. BFCM days are also

###### &#x20; Promotion\_Discount days), so a lift attributed to one flag may partly

###### &#x20; reflect another. These numbers describe \*\*observed association\*\*, not

###### &#x20; isolated causal effect.

###### \- The brand search / affiliate "demand capture" observation (Section 2) is

###### &#x20; a correlational pattern, not a proof of incrementality. Confirming it

###### &#x20; would require a controlled experiment (e.g. a geo or channel holdout).

###### \- No machine learning modeling was performed, per the case study's

###### &#x20; instructions — all findings are descriptive/exploratory.

