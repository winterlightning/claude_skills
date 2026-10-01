//! Writes from local tools, where the Python graphics processing runs.
//!
//! The catalog, artwork choices, stroke edits and discards are computed locally and only stored
//! here. These routes can overwrite the catalog, so they require the PUSH_TOKEN secret
//! (`Authorization: Bearer ...`), separate from the reviewers' sign-in.

use crate::args;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::primitives::python_json;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use worker::{D1Database, D1PreparedStatement, Response, Result};

pub fn authorized(ctx: &Ctx) -> bool {
    let Some(expected) = ctx.env.secret("PUSH_TOKEN").ok().map(|s| s.to_string()).filter(|t| t.len() >= 32) else { return false };
    let given = ctx.header("Authorization").unwrap_or_default();
    let given = given.strip_prefix("Bearer ").unwrap_or("");
    given.len() == expected.len() && given.bytes().zip(expected.bytes()).fold(0u8, |acc, (a, b)| acc | (a ^ b)) == 0
}

#[derive(Deserialize)]
struct PushedIcon {
    key: String,
    #[serde(default)] icon_id: Option<String>,
    #[serde(default)] name: Option<String>,
    #[serde(default)] family: Option<String>,
    #[serde(default)] category: Option<String>,
    #[serde(default)] profile: Option<String>,
    #[serde(default)] canvas_size: Option<f64>,
    svg_sha256: String,
    #[serde(default)] python_source: Value,
    #[serde(default)] preview_url: Option<String>,
    #[serde(default)] original_sources: Value,
    #[serde(default)] variant_of: Option<String>,
    #[serde(default)] variant_root: Option<String>,
    #[serde(default)] variant_label: Option<String>,
    #[serde(default)] build_failed: bool,
    /// The current drawing; stored once per sha in `revisions`.
    #[serde(default)] svg: Option<String>,
    #[serde(default)] origin: Option<String>,
    /// The generated drawing's editable geometry; stored once per generated sha in `icon_graphs`.
    #[serde(default)] graph: Option<Value>,
}

