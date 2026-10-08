//! Round and sharp records of icons (corner_processing): POST /api/icons/styled.
//!
//! Each item `{source_key, style, svg, check, expected_sha256}` stores `<source_key>--<style>` as its own icon in the
//! source's family, with style round or sharp and style_of the source (migration 0019; the record field is
//! `icon_style`, since a record's `style` is its stroke style), so the list shows it under that style and it is
//! reviewed on its own. It is kept like an upload (uploaded_icons + revisions), so artwork serving and Pick work as
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
        return http::error(401, "Sign in or send the push token to store round and sharp icons.");
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
    let styled_keys: Vec<String> = items.iter().filter_map(|i| Some(format!("{}--{}", i["source_key"].as_str()?, i["style"].as_str()?))).collect();
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
        let fail = |message: &str| json!({"source_key": source_key, "style": style, "error": message});
        if !matches!(style, "round" | "sharp") {
            errors.push(fail("style must be round or sharp"));
            continue;
        }
        if !seen.insert((source_key, style)) {
            errors.push(fail("this icon and style are listed twice in the request"));
            continue;
        }
        // The corner check is the record's failed flag: a missing or unknown result is refused, never taken as ok.
        let Some(check) = item["check"].as_str().filter(|c| CHECKS.contains(c)) else {
            errors.push(fail("check must be ok, contact or fail"));
            continue;
        };
        let Some(source) = sources.iter().find(|s| s.key == source_key) else {
            errors.push(fail("no normal icon has this key"));
            continue;
        };
        let canvas = source.canvas_size.unwrap_or(48);
        let document = match pictographic_core::svg::safe_svg(item["svg"].as_str().unwrap_or(""), canvas) {
            Ok(document) => document,
            Err(message) => { errors.push(fail(&message)); continue; }
        };
        let digest = hex::encode(Sha256::digest(document.as_bytes()));
        let failed = check == "fail";
        let key = format!("{}--{style}", source.key);
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
        if same_drawing && existing.is_some_and(|e| e.corner_check.as_deref() == Some(check)) {
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
        let icon_id = format!("{}--{style}", source.icon_id.clone().unwrap_or_else(|| source.key.rsplit('/').next().unwrap_or("").to_string()));
        let name = source.name.clone().unwrap_or_else(|| icon_id.clone());
        let preview_url = format!("../api/icon-artwork/svg?icon={}&v={digest}", http::percent_encode(&key));
        let created = existing.and_then(|e| e.created_at.clone()).unwrap_or_else(|| now.clone());
        let record = json!({
            "key": key, "icon_id": icon_id, "name": name, "family": family, "profile": source.profile, "canvas_size": canvas,
            "category": source.category, "icon_style": style, "style_of": source.key, "svg_sha256": digest, "uploaded_icon": true,
            "artwork_source": "use_org", "preview_url": preview_url, "author": format!("corner_processing ({style})"),
            "created_at": created, "modified_at": now, "original_sources": source_record["original_sources"].clone(),
            "keywords": source_record["keywords"].clone(), "aliases": source_record["aliases"].clone(),
            "primitives": [], "contours": [], "relationships": [], "anchors": {},
            "style": source_record["style"].as_object().map(|_| source_record["style"].clone()).unwrap_or_else(|| json!({"stroke_width": 4})),
            "keyshape": source_record["keyshape"].clone(), "keyshape_bounds": source_record["keyshape_bounds"].clone(),
            "build_failed": failed, "errors": if failed { json!(["Corner check failed: the output's corners differ from the input's."]) } else { json!([]) },
            "corner_check": check});
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
            _ => statements.extend(super::edits::replaced_drawing(db, &key, &document, &digest, &format!("corner-{style}"), true, user, &now,
                details(vec![("status", json!("ready")), ("svg_sha256", json!(digest)), ("artwork_source", json!(format!("corner-{style}")))]))?),
        }
        statements.extend(super::icon_list::recount(db, &key, matches!(write, Write::Create))?);
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
