//! Reference-primitive progress — deploy.py's primitive routes over primitive_status.py.
//! `primitives.json` (built locally, pushed to R2) is parsed once per isolate and reused by ETag.

use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::primitives::{self as rules, StatusRow};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;
use worker::{Response, Result};

pub const PRIMITIVES_KEY: &str = "site/gallery/primitives.json";

thread_local! {
    static CACHE: RefCell<Option<(String, Rc<Vec<Value>>)>> = const { RefCell::new(None) };
}

/// The catalog rows of primitives.json.
pub async fn rows(ctx: &Ctx) -> Result<Rc<Vec<Value>>> {
    let bucket = ctx.env.bucket("FILES")?;
    let head = bucket.head(PRIMITIVES_KEY).await?.ok_or_else(|| worker::Error::RustError("primitives.json has not been pushed".into()))?;
    let etag = head.etag();
    if let Some(rows) = CACHE.with(|c| c.borrow().as_ref().filter(|(tag, _)| *tag == etag).map(|(_, rows)| rows.clone())) {
        return Ok(rows);
    }
    let object = bucket.get(PRIMITIVES_KEY).execute().await?.ok_or_else(|| worker::Error::RustError("primitives.json vanished".into()))?;
    let bytes = object.body().ok_or_else(|| worker::Error::RustError("empty primitives.json".into()))?.bytes().await?;
    let mut parsed: Value = serde_json::from_slice(&bytes).map_err(|e| worker::Error::RustError(e.to_string()))?;
    let rows = Rc::new(match parsed.get_mut("rows").map(Value::take) { Some(Value::Array(rows)) => rows, _ => vec![] });
    CACHE.with(|c| *c.borrow_mut() = Some((etag, rows.clone())));
    Ok(rows)
}

async fn status_rows(ctx: &Ctx) -> Result<Vec<StatusRow>> {
    db::all(&ctx.db, "SELECT uuid, status, reason, note, updated_by, updated_at, main_brief, sub_brief, sub_position FROM primitive_status", vec![]).await
}

async fn statuses(ctx: &Ctx) -> Result<Map<String, Value>> {
    Ok(rules::load_status(&status_rows(ctx).await?))
}

#[derive(Deserialize)]
struct BriefRow { uuid: String, family: String, brief: String, updated_by: String, updated_at: String }

async fn briefs(ctx: &Ctx) -> Result<Map<String, Value>> {
    let rows: Vec<BriefRow> = db::all(&ctx.db, "SELECT uuid, family, brief, updated_by, updated_at FROM primitive_briefs", vec![]).await?;
    Ok(rows.into_iter().map(|r| (r.uuid, json!({"family": r.family, "brief": r.brief, "updated_by": r.updated_by, "updated_at": r.updated_at}))).collect())
}

