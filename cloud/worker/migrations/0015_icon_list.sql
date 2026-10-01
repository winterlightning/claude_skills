-- Icon review lists icons a page at a time from D1 (GET /api/icons, core icon_query) instead of downloading the whole
-- catalog. Each icon keeps its full record (`record`, until now always '{}') and what the list shows, filters and
-- sorts by (core icon_index), worked out when the record is stored: catalog push, upload, combination build.
-- Rows stored before this have no card until the next catalog push (or POST /api/icons/reindex).
ALTER TABLE icons ADD COLUMN card TEXT;
ALTER TABLE icons ADD COLUMN search TEXT NOT NULL DEFAULT '';
ALTER TABLE icons ADD COLUMN sort_name TEXT NOT NULL DEFAULT '';
ALTER TABLE icons ADD COLUMN keyshape TEXT;
ALTER TABLE icons ADD COLUMN author TEXT;
ALTER TABLE icons ADD COLUMN side_role TEXT;
ALTER TABLE icons ADD COLUMN stroke_count INTEGER;
ALTER TABLE icons ADD COLUMN segment_count INTEGER;
ALTER TABLE icons ADD COLUMN created_ms INTEGER;
ALTER TABLE icons ADD COLUMN modified_ms INTEGER;
ALTER TABLE icons ADD COLUMN version_group TEXT NOT NULL DEFAULT '';
ALTER TABLE icons ADD COLUMN version INTEGER NOT NULL DEFAULT 1;
ALTER TABLE icons ADD COLUMN variant INTEGER NOT NULL DEFAULT 0;
ALTER TABLE icons ADD COLUMN has_original INTEGER NOT NULL DEFAULT 0;
ALTER TABLE icons ADD COLUMN artwork_source TEXT;
-- Measured mirror axes (review-facets.json) and the drawing they were measured on: they apply while it is current.
ALTER TABLE icons ADD COLUMN symmetry TEXT;
ALTER TABLE icons ADD COLUMN symmetry_sha TEXT;
CREATE INDEX icons_category ON icons(category);
CREATE INDEX icons_version_group ON icons(version_group);
CREATE INDEX feedback_author ON feedback(icon, author);
CREATE INDEX icons_variant_of ON icons(family, variant_of);
