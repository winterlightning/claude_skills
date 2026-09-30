//! The gallery's Browser Edit and Pick panels: stroke edits and artwork choices (deploy.py
//! `/api/stroke-edits*` and `/api/icon-artwork`).
//!
//! The documents live in D1 (`store_documents`, the same stores and keys the local gallery's cloud
//! stores use). Edit geometry, validation and SVG rendering are Python: they run in the graphics
//! container (cloud/graphics) behind the GRAPHICS service binding, built from the same modules as
//! deploy.py, so the cloud computes exactly what a local gallery would. The Worker only loads the
//! inputs, stores the results and keeps the catalog row, drawing and review in step.

use super::files;
use super::internal::put_statement;
use crate::args;
use crate::db::{self, details};
use crate::data;
use crate::http::{self, percent_encode, Ctx};
use pictographic_core::catalog::Icon;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use std::collections::HashMap;
use worker::wasm_bindgen::JsValue;
use worker::{Headers, Method, RequestInit, Response, Result};

const EDITS: &str = "stroke-edits";
const ARTWORK: &str = "icon-artwork";

/// Stroke edits are kept per generated drawing, like `CloudStrokeEditStore.cloud_key`.
fn edit_key(key: &str, sha: &str) -> String {
    format!("{key}@{sha}")
}

async fn document(ctx: &Ctx, store: &str, key: &str) -> Result<Option<Value>> {
    #[derive(Deserialize)]
    struct Row { document: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT document FROM store_documents WHERE store = ? AND key = ?",
                                     args![store, key]).await?;
    Ok(row.and_then(|r| serde_json::from_str(&r.document).ok()))
}

/// The generated drawing's sha (icon_artwork.baseline): the pushed build revision, unless the row
/// already shows a picked drawing, whose choice names the generated revision it was made from.
async fn baseline_sha(ctx: &Ctx, icon: &Icon, choice: Option<&Value>) -> Result<String> {
    let built = data::exists(&ctx.db, "SELECT 1 FROM icon_graphs WHERE svg_sha256 = ?", args![icon.svg_sha256.clone()]).await?;
    Ok(match choice.and_then(|c| c["source_svg_sha256"].as_str()) {
        Some(source) if !built => source.to_string(),
        _ => icon.svg_sha256.clone(),
    })
}

