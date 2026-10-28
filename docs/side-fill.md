# Fill side pairs

The 64 side pairs combined from **fill variants** of their main (solo) and sub: Progression › Side pairs ›
*Fill side pairs* (`side-fill.html`), with *Fill main icons* and *Fill sub icons*. They are stored the way the 72 set is:
the parts and the outputs are icons, and a pair's choices are per-part rows in D1.

## Where everything lives

| What | Where |
| --- | --- |
| A main's fill variants (current, `region-N`, `group-*`) | icons `main-fill-48/…`, `variant_of = solo/<name>`, `variant_label` |
| A sub's fill (closed fills included) | icons `sub-fill-32/…`, `variant_of = sub/<name>` |
| The outline of a part | the solo / sub icon itself (nothing is uploaded for it) |
| A pair's picks | `reference_part_fills(reference_id, role, rank, icon, layout, built_sha, options, combined)` |
| A pick's combined drawing | a Side combination 64 icon of style **fill**: `side_combination64/<reference_id>--fill` (alternatives `--fill-2`, …), `style_of` the pair's normal key, its key kept on the pick (`combined`). Icon review shows it under Style › Fill. |
| The page listings and totals | `fill_pairs`, `fill_parts`, `fill_counts` (written by the import, kept by every write) |

Every SVG is a `revisions` row; reviews are Icon review's. A variant or combined icon starts **Ready**. Rank 1 is a
pair's output, later ranks are alternatives. A combined icon is `build_failed` while one of its parts is not approved
in Icon review (as for side pairs), and Icon review approves it only after both parts are; approving the parts clears
the flag (`combined_parts` rechecks fill picks too). Removing a pick deletes its combined icon unless someone reviewed it.

`options` (main row): `omit` (main elements left out), `overlap: "join"` (an outline sub joined, not cut),
`sub_scaled` (a filled sub under 20 px scales its stroke too).

## The combine runs in the browser

`side-fill-combine.js` is a port of `icon_set/scripts/side_fill/pick_combine.py` (itself the build's
`combine_fill_side_layouts.place_part` and `combine_fill_side.cut_main` / `cut_outline_strokes`) on Clipper
(`clipper.js` 6.4.2). The pair page combines every pick and candidate from the parts' *current* drawings, so a part
redrawn in Icon review changes its pairs at once; a pick built from an older drawing shows *Build again*. Building
posts the drawing made in the page (`POST /api/side-fill/build`). The layout editor's preview (keyshape checks, the
4px result, the 8px stress cut) is `side-fill-layout.js`.

`node --test icon_set/tests/js/side-fill.test.mjs` checks the JS against 240 Python goldens of every kind of pick:
the visible difference (slivers under 0.3 px left out) stays under 1 px².

## D1 reads

No route counts or scans. Lists are keyset pages on `(state, sort_key)` / `(role, status, sort_key)` with `LIMIT`; picks,
icons and reviews are key lookups; totals are `fill_counts` rows. Every response says what it read in
`X-D1-Rows-Read`, and `cloud/worker/tests/side_fill` fails when a route reads more than its ceiling:

| Request | Rows read (3,614 pairs, ~1,900 fill icons) | Ceiling |
| --- | --- | --- |
| a page of 60 pairs | 660–910 | 1,200 |
| one pair (with its parts' variants) | ~30 | 80 |
| a page of 48 mains / subs | 330–370 | 500 |
| pick, insert, move, unpick | a few | 40 |

A tile image is `/api/icon-artwork/svg` (one icon row and one revision); the pair page reads its drawings with one
`/api/combinations/drawings` request.

## The snapshot's drawings are in R2

`icon_set/data/side-fill` is the snapshot the Python tools read. Its JSON (layouts, review decisions, region recipes)
is in git; its 8,056 SVG drawings (sources, fills, the Oct 26 backup) are R2 objects under
`references/side-fill-data/<path>`, and `svg-manifest.json` names each with its sha256.

```
python3 cloud/migrate/side_fill_svgs.py pull        # a fresh checkout: the drawings from R2 (R2 keys in cloud/.env)
python3 cloud/migrate/side_fill_svgs.py check       # the files here against the manifest
python3 cloud/migrate/side_fill_svgs.py manifest    # after changing drawings, then `push --backend s3`
```

## Commands

```
python3 -m icon_set side-fill build        # every variant and review row into icon_set/state/side-fill
python3 -m icon_set side-fill icons        # the fill variant icons + manifest (never a rejected variant)
python3 -m icon_set side-fill d1-import    # side-fill-import.sql (listings) and side-fill-picks.sql (picks)
python3 -m icon_set side-fill check        # every pick combined from the icon files vs the SVG reviewed in the gallery
python3 -m icon_set side-fill goldens      # fixtures for side-fill.test.mjs
```

## Putting it on a site (in this order)

1. `wrangler d1 migrations apply <db> --remote` (0023: the tables, the indexes, the two fill upload families), then deploy
   the Worker. The combined-part checks read `reference_part_fills`, so the migration goes first.
2. `wrangler d1 execute <db> --remote --file icon_set/state/side-fill/side-fill-import.sql`
3. `python3 cloud/migrate/upload_fill_parts.py --base-url <site>` (dry run), then `--send`. A rerun sends only what
   changed (`fill-icons/uploaded.json`).
4. `wrangler d1 execute <db> --remote --file icon_set/state/side-fill/side-fill-picks.sql` (it replaces only the
   imported picks; picks made on the site are kept).
5. `node cloud/migrate/build_fill_pairs.mjs --base-url <site> --token "$PICTOGRAPHIC_PUSH_TOKEN"` (dry run), then
   `--send`: each pick's combined icon, made by the pages' own engine, into Icon review.
6. Publish the gallery (`side-fill*.html|js|css`, `side-fill-combine.js`, `side-fill-layout.js`, `clipper.js`,
   `side-fill-keyshapes.json`).

Locally: `wrangler dev --persist-to <dir>` on a seeded D1 (`cloud/worker/tests/side_fill/make_local_seed.py`), the same
steps against `http://localhost:<port>`, and `python3 -m icon_set dev --cloud-api http://localhost:<port>` for the pages
(they read D1 only, so they need cloud mode).
