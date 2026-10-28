//! SQL shared by the combination list, counts and their SQLite regression tests.

use crate::combination_identity::container72_icon;

/// One row per combination and its size-specific state. The upload fallback runs
/// only for container pairs without build metadata; built pairs and totals do not
/// pay for resolving an unused combined icon key.
pub fn cte(size: i64) -> String {
    let (parts, existing) = if size == 72 {
        ("SELECT p.reference_id, p.role, s.icon, s.built_sha, i.svg_sha256 AS current_sha
          FROM reference_parts p LEFT JOIN reference_part_sizes s ON s.reference_id = p.reference_id AND s.role = p.role AND s.size = 72
          LEFT JOIN icons i ON i.key = s.icon",
         format!("CASE WHEN max(pt.role IN ('container', 'symbol')) AND EXISTS ({}) THEN 'built' ELSE 'unbuilt' END",
             container72_icon("r.reference_id")))
    } else {
        ("SELECT p.reference_id, p.role, p.icon, p.built_sha, i.svg_sha256 AS current_sha
          FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon",
         "'unbuilt'".into())
    };
    format!("WITH parts AS ({parts}),
combos AS (
    SELECT r.reference_id, r.concept,
        CASE WHEN max(pt.role IN ('container', 'symbol')) THEN 'container' ELSE 'side' END AS kind,
        CASE WHEN count(pt.built_sha) = 0 THEN {existing}
             WHEN max(pt.built_sha IS NOT NULL AND pt.current_sha IS NOT NULL AND pt.built_sha != pt.current_sha) THEN 'stale'
             ELSE 'built' END AS state,
        max(pt.icon IS NULL) AS missing
    FROM \"references\" r JOIN parts pt ON pt.reference_id = r.reference_id
    WHERE r.kind = 'combination' GROUP BY r.reference_id)")
}

/// The combined icon expression for a `combos c` row, used only by callers that
/// need artwork identity. Preserve the smallest linked key and canonical fallback.
pub fn icon_key(size: i64) -> String {
    if size == 72 {
        format!("CASE WHEN c.kind = 'container' THEN COALESCE(({}), 'container-combination-72/' || c.reference_id) ELSE 'combination-72/' || c.reference_id END",
            container72_icon("c.reference_id"))
    } else {
        "c.kind || '_combination64/' || c.reference_id".into()
    }
}

/// `filter` contains only the route's SQL predicates; user values remain bound parameters.
pub fn page(size: i64, filter: &str) -> String {
    format!("{}
        SELECT c.reference_id, c.concept, c.kind, c.state, i.key AS icon_key, i.svg_sha256 AS icon_sha,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM combos c LEFT JOIN icons i ON i.key = {}
        {filter} ORDER BY c.reference_id LIMIT ? OFFSET ?", cte(size), icon_key(size))
}
