# Fill side pairs

The 64 side pairs combined from **fill variants** of their main (solo) and sub: Progression › Side pairs ›
*Fill side pairs* (`side-fill.html`), with *Fill main icons* and *Fill sub icons*. They are stored the way the 72 set is:
the parts and the outputs are icons, and a pair's choices are per-part rows in D1.

## Where everything lives

| What | Where |
| --- | --- |
| A main's fill variants (current, `region-N`, `group-*`) | icons of style **fill** in the solo family: `solo/<name>--fill` (current), `solo/<name>--fill-region-3`, `solo/<name>--fill-group-wheels`…, `style_of = solo/<name>` (a few mains are `container/…`, the same way) |
| A sub's fill (closed fills included) | an icon of style **fill** in the sub family: `sub/<name>--fill`, `style_of = sub/<name>` |
| The outline of a part | the normal solo / sub icon itself (nothing is stored for it) |
| A pair's picks | `reference_part_fills(reference_id, role, rank, icon, layout, built_sha, options, combined)` |
| A pick's combined drawing | a Side combination 64 icon of style **fill**: `side_combination64/<reference_id>--fill` (alternatives `--fill-2`, …), `style_of` the pair's normal key, its key kept on the pick (`combined`). Icon review shows it under Style › Fill. |
| The page listings and totals | `fill_pairs`, `fill_parts`, `fill_counts` (written by the import, kept by every write) |

The fill variants sit beside their normal icon the way round and sharp ones do (`POST /api/icons/styled`, style
`fill`): Icon review lists them under the solo / sub family with Style › Fill. Every SVG is a `revisions` row; reviews
are Icon review's. A variant or combined icon starts **Ready**. Rank 1 is a
pair's output, later ranks are alternatives. A combined icon is `build_failed` while one of its parts is not approved
in Icon review (as for side pairs), and Icon review approves it only after both parts are; approving the parts clears
the flag (`combined_parts` rechecks fill picks too). Removing a pick deletes its combined icon unless someone reviewed it.

**Edits never overwrite each other.** Every pick, move and unpick gives the pair a new `version`; a build names the
version it combined and is refused (409, nothing written) when the pair changed since, as is a pick / move / unpick
that names an older one. Adding a pick is explicit (`append`, refused at 9 picks; `insert` at a rank); otherwise a
pick replaces the one at its rank, which must exist. A new pick's output key skips every `--fill[-n]` icon that
exists, so a kept reviewed output of a removed pick is never written over. Replace on the parts pages names the
drawing it replaces (`expected_sha256`), Add fill only creates. A part's first fill marks it filled and lets the pairs
that waited for one be picked.

**The import keeps the site's work.** Pick, move and unpick mark the pair edited on the site (`edited_at`): the picks
SQL never touches its picks again. It upserts the others, keeping each pick's output and, when its choice is
unchanged, its built drawing, and removes only imported picks the build no longer has. The listings keep an edited
pair's state and a part filled on the site.

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

## A part redrawn on the site

A part whose snapshot drawing is not the site's current one has no fill to upload (Fill main / sub icons: *Source
changed*, *No source*). Read the parts' current drawings with one bounded request
(`GET /api/combinations/drawings?keys=…`, ≤ 100 keys, about two rows each), then `side-fill sources drawings.json
--write`: their drawings go into the snapshot and `data/site-drawings.json` records them as the site's. Then
`side-fill build --steps reviews` (the engine's defaults: decisions reviewed on another drawing are keyed by its sha
and not applied), `publish_stroke_fills main sub --names … --apply` (only those parts: a rebuilt review can differ
elsewhere), `side-fill build --steps mains,baseline,recombine,duplicates,layouts,gallery --ids <their pairs>`,
`icons`, `d1-import` and the upload. When the site's drawing is the one the pairs were laid out on, its pairs
combine again; when it is newer, the fill is uploaded and its pairs wait for a layout. `node cloud/migrate/pick_new_pairs.mjs
--base-url <site> --cookie pictographic_session=…` (dry run, then `--send`) then gives every such pair without a pick
an output, as the pair page would: the main's current fill with the sub's fill (else outlines) on the pair's placement,
a redrawn part on one box over the area its old boxes covered. It skips text subs and rejected parts.

## Replacing a fill

On *Fill main icons* / *Fill sub icons*, signed in: **Replace** under a fill variant takes an SVG as its new drawing,
**Add fill…** stores a new variant (`current` / `fill`, or a name such as `region-5`). Both save through
`POST /api/icons/styled` (style fill, `replace: true`): the variant is Ready in Icon review again (approve it there)
and every pick using it shows *Build again* on its pair page. *Needs a new layout* lists mains redrawn on the site
after their pairs were laid out: their fill is current, their pairs wait for a layout on the new drawing.

## Keyshape

An output's keyshape is its parts' boxes plus the 4px stroke (as the grid, its *Off keyshape only* filter and Icon
review show it): a 56 square, 60×44 or 44×60 within 1px, else FREE. `node cloud/migrate/fit_fill_keyshapes.mjs
--base-url <site>` lays out again the picks that miss, without changing how they read: the two parts scaled together
or moved apart, the sub cutting no more than 4% more of the main, no more than 4px further from it, and on the same
side of it. It writes `data/keyshape-fit-layouts.json`, which `d1-import` applies to the picks, and lists the picks it
cannot fit (`unfit`): those need a layout by hand on the pair page.

