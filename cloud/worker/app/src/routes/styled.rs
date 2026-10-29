//! Round and sharp records of icons (corner_processing) and the fill variants of the 64 side pairs' parts:
//! POST /api/icons/styled.
//!
//! Each item `{source_key, style, svg, check, expected_sha256}` stores `<source_key>--<style>` as its own icon in the
//! source's family, with style round or sharp and style_of the source (migration 0019; the record field is
//! `icon_style`, since a record's `style` is its stroke style), so the list shows it under that style and it is
//! reviewed on its own. A side pair part (a solo, container or sub icon) has several fill variants (`{source_key, style: "fill", variant?, svg}`):
//! `<source_key>--fill` is its fill (variant current / fill), `<source_key>--fill-<variant>` the others (region-3,
//! group-wheels…); a fill has no corner check and keeps its source's canvas. A part's first fill also makes it a
//! filled part of the fill side pairs and lets the pairs that waited for one be picked (core side_fill FIRST_FILL).
//! Send `expected_sha256` (the drawing you replace, or null to only create) so a newer drawing is never overwritten. It is kept like an upload (uploaded_icons + revisions), so artwork serving and Pick work as
//! for any uploaded icon. A new drawing starts Ready; one whose corner check failed is a failed build (the Failed tab).
//!
//! Sending the same drawing with the same check changes nothing. The same drawing with another check result changes
//! only the record's check and failed flag. A different drawing replaces the record's like a re-upload
//! (`edits::replaced_drawing`): Ready again, its feedback resolved and any pick or Browser Edit made from the old
//! drawing dropped, so the new one is what is shown. A record people have worked on (a pick, a saved edit, a review
//! other than Ready, or feedback) is kept and reported in `kept_manual` unless the request says `replace: true`.
//! `expected_sha256` is the drawing the publisher last saw (null for none): a record that changed since is a
//! conflict, and the write itself only lands on the drawing read here. `results` gives each stored or unchanged
//! record's key, drawing and outcome, which the publisher remembers to send only what changed next time.

use crate::args;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::collections::HashSet;
use worker::{Response, Result};

const MAX_ITEMS: usize = 50;
const CHECKS: [&str; 3] = ["ok", "contact", "fail"];
/// The families whose icons have fill variants: the mains (solo, a few container) and subs of the 64 side pairs.
const FILL_FAMILIES: [&str; 3] = ["solo", "container", "sub"];

/// The record an item stores: `<source_key>--<style>`, or for a fill variant other than the fill itself
/// `<source_key>--fill-<variant>`. None for a variant that is not a short lowercase name.
fn styled_key(item: &Value) -> Option<String> {
    let (source, style) = (item["source_key"].as_str()?, item["style"].as_str()?);
    match item["variant"].as_str().filter(|_| style == "fill") {
        None | Some("current" | "fill") => Some(format!("{source}--{style}")),
        Some(v) if (1..=60).contains(&v.len()) && v.bytes().all(|b| b.is_ascii_lowercase() || b.is_ascii_digit() || b == b'-') =>
            Some(format!("{source}--fill-{v}")),
        Some(_) => None,
    }
}

/// The fill variant a styled key names (current for a main's fill, fill for a sub's), or None for another key.
pub fn fill_variant<'a>(key: &'a str, source: &str) -> Option<&'a str> {
    let rest = key.strip_prefix(source)?.strip_prefix("--fill")?;
    if rest.is_empty() { Some(if source.starts_with("sub/") { "fill" } else { "current" }) } else { rest.strip_prefix('-').filter(|v| !v.is_empty()) }
}

#[derive(Deserialize)]
struct Source { key: String, icon_id: Option<String>, name: Option<String>, family: Option<String>, category: Option<String>,
                profile: Option<String>, canvas_size: Option<i64>, record: String }

#[derive(Deserialize)]
struct Existing { key: String, svg_sha256: String, corner_check: Option<String>, created_at: Option<String>, manual: i64 }