/// POST /api/catalog/push — one chunk of the effective catalog (artwork choices applied locally).
/// `{"push_id", "icons": [...], "final": bool, "details": {...}}`. The final chunk removes built
/// icons that were not in this push and records the push (with the icons.json layout).
pub async fn catalog_push(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let Some(push_id) = data.get("push_id").and_then(Value::as_str).filter(|p| !p.is_empty() && p.len() <= 64) else {
        return http::error(400, "push_id is required.");
    };
    let icons: Vec<PushedIcon> = match serde_json::from_value(data.get("icons").cloned().unwrap_or(json!([]))) {
        Ok(icons) => icons,
        Err(error) => return http::error(400, &format!("Invalid icons: {error}")),
    };
    let now = iso_utc(chrono::Utc::now());
    let mut statements = Vec::new();
    for icon in &icons {
        let sources = if icon.original_sources.is_null() { "[]".to_string() } else { icon.original_sources.to_string() };
        statements.push(db::stmt(&ctx.db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, \
            python_source, preview_url, original_sources, variant_of, variant_root, variant_label, build_failed, uploaded, pushed_at) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?) ON CONFLICT(key) DO UPDATE SET icon_id = excluded.icon_id, \
            name = excluded.name, family = excluded.family, category = excluded.category, profile = excluded.profile, \
            canvas_size = excluded.canvas_size, svg_sha256 = excluded.svg_sha256, python_source = excluded.python_source, \
            preview_url = excluded.preview_url, original_sources = excluded.original_sources, variant_of = excluded.variant_of, \
            variant_root = excluded.variant_root, variant_label = excluded.variant_label, build_failed = excluded.build_failed, \
            pushed_at = excluded.pushed_at WHERE icons.uploaded = 0 \
            AND NOT (icons.family IN ('side_combination64', 'container_combination64', 'combination-72') \
                     AND EXISTS (SELECT 1 FROM revisions r WHERE r.svg_sha256 = icons.svg_sha256 AND r.origin = 'combination-build'))",
            args![icon.key.clone(), icon.icon_id.clone(), icon.name.clone(), icon.family.clone(), icon.category.clone(),
                  icon.profile.clone(), icon.canvas_size.map(|c| c.round() as i64), icon.svg_sha256.clone(),
                  (!icon.python_source.is_null()).then(|| icon.python_source.to_string()), icon.preview_url.clone(),
                  sources, icon.variant_of.clone(), icon.variant_root.clone(), icon.variant_label.clone(), icon.build_failed,
                  push_id])?);
        if let Some(graph) = icon.graph.as_ref().filter(|g| g.is_object()) {
            if let Some(sha) = graph.get("svg_sha256").and_then(Value::as_str) {
                statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO icon_graphs(svg_sha256, icon, graph) VALUES (?, ?, ?)",
                    args![sha, icon.key.clone(), graph.to_string()])?);
            }
        }
        if let Some(svg) = &icon.svg {
            statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, ?, ?)",
                args![icon.svg_sha256.clone(), icon.key.clone(), svg.clone(), icon.origin.clone().unwrap_or_else(|| "build".into()), now.clone()])?);
        }
    }
    let is_final = data.get("final").and_then(Value::as_bool).unwrap_or(false);
    // Leftover drawings the review pages still show (failed builds without a catalog row), replaced
    // as a whole by the push that carries them.
    if let Some(extras) = data.get("extra_drawings").and_then(Value::as_array) {
        statements.push(db::stmt(&ctx.db, "DELETE FROM extra_drawings", vec![])?);
        for extra in extras {
            let (Some(profile), Some(icon_id), Some(sha), Some(svg)) = (extra["profile"].as_str(), extra["icon_id"].as_str(),
                extra["svg_sha256"].as_str(), extra["svg"].as_str()) else { continue };
            let failed = extra["failed"].as_bool().unwrap_or(false);
            statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'extra', ?)",
                args![sha, format!("{}/{icon_id}", profile.to_lowercase()), svg, now.clone()])?);
            statements.push(db::stmt(&ctx.db, "INSERT OR REPLACE INTO extra_drawings(profile, icon_id, failed, svg_sha256) VALUES (?, ?, ?, ?)",
                args![profile, icon_id, failed, sha])?);
        }
    }
    if is_final {
        // Combined icons belong to the combination tables (built in the browser, combinations.rs): a push adds
        // the ones it builds but never removes one.
        statements.push(db::stmt(&ctx.db, "DELETE FROM icons WHERE uploaded = 0 AND pushed_at != ? \
            AND family NOT IN ('side_combination64', 'container_combination64', 'combination-72')", args![push_id])?);
        let push_details = data.get("details").cloned().unwrap_or(json!({}));
        statements.push(db::stmt(&ctx.db, "INSERT INTO catalog_pushes(pushed_at, pushed_by, details) VALUES (?, ?, ?)",
                                 args![now.clone(), user, python_json(&push_details)])?);
    }
    let results = db::batch(&ctx.db, statements).await?;
    let removed = if is_final { results.get(results.len().saturating_sub(2)).map(db::changes).unwrap_or(0) } else { 0 };
    http::json(200, &json!({"saved": icons.len(), "final": is_final, "removed": removed}))
}

const STORES: [&str; 2] = ["icon-artwork", "stroke-edits"];

