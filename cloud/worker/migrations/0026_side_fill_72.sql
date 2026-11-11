-- Fill side pairs at 72 (the 72 set's main-54 + sub-36 pairs on the 72 canvas), beside the 64 ones of 0023: the same
-- tables, keyed by size as well. Every row 0023 wrote is a 64 row and stays as it is.
--
-- Icons (no new families), as at 64:
--   main-54/<name>--fill, main-54/<name>--fill-<variant>   a 72 main's fill variants, style_of 'main-54/<name>'
--   sub-36/<name>--fill, sub-36/<name>--fill-<variant>     a 72 sub's fill variants, style_of 'sub-36/<name>'
--   combination-72/<reference_id>--fill[-<n>]              a 72 pair's combined pick, style fill, style_of the pair's
--                                                          normal combination-72/<reference_id>
-- fill_counts keeps its key: the 72 totals are the scopes 'pairs:72', 'main:72', 'sub:72'.

-- A pair's picks, now per size: a 64 and a 72 pick of one reference never share a row.
CREATE TABLE reference_part_fills_sized (
    reference_id TEXT NOT NULL REFERENCES "references"(reference_id),
    size INTEGER NOT NULL DEFAULT 64 CHECK(size IN (64, 72)),
    role TEXT NOT NULL CHECK(role IN ('main', 'sub')),
    rank INTEGER NOT NULL DEFAULT 1 CHECK(rank BETWEEN -9 AND 9 AND rank != 0),   -- negative only mid-renumber
    icon TEXT, layout TEXT, built_sha TEXT, options TEXT, combined TEXT, updated_at TEXT, updated_by TEXT,
    PRIMARY KEY(reference_id, size, role, rank));
INSERT INTO reference_part_fills_sized(reference_id, size, role, rank, icon, layout, built_sha, options, combined, updated_at, updated_by)
    SELECT reference_id, 64, role, rank, icon, layout, built_sha, options, combined, updated_at, updated_by FROM reference_part_fills;
DROP TABLE reference_part_fills;
ALTER TABLE reference_part_fills_sized RENAME TO reference_part_fills;
CREATE INDEX reference_part_fills_icon ON reference_part_fills(icon);
CREATE INDEX reference_part_fills_combined ON reference_part_fills(combined);

-- The pairs as the pages list them, one row per reference and size.
CREATE TABLE fill_pairs_sized (
    reference_id TEXT NOT NULL REFERENCES "references"(reference_id),
    size INTEGER NOT NULL DEFAULT 64 CHECK(size IN (64, 72)),
    sort_key TEXT NOT NULL,
    state TEXT NOT NULL CHECK(state IN ('picked', 'unpicked', 'uncombined')),
    main_source TEXT, sub_source TEXT,
    main_layout TEXT, sub_layout TEXT,        -- the pair's own placement on its size's grid: a new pick starts from it
    note TEXT,
    version INTEGER NOT NULL DEFAULT 0,
    edited_at TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY(reference_id, size));
INSERT INTO fill_pairs_sized(reference_id, size, sort_key, state, main_source, sub_source, main_layout, sub_layout, note, version, edited_at, updated_at)
    SELECT reference_id, 64, sort_key, state, main_source, sub_source, main_layout, sub_layout, note, version, edited_at, updated_at FROM fill_pairs;
DROP TABLE fill_pairs;
ALTER TABLE fill_pairs_sized RENAME TO fill_pairs;
CREATE INDEX fill_pairs_page ON fill_pairs(size, state, sort_key);
CREATE INDEX fill_pairs_order ON fill_pairs(size, sort_key);
CREATE INDEX fill_pairs_main ON fill_pairs(main_source);
CREATE INDEX fill_pairs_sub ON fill_pairs(sub_source);

-- A part's key names its family (solo/…, sub/… at 64; main-54/…, sub-36/… at 72), so it stays the key; the size
-- column lets each page list its own parts.
ALTER TABLE fill_parts ADD COLUMN size INTEGER NOT NULL DEFAULT 64 CHECK(size IN (64, 72));
DROP INDEX fill_parts_page;
DROP INDEX fill_parts_order;
CREATE INDEX fill_parts_page ON fill_parts(size, role, status, sort_key);
CREATE INDEX fill_parts_order ON fill_parts(size, role, sort_key);