async fn graph(ctx: &Ctx, sha: &str) -> Result<Option<Value>> {
    #[derive(Deserialize)]
    struct Row { graph: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT graph FROM icon_graphs WHERE svg_sha256 = ?", args![sha]).await?;
    Ok(row.and_then(|r| serde_json::from_str(&r.graph).ok()))
}

fn no_graph() -> Result<Response> {
    http::error(503, "This icon's geometry is not in the cloud yet. Push the catalog again (cloud/migrate/push_catalog.py), then reload.")
}

/// POST one request to the graphics container. Err is the response to send: its own 4xx answer
/// (same messages as deploy.py) or a 503 while the container is starting or unavailable.
pub(super) async fn graphics(ctx: &Ctx, path: &str, body: &Value) -> Result<std::result::Result<Value, Response>> {
    let unavailable = || http::error(503, "The graphics service is starting. Try again in a few seconds.");
    let fetcher = ctx.env.service("GRAPHICS")?;
    let headers = Headers::new();
    headers.set("Content-Type", "application/json")?;
    let mut init = RequestInit::new();
    init.with_method(Method::Post).with_headers(headers).with_body(Some(JsValue::from_str(&body.to_string())));
    let mut response = match fetcher.fetch(format!("https://graphics{path}"), Some(init)).await {
        Ok(response) => response,
        Err(error) => {
            worker::console_error!("graphics {path} failed: {error}");
            return Ok(Err(unavailable()?));
        }
    };
    let status = response.status_code();
    let Ok(value) = response.json::<Value>().await else {
        worker::console_error!("graphics {path} answered {status} without JSON");
        return Ok(Err(unavailable()?));
    };
    Ok(match status {
        200 => Ok(value),
        400..=499 => Err(http::json(status, &value)?),
        _ => {
            worker::console_error!("graphics {path} answered {status}: {value}");
            Err(http::json(502, &json!({"error": value["error"].as_str().unwrap_or("The graphics service failed.")}))?)
        }
    })
}

async fn icon_or_404(ctx: &Ctx, key: &str) -> Result<std::result::Result<Icon, Response>> {
    Ok(match data::icon(&ctx.db, key, true).await? {
        Some(icon) if !icon.uploaded => Ok(icon),
        // Uploaded icons have no stroke geometry; their Manual Edit and Pick run on a local gallery.
        Some(_) => Err(http::json(501, &json!({"error": "Uploaded icons are edited on a local gallery (deploy.py --cloud-api).",
                                               "local": true}))?),
        None => Err(http::error(404, "Icon not found.")?),
    })
}

macro_rules! try_response {
    ($value:expr) => {
        match $value {
            Ok(value) => value,
            Err(response) => return Ok(response),
        }
    };
}

/// GET /api/stroke-edits?icon= — the saved edit of the current generated drawing, and which older
/// drawings have edits.
pub async fn get_stroke_edits(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("").to_string();
    let icon = try_response!(icon_or_404(ctx, &key).await?);
    let choice = document(ctx, ARTWORK, &key).await?;
    let sha = baseline_sha(ctx, &icon, choice.as_ref()).await?;
    #[derive(Deserialize)]
    struct Row { document: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT document FROM store_documents WHERE store = ? AND substr(key, 1, length(?)) = ?",
                                 args![EDITS, format!("{key}@"), format!("{key}@")]).await?;
    let mut edit = Value::Null;
    let mut previous = Vec::new();
    for document in rows.iter().filter_map(|r| serde_json::from_str::<Value>(&r.document).ok()) {
        if document["source_svg_sha256"].as_str() == Some(sha.as_str()) {
            edit = document;
        } else {
            previous.push(json!({"source_svg_sha256": document["source_svg_sha256"], "updated_at": document["updated_at"]}));
        }
    }
    http::json(200, &json!({"svg_sha256": sha, "edit": edit, "previous_versions": previous}))
}

/// POST /api/stroke-edits (save) and /api/stroke-edits/validate (check only).
pub async fn post_stroke_edits(ctx: &Ctx, data: &Value, user: &str, validate_only: bool) -> Result<Response> {
    let Some(key) = data["icon"].as_str() else { return http::error(400, "An icon key is required.") };
    let icon = try_response!(icon_or_404(ctx, key).await?);
    let choice = document(ctx, ARTWORK, key).await?;
    let sha = baseline_sha(ctx, &icon, choice.as_ref()).await?;
    let Some(graph) = graph(ctx, &sha).await? else { return no_graph() };
    if validate_only {
        let report = try_response!(graphics(ctx, "/validate", &json!({"icon": graph, "data": data})).await?);
        return http::json(200, &report);
    }
    let storage_key = edit_key(key, &sha);
    let old = document(ctx, EDITS, &storage_key).await?;
    let saved = try_response!(graphics(ctx, "/edit", &json!({"icon": graph, "data": data, "old": old, "user": user})).await?);
    // The document's revision is the request's + 1; the write needs the stored one to still be the request's.
    let expected = data["revision"].as_i64().unwrap_or(0);
    let now = iso_utc(chrono::Utc::now());
    let results = db::batch(&ctx.db, vec![
        put_statement(&ctx.db, EDITS, &storage_key, &saved, Some(expected), user, &now)?,
        db::activity_if_changed(&ctx.db, user, "stroke_edit", Some(key), details(vec![
            ("svg_sha256", json!(sha)), ("revision", saved["revision"].clone()),
            ("validation", saved["effective_validation_status"].clone())]))?,
    ]).await?;
    if db::changes(&results[0]) == 0 {
        return http::error(409, "Someone saved newer edits on another machine. Reload before saving again.");
    }
    http::json(200, &saved)
}

/// The fields `deploy.py:selected_artwork` changes on a catalog record, from a stored choice.
/// The gallery merges them into its record (`Object.assign`), in the Pick answer and on load.
fn artwork_overlay(key: &str, baseline: &str, choice: Option<&Value>) -> Option<Value> {
    let Some(choice) = choice else { return Some(json!({"key": key})) };
    let mode = choice["source_mode"].as_str().unwrap_or("use_org");
    let mut record = Map::new();
    record.insert("key".into(), json!(key));
    record.insert("artwork_source".into(), json!(mode));
    record.insert("generated_svg_sha256".into(), json!(baseline));
    record.insert("artwork_revision".into(), choice["revision"].clone());
    let mut validation = Value::Null;
    let sha = match mode {
        "use_edited" => {
            let edit = &choice["edited"];
            // Written by this Worker (older choices made on a local gallery are already in icons.json).
            let sha = choice["selected_svg_sha256"].as_str()?;
            if let Some(graph) = edit["edited_graph"].as_object() {
                record.extend(graph.clone());
            }
            record.insert("generated_graph".into(), edit["original_graph"].clone());
            let status = if edit["validation_override"].is_object() { "human-selected" } else { "valid" };
            validation = json!({"status": status, "automatic_status": edit["validation"]["status"]});
            sha.to_string()
        }
        "use_upload" => {
            let upload = if choice["selected_upload"].is_object() { &choice["selected_upload"] } else { &choice["uploaded"] };
            validation = json!({"status": "human-selected", "automatic_status": "not-run"});
            upload["svg_sha256"].as_str()?.to_string()
        }
        _ => baseline.to_string(),
    };
    let approval = &choice["original_exception"];
    if mode == "use_org" && approval["svg_sha256"].as_str() == Some(sha.as_str()) {
        validation = json!({"status": "human-selected", "exception": approval});
    }
    if matches!(validation["status"].as_str(), Some("valid" | "human-selected")) {
        record.insert("build_failed".into(), json!(false));
    }
    if !validation.is_null() {
        record.insert("validation".into(), validation);
    }
    record.insert("preview_url".into(), json!(format!("../api/icon-artwork/svg?icon={}&v={sha}", percent_encode(key))));
    record.insert("svg_sha256".into(), json!(sha));
    Some(Value::Object(record))
}

/// deploy.py `artwork_response`: the choice, which edit the Pick panel offers, and the record overlay.
fn artwork_response(key: &str, baseline: &str, choice: Option<&Value>, edit: Option<&Value>) -> Value {
    let edit_revision = edit.or_else(|| choice.map(|c| &c["edited"]).filter(|e| e.is_object()))
        .map(|e| e["revision"].clone()).unwrap_or(Value::Null);
    let revision = choice.map(|c| c["revision"].clone()).unwrap_or(json!(0));
    json!({
        "choice": choice.cloned().unwrap_or(Value::Null),
        "source_mode": choice.and_then(|c| c["source_mode"].as_str()).unwrap_or("use_org"),
        "svg_sha256": baseline,
        "edit_revision": edit_revision,
        "preview_url": format!("../api/icon-artwork/svg?icon={}&v={revision}", percent_encode(key)),
        "record": artwork_overlay(key, baseline, choice).unwrap_or_else(|| json!({"key": key})),
    })
}

/// The answer's record with the generated drawing's geometry under the overlay, as deploy.py
/// `selected_artwork` builds it on a catalog record. Pages without icons.json (the primitives side
/// view, Main / Sub icons) open the Browser Edit panel from it.
async fn with_geometry(ctx: &Ctx, mut response: Value, key: &str, baseline: &str) -> Result<Value> {
    let Some(Value::Object(mut record)) = graph(ctx, baseline).await? else { return Ok(response) };
    record.insert("key".into(), json!(key));
    record.insert("svg_sha256".into(), json!(baseline));
    record.insert("preview_url".into(), json!(format!("../api/icon-artwork/svg?icon={}&variant=use_org&v={baseline}", percent_encode(key))));
    if let Value::Object(overlay) = response["record"].take() {
        record.extend(overlay);
    }
    response["record"] = Value::Object(record);
    Ok(response)
}

/// GET /api/icon-artwork?icon=
pub async fn get_artwork(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("").to_string();
    let icon = try_response!(icon_or_404(ctx, &key).await?);
    let choice = document(ctx, ARTWORK, &key).await?;
    let sha = baseline_sha(ctx, &icon, choice.as_ref()).await?;
    let edit = document(ctx, EDITS, &edit_key(&key, &sha)).await?;
    let response = artwork_response(&key, &sha, choice.as_ref(), edit.as_ref());
    http::json(200, &with_geometry(ctx, response, &key, &sha).await?)
}

/// POST /api/icon-artwork — save a manual SVG (`action: upload`) or pick and approve the displayed
/// version (deploy.py `save_artwork_cloud`): the choice, the new drawing, the catalog row's current
/// revision and its approval are written in one batch, only if nobody changed the choice meanwhile.
pub async fn post_artwork(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let key = data["icon"].as_str().unwrap_or("").to_string();
    let icon = try_response!(icon_or_404(ctx, &key).await?);
    let old = document(ctx, ARTWORK, &key).await?;
    let current_mode = old.as_ref().and_then(|c| c["source_mode"].as_str()).unwrap_or("use_org");
    if data["approve_exception"] == json!(true) && current_mode != "use_org" {
        return http::error(409, "This is selected artwork. Approve that saved version in the editor instead of approving the original.");
    }
    let upload_only = data["action"].as_str() == Some("upload");
    if !upload_only && data::is_rejected(&ctx.db, &key, &icon.svg_sha256).await? {
        return http::error(409, "Restore this rejected icon before picking and approving its artwork.");
    }
    let sha = baseline_sha(ctx, &icon, old.as_ref()).await?;
    // A manual upload, or picking it or the original, reads only the icon's identity and canvas:
    // text icons (typeface glyphs) have no stroke geometry and must still take a designer's upload.
    let needs_geometry = !upload_only
        && (data["source_mode"].as_str() == Some("use_edited") || data["approve_exception"] == json!(true));
    let graph = match graph(ctx, &sha).await? {
        Some(graph) => graph,
        None if needs_geometry => return no_graph(),
        None => json!({"key": key, "svg_sha256": sha, "canvas_size": icon.canvas_size,
                       "family": icon.family, "name": icon.name}),
    };
    let edit = document(ctx, EDITS, &edit_key(&key, &sha)).await?;
    let answer = try_response!(graphics(ctx, "/artwork", &json!({
        "icon": graph, "data": data, "old": old, "edit": edit, "user": user})).await?);
    let mut choice = answer["choice"].clone();
    let selected = &answer["selected"];
    let drawing = selected["svg_sha256"].as_str().unwrap_or(&sha).to_string();
    if !upload_only {
        choice["selected_svg_sha256"] = json!(drawing);
    }
    let revision = choice["revision"].as_i64().unwrap_or(0);
    let expected = old.as_ref().and_then(|c| c["revision"].as_i64()).unwrap_or(0);
    let now = iso_utc(chrono::Utc::now());
    let mut statements = vec![put_statement(&ctx.db, ARTWORK, &key, &choice, Some(expected), user, &now)?];
    if !upload_only {
        // Each write below happens only if the choice above landed (this revision, this timestamp).
        let landed = "EXISTS (SELECT 1 FROM store_documents WHERE store = 'icon-artwork' AND key = ? \
                      AND json_extract(document, '$.revision') = ? AND updated_at = ?)";
        if let Some(svg) = selected["svg"].as_str() {
            statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'artwork', ?)",
                                     args![drawing.clone(), key.clone(), svg, now.clone()])?);
        }
        statements.push(db::stmt(&ctx.db, &format!("UPDATE icons SET svg_sha256 = ? WHERE key = ? AND uploaded = 0 AND {landed}"),
                                 args![drawing.clone(), key.clone(), key.clone(), revision, now.clone()])?);
        statements.push(db::stmt(&ctx.db, &format!("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) \
            SELECT ?, ?, 'approve', ?, ? WHERE {landed} ON CONFLICT(icon, svg_sha256) DO UPDATE SET status = excluded.status, \
            updated_at = excluded.updated_at, updated_by = excluded.updated_by, worker = NULL, claimed_at = NULL, note = ''"),
            args![key.clone(), drawing.clone(), now.clone(), user, key.clone(), revision, now.clone()])?);
        statements.push(db::activity_if_changed(&ctx.db, user, "review", Some(&key), details(vec![
            ("status", json!("approve")), ("svg_sha256", json!(drawing)), ("artwork_source", choice["source_mode"].clone())]))?);
    }
    let results = db::batch(&ctx.db, statements).await?;
    if db::changes(&results[0]) == 0 {
        return http::error(409, "Someone changed this artwork. Reload the source choices before saving.");
    }
    let mut response = artwork_response(&key, &sha, Some(&choice), edit.as_ref());
    if !upload_only {
        response["record"]["review_status"] = json!("approve");
        response["record"]["review_updated_by"] = json!(user);
        response["record"]["review_updated_at"] = json!(now);
    }
    http::json(200, &with_geometry(ctx, response, &key, &sha).await?)
}

