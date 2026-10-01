//! What Icon review lists, filters and sorts an icon by, worked out once from its catalog record when the record is
//! stored (catalog push, upload, combination build) rather than in the browser over the whole catalog.
//! Mirrors gallery.html: `strokeCount`, `segmentCount`, `versionGroupKey`, `iconVersion`, `matchesSearch`'s text.

use chrono::DateTime;
use serde_json::{json, Map, Value};

/// The record fields a review card shows (the full record is fetched when the icon is opened).
const CARD_FIELDS: [&str; 24] = ["key", "icon_id", "name", "family", "category", "profile", "canvas_size", "canvas_width",
    "canvas_height", "sizing_mode", "keyshape", "keyshape_bounds", "preview_url", "svg_sha256", "uploaded_icon", "author",
    "build_failed", "errors", "status", "variant_of", "variant_root", "variant_label", "reference_fidelity", "side_role"];

#[derive(Clone, Debug, Default, PartialEq)]
pub struct IconIndex {
    /// The card record (JSON text).
    pub card: String,
    /// Lowercased text `matchesSearch` looks in.
    pub search: String,
    pub sort_name: String,
    pub keyshape: Option<String>,
    pub author: Option<String>,
    pub side_role: Option<String>,
    /// Strokes and segments of the generated model; None when the record has no model to count.
    pub stroke_count: Option<i64>,
    pub segment_count: Option<i64>,
    pub created_ms: Option<i64>,
    pub modified_ms: Option<i64>,
    /// `versionGroupKey`: family/root, and the version number within it (`iconVersion`).
    pub version_group: String,
    pub version: i64,
    pub variant: bool,
    pub has_original: bool,
    /// The artwork the record itself says it shows (a pick made since the push overrides it, see icon_query).
    pub artwork_source: Option<String>,
    /// Measured mirror axes (review-facets.json) and the drawing they were measured on.
    pub symmetry: Option<String>,
    pub symmetry_sha: Option<String>,
}

fn text<'a>(record: &'a Value, field: &str) -> Option<&'a str> {
    record.get(field).and_then(Value::as_str).filter(|s| !s.is_empty())
}

/// JS truthiness of a record field, as `Boolean(icon.field)`.
fn truthy(value: &Value) -> bool {
    match value {
        Value::Null => false,
        Value::Bool(b) => *b,
        Value::Number(n) => n.as_f64().is_some_and(|f| f != 0.0),
        Value::String(s) => !s.is_empty(),
        _ => true,
    }
}

/// `modelAvailable`: a generated drawing shown as built, with its stroke model.
fn model_available(record: &Value) -> bool {
    !truthy(&record["uploaded_icon"])
        && text(record, "artwork_source").is_none_or(|s| s == "use_org")
        && record["primitives"].is_array()
}

/// `strokeCount`: one per contour, plus each primitive no contour claims.
pub fn stroke_count(record: &Value) -> Option<i64> {
    if !model_available(record) {
        return None;
    }
    let contours = record["contours"].as_array().cloned().unwrap_or_default();
    let claimed: Vec<&Value> = contours.iter().filter_map(|c| c["members"].as_array()).flatten().collect();
    let free = record["primitives"].as_array()?.iter().filter(|p| !claimed.contains(&&p["element_id"])).count();
    Some((contours.len() + free) as i64)
}

/// `segmentCount`: a bezier counts its segments (at least one), anything else one.
pub fn segment_count(record: &Value) -> Option<i64> {
    if !model_available(record) {
        return None;
    }
    Some(record["primitives"].as_array()?.iter().map(|p| {
        if p["kind"] == "bezier" { p["segments"].as_array().map_or(0, Vec::len).max(1) as i64 } else { 1 }
    }).sum())
}

fn millis(record: &Value, field: &str) -> Option<i64> {
    DateTime::parse_from_rfc3339(text(record, field)?).ok().map(|t| t.timestamp_millis())
}

/// `iconVersion` as a number: v1 for an original, the `-vN` suffix (else 2) for a revision.
fn version(record: &Value) -> i64 {
    if !truthy(&record["variant_of"]) {
        return 1;
    }
    let id = text(record, "icon_id").unwrap_or("");
    id.rsplit_once("-v").and_then(|(_, n)| (!n.is_empty() && n.bytes().all(|b| b.is_ascii_digit())).then(|| n.parse().ok()).flatten())
        .unwrap_or(2)
}

/// The words `matchesSearchExceptCategory` joins (missing fields join as empty text, like Array.join).
fn search_text(record: &Value) -> String {
    let mut words: Vec<String> = ["name", "icon_id", "variant_label", "variant_root", "category"].iter()
        .map(|f| record[*f].as_str().unwrap_or("").to_string()).collect();
    for list in ["keywords", "aliases"] {
        for word in record[list].as_array().into_iter().flatten() {
            words.push(match word { Value::String(s) => s.clone(), Value::Null => String::new(), other => other.to_string() });
        }
    }
    words.join(" ").to_lowercase()
}

