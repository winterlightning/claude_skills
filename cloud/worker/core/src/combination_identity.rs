//! Native72 container uploads use their existing identity; browser-created pairs use canonical keys.
pub const ICON_KEY72: &str = "CASE WHEN c.kind = 'container' THEN COALESCE((SELECT x.key FROM icons x JOIN icon_references ir ON ir.icon = x.key WHERE ir.reference_id = c.reference_id AND x.family = 'container-combination-72' ORDER BY x.key LIMIT 1), 'container-combination-72/' || c.reference_id) ELSE 'combination-72/' || c.reference_id END";
pub const EXISTING_CONTAINER72: &str = "SELECT DISTINCT i.key, i.icon_id, i.uploaded, i.name, i.record, i.svg_sha256, i.original_sources FROM icons i LEFT JOIN icon_references r ON r.icon = i.key WHERE i.family = 'container-combination-72' AND (r.reference_id = ? OR i.key = ?) ORDER BY i.key";

// A browser build of an uploaded icon keeps its upload intact, but serves its current revision.
pub const CURRENT_UPLOADED_SVG: &str = "SELECT svg FROM revisions WHERE svg_sha256 = ?1 UNION ALL SELECT svg FROM uploaded_icons WHERE icon = ?2 AND NOT EXISTS (SELECT 1 FROM revisions WHERE svg_sha256 = ?1) LIMIT 1";
