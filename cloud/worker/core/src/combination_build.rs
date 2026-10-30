//! Atomic guards and artwork selection for explicit container rebuilds.

pub const GUARD: &str = "INSERT INTO combination_build_guard(ok) SELECT NULL
    WHERE (SELECT svg_sha256 FROM icons WHERE key = ?1) IS NOT ?2
       OR (SELECT document FROM store_documents WHERE store = 'icon-artwork' AND key = ?1) IS NOT ?3
       OR EXISTS (SELECT 1 FROM json_each(?4) p LEFT JOIN icons i ON i.key = p.key
                  WHERE i.svg_sha256 IS NOT json_extract(p.value, '$.svg_sha256'))";

// Keep uploaded candidates and browser edits available in Pick, and retain their revision rows.
// Increment the choice revision so a stale Pick tab cannot reselect its older drawing after this build.
pub const SELECT_BUILD: &str = "UPDATE store_documents SET document = json_set(document,
    '$.source_mode', 'use_org', '$.source_svg_sha256', ?2, '$.selected_svg_sha256', ?2,
    '$.revision', COALESCE(json_extract(document, '$.revision'), 0) + 1,
    '$.updated_at', ?3, '$.updated_by', ?4, '$.selected_at', ?3, '$.selected_by', ?4),
    updated_at = ?3, updated_by = ?4 WHERE store = 'icon-artwork' AND key = ?1";

pub fn is_conflict(message: &str) -> bool {
    message.contains("NOT NULL constraint failed: combination_build_guard.ok")
}
