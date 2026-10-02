-- Icon review lists icons a page at a time from D1 (GET /api/icons, core icon_query). A page reads only its own
-- rows: each icon stores what the list filters, sorts and counts by, and the database keeps it current.
--
--   * List columns from the record (core icon_index), written by catalog push, upload and combination build.
--   * Review state (icon_state below), recomputed by triggers whenever a review, feedback, split, artwork pick,
--     icon graph or the icon itself changes: every write path keeps it, nothing has to remember to.
--   * icon_counts / icon_facet_counts: the tab, category and filter-choice counts, kept by triggers on icons.
--   * icon_search: a trigram full-text index of the search text, so a search reads only the icons that match.
--
-- Rows stored before this have no card until the next catalog push or POST /api/icons/reindex.
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
-- Review state as Icon review shows it (gallery.html iconState and friends), kept by the triggers below.
ALTER TABLE icons ADD COLUMN decision TEXT;
ALTER TABLE icons ADD COLUMN actor TEXT;
ALTER TABLE icons ADD COLUMN state TEXT;
ALTER TABLE icons ADD COLUMN mode TEXT;
ALTER TABLE icons ADD COLUMN artwork TEXT;
ALTER TABLE icons ADD COLUMN strokes INTEGER;
ALTER TABLE icons ADD COLUMN segments INTEGER;
ALTER TABLE icons ADD COLUMN axes TEXT;
ALTER TABLE icons ADD COLUMN reason TEXT;
ALTER TABLE icons ADD COLUMN has_feedback INTEGER NOT NULL DEFAULT 0;
ALTER TABLE icons ADD COLUMN cannot_fix INTEGER NOT NULL DEFAULT 0;
-- The artwork picked since the push, when it applies (its mode), else NULL: the card then shows the Worker's drawing.
ALTER TABLE icons ADD COLUMN picked TEXT;

