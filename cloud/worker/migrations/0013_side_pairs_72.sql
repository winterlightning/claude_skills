-- Side pairs on the 72 canvas: a main drawn on 54 (family main-54) and a sub drawn on 36 (sub-36) make the
-- combined icon combination-72/<reference_id>, built in the browser by combine-side.js at size 72 (the sub placed
-- exactly as drawn). reference_parts keeps what a combination is (its parts' references, the sub's position) and
-- its 64 build; this table holds each part's 72 build, a row once an icon or layout is picked for it.
--
-- icon       the 72 icon picked for the part (main-54/... or sub-36/...); an upload of one of those families whose
--            reference_id is the part's reference fills an empty pick (POST /api/icons/upload)
-- layout     the part's boxes on the 72 grid, as reference_parts.layout on the 64 grid
-- built_sha  the part's drawing the 72 pair was last built from; stale when it differs from the icon's current one
CREATE TABLE reference_part_sizes (
    reference_id TEXT NOT NULL REFERENCES "references"(reference_id),
    role TEXT NOT NULL CHECK(role IN ('main', 'sub')),
    size INTEGER NOT NULL CHECK(size = 72),
    icon TEXT, layout TEXT, built_sha TEXT, updated_at TEXT, updated_by TEXT,
    PRIMARY KEY(reference_id, role, size));
CREATE INDEX reference_part_sizes_icon ON reference_part_sizes(icon);
CREATE INDEX reference_parts_part_reference ON reference_parts(part_reference_id);

-- The 72 set's families: its parts and its combined icons.
INSERT OR IGNORE INTO upload_families(id, name, canvas_size, created_at, created_by) VALUES
    ('main-54', 'Main 54 (72 side pairs)', 54, '2026-10-01T00:00:00.000Z', 'migration'),
    ('sub-36', 'Sub 36 (72 side pairs)', 36, '2026-10-01T00:00:00.000Z', 'migration'),
    ('combination-72', 'Side combination 72', 72, '2026-10-01T00:00:00.000Z', 'migration');