/// GET /api/icon-artwork/overrides — every picked artwork as a record overlay. The built icons.json in
/// R2 does not change when someone picks a version; the gallery applies these after loading it.
pub async fn get_overrides(ctx: &Ctx) -> Result<Response> {
    let mut records = overrides(ctx).await?;
    // Pairs made from a primitive first: their complete records, then every saved pair's overlay.
    records.extend(super::side_pairs::records(ctx).await?);
    records.extend(super::side::overlays(ctx).await?);
    records.extend(super::container_pairs::records(ctx).await?);
    http::json(200, &json!({"records": records}))
}

/// Every picked artwork that still applies, as a record overlay (see `artwork_overlay`).
async fn overrides(ctx: &Ctx) -> Result<Vec<Value>> {
    #[derive(Deserialize)]
    struct Row { key: String, document: String, icon_sha: String, built: f64 }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT s.key, s.document, i.svg_sha256 AS icon_sha, \
        EXISTS (SELECT 1 FROM icon_graphs g WHERE g.svg_sha256 = i.svg_sha256) AS built \
        FROM store_documents s JOIN icons i ON i.key = s.key WHERE s.store = 'icon-artwork' AND i.uploaded = 0", vec![]).await?;
    let records: Vec<Value> = rows.into_iter().filter_map(|row| {
        let choice: Value = serde_json::from_str(&row.document).ok()?;
        let source = choice["source_svg_sha256"].as_str()?.to_string();
        let baseline = if row.built != 0.0 { row.icon_sha } else { source.clone() };
        // A choice made for an older generated drawing no longer applies once the icon is rebuilt.
        (source == baseline).then(|| artwork_overlay(&row.key, &baseline, Some(&choice))).flatten()
    }).collect();
    Ok(records)
}

