-- Browser Edit and Manual Edit also support uploaded icons, including solo-64.
-- 0015 excluded their choices, so list cards kept the original thumbnail URL and
-- edited uploads disappeared from the Edited filter. Match uploaded choices to
-- the current source or selected hash; an unrelated replacement must not revive
-- an old choice. A selected revision remains selected even after its graph loads.
DROP VIEW icon_state;
CREATE VIEW icon_state AS SELECT i.key AS key,
  (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) AS decision,
  (CASE WHEN sp.icon IS NOT NULL THEN sp.created_by WHEN (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN NULLIF((SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1), '') ELSE r.updated_by END) AS actor,
  (CASE WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) = 'rejected' THEN 'rejected'
              WHEN i.family IN ('side_combination64', 'container_combination64') AND i.build_failed AND (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) != 'pending' THEN 'failed'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) IN ('pending', 'claimed') THEN 'pending'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) IN ('ready', 're-generated') AND i.build_failed THEN 'failed'
              WHEN (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) = 're-generated' THEN 'ready'
              ELSE (CASE WHEN sp.icon IS NOT NULL OR (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) IS NOT NULL THEN 'rejected' ELSE COALESCE(r.status, 'ready') END) END) AS state,
  COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') AS mode,
  (CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_edited' THEN 'edited' WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_upload' OR (i.uploaded AND COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org') THEN 'uploaded'
              WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'work_fix' THEN 'work_fix' ELSE 'original' END) AS artwork,
  CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org' THEN i.stroke_count END AS strokes,
  CASE WHEN COALESCE((CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END), i.artwork_source, 'use_org') = 'use_org' THEN i.segment_count END AS segments,
  CASE WHEN i.symmetry_sha = i.svg_sha256 THEN i.symmetry END AS axes,
  COALESCE((SELECT CASE WHEN f.reason = 'bad-draw' THEN 'bad-stroke' ELSE COALESCE(NULLIF(f.reason, ''), 'other') END
              FROM feedback f WHERE f.icon = i.key AND f.svg_sha256 = i.svg_sha256 ORDER BY f.id DESC LIMIT 1), 'missing') AS reason,
  EXISTS (SELECT 1 FROM feedback f WHERE f.icon = i.key) AS has_feedback,
  (r.status = 'pending' AND COALESCE(r.worker, '') != '') AS cannot_fix,
  (CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL) THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END) AS picked
FROM icons i
LEFT JOIN reviews r ON r.icon = i.key AND r.svg_sha256 = i.svg_sha256
LEFT JOIN split_requests sp ON sp.icon = i.key AND sp.svg_sha256 = i.svg_sha256 AND sp.active = 1
LEFT JOIN store_documents d ON d.store = 'icon-artwork' AND d.key = i.key
  AND (i.uploaded = 0 OR json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256
       OR json_extract(d.document, '$.selected_svg_sha256') = i.svg_sha256)
LEFT JOIN icon_graphs g ON g.svg_sha256 = i.svg_sha256;

-- Repair existing choices without changing drawings, reviews or counts.
-- Only artwork fields change: icon_counts does not group by any of these fields.
UPDATE icons SET (mode, artwork, strokes, segments, picked) =
  (SELECT v.mode, v.artwork, v.strokes, v.segments, v.picked FROM icon_state v WHERE v.key = icons.key)
WHERE key IN (SELECT key FROM store_documents WHERE store = 'icon-artwork');
