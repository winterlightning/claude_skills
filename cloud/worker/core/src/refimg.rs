//! Uploaded reference images (SVG or PNG) — ported from reference_images.py.

use sha2::{Digest, Sha256};

pub const MAX_IMAGES: usize = 4;
pub const PNG_LIMIT: usize = 2 * 1024 * 1024;
pub const SVG_LIMIT: usize = 1024 * 1024;
const PNG_SIGNATURE: &[u8] = b"\x89PNG\r\n\x1a\n";

pub fn limit(kind: &str) -> usize {
    if kind == "png" { PNG_LIMIT } else { SVG_LIMIT }
}

pub fn mime(kind: &str) -> &'static str {
    if kind == "png" { "image/png" } else { "image/svg+xml" }
}

pub fn is_id(text: &str) -> bool {
    text.len() == 64 && text.bytes().all(|b| b.is_ascii_digit() || (b'a'..=b'f').contains(&b))
}

/// `_kind`: png by signature, else a well-formed SVG root without DTDs.
pub fn kind(data: &[u8]) -> Result<&'static str, String> {
    if data.starts_with(PNG_SIGNATURE) {
        return Ok("png");
    }
    let generic = || "Reference images must be SVG or PNG files.".to_string();
    let text = std::str::from_utf8(data).map_err(|_| generic())?;
    if crate::svg::declares_dtd(text) {
        return Err("SVG references may not declare a DOCTYPE or entities.".into());
    }
    if !crate::svg::root_is_svg(text) {
        return Err(generic());
    }
    Ok("svg")
}

/// `_name`: a safe display name ending in the detected kind.
pub fn name(original: Option<&str>, kind: &str) -> String {
    let base = original.unwrap_or("").rsplit(['/', '\\']).next().unwrap_or("");
    let stem = match base.rfind('.') {
        Some(0) | None => base,
        Some(dot) => &base[..dot],
    }.to_lowercase();
    let mut cleaned = String::new();
    let mut dash = false;
    for c in stem.chars() {
        if c.is_ascii_lowercase() || c.is_ascii_digit() || matches!(c, '.' | '_' | '-') {
            cleaned.push(c);
            dash = false;
        } else if !dash {
            cleaned.push('-');
            dash = true;
        }
    }
    let trimmed: String = cleaned.trim_matches(|c| matches!(c, '.' | '-' | '_')).chars().take(72).collect();
    format!("{}.{kind}", if trimmed.is_empty() { "reference" } else { &trimmed })
}

pub fn id(data: &[u8]) -> String {
    hex::encode(Sha256::digest(data))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn kinds_and_names() {
        assert_eq!(kind(b"\x89PNG\r\n\x1a\nrest").unwrap(), "png");
        assert_eq!(kind(br#"<svg xmlns="http://www.w3.org/2000/svg"/>"#).unwrap(), "svg");
        assert!(kind(b"<html/>").is_err());
        assert!(kind(b"<!DOCTYPE svg><svg/>").unwrap_err().contains("DOCTYPE"));
        assert_eq!(name(Some("My Sketch (1).PNG"), "png"), "my-sketch-1.png");
        assert_eq!(name(None, "svg"), "reference.svg");
        assert!(is_id(&id(b"x")));
    }
}
