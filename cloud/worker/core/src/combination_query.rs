//! SQL shared by the combination list, counts and their SQLite regression tests.

use crate::combination_identity::CONTAINER72_ICONS;

/// One row per combination, including its size-specific state and combined icon key.
/// Uploaded container72 identities are grouped once and joined by reference, so both
/// the state fallback and the icon lookup avoid correlated scans of the icon family.
pub fn cte(size: i64) -> String {
    let (identities, parts, join, existing, icon_key) = if size == 72 {
        (format!("container72_icons AS MATERIALIZED ({CONTAINER72_ICONS}),"),
         "SELECT p.reference_id, p.role, s.icon, s.built_sha, i.svg_sha256 AS current_sha
          FROM reference_parts p LEFT JOIN reference_part_sizes s ON s.reference_id = p.reference_id AND s.role = p.role AND s.size = 72
          LEFT JOIN icons i ON i.key = s.icon",
         "LEFT JOIN container72_icons ci ON ci.reference_id = r.reference_id",
         "CASE WHEN max(pt.role IN ('container', 'symbol')) AND max(ci.icon_key) IS NOT NULL THEN 'built' ELSE 'unbuilt' END",
         "CASE WHEN max(pt.role IN ('container', 'symbol')) THEN COALESCE(max(ci.icon_key), 'container-combination-72/' || r.reference_id) ELSE 'combination-72/' || r.reference_id END")
    } else {
        (String::new(),
         "SELECT p.reference_id, p.role, p.icon, p.built_sha, i.svg_sha256 AS current_sha
          FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon",
         "", "'unbuilt'",
         "CASE WHEN max(pt.role IN ('container', 'symbol')) THEN 'container_combination64/' ELSE 'side_combination64/' END || r.reference_id")
    };
    format!("WITH {identities} parts AS ({parts}),
combos AS (
    SELECT r.reference_id, r.concept,
        CASE WHEN max(pt.role IN ('container', 'symbol')) THEN 'container' ELSE 'side' END AS kind,
        CASE WHEN count(pt.built_sha) = 0 THEN {existing}
             WHEN max(pt.built_sha IS NOT NULL AND pt.current_sha IS NOT NULL AND pt.built_sha != pt.current_sha) THEN 'stale'
             ELSE 'built' END AS state,
        max(pt.icon IS NULL) AS missing,
        {icon_key} AS icon_key
    FROM \"references\" r JOIN parts pt ON pt.reference_id = r.reference_id
    {join}
    WHERE r.kind = 'combination' GROUP BY r.reference_id)")
}

/// `filter` contains only the route's SQL predicates; user values remain bound parameters.
pub fn page(size: i64, filter: &str) -> String {
    format!("{}
        SELECT c.reference_id, c.concept, c.kind, c.state, i.key AS icon_key, i.svg_sha256 AS icon_sha,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM combos c LEFT JOIN icons i ON i.key = c.icon_key
        {filter} ORDER BY c.reference_id LIMIT ? OFFSET ?", cte(size))
}