/// GET /api/store/<store>[?key=|?prefix=] and POST /api/store/<store> `{key, document, expected_revision?}`.
/// A null document deletes. With `expected_revision`, the write only happens when the stored
/// document's `revision` still equals it (0 = must not exist yet), so two machines editing the
/// same icon cannot silently overwrite each other; a lost race answers 409 with the current document.
pub async fn store(ctx: &Ctx, data: Option<&Value>, user: &str) -> Result<Response> {
    let store = ctx.path.trim_start_matches("/api/store/");
    if !STORES.contains(&store) {
        return http::error(404, "Unknown store.");
    }
    #[derive(Deserialize)]
    struct Row { key: String, document: String, updated_at: String, updated_by: String }
    let entry = |r: Row| (r.key, json!({"document": serde_json::from_str::<Value>(&r.document).unwrap_or(Value::Null),
                                        "updated_at": r.updated_at, "updated_by": r.updated_by}));
    let select = "SELECT key, document, updated_at, updated_by FROM store_documents WHERE store = ?";
    let Some(data) = data else {
        let rows: Vec<Row> = match (ctx.param("key"), ctx.param("prefix")) {
            (Some(key), _) => db::all(&ctx.db, &format!("{select} AND key = ?"), args![store, key]).await?,
            (None, Some(prefix)) => db::all(&ctx.db, &format!("{select} AND substr(key, 1, length(?)) = ? ORDER BY key"),
                                            args![store, prefix, prefix]).await?,
            (None, None) => db::all(&ctx.db, &format!("{select} ORDER BY key"), args![store]).await?,
        };
        let documents: Map<String, Value> = rows.into_iter().map(entry).collect();
        return http::json(200, &json!({"store": store, "documents": documents}));
    };
    let Some(key) = data.get("key").and_then(Value::as_str).filter(|k| !k.is_empty() && k.len() <= 512) else {
        return http::error(400, "key is required.");
    };
    let actor = data.get("user").and_then(Value::as_str).unwrap_or(user);
    let document = data.get("document").cloned().unwrap_or(Value::Null);
    let expected = data.get("expected_revision").and_then(Value::as_i64);
    let now = iso_utc(chrono::Utc::now());
    let write = put_statement(&ctx.db, store, key, &document, expected, actor, &now)?;
    let results = db::batch(&ctx.db, vec![write]).await?;
    if expected.is_some() && !document.is_null() && db::changes(&results[0]) == 0 {
        let current: Option<Row> = db::first(&ctx.db, &format!("{select} AND key = ?"), args![store, key]).await?;
        return http::json(409, &json!({"error": "Someone saved a newer version. Reload before saving again.",
                                       "current": current.map(|r| entry(r).1)}));
    }
    http::json(200, &json!({"saved": true, "store": store, "key": key, "updated_at": now}))
}

/// One store write as a batch statement. A null document deletes. With `expected`, the write only
/// happens when the stored document's `revision` still equals it (0 = must not exist yet): zero
/// changes then means someone else saved first.
pub fn put_statement(db: &D1Database, store: &str, key: &str, document: &Value, expected: Option<i64>, actor: &str,
                     now: &str) -> Result<D1PreparedStatement> {
    match (document.is_null(), expected) {
        (true, _) => db::stmt(db, "DELETE FROM store_documents WHERE store = ? AND key = ?", args![store, key]),
        (false, Some(0)) => db::stmt(db, "INSERT OR IGNORE INTO store_documents(store, key, document, updated_at, updated_by) \
            VALUES (?, ?, ?, ?, ?)", args![store, key, document.to_string(), now, actor]),
        (false, Some(revision)) => db::stmt(db, "UPDATE store_documents SET document = ?, updated_at = ?, updated_by = ? \
            WHERE store = ? AND key = ? AND json_extract(document, '$.revision') = ?",
            args![document.to_string(), now, actor, store, key, revision]),
        (false, None) => db::stmt(db, "INSERT INTO store_documents(store, key, document, updated_at, updated_by) VALUES (?, ?, ?, ?, ?) \
            ON CONFLICT(store, key) DO UPDATE SET document = excluded.document, updated_at = excluded.updated_at, updated_by = excluded.updated_by",
            args![store, key, document.to_string(), now, actor]),
    }
}

/// GET /api/activity?icon=&icon_prefix=&action_prefix= — the activity log, oldest first
/// (local tools rebuild decision history from it).
pub async fn read_activity(ctx: &Ctx) -> Result<Response> {
    let icon = ctx.param("icon");
    let icon_prefix = ctx.param("icon_prefix").unwrap_or("");
    let action_prefix = ctx.param("action_prefix").unwrap_or("");
    let mut conditions = Vec::new();
    let mut values = Vec::new();
    if let Some(icon) = icon {
        conditions.push("icon = ?");
        values.push(crate::db::Arg::from(icon));
    }
    if !icon_prefix.is_empty() {
        conditions.push("substr(icon, 1, length(?)) = ?");
        values.extend(args![icon_prefix, icon_prefix]);
    }
    if !action_prefix.is_empty() {
        conditions.push("substr(action, 1, length(?)) = ?");
        values.extend(args![action_prefix, action_prefix]);
    }
    // Matches any of the given filters (deploy.py's history uses "icon is primitive:* OR action is primitive_*").
    let filter = if conditions.is_empty() { String::new() } else { format!(" WHERE {}", conditions.join(" OR ")) };
    let rows: Vec<Map<String, Value>> = db::all(&ctx.db,
        &format!("SELECT id, username, action, icon, details, created_at FROM activity_log{filter} ORDER BY id"), values).await?;
    http::json(200, &crate::routes::reviews::tidy(Value::Array(rows.into_iter().map(Value::Object).collect())))
}

