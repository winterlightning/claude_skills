//! Side pairs on the primitives page (deploy.py `/api/combination-experiment`, `recombine_side_pair`,
//! `save_side_layout`, `apply_side_layout` and `preview_side_layout`).
//!
//! The pair rows are the published `experiment-combination.json` in R2. Each pair is combined from the
//! current main and sub drawings (a version picked in Icon review or on the side pages is the icon row's
//! drawing), by the graphics container running the gallery's own combination engine. Results live in D1:
//!
//! * store `side-layouts`, key `<pair id>`: a recombined or hand-adjusted pair, shaped like deploy.py
//!   `combination_layouts` entries (`main` / `sub` pin the published row's drawings), plus `drawings`
//!   (the drawings it was rendered from) and `svg_sha256`. It is also a new revision of the pair's
//!   Side combination 64 icon, so Icon review shows the new drawing for review.
//! * store `side-renders`, key `<pair id>|<sub>`: the automatic render of a pair that has no published
//!   preview, reused while its drawings are unchanged.

use super::edits::graphics;
use super::internal::put_statement;
use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::value::RawValue;
use serde_json::{json, Map, Value};
use sha2::{Digest, Sha256};
use std::collections::HashMap;
use worker::{Headers, Response, Result};

const LAYOUTS: &str = "side-layouts";
const RENDERS: &str = "side-renders";
const PAIRS_JSON: &str = "site/gallery/experiment-combination.json";
const FAMILY_PREFIX: &str = "side_combination64/";
const MAX_TARGETS: usize = 200;

macro_rules! try_response {
    ($value:expr) => {
        match $value {
            Ok(value) => value,
            Err(response) => return Ok(response),
        }
    };
}

/// The rows with these ids: pairs saved on the cloud (side_pairs.rs: made from a primitive, or a published
/// pair with another main / sub), then the published rows.
async fn pair_rows(ctx: &Ctx, ids: &[&str]) -> Result<HashMap<String, Value>> {
    let mut rows = super::side_pairs::rows(ctx, ids).await?;
    let ids: Vec<&str> = ids.iter().copied().filter(|id| !rows.contains_key(*id)).collect();
    if !ids.is_empty() {
        rows.extend(published_rows(ctx, &ids).await?);
    }
    Ok(rows)
}

/// The published rows with these ids (11 MB file: only the wanted rows are parsed).
pub(super) async fn published_rows(ctx: &Ctx, ids: &[&str]) -> Result<HashMap<String, Value>> {
    let mut rows = HashMap::new();
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(PAIRS_JSON).execute().await? else { return Ok(rows) };
    let Some(body) = object.body() else { return Ok(rows) };
    let text = body.text().await?;
    #[derive(Deserialize)]
    struct File<'a> { #[serde(borrow)] rows: Vec<&'a RawValue> }
    #[derive(Deserialize)]
    struct Id { id: String }
    let file: File = serde_json::from_str(&text).map_err(|e| worker::Error::RustError(e.to_string()))?;
    for raw in file.rows {
        let Ok(Id { id }) = serde_json::from_str::<Id>(raw.get()) else { continue };
        if ids.contains(&id.as_str()) {
            if let Ok(row) = serde_json::from_str::<Value>(raw.get()) {
                rows.insert(id, row);
            }
        }
    }
    Ok(rows)
}

async fn pair_row(ctx: &Ctx, id: &str) -> Result<std::result::Result<Value, Response>> {
    Ok(match pair_rows(ctx, &[id]).await?.remove(id) {
        Some(row) => Ok(row),
        None => Err(http::error(404, "Choose an available icon pair.")?),
    })
}

/// The chosen item of `role`: the named one, else the one the side page shows (sideParts: the first
/// solo / combination_main main, the first sub).
fn item<'a>(row: &'a Value, role: &str, name: Option<&str>) -> Option<&'a Value> {
    let items = row[if role == "main" { "mains" } else { "subs" }].as_array()?;
    match name.filter(|n| !n.is_empty()) {
        Some(name) => items.iter().find(|i| i["icon"].as_str() == Some(name)),
        None if role == "main" => items.iter()
            .find(|i| matches!(i["family"].as_str(), Some("solo" | "combination_main"))).or_else(|| items.first()),
        None => items.first(),
    }
}