## The original

*Show original* (Fill side pairs) puts each pair's normal Side combination 64 icon, `side_combination64/<id>`, beside
its fill output; the pair page always shows it. The grid then asks for them with the page (`original=1`: one key
lookup a pair, about 120 rows for 60 pairs).

## D1 reads

No route counts or scans. Lists are keyset pages on `(state, sort_key)` / `(role, status, sort_key)` with `LIMIT`; picks,
icons and reviews are key lookups; totals are `fill_counts` rows. Every response says what it read in
`X-D1-Rows-Read` (its lookups; the reads inside a write batch are not counted), and `cloud/worker/tests/side_fill`
fails when a route reads more than its ceiling:

| Request | Rows read (3,614 pairs, ~1,900 fill icons) | Ceiling |
| --- | --- | --- |
| a page of 60 pairs | 660–910 | 1,200 |
| one pair (with its parts' variants) | ~30 | 80 |
| a page of 48 mains / subs | 330–370 | 500 |
| pick, insert, move, unpick | a few | 40 |

A tile image is `/api/icon-artwork/svg` (one icon row and one revision); the pair page reads its drawings with one
`/api/combinations/drawings` request.

## The snapshot is data, in R2

`icon_set/data/side-fill` is the snapshot the Python tools read (layouts, review decisions, region recipes, the source
and fill drawings, the Oct 26 backup). It is data, so git holds none of it (the folder is ignored): its 9,273 files are
R2 objects stored once by content (`references/side-fill-data/objects/<sha256>`, never overwritten), and
`references/side-fill-data/manifest.json` maps each path to its sha256. The manifest is written last, so a push that
fails part way leaves the previous snapshot whole.
The JS goldens (`icon_set/tests/js/fixtures/side-fill`) are made from it and are not in git either.

```
python3 cloud/migrate/side_fill_data.py pull        # a fresh checkout: the snapshot from R2 (R2 keys in cloud/.env)
python3 cloud/migrate/side_fill_data.py check       # the files here against the manifest
python3 cloud/migrate/side_fill_data.py manifest    # after changing files, then `push --backend s3`
python3 -m icon_set side-fill goldens               # the JS goldens; without them side-fill.test.mjs is skipped
```

The pages read the source keyshapes from `laboratory.json`, as the Side pairs editor does.

## Commands

```
python3 -m icon_set side-fill build        # every variant and review row into icon_set/state/side-fill
python3 -m icon_set side-fill icons        # the fill variant icons + manifest (never a rejected variant)
python3 -m icon_set side-fill d1-import    # side-fill-import.sql (listings) and side-fill-picks.sql (picks)
python3 -m icon_set side-fill check        # every pick combined from the icon files vs the SVG reviewed in the gallery
python3 -m icon_set side-fill sources drawings.json --write   # the site's current drawings of redrawn / missing parts
python3 -m icon_set side-fill goldens      # fixtures for side-fill.test.mjs
```

## Putting it on a site (in this order)

1. `wrangler d1 migrations apply <db> --remote` (0023: the tables and indexes; no new families), then deploy
   the Worker. The combined-part checks read `reference_part_fills`, so the migration goes first.
2. `wrangler d1 execute <db> --remote --file icon_set/state/side-fill/side-fill-import.sql`
3. `PICTOGRAPHIC_SESSION=<jakes's session cookie> python3 cloud/migrate/upload_fill_parts.py --base-url <site> --approve`
   (dry run), then `--send --approve`: the fill variants into the solo / sub families, 50 a request, each approved in
   Icon review as jakes (the person whose session it is), so the outputs built from them are not Failed check. A
   rerun sends and approves only what changed (`fill-icons/uploaded.json`). An output on an outline uses the normal
   solo / sub icon itself: it is Failed check while that icon is not approved.
4. `wrangler d1 execute <db> --remote --file icon_set/state/side-fill/side-fill-picks.sql` (it replaces only the
   imported picks; picks made on the site are kept).
5. `node cloud/migrate/build_fill_pairs.mjs --base-url <site> --token "$PICTOGRAPHIC_PUSH_TOKEN"` (dry run), then
   `--send`: each pick's combined icon, made by the pages' own engine, into Icon review.
6. Publish the gallery (`side-fill*.html|js|css`, `side-fill-combine.js`, `side-fill-layout.js`, `clipper.js`), and
   push the snapshot to R2 (`side_fill_data.py push --backend s3`) so others can pull it.

Locally: `wrangler dev --persist-to <dir> --var PUSH_TOKEN:<32+ characters>` on a seeded D1 (`cloud/worker/tests/side_fill/make_local_seed.py`), the same
steps against `http://localhost:<port>`, and `python3 -m icon_set dev --cloud-api http://localhost:<port>` for the pages
(they read D1 only, so they need cloud mode).