/// GET /api/side-components and /gallery/side-components.json: the built file with each drawing's
/// picked artwork applied (deploy.py `side_components_data`). The R2 copy changes only on a catalog
/// push, so without this a version picked in Icon review or on the side pages would not show there.
pub async fn side_components(ctx: &Ctx) -> Result<Response> {
    let missing = "side-components.json is not built yet. Run the gallery build.";
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(files::SIDE_COMPONENTS_JSON).execute().await? else { return http::error(404, missing) };
    let Some(body) = object.body() else { return http::error(404, missing) };
    let Ok(mut data) = serde_json::from_str::<Value>(&body.text().await?) else { return http::error(503, missing) };
    let overlays: HashMap<String, Value> = overrides(ctx).await?.into_iter()
        .filter_map(|record| Some((record["key"].as_str()?.to_string(), record))).collect();
    for (list, role) in [("mains", "main"), ("subs", "sub")] {
        let Some(items) = data[list].as_array_mut() else { continue };
        for item in items.iter_mut() {
            let Some(drawings) = item["drawings"].as_array_mut() else { continue };
            for drawing in drawings.iter_mut() {
                let Some(overlay) = drawing["key"].as_str().and_then(|key| overlays.get(key)) else { continue };
                for field in ["preview_url", "svg_sha256"] {
                    if !overlay[field].is_null() {
                        drawing[field] = overlay[field].clone();
                    }
                }
                // side_components._drawing: a valid pick or an approved exception passes.
                let validation = &overlay["validation"];
                match validation["status"].as_str() {
                    Some("valid") => drawing["status"] = json!("pass"),
                    Some("human-selected") => {
                        drawing["status"] = json!("pass");
                        drawing["exception"] = if validation["exception"].is_object() { validation["exception"].clone() } else { validation.clone() };
                    }
                    _ => continue,
                }
                drawing["errors"] = json!([]);
            }
            let failing = drawings.iter().filter(|d| d["status"] != "pass").count();
            let status = if drawings.iter().any(|d| d["status"] == "pass") { "done" } else if drawings.is_empty() { "missing" } else { "failing" };
            item["status"] = json!(status);
            item["failing_variants"] = json!(failing);
        }
        let items = data[list].as_array().cloned().unwrap_or_default();
        let count = |status: &str| items.iter().filter(|i| i["status"] == status).count();
        let counts = json!({
            "done": count("done"), "failing": count("failing"), "missing": count("missing"), "total": items.len(),
            "done_with_failing_variants": items.iter().filter(|i| i["status"] == "done" && i["failing_variants"].as_u64().unwrap_or(0) > 0).count(),
            "blocked_pairs": items.iter().filter(|i| i["status"] != "done").map(|i| i["uses"].as_u64().unwrap_or(0)).sum::<u64>(),
        });
        if !data["counts"].is_object() {
            data["counts"] = json!({});
        }
        match data["counts"][role].as_object_mut() {
            Some(existing) => existing.extend(counts.as_object().cloned().unwrap_or_default()),
            None => data["counts"][role] = counts,
        }
    }
    http::json(200, &data)
}