/// The catalog key of a pair item (the page's sideSubKey). Native text has no catalog drawing.
fn item_key(item: &Value) -> Option<String> {
    if item["native_text"] == json!(true) {
        return None;
    }
    if let Some(key) = item["model_key"].as_str() {
        return Some(key.to_string());
    }
    Some(format!("{}/{}", item["family"].as_str().unwrap_or(""), item["icon"].as_str()?))
}

/// The catalog drawings an item was made from: its own sha and, for a sub combined as a normalized
/// SUB32 copy, `source_sha256` (side_recombine.published_drawings).
fn made_from(item: &Value, sha: &str) -> bool {
    [&item["sha256"], &item["source_sha256"]].iter().any(|s| s.as_str() == Some(sha))
}

pub(super) struct Parts { pub main: String, pub sub: String, pub main_key: Option<String>, pub sub_key: Option<String>, pub documents: Value, pub drawings: Value }

/// The pair's main and sub, with each one's current drawing where it differs from the published row.
pub(super) async fn parts(ctx: &Ctx, row: &Value, main: Option<&str>, sub: Option<&str>) -> Result<std::result::Result<Parts, Response>> {
    let mut names = Map::new();
    let mut keys: Map<String, Value> = Map::new();
    let mut documents = Map::new();
    let mut drawings = Map::new();
    for (role, name) in [("main", main), ("sub", sub)] {
        let Some(item) = item(row, role, name) else {
            return Ok(Err(http::error(422, &format!("The {role} does not belong to this pair."))?));
        };
        names.insert(role.into(), item["icon"].clone());
        keys.insert(role.into(), item_key(item).map(Value::String).unwrap_or(Value::Null));
        // The drawing it combines from: the catalog row's current one, else the published item's.
        let mut current = item["sha256"].as_str().unwrap_or("").to_string();
        if let Some(key) = item_key(item) {
            if let Some((sha, svg)) = super::edits::current_drawing(ctx, &key).await? {
                if !made_from(item, &sha) {
                    documents.insert(role.into(), json!(svg));
                }
                current = sha;
            }
        }
        drawings.insert(role.into(), json!(current));
    }
    Ok(Ok(Parts {
        main: names["main"].as_str().unwrap_or("").to_string(),
        sub: names["sub"].as_str().unwrap_or("").to_string(),
        main_key: keys["main"].as_str().map(str::to_string),
        sub_key: keys["sub"].as_str().map(str::to_string),
        documents: Value::Object(documents),
        drawings: Value::Object(drawings),
    }))
}

pub(super) async fn render(ctx: &Ctx, row: &Value, parts: &Parts, layout: &Value, elements: bool) -> Result<std::result::Result<Value, Response>> {
    let mut body = json!({"row": row, "main": parts.main, "sub": parts.sub, "documents": parts.documents});
    if !layout.is_null() {
        body["layout"] = layout.clone();
    }
    if elements {
        body["elements"] = json!(true);
    }
    graphics(ctx, "/side/render", &body).await
}

/// Why a main / sub is not approved, or None (cloud/migrate/recombine_side_pairs.py `not_approved`): approved in
/// Icon review (the status /api/reviews shows), on a drawing that builds or was picked.
async fn not_approved(ctx: &Ctx, key: Option<&str>) -> Result<Option<String>> {
    let Some(key) = key else { return Ok(None) };  // native text: no catalog drawing to review
    let Some(icon) = data::icon(&ctx.db, key, true).await?.filter(|i| !i.uploaded) else {
        return Ok(Some("has no drawing on production".into()));
    };
    let status = data::detail(&ctx.db, key, &icon.svg_sha256).await?.status;
    if status != "approve" {
        let word = match status.as_str() {
            "pending" | "disapprove" => "disapproved", "claimed" => "being fixed", "rejected" => "rejected", _ => "not reviewed",
        };
        return Ok(Some(format!("not approved in Icon review ({word})")));
    }
    if icon.build_failed && !super::edits::picked(ctx, &icon).await? {
        return Ok(Some("fails the build check".into()));
    }
    Ok(None)
}

/// The reasons a pair's combined icon fails its check: its main or sub is not approved.
pub(super) async fn pair_reasons(ctx: &Ctx, parts: &Parts) -> Result<Vec<String>> {
    let mut reasons = Vec::new();
    for (role, name, key) in [("Main", &parts.main, &parts.main_key), ("Sub", &parts.sub, &parts.sub_key)] {
        if let Some(why) = not_approved(ctx, key.as_deref()).await? {
            reasons.push(format!("{role} {name} {why}"));
        }
    }
    Ok(reasons)
}