/// The card: the shown fields, the first original's URL and the validation summary `checkIssues` reads.
fn card(record: &Value) -> Value {
    let mut card = Map::new();
    for field in CARD_FIELDS {
        if let Some(value) = record.get(field).filter(|v| !v.is_null()) {
            card.insert(field.into(), value.clone());
        }
    }
    if let Some(first) = record["original_sources"].as_array().and_then(|s| s.first()) {
        card.insert("original_sources".into(), json!([{"url": first["url"]}]));
    }
    if let Some(validation) = record["validation"].as_object() {
        let summary: Map<String, Value> = ["status", "automatic_status", "exception"].iter()
            .filter_map(|k| validation.get(*k).map(|v| (k.to_string(), v.clone()))).collect();
        card.insert("validation".into(), Value::Object(summary));
    }
    Value::Object(card)
}

/// Mirror axes in a fixed order, comma-joined ("" = measured, none).
fn axes(facet: &Value) -> Option<String> {
    let list = facet["axes"].as_array()?;
    Some(["vertical", "horizontal"].iter().filter(|a| list.iter().any(|v| v == **a)).copied().collect::<Vec<_>>().join(","))
}

pub fn index(record: &Value, facet: Option<&Value>) -> IconIndex {
    let family = record["family"].as_str().unwrap_or("");
    let icon_id = record["icon_id"].as_str().unwrap_or("");
    let root = text(record, "variant_root").or_else(|| text(record, "variant_of")).unwrap_or(icon_id);
    IconIndex {
        card: card(record).to_string(),
        search: search_text(record),
        sort_name: text(record, "name").unwrap_or(icon_id).to_string(),
        keyshape: text(record, "keyshape").map(str::to_string),
        author: text(record, "author").map(str::to_string),
        side_role: text(record, "side_role").map(str::to_string),
        stroke_count: stroke_count(record),
        segment_count: segment_count(record),
        created_ms: millis(record, "created_at"),
        modified_ms: millis(record, "modified_at"),
        version_group: format!("{family}/{root}"),
        version: version(record),
        variant: truthy(&record["variant_of"]),
        has_original: record["original_sources"].as_array().is_some_and(|s| !s.is_empty()),
        artwork_source: text(record, "artwork_source").map(str::to_string),
        symmetry: facet.and_then(axes),
        symmetry_sha: facet.and_then(|f| text(f, "svg_sha256")).map(str::to_string),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn record() -> Value {
        json!({"key": "solo/cup", "icon_id": "cup", "name": "Cup", "family": "solo", "category": "food",
               "keywords": ["mug", null], "aliases": ["Beaker"], "artwork_source": "use_org",
               "primitives": [{"kind": "line", "element_id": "a"}, {"kind": "bezier", "element_id": "b", "segments": [1, 2, 3]},
                              {"kind": "bezier", "element_id": "c", "segments": []}],
               "contours": [{"members": ["a", "b"]}], "created_at": "2026-09-01T10:00:00+07:00",
               "validation": {"status": "valid", "errors": [], "exception": null, "negative_space": {"big": true}},
               "original_sources": [{"url": "originals/x.svg", "source_path": "p"}, {"url": "originals/y.svg"}],
               "python_source": {"path": "m.py"}})
    }

    #[test]
    fn counts_strokes_and_segments_like_the_page() {
        let r = record();
        assert_eq!(stroke_count(&r), Some(2)); // one contour + the unclaimed "c"
        assert_eq!(segment_count(&r), Some(5)); // 1 + 3 + max(1, 0)
        let mut edited = r.clone();
        edited["artwork_source"] = json!("use_edited");
        assert_eq!(stroke_count(&edited), None);
        let mut uploaded = r;
        uploaded["uploaded_icon"] = json!(true);
        assert_eq!(segment_count(&uploaded), None);
    }

    #[test]
    fn index_fields() {
        let i = index(&record(), Some(&json!({"axes": ["horizontal", "vertical"], "svg_sha256": "s"})));
        assert_eq!(i.search, "cup cup   food mug  beaker");
        assert_eq!(i.version_group, "solo/cup");
        assert_eq!((i.version, i.variant, i.has_original), (1, false, true));
        assert_eq!(i.created_ms, Some(1788231600000));
        assert_eq!(i.symmetry.as_deref(), Some("vertical,horizontal"));
        let card: Value = serde_json::from_str(&i.card).unwrap();
        assert_eq!(card["original_sources"], json!([{"url": "originals/x.svg"}]));
        assert_eq!(card["validation"], json!({"status": "valid", "exception": null}));
        assert!(card.get("primitives").is_none() && card.get("python_source").is_none());
    }

    #[test]
    fn versions() {
        let v = |id: &str, of: Value| index(&json!({"family": "solo", "icon_id": id, "variant_of": of, "variant_root": "cup"}), None);
        assert_eq!(v("cup-v3", json!("cup")).version, 3);
        assert_eq!(v("cup-redraw", json!("cup")).version, 2);
        assert_eq!(v("cup", json!("")).version, 1);
        assert_eq!(v("cup-v3", json!("cup")).version_group, "solo/cup");
        assert_eq!(index(&json!({"family": "sub", "icon_id": "x", "variant_root": ""}), Some(&json!({"axes": []}))).symmetry.as_deref(), Some(""));
    }
}