/// GET /api/icon-artwork/svg?icon=&variant= — a candidate drawing for the Pick panel.
pub async fn get_artwork_variant(ctx: &Ctx, variant: &str) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("").to_string();
    let icon = try_response!(icon_or_404(ctx, &key).await?);
    let choice = document(ctx, ARTWORK, &key).await?;
    let sha = baseline_sha(ctx, &icon, choice.as_ref()).await?;
    let edited_graph = |edit: &Value| edit["edited_graph"].is_object().then(|| edit["edited_graph"].clone());
    let graph = match variant {
        "use_org" => return stored_drawing(ctx, &sha).await,
        "use_upload" => {
            let svg = choice.as_ref().and_then(|c| c["uploaded"]["svg"].as_str());
            return match svg { Some(svg) => http::svg(svg), None => http::error(400, "That artwork version has not been saved.") };
        }
        "browser_edit" => {
            let edit = document(ctx, EDITS, &edit_key(&key, &sha)).await?;
            edit.as_ref().and_then(edited_graph).or_else(|| choice.as_ref().and_then(|c| edited_graph(&c["edited"])))
        }
        "use_edited" => {
            if let Some(selected) = choice.as_ref().and_then(|c| c["selected_svg_sha256"].as_str()) {
                if choice.as_ref().and_then(|c| c["source_mode"].as_str()) == Some("use_edited") {
                    return stored_drawing(ctx, selected).await;
                }
            }
            choice.as_ref().and_then(|c| edited_graph(&c["edited"]))
        }
        _ => return http::error(400, "Unknown artwork source."),
    };
    let Some(graph) = graph else { return http::error(400, "No browser edit has been saved yet.") };
    let rendered = try_response!(graphics(ctx, "/render", &json!({"graph": graph})).await?);
    http::svg(rendered["svg"].as_str().unwrap_or(""))
}