fn digest(svg: &str) -> String {
    hex::encode(Sha256::digest(svg.as_bytes()))
}

pub(super) async fn document(ctx: &Ctx, store: &str, key: &str) -> Result<Option<Value>> {
    #[derive(Deserialize)]
    struct Row { document: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT document FROM store_documents WHERE store = ? AND key = ?", args![store, key]).await?;
    Ok(row.and_then(|r| serde_json::from_str(&r.document).ok()))
}

/// Save a pair's combined result (combination_layouts.save) and make it its Side combination 64 icon's drawing.
pub(super) async fn save(ctx: &Ctx, row: &Value, parts: &Parts, layout: &Value, result: &Value, user: &str) -> Result<Value> {
    let pair_id = row["id"].as_str().unwrap_or("").to_string();
    let pin = |role: &str, name: &str| json!({"icon": name, "sha256": item(row, role, Some(name)).map(|i| i["sha256"].clone()).unwrap_or(json!(""))});
    let mut stored = result.clone();
    if let Some(object) = stored.as_object_mut() {
        object.remove("elements");
    }
    let svg = result["svg"].as_str().unwrap_or("");
    let sha = digest(svg);
    let now = iso_utc(chrono::Utc::now());
    let entry = json!({"main": pin("main", &parts.main), "sub": pin("sub", &parts.sub), "layout": layout, "result": stored,
                       "drawings": parts.drawings, "svg_sha256": sha, "user": user, "updated_at": now});
    let key = format!("{FAMILY_PREFIX}{pair_id}");
    // The pair's Side combination 64 icon takes the new drawing: Ready when its main and sub are approved,
    // Failed check (with the reasons) when not — the same rule as recombine_side_pairs.py.
    let reasons = pair_reasons(ctx, parts).await?;
    let record = json!({"main_key": parts.main_key, "sub_key": parts.sub_key, "errors": reasons});
    // A pair made from a primitive gets its icon row on its first drawing (side_pairs.rs).
    let made = if row["custom"] == json!(true) { super::side_pairs::saving(ctx, row, parts, &now)? } else { vec![] };
    db::batch(&ctx.db, made.into_iter().chain([
        put_statement(&ctx.db, LAYOUTS, &pair_id, &entry, None, user, &now)?,
        db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'side-layout', ?)",
                 args![sha.clone(), key.clone(), svg, now.clone()])?,
        db::stmt(&ctx.db, "UPDATE icons SET svg_sha256 = ?, build_failed = ?, record = ? WHERE key = ? AND family = 'side_combination64'",
                 args![sha.clone(), !reasons.is_empty(), record.to_string(), key.clone()])?,
        // Logged every time: a pair without a Side combination 64 icon changes no icon row.
        db::stmt(&ctx.db, "INSERT INTO activity_log(username, action, icon, details, created_at) VALUES (?, 'side_layout', ?, ?, ?)",
                 args![user, key.clone(), Value::Object(details(vec![("svg_sha256", json!(sha)), ("adjusted", json!(!layout.is_null())),
                     ("main", json!(parts.main)), ("sub", json!(parts.sub))])).to_string(), now.clone()])?,
    ]).collect()).await?;
    Ok(entry)
}

fn login(user: &str) -> Option<Result<Response>> {
    (user == "system").then(|| http::error(401, "Log in to save layouts."))
}

/// POST /api/combination-experiment {id, main?, sub?}: a pair without a published preview, rendered
/// automatically from its current drawings (the page asks for these as tiles come into view).
pub async fn experiment(ctx: &Ctx, data: &Value) -> Result<Response> {
    let Some(id) = data["id"].as_str() else { return http::error(400, "Choose an available icon pair.") };
    let row = try_response!(pair_row(ctx, id).await?);
    let parts = try_response!(parts(ctx, &row, data["main"].as_str(), data["sub"].as_str()).await?);
    let key = format!("{id}|{}|{}", parts.main, parts.sub);
    if let Some(cached) = document(ctx, RENDERS, &key).await? {
        if cached["drawings"] == parts.drawings {
            return http::json(200, &cached["result"]);
        }
    }
    let result = try_response!(render(ctx, &row, &parts, &Value::Null, false).await?);
    let now = iso_utc(chrono::Utc::now());
    db::batch(&ctx.db, vec![put_statement(&ctx.db, RENDERS, &key, &json!({"drawings": parts.drawings, "result": result}),
                                          None, "system", &now)?]).await?;
    http::json(200, &result)
}