-- One icon's review state from its rows (filter by key: every lookup is by primary key or index). An active split
-- or any rejected revision rejects; otherwise the current revision's review (re-generated is ready, disapproved and
-- claimed are "pending"); a failing build waiting for a decision is "failed", and a failed side / container
-- combination is failed unless rejected or disapproved. Artwork picked since the push applies while made for the
-- drawing the icon has (or before the icon has a generated graph).
CREATE VIEW icon_state AS SELECT i.key AS key,
  (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) AS decision,
  (CASE WHEN sp.icon IS NOT NULL THEN sp.created_by WHEN (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN NULLIF((SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1), '') ELSE r.updated_by END) AS actor,
  (CASE WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) = 'rejected' THEN 'rejected'
              WHEN i.family IN ('side_combination64', 'container_combination64') AND i.build_failed AND (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) != 'pending' THEN 'failed'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) IN ('pending', 'claimed') THEN 'pending'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) IN ('ready', 're-generated') AND i.build_failed THEN 'failed'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) = 're-generated' THEN 'ready'
              ELSE (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) END) AS state,
  COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') AS mode,
  (CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_edited' THEN 'edited' WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_upload' OR (i.uploaded AND COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org') THEN 'uploaded'
              WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'work_fix' THEN 'work_fix' ELSE 'original' END) AS artwork,
  CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org' THEN i.stroke_count END AS strokes,
  CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org' THEN i.segment_count END AS segments,
  CASE WHEN i.symmetry_sha = i.svg_sha256 THEN i.symmetry END AS axes,
  COALESCE((SELECT CASE WHEN f.reason = 'bad-draw' THEN 'bad-stroke' ELSE COALESCE(NULLIF(f.reason, ''), 'other') END
              FROM feedback f WHERE f.icon = i.key AND f.svg_sha256 = i.svg_sha256 ORDER BY f.id DESC LIMIT 1), 'missing') AS reason,
  EXISTS (SELECT 1 FROM feedback f WHERE f.icon = i.key) AS has_feedback,
  (r.status = 'pending' AND COALESCE(r.worker, '') != '') AS cannot_fix,
  (CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END) AS picked
FROM icons i
LEFT JOIN reviews r ON r.icon = i.key AND r.svg_sha256 = i.svg_sha256
LEFT JOIN split_requests sp ON sp.icon = i.key AND sp.svg_sha256 = i.svg_sha256 AND sp.active = 1
LEFT JOIN store_documents d ON d.store = 'icon-artwork' AND d.key = i.key AND i.uploaded = 0
LEFT JOIN icon_graphs g ON g.svg_sha256 = i.svg_sha256;

CREATE TRIGGER icon_state_review_insert AFTER INSERT ON reviews BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.icon; END;
CREATE TRIGGER icon_state_review_update AFTER UPDATE ON reviews BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key IN (OLD.icon, NEW.icon); END;
CREATE TRIGGER icon_state_review_delete AFTER DELETE ON reviews BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = OLD.icon; END;
CREATE TRIGGER icon_state_split_insert AFTER INSERT ON split_requests BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.icon; END;
CREATE TRIGGER icon_state_split_update AFTER UPDATE ON split_requests BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key IN (OLD.icon, NEW.icon); END;
CREATE TRIGGER icon_state_split_delete AFTER DELETE ON split_requests BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = OLD.icon; END;
CREATE TRIGGER icon_state_feedback_insert AFTER INSERT ON feedback BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.icon; END;
CREATE TRIGGER icon_state_feedback_update AFTER UPDATE ON feedback BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key IN (OLD.icon, NEW.icon); END;
CREATE TRIGGER icon_state_feedback_delete AFTER DELETE ON feedback BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = OLD.icon; END;
CREATE TRIGGER icon_state_pick_insert AFTER INSERT ON store_documents WHEN NEW.store = 'icon-artwork' BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.key; END;
CREATE TRIGGER icon_state_pick_update AFTER UPDATE ON store_documents WHEN NEW.store = 'icon-artwork' BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key IN (OLD.key, NEW.key); END;
CREATE TRIGGER icon_state_pick_delete AFTER DELETE ON store_documents WHEN OLD.store = 'icon-artwork' BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = OLD.key; END;
CREATE TRIGGER icon_state_graph_insert AFTER INSERT ON icon_graphs BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE svg_sha256 = NEW.svg_sha256; END;
CREATE TRIGGER icon_state_icon_insert AFTER INSERT ON icons BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.key; END;
CREATE TRIGGER icon_state_icon_update AFTER UPDATE OF svg_sha256, build_failed, family, uploaded, artwork_source, stroke_count,
  segment_count, symmetry, symmetry_sha ON icons BEGIN UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key = NEW.key; END;
CREATE INDEX icons_svg_sha256 ON icons(svg_sha256);

-- Counts by family, side role, state, category and failed build: the review tabs, categories and totals read these.
CREATE TABLE icon_counts (family TEXT NOT NULL, side_role TEXT NOT NULL, state TEXT NOT NULL, category TEXT NOT NULL,
  built_failed INTEGER NOT NULL, n INTEGER NOT NULL, PRIMARY KEY(family, side_role, state, category, built_failed));
INSERT INTO icon_counts SELECT COALESCE(icons.family, ''), COALESCE(icons.side_role, ''), COALESCE(icons.state, ''), COALESCE(icons.category, ''), icons.build_failed, COUNT(*) FROM icons GROUP BY 1, 2, 3, 4, 5;
CREATE TRIGGER icon_counts_insert AFTER INSERT ON icons BEGIN INSERT INTO icon_counts(family, side_role, state, category, built_failed, n) VALUES (COALESCE(NEW.family, ''), COALESCE(NEW.side_role, ''), COALESCE(NEW.state, ''), COALESCE(NEW.category, ''), NEW.build_failed, 1) ON CONFLICT(family, side_role, state, category, built_failed) DO UPDATE SET n = n + 1; END;
CREATE TRIGGER icon_counts_delete AFTER DELETE ON icons BEGIN UPDATE icon_counts SET n = n - 1 WHERE (family, side_role, state, category, built_failed) = (COALESCE(OLD.family, ''), COALESCE(OLD.side_role, ''), COALESCE(OLD.state, ''), COALESCE(OLD.category, ''), OLD.build_failed); END;
CREATE TRIGGER icon_counts_update AFTER UPDATE OF family, side_role, state, category, build_failed ON icons BEGIN
  UPDATE icon_counts SET n = n - 1 WHERE (family, side_role, state, category, built_failed) = (COALESCE(OLD.family, ''), COALESCE(OLD.side_role, ''), COALESCE(OLD.state, ''), COALESCE(OLD.category, ''), OLD.build_failed);
  INSERT INTO icon_counts(family, side_role, state, category, built_failed, n) VALUES (COALESCE(NEW.family, ''), COALESCE(NEW.side_role, ''), COALESCE(NEW.state, ''), COALESCE(NEW.category, ''), NEW.build_failed, 1) ON CONFLICT(family, side_role, state, category, built_failed) DO UPDATE SET n = n + 1;
END;
-- The filter choices: authors and families of every icon, keyshapes and categories of built ones, and how many are built.
CREATE TABLE icon_facet_counts (kind TEXT NOT NULL, value TEXT NOT NULL, n INTEGER NOT NULL, PRIMARY KEY(kind, value));
INSERT INTO icon_facet_counts SELECT 'author', COALESCE(author, 'unknown'), COUNT(*) FROM icons GROUP BY 2;
INSERT INTO icon_facet_counts SELECT 'family', COALESCE(family, ''), COUNT(*) FROM icons GROUP BY 2;
INSERT INTO icon_facet_counts SELECT 'total', 'built', COUNT(*) FROM icons WHERE NOT build_failed;
CREATE TRIGGER icon_facets_insert AFTER INSERT ON icons BEGIN
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'author', COALESCE(NEW.author, 'unknown'), 1 WHERE 1 ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'family', COALESCE(NEW.family, ''), 1 WHERE 1 ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'keyshape', NEW.keyshape, 1 WHERE NEW.keyshape IS NOT NULL AND NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'category', NEW.category, 1 WHERE COALESCE(NEW.category, '') != '' AND NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'total', 'built', 1 WHERE NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
END;
CREATE TRIGGER icon_facets_delete AFTER DELETE ON icons BEGIN
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'author' AND value = COALESCE(OLD.author, 'unknown') AND 1;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'family' AND value = COALESCE(OLD.family, '') AND 1;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'keyshape' AND value = OLD.keyshape AND OLD.keyshape IS NOT NULL AND NOT OLD.build_failed;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'category' AND value = OLD.category AND COALESCE(OLD.category, '') != '' AND NOT OLD.build_failed;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'total' AND value = 'built' AND NOT OLD.build_failed;
END;
CREATE TRIGGER icon_facets_update AFTER UPDATE OF author, family, keyshape, category, build_failed ON icons BEGIN
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'author' AND value = COALESCE(OLD.author, 'unknown') AND 1;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'family' AND value = COALESCE(OLD.family, '') AND 1;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'keyshape' AND value = OLD.keyshape AND OLD.keyshape IS NOT NULL AND NOT OLD.build_failed;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'category' AND value = OLD.category AND COALESCE(OLD.category, '') != '' AND NOT OLD.build_failed;
  UPDATE icon_facet_counts SET n = n - 1 WHERE kind = 'total' AND value = 'built' AND NOT OLD.build_failed;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'author', COALESCE(NEW.author, 'unknown'), 1 WHERE 1 ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'family', COALESCE(NEW.family, ''), 1 WHERE 1 ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'keyshape', NEW.keyshape, 1 WHERE NEW.keyshape IS NOT NULL AND NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'category', NEW.category, 1 WHERE COALESCE(NEW.category, '') != '' AND NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
  INSERT INTO icon_facet_counts(kind, value, n) SELECT 'total', 'built', 1 WHERE NOT NEW.build_failed ON CONFLICT(kind, value) DO UPDATE SET n = n + 1;
END;

-- Search text, trigram-indexed: substrings of three or more characters are found without reading every icon.
CREATE VIRTUAL TABLE icon_search USING fts5(search, key UNINDEXED, tokenize = 'trigram');
INSERT INTO icon_search(search, key) SELECT search, key FROM icons;
CREATE TRIGGER icon_search_insert AFTER INSERT ON icons BEGIN INSERT INTO icon_search(search, key) VALUES (NEW.search, NEW.key); END;
CREATE TRIGGER icon_search_delete AFTER DELETE ON icons BEGIN DELETE FROM icon_search WHERE key = OLD.key; END;
CREATE TRIGGER icon_search_update AFTER UPDATE OF search ON icons BEGIN
  DELETE FROM icon_search WHERE key = OLD.key;
  INSERT INTO icon_search(search, key) VALUES (NEW.search, NEW.key);
END;

-- The list's orders, within a family and across families, by state where tabs pick one.
CREATE INDEX icons_list_family_state ON icons(family, state, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_family ON icons(family, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_state ON icons(state, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_name ON icons(sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_created_asc ON icons(family, COALESCE(created_ms, 9223372036854775807), sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_created_desc ON icons(family, COALESCE(created_ms, -9223372036854775807) DESC, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_modified_asc ON icons(family, COALESCE(modified_ms, 9223372036854775807), sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_modified_desc ON icons(family, COALESCE(modified_ms, -9223372036854775807) DESC, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_strokes_asc ON icons(family, COALESCE(strokes, 9223372036854775807), sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_strokes_desc ON icons(family, COALESCE(strokes, -9223372036854775807) DESC, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_segments_asc ON icons(family, COALESCE(segments, 9223372036854775807), sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_list_segments_desc ON icons(family, COALESCE(segments, -9223372036854775807) DESC, sort_name COLLATE NOCASE, key COLLATE NOCASE);
CREATE INDEX icons_actor ON icons(actor, state);
CREATE INDEX icons_side_role ON icons(side_role, sort_name COLLATE NOCASE);
CREATE INDEX icons_version_group ON icons(version_group);
CREATE INDEX icons_variant_of ON icons(family, variant_of);
CREATE INDEX feedback_author ON feedback(author, icon);