async fn stored_drawing(ctx: &Ctx, sha: &str) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { svg: String }
    match db::first::<Row>(&ctx.db, "SELECT svg FROM revisions WHERE svg_sha256 = ?", args![sha]).await? {
        Some(row) => http::svg(&row.svg),
        None => http::error(503, "Artwork is unavailable on this server."),
    }
}

/// The drawing an icon shows now, as (svg_sha256, svg): its picked artwork (the same choice
/// `artwork_overlay` shows in Icon review and on the side pages), else its catalog row's drawing.
/// Choices made on a local gallery before the cloud editor never moved the row, so the row alone
/// is not enough: an uploaded SVG lives only in its choice.
pub(super) async fn current_drawing(ctx: &Ctx, key: &str) -> Result<Option<(String, String)>> {
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return Ok(None) };
    if !icon.uploaded {
        if let Some(choice) = document(ctx, ARTWORK, key).await? {
            let baseline = baseline_sha(ctx, &icon, Some(&choice)).await?;
            // A choice made for an older generated drawing no longer applies (get_overrides).
            if choice["source_svg_sha256"].as_str() == Some(baseline.as_str()) {
                match choice["source_mode"].as_str() {
                    Some("use_upload") => {
                        let upload = if choice["selected_upload"].is_object() { &choice["selected_upload"] } else { &choice["uploaded"] };
                        if let (Some(sha), Some(svg)) = (upload["svg_sha256"].as_str(), upload["svg"].as_str()) {
                            return Ok(Some((sha.to_string(), svg.to_string())));
                        }
                    }
                    Some("use_edited") => {
                        if let Some(selected) = choice["selected_svg_sha256"].as_str() {
                            if let Some(svg) = revision_svg(ctx, selected).await? {
                                return Ok(Some((selected.to_string(), svg)));
                            }
                        }
                    }
                    _ => {}
                }
            }
        }
    }
    Ok(revision_svg(ctx, &icon.svg_sha256).await?.map(|svg| (icon.svg_sha256.clone(), svg)))
}

