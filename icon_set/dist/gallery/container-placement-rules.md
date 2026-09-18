# Container placement rules

Minimum padding is **2 canvas units**, measured between visible stroke edges on the 64×64 composition. Both container and content retain stroke width 4. Therefore their centerlines must remain at least 6 units apart. The orange debug buffer expands the content ink by 2 units in every direction; it must not overlap any container ink, including internal details.

The reusable runner reads the **current exported SVGs**, including CSS-styled edits, and records their paths and SHA-256 hashes alongside the source reference IDs from batch pairings. It does not regenerate primitives, overwrite accepted trials, or publish to Progression. Its output is a composition trial, not a native SUB32 icon.

## Placement

1. Use a saved content polygon and preferred center when available. Otherwise propose the largest enclosed empty region, falling back to inset bounds for open shapes. Automatic areas require visual review.
2. Fit the content proportionally. Try longest visible ink dimension 32, then 28, then 24 units; preserve stroke 4 independently of scaling. These dimensions apply to solo content in this runner, not the separate text-family height rule.
3. Search integer center positions within 10 units of the preferred center. Prefer the nearest valid position at the largest fitting size.
4. Use raster geometry for placement search, then adaptive vector-distance checks for the final ink gap. Touching/crossing contours fail; uncertain curve boundaries require review. Canvas bounds and raster content-area containment are also checked.
5. If no candidate fits, emit a review preview and the failed checks. Do not hide container strokes or relax padding. A gap pass alone does not establish that the composition conveys its intended meaning or that the sub icon remains legible.

## Run later

From the repository root:

```sh
python3 icon_set/scripts/compose_container_trials.py \
  --host desktop-monitor --sub badminton-shuttlecock \
  --padding 2 --out icon_set/work/container-placement-example
```

Replay existing pairings into a separate review folder:

```sh
python3 icon_set/scripts/compose_container_trials.py \
  --batch icon_set/data/container-solo-trials.json \
  --padding 2 --out icon_set/work/container-placement-batch
```

Add `--areas icon_set/data/container-content-areas.example.json` for saved placement areas. `--limit 5` provides a small batch check. Each output folder contains SVGs, buffer previews, results.json with measurements and source identity, and index.html. Unsupported input geometry is reported as blocked rather than silently approximated.

## AI content-area workflow

An agent should inspect the current container, identify its intended content space (screen, sign face, page, etc.), and write a polygon and preferred center in 64-unit coordinates. Use the example JSON as the contract. Start with `status: proposed`. After visual review, mark the area `reviewed`; this is an area review, not final composition approval. Save the exact container SVG hash so an edited container invalidates its old area.

Avoid selecting decorative holes, heads, handles, or stands just because they enclose empty space. Open containers especially need this semantic decision. For intentionally overlapping symbols, use `composition_mode: overlay`; these always remain review-overlay and never receive a containment pass. The script consumes an agent's saved proposal; it does not call an AI service itself.

Statuses: clearance-pass means reviewed content area plus passing gap and fit checks; review-area means the gap passes but the area needs review; review-fit means a fit or gap check failed or is uncertain; review-overlay means intentional overlap needs separate review; blocked means inputs need correction. Content-area containment uses a raster estimate, while stroke clearance uses vector error bounds.

## Saved visual decisions

The runner now loads `icon_set/data/container-content-areas.json` by default: 210 visually selected placements (174 used as main containers), including 207 safe polygons and three center-only placements. Every polygon excludes the 2-unit ink buffer with an additional conservative raster margin. The polygons describe where sub-icon ink may go; do not inset them by another 2 units. Final vector clearance checks still apply.

Both brain variants and the prohibition symbol have `kind: center-only`, center `[32, 32]`, no polygon, and overlay mode. Placement preserves that center and always requires overlay review; a center is not a promise of clearance. The brain-v2 exception was explicitly requested by the user. The other two follow the same visual reasoning.

Safe zones were reviewed across all seven contact sheets. Open frames use manually bounded interior regions. The camera uses its lens, the book its right page, the tent its central opening, and whiteboards the area beside the teacher. Existing pair previews retain their earlier placements until rerun.

## Center-first placement preference

For container combinations, prioritize the intended content center. Keep the sub-icon on the content area's vertical centerline where feasible, then adjust vertical placement for optical balance and the required ink clearance. Do not treat a sideways placement found by a clearance search as visually approved. If a native-size symbol cannot clear in a centered position, mark that combination for visual review or a container revision. The container canvas center is not necessarily the content center when handles, headers, stands or other furniture are present.

Saved policy and optical overrides: `icon_set/data/container-placement-preferences.json`.
