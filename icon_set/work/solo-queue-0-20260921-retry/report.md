# Solo queue — offset 0

Requested offset: **0**. Returned page: **10 references** (91 eligible at fetch). The worklist stayed fixed; no next page or replacement items were fetched.

Outcome: **3 revised originals built; 7 unresolved; 0 combinations; 0 skipped for changed status.** Final export verification in `export-verification.json` confirms all three are in the solo manifest, have zero errors and warnings, match their current Python geometry, and match the manifest SHA-256 hashes. Actual exported SVGs were visually reviewed at 48 pixels in both themes.

Every reference was rendered and visually inspected. Immediately before starting each item, its status and saved brief were read from `http://localhost:8000/api/primitives/status` and `/api/primitives/briefs`. All ten had default TODO status and saved family `solo`. Exact source UUIDs, source paths and editorial briefs are retained in `fixed-worklist.json` and `intake-records.json`. All ten are standalone objects or natural groups/interactions. No classification or component-brief saves were needed, so there are **no saving failures or retry payloads**.

## Complete accounting

| # | Source UUID | Subject | Outcome |
|---|---|---|---|
| 1 | `42cdb953-b64a-446a-9e2f-0a5e1116e601` | Three labeled ring binders | Unresolved visual identity. Existing HRECT_L draft is valid but consists of three empty spines. Labels and finger holes do not fit the required spacing. |
| 2 | `3278a9d5-891d-4c6a-acc3-7bd972888b5c` | Blackberry with one leaf | Unresolved visual identity. Existing VRECT_L draft is valid but the empty scalloped outline reads like a bowl; distinct berry drupelets are lost. |
| 3 | `86657946-998d-44be-80c5-35a4d1b96f55` | Raspberry with three leaves | Unresolved visual identity. Existing VRECT_L draft is valid but loses the raspberry cells and replaces the three leaves with one. |
| 4 | `e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a` | Litter tray with slotted scoop | Generated: valid, zero errors and warnings; reviewed in light and dark at 48 px. |
| 5 | `a31f3f41-e636-492d-ad83-a82ed5593583` | Open-front hooded cloak | Generated: valid, zero errors and warnings; reviewed in light and dark at 48 px. |
| 6 | `82c1163c-aaf6-4c80-9120-18bf38090361` | Two interlocking toothed wheels | Unresolved spacing. Diagonal simplified gear trial fails gear/hub and gear/gear clearances. |
| 7 | `b484255b-2a40-40d1-9943-7e27cfb9f399` | Diagonal pair of meshing gears | Unresolved spacing. Reference has the same construction and constraints as item 6; the shared diagonal trial fails. |
| 8 | `f4812ef0-fce6-4380-9124-384916ee103d` | Lobster with pointed closed claws | Unresolved. Existing draft fails leg spacing and tail separation. A wider HRECT_L trial passes after reducing legs and tail detail, but loses convincing lobster identity. |
| 9 | `813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0` | Lobster with broad open pincers | Unresolved. Existing draft fails the same leg and tail spacing; narrow pincers also lose the broad notched source shape at native size. |
| 10 | `7f4d0d07-e981-4efd-ae8c-b673077a9b75` | Pick entering open padlock | Generated: valid, zero errors and warnings; reviewed in light and dark at 48 px. |

## Generated drawings

### Litter tray with slotted scoop

A shallow tray holds a diagonal scoop with a long handle and one wide slot. SQUARE uses centerline extrema (6,6)–(42,42) to preserve the broad tray and raised tool. The upright prior candidate read as a cup and straw; the diagonal revision separates those silhouettes. Omitted the second slot, doubled rim and outlined handle to keep measurable space. The source supplies the physical arrangement; Lucide `shovel` supplies the broad blade and central handle construction principle.

- Original: `icon_set/model/icons/solo/litter_tray_with_slotted_scoop_e6e7ff28_6ade_4296_95f7_4a6c7bd1ce2a.py`
- Export: `published/solo48/litter-tray-with-slotted-scoop.svg`

