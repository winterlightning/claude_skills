//! Build validation, atomic guards and artwork selection for explicit rebuilds.

use serde::Deserialize;
use sha2::{Digest, Sha256};

/// Server-resolved native text. Its form is the drawing the side engine embeds.
#[derive(Deserialize)]
pub struct NativeTextPart {
    pub reference_id: String,
    pub role: String,
    pub icon: Option<String>,
    pub svg_sha256: Option<String>,
    pub document: Option<String>,
    pub current_sha: Option<String>,
    pub review: Option<String>,
}

impl NativeTextPart {
    /// A valid but unapproved drawing may be saved as a failed build, like other parts.
    pub fn validate(&self, requested_sha: Option<&str>) -> Result<Option<String>, String> {
        let Some(icon) = self.icon.as_deref() else {
            return Err(format!("The {} has no unambiguous native text icon. Pick an existing drawing.", self.role));
        };
        let Some((sha, document)) = self.svg_sha256.as_deref().zip(self.document.as_deref()) else {
            return Err("The native text form has no drawing or hash. Reload its form before building.".into());
        };
        if requested_sha != Some(sha) || self.current_sha.as_deref() != Some(sha)
            || hex::encode(Sha256::digest(document.as_bytes())) != sha
        {
            return Err("The native text drawing changed. Refresh its form, reload and build again.".into());
        }
        Ok((self.review.as_deref() != Some("approve")).then(|| {
            let name = icon.strip_prefix("text/").unwrap_or(icon);
            format!("Sub {name} is not approved in Icon review")
        }))
    }
}

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
