//! Round and sharp records of icons (corner_processing): POST /api/icons/styled.
//!
//! Each item `{source_key, style, svg, check}` stores `<source_key>--<style>` as its own icon in the source's family,
//! with style round or sharp and style_of the source (migration 0019; the record field is `icon_style`, since a
//! record's `style` is its stroke style), so the list shows it under that style and it
//! is reviewed on its own. It is kept like an upload (uploaded_icons + revisions), so artwork serving, Browser Edit
//! and Pick work as for any uploaded icon. A new drawing starts Ready; one whose corner check failed is a failed
//! build (the Failed tab). Sending the same drawing again changes nothing; a different one becomes the current
//! revision and its review starts at Ready.

use crate::args;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use worker::{Response, Result};

const MAX_ITEMS: usize = 50;

#[derive(Deserialize)]
struct Source { key: String, icon_id: Option<String>, name: Option<String>, family: Option<String>, category: Option<String>,
                profile: Option<String>, canvas_size: Option<i64>, record: String }

#[derive(Deserialize)]
struct Existing { key: String, svg_sha256: String }

pub async fn post_styled(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" && !super::internal::authorized(ctx) {
        return http::error(401, "Sign in or send the push token to store round and sharp icons.");
    }
    let Some(items) = data["items"].as_array().filter(|items| !items.is_empty() && items.len() <= MAX_ITEMS) else {
        return http::error(400, &format!("Send 1 to {MAX_ITEMS} items."));
    };
    let db = &ctx.db;
    let now = iso_utc(chrono::Utc::now());
    let (mut created, mut updated, mut unchanged, mut errors) = (0, 0, 0, Vec::new());
    let mut statements = Vec::new();
    // Every source and every record that exists already, in two reads (not two per item).
    let source_keys: Vec<&str> = items.iter().filter_map(|i| i["source_key"].as_str()).collect();
    let styled_keys: Vec<String> = items.iter().filter_map(|i| Some(format!("{}--{}", i["source_key"].as_str()?, i["style"].as_str()?))).collect();
    let sources: Vec<Source> = db::all(db, "SELECT key, icon_id, name, family, category, profile, canvas_size, record FROM icons \
        WHERE key IN (SELECT value FROM json_each(?)) AND style = 'normal'", args![json!(source_keys).to_string()]).await?;
    let existing: Vec<Existing> = db::all(db, "SELECT key, svg_sha256 FROM icons WHERE key IN (SELECT value FROM json_each(?))",
                                          args![json!(styled_keys).to_string()]).await?;
    for item in items {
        let source_key = item["source_key"].as_str().unwrap_or("");
        let style = item["style"].as_str().unwrap_or("");
        let fail = |message: &str| json!({"source_key": source_key, "style": style, "error": message});
        if !matches!(style, "round" | "sharp") {
            errors.push(fail("style must be round or sharp"));
            continue;
        }
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
        let failed = item["check"].as_str() == Some("fail");
        let key = format!("{}--{style}", source.key);
        let existing = existing.iter().find(|e| e.key == key);
        if existing.as_ref().is_some_and(|e| e.svg_sha256 == digest) {
            unchanged += 1;
            continue;
        }
        let source_record: Value = serde_json::from_str(&source.record).unwrap_or_else(|_| json!({}));
        let family = source.family.clone().unwrap_or_default();
        let icon_id = format!("{}--{style}", source.icon_id.clone().unwrap_or_else(|| source.key.rsplit('/').next().unwrap_or("").to_string()));
        let name = source.name.clone().unwrap_or_else(|| icon_id.clone());
        let preview_url = format!("../api/icon-artwork/svg?icon={}&v={digest}", http::percent_encode(&key));
        let record = json!({
            "key": key, "icon_id": icon_id, "name": name, "family": family, "profile": source.profile, "canvas_size": canvas,
            "category": source.category, "icon_style": style, "style_of": source.key, "svg_sha256": digest, "uploaded_icon": true,
            "artwork_source": "use_org", "preview_url": preview_url, "author": format!("corner_processing ({style})"),
            "created_at": now, "modified_at": now, "original_sources": source_record["original_sources"].clone(),
            "keywords": source_record["keywords"].clone(), "aliases": source_record["aliases"].clone(),
            "primitives": [], "contours": [], "relationships": [], "anchors": {},
            "style": source_record["style"].as_object().map(|_| source_record["style"].clone()).unwrap_or_else(|| json!({"stroke_width": 4})),
            "keyshape": source_record["keyshape"].clone(), "keyshape_bounds": source_record["keyshape_bounds"].clone(),
            "build_failed": failed, "errors": if failed { json!(["Corner check failed: the output's corners differ from the input's."]) } else { json!([]) },
            "corner_check": item["check"].clone()});
        let record_text = record.to_string();
        if existing.is_some() {
            statements.extend(super::icon_list::uncount(db, &key)?);
            statements.push(db::stmt(db, "UPDATE uploaded_icons SET record = ?, svg = ? WHERE icon = ?",
                                     args![record_text.clone(), document.clone(), key.clone()])?);
            statements.push(db::stmt(db, "UPDATE icons SET svg_sha256 = ?, preview_url = ?, record = ?, build_failed = ?, pushed_at = ? \
                WHERE key = ?", args![digest.clone(), preview_url.clone(), record_text, failed as i64, now.clone(), key.clone()])?);
            updated += 1;
        } else {
            statements.push(db::stmt(db, "INSERT INTO uploaded_icons VALUES (?, ?, ?)", args![key.clone(), record_text.clone(), document.clone()])?);
            statements.push(db::stmt(db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, \
                original_sources, uploaded, build_failed, record, pushed_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?)",
                args![key.clone(), icon_id, name, family, source.category.clone(), source.profile.clone(), canvas, digest.clone(),
                      preview_url, record["original_sources"].to_string(), failed as i64, record_text, now.clone()])?);
            created += 1;
        }
        statements.push(super::icon_list::index_statement(db, &key, &record, None)?);
        statements.push(db::stmt(db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, ?, ?)",
                                 args![digest.clone(), key.clone(), document, format!("corner-{style}"), now.clone()])?);
        statements.push(db::stmt(db, "INSERT OR IGNORE INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, 'ready', ?, ?)",
                                 args![key.clone(), digest.clone(), now.clone(), user])?);
        statements.extend(super::icon_list::recount(db, &key, true)?);
    }
    if created + updated > 0 {
        statements.push(db::activity(db, user, "styled", None, details(vec![("created", json!(created)), ("updated", json!(updated))]))?);
        db::batch(db, statements).await?;
    }
    http::json(200, &json!({"created": created, "updated": updated, "unchanged": unchanged, "errors": errors}))
}
