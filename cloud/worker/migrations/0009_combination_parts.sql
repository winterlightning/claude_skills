-- One set of combination tables: a combination is a "references" row (kind = 'combination') and its
-- reference_parts; its built drawing is the icon side_combination64/<reference_id> or
-- container_combination64/<reference_id>, linked through icon_references. These columns hold what the
-- side-pairs, side-layouts, side-renders stores and container_centers held (backfill_combinations.py).
--
-- icon       the icon drawn for this part (a part reference links to several versions in icon_references)
-- layout     JSON list of boxes on the 64 grid, [{"paths": [0, 1], "x", "y", "w", "h"}], each moving a group
--            of the part's paths; NULL = automatic placement from position
-- built_sha  the part's drawing sha the combination was last built from; stale when it differs from
--            icons.svg_sha256 of `icon`
ALTER TABLE reference_parts ADD COLUMN icon TEXT;
ALTER TABLE reference_parts ADD COLUMN layout TEXT;
ALTER TABLE reference_parts ADD COLUMN built_sha TEXT;
ALTER TABLE reference_parts ADD COLUMN updated_at TEXT;
ALTER TABLE reference_parts ADD COLUMN updated_by TEXT;
CREATE INDEX reference_parts_icon ON reference_parts(icon);
CREATE INDEX icon_references_reference ON icon_references(reference_id);

-- The meaning layer's composite parts: empty, never read. Combinations live in reference_parts only.
DROP TABLE physical_parts;