/// POST /api/icons/discard-record — the database half of discard_icon.py `discard_many`:
/// local code already removed the Python source and published files.
pub async fn discard_record(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let Some(icons) = data.get("icons").and_then(Value::as_array).filter(|l| !l.is_empty() && l.len() <= 500) else {
        return http::error(400, "Choose between 1 and 500 icons to discard.");
    };
    let actor = data.get("user").and_then(Value::as_str).unwrap_or(user);
    let mut statements = Vec::new();
    let mut discarded = Vec::new();
    for item in icons {
        let Some(key) = item.get("icon").and_then(Value::as_str) else { continue };
        for table in ["reviews", "icon_flags", "icon_types", "feedback"] {
            statements.push(db::stmt(&ctx.db, &format!("DELETE FROM {table} WHERE icon = ?"), args![key])?);
        }
        statements.push(db::stmt(&ctx.db, "DELETE FROM icons WHERE key = ? AND uploaded = 0", args![key])?);
        statements.push(db::activity(&ctx.db, actor, "discard", Some(key), details(vec![
            ("svg_sha256", item.get("svg_sha256").cloned().unwrap_or(Value::Null)),
            ("source", item.get("source").cloned().unwrap_or(Value::Null)),
            ("archive", item.get("archive").cloned().unwrap_or(Value::Null))]))?);
        discarded.push(key.to_string());
    }
    let results = db::batch(&ctx.db, statements).await?;
    let mut removed = Vec::new();
    for (index, key) in discarded.iter().enumerate() {
        let base = index * 6;
        removed.push(json!({"icon": key, "removed_rows": {
            "reviews": db::changes(&results[base]), "icon_flags": db::changes(&results[base + 1]),
            "icon_types": db::changes(&results[base + 2]), "feedback": db::changes(&results[base + 3])}}));
    }
    http::json(200, &json!({"discarded": removed}))
}

/// PUT /api/files/<key> — store one file in R2 (raw body). DELETE removes it.
/// Keys are limited to the site, reference and store prefixes the Worker serves from.
pub async fn file(ctx: &mut Ctx) -> Result<Response> {
    let key = ctx.path.trim_start_matches("/api/files/").to_string();
    let allowed = ["site/", "references/", "stores/"].iter().any(|prefix| key.starts_with(prefix));
    if !allowed || key.split('/').any(|part| part.is_empty() || part == "." || part == "..") {
        return http::error(400, "Choose a key under site/, references/ or stores/.");
    }
    let bucket = ctx.env.bucket("FILES")?;
    if ctx.method == worker::Method::Delete {
        bucket.delete(&key).await?;
        return http::json(200, &json!({"deleted": key}));
    }
    let content_type = ctx.header("Content-Type").unwrap_or_else(|| "application/octet-stream".into());
    let bytes = ctx.req.bytes().await?;
    let size = bytes.len();
    bucket.put(&key, bytes).http_metadata(worker::HttpMetadata { content_type: Some(content_type), ..Default::default() })
        .execute().await?;
    http::json(200, &json!({"saved": key, "size": size}))
}

/// POST /api/activity — log an action taken by local tools (generation, stroke edits, ...).
pub async fn activity(ctx: &Ctx, data: &Value) -> Result<Response> {
    let user = data.get("user").and_then(Value::as_str).filter(|u| !u.is_empty()).unwrap_or("system");
    let Some(action) = data.get("action").and_then(Value::as_str).filter(|a| !a.is_empty() && a.len() <= 80) else {
        return http::error(400, "action is required.");
    };
    let icon = data.get("icon").and_then(Value::as_str);
    let fields = data.get("details").and_then(Value::as_object).cloned().unwrap_or_default();
    db::batch(&ctx.db, vec![db::activity(&ctx.db, user, action, icon, fields)?]).await?;
    http::json(201, &json!({"saved": true}))
}
