-- Fill side pairs: the 64 side pairs combined from fill variants of their main (solo) and sub, stored the way the
-- 72 set is (migration 0013): the parts and the combined icons are icons, a pair's picks are per-part rows.
--
-- Icons (no new icon tables; uploaded with POST /api/icons/upload, combined with POST /api/side-fill/build):
--   main-fill-48/…                          a fill variant of a solo main (current, region-N, group-*):
--                                           icons.variant_of = 'solo/<name>', variant_label = the variant
--   sub-fill-32/…                           a sub's fill (closed fills included): variant_of = 'sub/<name>'
--   The outline variant is the solo / sub icon itself: a pick uses its key directly, nothing is uploaded for it.
--   side-combination-fill-64/<reference_id>[--<n>]   a pair's combined pick, built in the browser; its key is kept on
--                                           the pick (reference_part_fills.combined), so it follows the pick when
--                                           ranks move up
-- Their SVGs are revisions rows and their reviews start Ready, as for every upload and build.
--
-- Reads stay bounded (no COUNT(*), no OFFSET, no scan of "references" or icons): the pages list fill_pairs and
-- fill_parts by their (state, sort_key) indexes with LIMIT, look picks up by primary key, variants through
-- icons_variant_of (family, variant_of), and totals from fill_counts, which every write keeps in step.
INSERT OR IGNORE INTO upload_families(id, name, canvas_size, created_at, created_by) VALUES
    ('main-fill-48', 'Fill main 48 (fill side pairs)', 48, '2026-10-28T00:00:00.000Z', 'migration'),
    ('sub-fill-32', 'Fill sub 32 (fill side pairs)', 32, '2026-10-28T00:00:00.000Z', 'migration'),
    ('side-combination-fill-64', 'Fill side combination 64', 64, '2026-10-28T00:00:00.000Z', 'migration');

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