/// Whether an icon shows a picked artwork (a failed build approved through a picked version counts as built).
pub(super) async fn picked(ctx: &Ctx, icon: &Icon) -> Result<bool> {
    let Some(choice) = document(ctx, ARTWORK, &icon.key).await? else { return Ok(false) };
    let baseline = baseline_sha(ctx, icon, Some(&choice)).await?;
    Ok(choice["source_svg_sha256"].as_str() == Some(baseline.as_str()))
}

async fn revision_svg(ctx: &Ctx, sha: &str) -> Result<Option<String>> {
    #[derive(Deserialize)]
    struct Row { svg: String }
    Ok(db::first::<Row>(&ctx.db, "SELECT svg FROM revisions WHERE svg_sha256 = ?", args![sha]).await?.map(|r| r.svg))
}

/// The drawing a picked choice displays (deploy.py serves the choice before a worker's fix), or None.
pub async fn picked_drawing(ctx: &Ctx, icon: &Icon) -> Result<Option<Response>> {
    if icon.uploaded {
        return Ok(None);
    }
    let Some(choice) = document(ctx, ARTWORK, &icon.key).await? else { return Ok(None) };
    let sha = baseline_sha(ctx, icon, Some(&choice)).await?;
    if choice["source_svg_sha256"].as_str() != Some(sha.as_str()) {
        return Ok(None); // made for an older generated drawing
    }
    Ok(match (choice["source_mode"].as_str(), choice["selected_svg_sha256"].as_str()) {
        (Some("use_edited" | "use_upload"), Some(selected)) => Some(stored_drawing(ctx, selected).await?),
        (Some("use_upload"), None) => choice["selected_upload"]["svg"].as_str().or(choice["uploaded"]["svg"].as_str())
            .map(http::svg).transpose()?,
        _ => None,
    })
}
