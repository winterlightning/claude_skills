//! Native72 container uploads use their existing identity; browser-created pairs use canonical keys.
// Resolve the whole family once, rather than searching it again for every reference.
// min(key) preserves the list's existing ORDER BY key LIMIT 1 duplicate policy.
pub const CONTAINER72_ICONS: &str = "SELECT ir.reference_id, min(i.key) AS icon_key FROM icons i JOIN icon_references ir ON ir.icon = i.key WHERE i.family = 'container-combination-72' GROUP BY ir.reference_id";
pub const EXISTING_CONTAINER72: &str = "SELECT i.key, i.icon_id, i.uploaded, i.name, i.record, i.svg_sha256, i.original_sources FROM icons i WHERE i.key IN (SELECT icon FROM icon_references WHERE reference_id = ? UNION SELECT ?) AND i.family = 'container-combination-72' ORDER BY i.key";

// A browser build of an uploaded icon keeps its upload intact, but serves its current revision.
pub const CURRENT_UPLOADED_SVG: &str = "SELECT svg FROM revisions WHERE svg_sha256 = ?1 UNION ALL SELECT svg FROM uploaded_icons WHERE icon = ?2 AND NOT EXISTS (SELECT 1 FROM revisions WHERE svg_sha256 = ?1) LIMIT 1";