### Open-front hooded cloak

A rounded hood sits above broader shoulders and two parted panels. VRECT_L uses (8,4)–(40,44) for its upright garment proportions. The final 28-unit-wide hood reduces the oversized ring of the earlier 32-unit trial; its teardrop opening, shoulder transitions and mirrored panels remain visible at 48 px. Omitted the small neck fastener and secondary hem shaping. The source supplies the hood and open front; Lucide `shirt` informs explicit neckline and garment silhouette construction.

- Original: `icon_set/model/icons/solo/open_front_hooded_cloak_a31f3f41_e636_492d_ad83_a82ed5593583.py`
- Export: `published/solo48/open-front-hooded-cloak.svg`

### Pick entering open padlock

A bent pick with a diagonal oblong grip enters an open padlock. SQUARE uses (6,6)–(42,42) to balance the lower-left tool and upper-right lock. The shackle opening and tool grip stay readable in both themes. As in the reference, the housing is interrupted around the entering tool; the keyhole is reduced to a short slot. The grip has an actual radius-5 capsule construction and a split arc at the tool attachment. Lucide `lock-open` informs the rounded housing and open shackle.

- Original: `icon_set/model/icons/solo/pick_entering_open_padlock_7f4d0d07_e981_4efd_ae8c_b673077a9b75.py`
- Export: `published/solo48/pick-entering-open-padlock.svg`

## Unresolved findings

The binder draft uses three 8-unit-wide spines with 8-unit gaps, filling the 40-unit HRECT_L width. A separate diameter-4 finger hole with 8-unit centerline clearance to both walls would require a 20-unit spine. Three would require 76 units including the gaps. Omitting all identifying details produces plain rectangles, so the technically valid draft remains unreleased. Lucide `library` provided a repeated upright construction reference.

The berry drafts were revalidated and reviewed at 48 px in both themes. Both pass numeric checks but fail the source identity requirements. Lucide `grape` demonstrates readable separate cells, but its cell count and thin-stroke density cannot simply be copied to these profiles. No new berry export is claimed.

The gear trial retains two hubs and reduces the teeth to four broad teeth on each wheel. It still leaves only **5.071 centerline units** between a hub and its gear outline, and **2.828** between gears, versus the required **8**. Increasing the hubs' surrounding rings or the pair's separation would outgrow this layout; deleting the teeth/hubs would lose the requested subject. See `gears-trial-validation.txt` and `gears-trial.svg`. Lucide `cog` informed the radial hub/body relationship.

Both original lobster drafts fail parallel leg separations of approximately **6.946–7.155** centerline units, and a last-leg/tail separation of approximately **0.088**, versus **8** required. The new wider trial removed the conflicting leg rows and simplified the fan tail; it validates but reads too generically to replace the source. No lobster export is claimed. Lucide `shrimp` was inspected for crustacean contour and tail treatment; it is not a useful direct construction match for these raised-claw front views.

## Evidence and preservation

- `validation.json`: selected original validation results.
- `cloak-full-qa.json`: final cloak export checks, including passing internal spacing.
- `export-verification.json`: manifest membership, validation, export hash and current-geometry comparisons.
- `review-light.png`, `review-dark.png`: contact-sheet renders with 48-pixel samples.
- `exports-light.png`, `exports-dark.png`: actual exported SVGs at 48 pixels and enlarged.
- `unresolved-light.png`, `unresolved-dark.png`: existing unresolved drafts at native size.
- Per-UUID `*-current.json` and `*-draft-validation.txt`: intake and unresolved checks.
- `litter-prior.py.txt`, `cloak-prior.py.txt`, `pick-prior.py.txt`: preserved prior drafts, including the pre-existing litter-tray edits.

Only the selected originals were targeted for builds. Other registered icons reused their prior results. The shared output lock was respected; no other process was interrupted. Original reference artwork and editorial metadata were preserved. No full-library metadata seeding, commit, publish or deployment was performed. The three revised originals identify the author as `gpt-6-astra`.
