## Token usage and API-equivalent cost — corrected from session records

The original claim that usage could not be measured was incorrect. Local session records contain 52 response usage records for the original batch turn; their sum exactly matches its final cumulative counters. This audit excludes the follow-up question and audit work. [Usage evidence](work/usage-audit.json).

Model: **gpt-6-astra**. Reasoning: **medium**. Service tier is not recorded.

| Category | Tokens |
|---|---:|
| Total input | 5,749,837 |
| Cached input, included in input | 5,587,840 |
| Uncached input | 161,997 |
| Output | 44,938 |
| Reasoning, included in output | 16,037 |
| Cache writes | 0 |
| Total input + output | **5,794,775** |

These counters include repeated cached context across requests; they are not a count of unique written words. Shared setup, tool interactions, image review, repairs, rejected candidates, tests, builds and the original report are included.

- Total batch tokens / 50 attempted entries = **115,895.5** tokens per attempt.
- Total batch tokens / 30 successful icons = **193,159.2** allocated tokens per successful icon.
- This is an allocated average, not usage directly attributable only to the 30 successes. Their exclusive usage cannot be separated reliably from the interleaved batch. Already-existing skips: 0.

Using standard short-context rates ($10/M uncached input, $1/M cached input, $50/M output), the model-token API-equivalent estimate is **$9.45471 total**, or **$0.31516 per successful icon**. Calculation: (161,997 × 10 + 5,587,840 × 1 + 44,938 × 50) / 1,000,000. Cache writes are zero and reasoning is not counted twice. Maximum input in one request was 163,343, below the 272K long-context threshold. If Fast rates applied, the token estimate would be **$18.90942**. The actual tier and separately billed tool charges are unavailable; these are conditional token-only API equivalents, not an actual additional subscription bill. [Official pricing, checked 2026-09-21](https://developers.openai.com/api/docs/pricing).

The 5-entry and 25-entry checkpoint reports originally said usage was unavailable. That was a failure to locate the local counters, not evidence that no counters existed. Per-icon measurements were not captured.

The 20 blocked entries comprise 7 routing decisions and **13 unfinished drawing attempts**. The latter are not proven impossible under the profile; they require further redesign. Seven failed semantic review and six failed release QA. Calling all of them blocked without emphasizing that distinction overstated completion.