/// The styled records that exist already, with what a republish must not lose: a pick or Browser Edit, a review
/// other than Ready of the current drawing (an approval, disapproval or claim) and feedback.
const EXISTING: &str = "SELECT i.key, i.svg_sha256, json_extract(i.record, '$.corner_check') AS corner_check, \
    json_extract(i.record, '$.created_at') AS created_at, \
    (EXISTS (SELECT 1 FROM store_documents d WHERE d.store = 'icon-artwork' AND d.key = i.key) \
     OR EXISTS (SELECT 1 FROM store_documents d WHERE d.store = 'stroke-edits' AND substr(d.key, 1, length(i.key) + 1) = i.key || '@') \
     OR EXISTS (SELECT 1 FROM reviews r WHERE r.icon = i.key AND r.svg_sha256 = i.svg_sha256 AND r.status != 'ready') \
     OR EXISTS (SELECT 1 FROM feedback f WHERE f.icon = i.key)) AS manual \
    FROM icons i WHERE i.key IN (SELECT value FROM json_each(?))";

enum Write { Create, Replace, Check }

pub async fn post_styled(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" && !super::internal::authorized(ctx) {
        return http::error(401, "Sign in or send the push token to store round, sharp and fill icons.");
    }
    let Some(items) = data["items"].as_array().filter(|items| !items.is_empty() && items.len() <= MAX_ITEMS) else {
        return http::error(400, &format!("Send 1 to {MAX_ITEMS} items."));
    };
    let replace = data["replace"] == json!(true);
    let db = &ctx.db;
    let now = iso_utc(chrono::Utc::now());
    let (mut unchanged, mut errors, mut kept_manual, mut results) = (0, Vec::new(), Vec::new(), Vec::new());
    // Every source and every record that exists already, in two reads (not two per item).
    let source_keys: Vec<&str> = items.iter().filter_map(|i| i["source_key"].as_str()).collect();
    let styled_keys: Vec<String> = items.iter().filter_map(styled_key).collect();
    let sources: Vec<Source> = db::all(db, "SELECT key, icon_id, name, family, category, profile, canvas_size, record FROM icons \
        WHERE key IN (SELECT value FROM json_each(?)) AND style = 'normal'", args![json!(source_keys).to_string()]).await?;
    let existing: Vec<Existing> = db::all(db, EXISTING, args![json!(styled_keys).to_string()]).await?;
    let mut seen = HashSet::new();
    // (key, drawing, what the write does, index of its guarded statement in `statements`)
    let mut writes: Vec<(String, String, Write, usize)> = Vec::new();
    let mut statements = Vec::new();
    for item in items {
        let source_key = item["source_key"].as_str().unwrap_or("");
        let style = item["style"].as_str().unwrap_or("");
        let fail = |message: &str| json!({"source_key": source_key, "style": style, "variant": item["variant"], "error": message});
        if !matches!(style, "round" | "sharp" | "fill") {
            errors.push(fail("style must be round, sharp or fill"));
            continue;
        }
        let fill = style == "fill";
        let Some(key) = styled_key(item) else {
            errors.push(fail("variant must be a short lowercase name (letters, digits, hyphens)"));
            continue;
        };
        if !seen.insert(key.clone()) {
            errors.push(fail("this icon and style are listed twice in the request"));
            continue;
        }
        // The corner check is the record's failed flag: a missing or unknown result is refused, never taken as ok.
        // A fill variant has none.
        let check = if fill { None } else {
            let Some(check) = item["check"].as_str().filter(|c| CHECKS.contains(c)) else {
                errors.push(fail("check must be ok, contact or fail"));
                continue;
            };
            Some(check)
        };
        let Some(source) = sources.iter().find(|s| s.key == source_key) else {
            errors.push(fail("no normal icon has this key"));
            continue;
        };
        if fill && !source.family.as_deref().is_some_and(|f| FILL_FAMILIES.contains(&f)) {
            errors.push(fail("only solo, container and sub icons have fill variants"));
            continue;
        }
        let canvas = source.canvas_size.unwrap_or(48);
        // A fill keeps the canvas its source drawing has (a 32 × 40 sub, …).
        let cleaned = if fill { pictographic_core::svg::safe_svg_any_canvas(item["svg"].as_str().unwrap_or("")) }
                      else { pictographic_core::svg::safe_svg(item["svg"].as_str().unwrap_or(""), canvas) };
        let document = match cleaned {
            Ok(document) => document,
            Err(message) => { errors.push(fail(&message)); continue; }
        };
        let digest = hex::encode(Sha256::digest(document.as_bytes()));
        let failed = check == Some("fail");
        let existing = existing.iter().find(|e| e.key == key);
        let expected = match &item["expected_sha256"] {
            Value::Null => None,
            Value::String(sha) => Some(sha.as_str()),
            _ => { errors.push(fail("expected_sha256 must be a sha or null")); continue; }
        };
        if item.get("expected_sha256").is_some() && expected != existing.map(|e| e.svg_sha256.as_str()) {
            errors.push(json!({"source_key": source_key, "style": style, "conflict": true,
                               "error": "this record changed since the publisher read it; fetch and send again",
                               "svg_sha256": existing.map(|e| e.svg_sha256.clone())}));
            continue;
        }
        let same_drawing = existing.is_some_and(|e| e.svg_sha256 == digest);
        if same_drawing && existing.is_some_and(|e| e.corner_check.as_deref() == check) {
            unchanged += 1;
            results.push(json!({"key": key, "svg_sha256": digest, "outcome": "unchanged"}));
            continue;
        }
        if !same_drawing && !replace && existing.is_some_and(|e| e.manual != 0) {
            kept_manual.push(json!({"source_key": source_key, "style": style, "key": key}));
            continue;
        }
        let source_record: Value = serde_json::from_str(&source.record).unwrap_or_else(|_| json!({}));
        let family = source.family.clone().unwrap_or_default();
        let icon_id = format!("{}{}", source.icon_id.clone().unwrap_or_else(|| source.key.rsplit('/').next().unwrap_or("").to_string()),
                              &key[source.key.len()..]);
        let name = source.name.clone().unwrap_or_else(|| icon_id.clone());
        let preview_url = format!("../api/icon-artwork/svg?icon={}&v={digest}", http::percent_encode(&key));
        let created = existing.and_then(|e| e.created_at.clone()).unwrap_or_else(|| now.clone());
        let origin = if fill { "side-fill".to_string() } else { format!("corner-{style}") };
        let mut record = json!({
            "key": key, "icon_id": icon_id, "name": name, "family": family, "profile": source.profile, "canvas_size": canvas,
            "category": source.category, "icon_style": style, "style_of": source.key, "svg_sha256": digest, "uploaded_icon": true,
            "artwork_source": "use_org", "preview_url": preview_url,
            "author": if fill { "fill side pairs".to_string() } else { format!("corner_processing ({style})") },
            "created_at": created, "modified_at": now, "original_sources": source_record["original_sources"].clone(),
            "keywords": source_record["keywords"].clone(), "aliases": source_record["aliases"].clone(),
            "primitives": [], "contours": [], "relationships": [], "anchors": {},
            "style": source_record["style"].as_object().map(|_| source_record["style"].clone()).unwrap_or_else(|| json!({"stroke_width": 4})),
            "keyshape": source_record["keyshape"].clone(), "keyshape_bounds": source_record["keyshape_bounds"].clone(),
            "build_failed": failed, "errors": if failed { json!(["Corner check failed: the output's corners differ from the input's."]) } else { json!([]) },
            "corner_check": check});
        if fill {
            record.as_object_mut().unwrap().remove("corner_check");
            record["fill_variant"] = json!(fill_variant(&key, &source.key));
        }
        let record_text = record.to_string();
        // Out of the counts first, so a record created by someone else meanwhile is not counted twice.
        statements.extend(super::icon_list::uncount(db, &key)?);
        let write = match existing {
            None => {
                // OR IGNORE: a record another publisher created meanwhile is reported, not a failed batch.
                writes.push((key.clone(), digest.clone(), Write::Create, statements.len()));
                statements.push(db::stmt(db, "INSERT OR IGNORE INTO icons(key, icon_id, name, family, category, profile, canvas_size, \
                    svg_sha256, preview_url, original_sources, uploaded, build_failed, record, pushed_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?)",
                    args![key.clone(), icon_id, name, family, source.category.clone(), source.profile.clone(), canvas, digest.clone(),
                          preview_url, record["original_sources"].to_string(), failed as i64, record_text.clone(), now.clone()])?);
                statements.push(db::stmt(db, "INSERT OR IGNORE INTO uploaded_icons VALUES (?, ?, ?)", args![key.clone(), record_text, document.clone()])?);
                Write::Create
            }
            Some(old) => {
                // Guarded on the drawing read above: a record replaced meanwhile is a conflict, written by nobody twice.
                writes.push((key.clone(), digest.clone(), if same_drawing { Write::Check } else { Write::Replace }, statements.len()));
                statements.push(db::stmt(db, "UPDATE icons SET svg_sha256 = ?, preview_url = ?, record = ?, build_failed = ?, pushed_at = ? \
                    WHERE key = ? AND svg_sha256 = ?", args![digest.clone(), preview_url, record_text.clone(), failed as i64, now.clone(),
                                                            key.clone(), old.svg_sha256.clone()])?);
                statements.push(db::stmt(db, "UPDATE uploaded_icons SET record = ?, svg = ? WHERE icon = ? \
                    AND EXISTS (SELECT 1 FROM icons WHERE key = ? AND svg_sha256 = ?)",
                    args![record_text, document.clone(), key.clone(), key.clone(), digest.clone()])?);
                if same_drawing { Write::Check } else { Write::Replace }
            }
        };
        // digest is hex: safe in the guard's SQL text.
        statements.push(super::icon_list::index_statement(db, &key, &record, Some(&format!("svg_sha256 = '{digest}'")))?);
        match write {
            Write::Check => {}
            // A new drawing: Ready, like a re-upload; a pick or Browser Edit of the old drawing no longer shows.
            _ => statements.extend(super::edits::replaced_drawing(db, &key, &document, &digest, &origin, true, user, &now,
                details(vec![("status", json!("ready")), ("svg_sha256", json!(digest)), ("artwork_source", json!(origin.clone()))]))?),
        }
        statements.extend(super::icon_list::recount(db, &key, matches!(write, Write::Create))?);
        if fill {
            // A part's first fill makes it a filled part of the fill side pairs, and the pairs that waited for a fill
            // can be picked (no change once the part is filled).
            let all = args![source.key.clone(), now.clone(), pictographic_core::side_fill::NO_FILL_NOTE];
            for (sql, n) in pictographic_core::side_fill::FIRST_FILL {
                statements.push(db::stmt(db, sql, all[..n].to_vec())?);
            }
        }
    }
    let (mut created, mut updated, mut checks) = (0, 0, 0);
    if !writes.is_empty() {
        let answers = db::batch(db, statements).await?;
        for (key, digest, write, at) in &writes {
            if db::changes(&answers[*at]) == 0 {
                errors.push(json!({"key": key, "conflict": true, "error": "this record changed while it was being written; fetch and send again"}));
                continue;
            }
            let outcome = match write {
                Write::Create => { created += 1; "created" }
                Write::Replace => { updated += 1; "updated" }
                Write::Check => { checks += 1; "check_changed" }
            };
            results.push(json!({"key": key, "svg_sha256": digest, "outcome": outcome}));
        }
        if created + updated + checks > 0 {
            db::batch(db, vec![db::activity(db, user, "styled", None, details(vec![
                ("created", json!(created)), ("updated", json!(updated)), ("check_changed", json!(checks))]))?]).await?;
        }
    }
    http::json(200, &json!({"created": created, "updated": updated, "check_changed": checks, "unchanged": unchanged,
                            "kept_manual": kept_manual, "errors": errors, "results": results}))
}
