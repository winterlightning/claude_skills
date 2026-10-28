//! Native72 container uploads use their existing identity; browser-created pairs use canonical keys.
/// `reference` is a trusted SQL expression, never request text. Start from that
/// reference's indexed links. CROSS JOIN keeps SQLite from reversing the join
/// and searching the entire container family for each reference instead.
pub(crate) fn container72_icon(reference: &str) -> String {
    format!("SELECT x.key FROM icon_references ir CROSS JOIN icons x ON x.key = ir.icon
        WHERE ir.reference_id = {reference} AND x.family = 'container-combination-72'
        ORDER BY x.key LIMIT 1")
}

pub const EXISTING_CONTAINER72: &str = "SELECT i.key, i.icon_id, i.uploaded, i.name, i.record, i.svg_sha256, i.original_sources FROM icons i WHERE i.key IN (SELECT icon FROM icon_references WHERE reference_id = ? UNION SELECT ?) AND i.family = 'container-combination-72' ORDER BY i.key";

// A browser build of an uploaded icon keeps its upload intact, but serves its current revision.
pub const CURRENT_UPLOADED_SVG: &str = "SELECT svg FROM revisions WHERE svg_sha256 = ?1 UNION ALL SELECT svg FROM uploaded_icons WHERE icon = ?2 AND NOT EXISTS (SELECT 1 FROM revisions WHERE svg_sha256 = ?1) LIMIT 1";