/// POST /api/combinations/side/preview {id, main, sub, layout, elements}: the layout editor's live render.
pub async fn preview(ctx: &Ctx, data: &Value) -> Result<Response> {
    let Some(id) = data["id"].as_str() else { return http::error(400, "Choose an available icon pair.") };
    let row = try_response!(pair_row(ctx, id).await?);
    let parts = try_response!(parts(ctx, &row, data["main"].as_str(), data["sub"].as_str()).await?);
    let result = try_response!(render(ctx, &row, &parts, &data["layout"], data["elements"] == json!(true)).await?);
    http::json(200, &result)
}

/// POST /api/combinations/side/recombine {pair_id, main, sub}: automatic placement with the current drawings.
pub async fn recombine(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if let Some(response) = login(user) {
        return response;
    }
    let Some(id) = data["pair_id"].as_str() else { return http::error(400, "Choose an available icon pair.") };
    let row = try_response!(pair_row(ctx, id).await?);
    let parts = try_response!(parts(ctx, &row, data["main"].as_str(), data["sub"].as_str()).await?);
    let result = try_response!(render(ctx, &row, &parts, &Value::Null, false).await?);
    let entry = save(ctx, &row, &parts, &Value::Null, &result, user).await?;
    http::json(200, &json!({"result": result, "url": null, "saved": entry}))
}

/// POST /api/combinations/side/layout {pair_id, main, sub, layout}: save a hand-adjusted layout, or with
/// a null layout go back to automatic placement (rendered from the current drawings, and saved as such).
pub async fn save_layout(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if let Some(response) = login(user) {
        return response;
    }
    let Some(id) = data["pair_id"].as_str() else { return http::error(400, "Choose a side pair.") };
    let row = try_response!(pair_row(ctx, id).await?);
    let parts = try_response!(parts(ctx, &row, data["main"].as_str(), data["sub"].as_str()).await?);
    let layout = &data["layout"];
    let result = try_response!(render(ctx, &row, &parts, layout, false).await?);
    let entry = save(ctx, &row, &parts, layout, &result, user).await?;
    let shown = if layout.is_null() { Value::Null } else { entry.clone() };
    http::json(200, &json!({"layout": shown, "url": null, "result": result, "saved": entry}))
}

/// POST /api/combinations/side/layout/apply {pair_id, main, sub, layout, targets: [{pair_id, sub}]}:
/// save the layout, then move it onto other pairs with the same main (combination_layouts.transfer).
pub async fn apply_layout(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if let Some(response) = login(user) {
        return response;
    }
    let targets = data["targets"].as_array().cloned().unwrap_or_default();
    let (Some(id), false) = (data["pair_id"].as_str(), data["layout"].is_null()) else {
        return http::error(404, "Choose an available icon pair and a layout.");
    };
    if targets.len() > MAX_TARGETS || targets.iter().any(|t| !t["pair_id"].is_string()) {
        return http::error(400, "Choose a side pair and the pairs to apply it to.");
    }
    let mut ids: Vec<&str> = targets.iter().filter_map(|t| t["pair_id"].as_str()).collect();
    ids.push(id);
    let rows = pair_rows(ctx, &ids).await?;
    let Some(row) = rows.get(id) else { return http::error(404, "Choose an available icon pair and a layout.") };
    let parts_of = try_response!(parts(ctx, row, data["main"].as_str(), data["sub"].as_str()).await?);
    let result = try_response!(render(ctx, row, &parts_of, &data["layout"], false).await?);
    let entry = save(ctx, row, &parts_of, &data["layout"], &result, user).await?;
    let source = json!({"layout": entry, "url": null, "result": result, "saved": entry});

    let mut requests = Vec::new();
    let mut results = Vec::new();
    for target in &targets {
        let pair_id = target["pair_id"].as_str().unwrap_or("");
        let Some(target_row) = rows.get(pair_id).filter(|_| pair_id != id) else {
            results.push(json!({"pair_id": pair_id, "ok": false, "error": "Not an available side pair."}));
            continue;
        };
        match parts(ctx, target_row, Some(&parts_of.main), target["sub"].as_str()).await? {
            Ok(target_parts) => requests.push((target_row, target_parts)),
            Err(_) => results.push(json!({"pair_id": pair_id, "ok": false, "error": "This pair does not use the same main, or the sub does not belong to it."})),
        }
    }
    if !requests.is_empty() {
        let body = json!({"row": row, "main": parts_of.main, "sub": parts_of.sub, "layout": data["layout"],
            "targets": requests.iter().map(|(r, p)| json!({"row": r, "sub": p.sub, "documents": p.documents})).collect::<Vec<_>>()});
        let answer = try_response!(graphics(ctx, "/side/apply", &body).await?);
        for moved in answer["results"].as_array().cloned().unwrap_or_default() {
            let pair_id = moved["pair_id"].as_str().unwrap_or("");
            let Some((target_row, target_parts)) = requests.iter().find(|(r, _)| r["id"].as_str() == Some(pair_id)) else { continue };
            if moved["ok"] != json!(true) {
                results.push(json!({"pair_id": pair_id, "ok": false, "error": moved["error"]}));
                continue;
            }
            let saved = save(ctx, target_row, target_parts, &moved["layout"], &moved["result"], user).await?;
            results.push(json!({"pair_id": pair_id, "ok": true, "layout": saved, "url": null, "result": moved["result"], "saved": saved}));
        }
    }
    http::json(200, &json!({"source": source, "results": results}))
}

