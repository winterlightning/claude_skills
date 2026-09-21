# Container symbol generation queue

`GET /api/combinations/generation-queue?kind=container&family=symbol&limit=10&offset=0`

Read-only queue of distinct container source requirements without a linked,
published standard SYMBOL32 drawing. Repeated combinations and resize variants
are not separate requirements. Equivalent source references may still share a
single drawing; inspect existing candidates before creating a new file.

Parameters: `limit` (1–500, default 50), `offset` (nonnegative, default 0),
optional `q` (concept/source ID search), `category`, and `batch` (exact primitive
metadata filters). Only `kind=container` and `family=symbol` are supported.
Omit category and batch to retrieve the full queue, including typeface identities.

Response follows the primitives queue: `total`, `limit`, `offset`, `next_offset`,
and `briefs`. Each brief includes source identity, reference URL/path when
available, SYMBOL32 instructions, existing candidates, and affected combinations.
`requirements_total`, `covered_requirements`, and `missing_requirements` describe
unfiltered coverage. Coverage requires a linked valid record in the published
symbol manifest, a 32×32 canvas, and no special sizing mode. Counts update as the
published catalogs change; this endpoint neither generates artwork nor writes
review state. Reference metadata is a starting brief, not a visual audit.

Python server changes require restarting the running gallery server once.

## Combine latest published components

`GET /api/combinations/container/latest?limit=10&offset=0`

Returns one result per defined container pair, with `pairs`, `total`, `limit`,
`offset` and `next_offset`. Follow `next_offset` until null to cover the complete
set. Maximum page size is 500. Optional `id` selects one pair; `q` searches its
concept or ID. Only standard 32×32 SYMBOL32 drawings are eligible; resize and
other special sizing modes are excluded.

For each linked component, the API follows explicit `variant_of` descendants
within the same family. Only valid published manifest entries qualify. Descendants
supersede ancestors; parallel eligible leaves are ordered by recorded creation
date, numeric revision, then ID. This means latest **published** artwork, not an
unbuilt Python edit or a saved manual browser edit. It does not guess relationships
from similar names. Both selected keys and source SVG hashes are returned.

Each available result includes a `svg_url`, native dimensions,
placement, and measured `fit` details. The SVG endpoint is
`GET /api/combinations/container/svg?id=PAIR_ID`. Missing pairs return 409 there;
unknown IDs return 404. The JSON listing keeps missing and blocked pairs visible.

Composition retains native dimensions and 4-unit strokes, with no scaling. Saved
content areas are used only when their source hash matches; otherwise containment
remains review. Placement uses current saved centers/optical overrides where
available. `pass`, `fail`, and `review` describe measured fit; they do not imply
visual approval (`fully_validated` remains false). Unsupported artwork is blocked.
These GET endpoints return previews without saving exports, approving artwork,
or changing generation/progression state. Results resolve afresh on each request;
download the SVG and retain its hashes for a fixed snapshot.

## Gallery and saved processing

Open `/gallery/primitives.html?view=container` and click **Combine all pairs**.
The page processes all defined pairs in batches, saves previews in the runtime
state directory, and displays them in each expanded container group. It shows
container and symbol requirements, missing components, processing progress, and
fit outcomes. Refreshing preserves completed batches. Changed catalogs invalidate
old preview results; rerun the button to use new versions.

`GET /api/combinations/container/results` returns counts, current selections,
and saved results without inline SVG markup.
`POST /api/combinations/container/combine` accepts JSON `limit`, `offset`, and
optional `snapshot` from the results endpoint. A mismatched snapshot returns 400
so a batch run cannot silently mix catalog revisions. Follow `next_offset` until
null. The UI uses batches of 100. This saves previews only; it does not approve
combinations or modify icon sources or published manifests.
