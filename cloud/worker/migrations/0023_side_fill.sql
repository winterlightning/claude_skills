-- Fill side pairs: the 64 side pairs combined from fill variants of their main (solo) and sub, stored the way the
-- 72 set is (migration 0013): the parts and the combined icons are icons, a pair's picks are per-part rows.
--
-- Icons (no new icon tables or families; parts stored with POST /api/icons/styled, combined with POST
-- /api/side-fill/build), each a style fill icon beside a normal one, as round / sharp are (0019):
--   solo/<name>--fill, solo/<name>--fill-<variant>   a solo main's fill variants (current, region-N, group-*),
--                                           style_of = 'solo/<name>'
--   sub/<name>--fill                        a sub's fill (closed fills included), style_of = 'sub/<name>'
--   The outline is the normal solo / sub icon itself: a pick uses its key directly, nothing is stored for it.
--   side_combination64/<reference_id>--fill[-<n>]   a pair's combined pick, built in the browser: a Side
--                                           combination 64 icon of style fill, style_of the pair's normal key. Its key
--                                           is kept on the pick (reference_part_fills.combined), so it follows the
--                                           pick when ranks move up
-- Their SVGs are revisions rows and their reviews start Ready, as for every upload and build.
--
-- Reads stay bounded (no COUNT(*), no OFFSET, no scan of "references" or icons): the pages list fill_pairs and
-- fill_parts by their (state, sort_key) indexes with LIMIT, look picks up by primary key, variants through
-- icons_style_of (style_of, style), and totals from fill_counts, which every write keeps in step.
CREATE INDEX icons_style_of ON icons(style_of, style);

-- A pair's pick: for each rank, the fill variant icon used for its main and its sub, and their boxes on the 64
-- grid ({paths, x, y, w, h} as reference_parts.layout). built_sha: the part drawing the combined icon of that rank
-- was last built from (NULL after the pick changed; stale when it differs from the icon's current drawing).
-- options (main row): {"omit": [element numbers of the main left out], "overlap": "join", "sub_scaled": true}.
-- combined (main row): the pick's combined icon key, once built.
CREATE TABLE reference_part_fills (
    reference_id TEXT NOT NULL REFERENCES "references"(reference_id),
    role TEXT NOT NULL CHECK(role IN ('main', 'sub')),
    rank INTEGER NOT NULL DEFAULT 1 CHECK(rank BETWEEN -9 AND 9 AND rank != 0),   -- negative only mid-renumber
    icon TEXT, layout TEXT, built_sha TEXT, options TEXT, combined TEXT, updated_at TEXT, updated_by TEXT,
    PRIMARY KEY(reference_id, role, rank));
CREATE INDEX reference_part_fills_icon ON reference_part_fills(icon);
CREATE INDEX reference_part_fills_combined ON reference_part_fills(combined);

-- The fill side pairs as the pages list them: one row per 64 side pair (written by the import, kept by every
-- pick / build). state: picked | unpicked | uncombined (the combine cannot draw it: note says why).
-- sort_key = lower(concept) || ' ' || reference_id: the page order and the keyset cursor.
CREATE TABLE fill_pairs (
    reference_id TEXT PRIMARY KEY REFERENCES "references"(reference_id),
    sort_key TEXT NOT NULL,
    state TEXT NOT NULL CHECK(state IN ('picked', 'unpicked', 'uncombined')),
    main_source TEXT, sub_source TEXT,
    main_layout TEXT, sub_layout TEXT,        -- the pair's own placement on the 64 grid: a new pick starts from it
    note TEXT,
    updated_at TEXT NOT NULL);
CREATE INDEX fill_pairs_page ON fill_pairs(state, sort_key);
CREATE INDEX fill_pairs_order ON fill_pairs(sort_key);

-- The mains and subs the fill pairs use, as the Fill main / sub pages list them: one row per source icon (solo/…,
-- sub/…), text subs and undrawn parts included. status: ready | outline | redrawn | no-source | no-fill |
-- not-drawn | text. Its fill variants are icons (variant_of = key), not repeated here.
CREATE TABLE fill_parts (
    key TEXT PRIMARY KEY,
    role TEXT NOT NULL CHECK(role IN ('main', 'sub')),
    sort_key TEXT NOT NULL,
    status TEXT NOT NULL,
    note TEXT,
    text TEXT,
    pair_count INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL);
CREATE INDEX fill_parts_page ON fill_parts(role, status, sort_key);
CREATE INDEX fill_parts_order ON fill_parts(role, sort_key);

-- The totals the filter buttons show (scope: pairs | main | sub; status, or 'all').
CREATE TABLE fill_counts (
    scope TEXT NOT NULL,
    status TEXT NOT NULL,
    n INTEGER NOT NULL,
    PRIMARY KEY(scope, status));