/// GET /api/combinations/side/layouts: every saved pair, by pair id (deploy.py returns its layouts file),
/// without the SVGs: thousands of pairs can be saved, and each drawing is served at
/// `combination-previews/<pair id>.svg` (saved_preview).
pub async fn layouts(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { key: String, document: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT key, json_remove(document, '$.result.svg', '$.result.elements') AS document \
        FROM store_documents WHERE store = ?", args![LAYOUTS]).await?;
    let entries: Map<String, Value> = rows.into_iter()
        .filter_map(|r| Some((r.key, serde_json::from_str(&r.document).ok()?))).collect();
    http::json(200, &Value::Object(entries))
}

/// Icon review overlays for Side combination 64 icons whose drawing is a saved pair (see edits::get_overrides).
pub async fn overlays(ctx: &Ctx) -> Result<Vec<Value>> {
    #[derive(Deserialize)]
    struct Row { key: String, sha: String, build_failed: f64, errors: Option<String> }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT s.key, json_extract(s.document, '$.svg_sha256') AS sha, i.build_failed, \
        json_extract(i.record, '$.errors') AS errors FROM store_documents s \
        JOIN icons i ON i.key = ? || s.key WHERE s.store = ? AND i.svg_sha256 = json_extract(s.document, '$.svg_sha256')",
        args![FAMILY_PREFIX, LAYOUTS]).await?;
    Ok(rows.into_iter().map(|r| {
        // The check state a per-pair save set, over the one icons.json was built with.
        let errors: Value = r.errors.as_deref().and_then(|e| serde_json::from_str(e).ok()).unwrap_or(json!([]));
        let failed = r.build_failed != 0.0;
        json!({
            "key": format!("{FAMILY_PREFIX}{}", r.key), "svg_sha256": r.sha,
            "preview_url": format!("combination-previews/{}.svg?v={}", r.key, &r.sha[..12.min(r.sha.len())]),
            "build_failed": failed, "errors": errors,
            "validation": if failed { json!({"status": "fail", "automatic_status": "fail", "errors": errors}) }
                          else { json!({"status": "valid", "automatic_status": "pass", "errors": []}) },
        })
    }).collect())
}

/// `gallery/combination-previews/<pair id>.svg`: a saved pair's drawing, while it is still the pair's
/// combined icon (a catalog push that republishes the icon replaces it). None: serve the published file.
pub async fn saved_preview(ctx: &Ctx, pair_id: &str) -> Result<Option<Response>> {
    let Some(entry) = document(ctx, LAYOUTS, pair_id).await? else { return Ok(None) };
    let sha = entry["svg_sha256"].as_str().unwrap_or("");
    #[derive(Deserialize)]
    struct Row { svg_sha256: String }
    let icon: Option<Row> = db::first(&ctx.db, "SELECT svg_sha256 FROM icons WHERE key = ?", args![format!("{FAMILY_PREFIX}{pair_id}")]).await?;
    if icon.is_some_and(|i| i.svg_sha256 != sha) {
        return Ok(None);
    }
    let Some(svg) = entry["result"]["svg"].as_str() else { return Ok(None) };
    let etag = format!("\"{sha}\"");
    let headers = Headers::new();
    headers.set("Content-Type", "image/svg+xml")?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").as_deref() == Some(etag.as_str()) {
        return Ok(Some(Response::empty()?.with_status(304).with_headers(headers)));
    }
    Ok(Some(Response::from_bytes(svg.as_bytes().to_vec())?.with_headers(headers)))
}