async fn symbol_links(ctx: &Ctx) -> Result<Map<String, Value>> {
    #[derive(Deserialize)]
    struct Row { uuid: String, icon_key: String, updated_by: String, updated_at: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT uuid, icon_key, updated_by, updated_at FROM primitive_symbol_links", vec![]).await?;
    Ok(rows.into_iter().map(|r| (r.uuid, json!({"icon_key": r.icon_key, "updated_by": r.updated_by, "updated_at": r.updated_at}))).collect())
}

pub async fn get(ctx: &Ctx) -> Result<Response> {
    let unavailable = |_| http::error(503, "Primitive progress is temporarily unavailable");
    match ctx.path.as_str() {
        "/api/primitives/briefs" => http::json(200, &Value::Object(briefs(ctx).await?)),
        "/api/primitives/symbol-links" => http::json(200, &Value::Object(symbol_links(ctx).await?)),
        "/api/primitives/status" => http::json(200, &Value::Object(statuses(ctx).await?)),
        "/api/primitives/prompt" => {
            let parse = |name: &str, default: &str| ctx.param(name).unwrap_or(default).trim().parse::<i64>();
            let (count, offset) = match (parse("count", "4"), parse("offset", "0")) {
                (Ok(count), Ok(offset)) if (1..=100).contains(&count) && offset >= 0 => (count, offset),
                _ => return http::error(400, "count must be 1-100 and offset a non-negative integer"),
            };
            let rows = match rows(ctx).await { Ok(rows) => rows, Err(e) => return unavailable(e) };
            let merged = rules::merge(&rows, &statuses(ctx).await?);
            let result = rules::make_ray_prompt(&merged, ctx.param("category").unwrap_or(""), count, offset);
            if ctx.param("format").unwrap_or("text") == "json" {
                return http::json(200, &result);
            }
            http::text(200, result["prompt"].as_str().unwrap_or(""), "text/plain; charset=utf-8")
        }
        path => {
            let rows = match rows(ctx).await { Ok(rows) => rows, Err(e) => return unavailable(e) };
            let merged = rules::merge(&rows, &statuses(ctx).await?);
            if path == "/api/primitives/summary" {
                return http::json(200, &rules::summarize(&merged));
            }
            let filtered: Vec<Value> = rules::filter_rows(&merged, ctx.param("category"), ctx.param("status"),
                                                          ctx.param("batch"), ctx.param("reason")).into_iter().cloned().collect();
            http::json(200, &Value::Array(filtered))
        }
    }
}

/// deploy.py `_canonical_uuids`: folded aliases act on their canonical primitive.
async fn canonical(ctx: &Ctx, uuids: &[Value]) -> Result<(Vec<Value>, HashSet<String>)> {
    let map = rules::canonical_map(&rows(ctx).await?);
    let resolved = uuids.iter().map(|uid| match uid.as_str() {
        Some(text) => map.get(&text.trim().to_lowercase()).map(|c| json!(c)).unwrap_or_else(|| uid.clone()),
        None => uid.clone(),
    }).collect();
    Ok((resolved, map.keys().cloned().collect()))
}

pub async fn post_status(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let (uuids, known) = match data.get("uuids") {
        Some(Value::Array(list)) => { let (resolved, known) = canonical(ctx, list).await?; (json!(resolved), known) }
        other => {
            let known = rows(ctx).await?.iter().filter_map(|r| r["uuid"].as_str().map(str::to_string)).collect();
            (other.cloned().unwrap_or(Value::Null), known)
        }
    };
    let status = data.get("status").and_then(Value::as_str).unwrap_or("");
    let (cleaned, reason, note) = match rules::validate(&uuids, status, data.get("reason").unwrap_or(&Value::Null),
                                                        data.get("note").unwrap_or(&json!("")), Some(&known)) {
        Ok(ok) => ok,
        Err(message) => return http::error(400, &message),
    };
    let updates = match rules::brief_updates(data, status, reason.as_deref(), cleaned.len()) {
        Ok(updates) => updates,
        Err(message) => return http::error(400, &message),
    };
    let current: std::collections::HashMap<String, StatusRow> = status_rows(ctx).await?.into_iter().map(|r| (r.uuid.clone(), r)).collect();
    let now = iso_utc(chrono::Utc::now());
    let mut statements = Vec::new();
    let mut changed = 0;
    for uid in &cleaned {
        let change = rules::status_change(current.get(uid), status, reason.as_deref(), &note, &updates, "user");
        match &change.write {
            Some(rules::StatusWrite::Delete) => statements.push(db::stmt(&ctx.db, "DELETE FROM primitive_status WHERE uuid = ?", args![uid])?),
            Some(rules::StatusWrite::Upsert { reason, note, main, sub, position }) => statements.push(db::stmt(&ctx.db,
                "INSERT INTO primitive_status(uuid, status, reason, note, updated_by, updated_at, main_brief, sub_brief, sub_position) \
                 VALUES (?, 'skip', ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(uuid) DO UPDATE SET reason = excluded.reason, note = excluded.note, \
                 updated_by = excluded.updated_by, updated_at = excluded.updated_at, main_brief = excluded.main_brief, \
                 sub_brief = excluded.sub_brief, sub_position = excluded.sub_position, combination_brief = NULL",
                args![uid, reason, note, user, now.clone(), main.clone(), sub.clone(), position.clone()])?),
            None => {}
        }
        if let Some((action, fields)) = change.record {
            let pairs = fields.as_object().cloned().unwrap_or_default();
            statements.push(db::activity(&ctx.db, user, &action, Some(&format!("primitive:{uid}")), pairs)?);
        }
        changed += change.changed as usize;
    }
    db::batch(&ctx.db, statements).await?;
    let saved = statuses(ctx).await?;
    let mut decisions = Map::new();
    for uid in uuids.as_array().into_iter().flatten().filter_map(Value::as_str) {
        let uid = uid.trim().to_lowercase();
        decisions.insert(uid.clone(), saved.get(&uid).cloned().unwrap_or(Value::Null));
    }
    http::json(200, &json!({"status": status, "reason": reason, "changed": changed, "unchanged": cleaned.len() - changed,
                            "decisions": decisions}))
}

pub async fn post_brief(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let (resolved, known) = canonical(ctx, &[data.get("uuid").cloned().unwrap_or(Value::Null)]).await?;
    let (uid, family, brief) = match rules::validate_primitive_brief(&resolved[0], data.get("family").unwrap_or(&Value::Null),
                                                                     data.get("brief").unwrap_or(&Value::Null), &known) {
        Ok(ok) => ok,
        Err(message) => return http::error(400, &message),
    };
    #[derive(Deserialize)]
    struct Previous { family: String, brief: String }
    let previous: Option<Previous> = db::first(&ctx.db, "SELECT family, brief FROM primitive_briefs WHERE uuid = ?", args![uid.clone()]).await?;
    if previous.as_ref().map(|p| (p.family.as_str(), p.brief.as_str())) != Some((family.as_str(), brief.as_str())) {
        let now = iso_utc(chrono::Utc::now());
        db::batch(&ctx.db, vec![
            db::stmt(&ctx.db, "INSERT INTO primitive_briefs VALUES (?, ?, ?, ?, ?) ON CONFLICT(uuid) DO UPDATE SET family = excluded.family, \
                brief = excluded.brief, updated_by = excluded.updated_by, updated_at = excluded.updated_at",
                args![uid.clone(), family.clone(), brief.clone(), user, now])?,
            db::activity(&ctx.db, user, "primitive_brief", Some(&format!("primitive:{uid}")), details(vec![
                ("family", json!(family)), ("brief", json!(brief)), ("previous_family", json!(previous.map(|p| p.family))),
                ("authority", json!("user"))]))?,
        ]).await?;
    }
    http::json(200, briefs(ctx).await?.get(&uid).unwrap_or(&Value::Null))
}

pub async fn post_symbol_link(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let icon_key = data.get("icon").cloned().unwrap_or(Value::Null);
    if !icon_key.is_null() {
        let family = match icon_key.as_str() {
            Some(key) => data::icon(&ctx.db, key, false).await?.and_then(|icon| icon.family),
            None => None,
        };
        if family.as_deref() != Some("symbol") {
            return http::error(400, "Choose an existing symbol-family icon.");
        }
    }
    let (resolved, known) = canonical(ctx, &[data.get("uuid").cloned().unwrap_or(Value::Null)]).await?;
    let uid = match resolved[0].as_str().map(|u| u.trim().to_lowercase()).filter(|u| rules::is_uuid(u)) {
        Some(uid) => uid,
        None => return http::error(400, &format!("Invalid primitive id: {}", rules::python_repr(&resolved[0]))),
    };
    if !known.contains(&uid) {
        return http::error(400, &format!("Unknown primitive: {uid}"));
    }
    let subject = format!("primitive:{uid}");
    let Some(key) = icon_key.as_str() else {
        db::batch(&ctx.db, vec![
            db::stmt(&ctx.db, "DELETE FROM primitive_symbol_links WHERE uuid = ?", args![uid.clone()])?,
            db::activity(&ctx.db, user, "primitive_symbol_unlinked", Some(&subject), details(vec![]))?,
        ]).await?;
        return http::json(200, &json!({"uuid": uid, "icon_key": null}));
    };
    let key = key.trim();
    let now = iso_utc(chrono::Utc::now());
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "INSERT INTO primitive_symbol_links(uuid, icon_key, updated_by, updated_at) VALUES (?, ?, ?, ?) \
            ON CONFLICT(uuid) DO UPDATE SET icon_key = excluded.icon_key, updated_by = excluded.updated_by, updated_at = excluded.updated_at",
            args![uid.clone(), key, user, now.clone()])?,
        db::activity(&ctx.db, user, "primitive_symbol_linked", Some(&subject), details(vec![("icon_key", json!(key))]))?,
    ]).await?;
    http::json(200, &json!({"uuid": uid, "icon_key": key, "updated_by": user, "updated_at": now}))
}
