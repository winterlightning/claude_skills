//! Icon review's list from D1 (core icon_query): a page of icon cards with the counts its tabs and categories show,
//! the filter choices, one icon's full record, and the stored columns those read (core icon_index).

use crate::args;
use crate::db::{self, Arg};
use crate::http::{self, Ctx};
use pictographic_core::icon_index::{index, IconIndex};
use pictographic_core::icon_query::{self, Params};
use pictographic_core::reviews::ReviewRow;
use pictographic_core::work;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use std::collections::HashMap;
use worker::{D1Database, D1PreparedStatement, Response, Result};

type Row = HashMap<String, Value>;

fn to_args(values: Vec<Value>) -> Vec<Arg> {
    values.into_iter().map(|v| match v {
        Value::Null => Arg::Null,
        Value::Bool(b) => Arg::Int(b as i64),
        Value::Number(n) => n.as_i64().map(Arg::Int).unwrap_or_else(|| Arg::Real(n.as_f64().unwrap_or(0.0))),
        Value::String(s) => Arg::Text(s),
        other => Arg::Text(other.to_string()),
    }).collect()
}

fn statement(db: &D1Database, (sql, args): (String, Vec<Value>)) -> Result<D1PreparedStatement> {
    db::stmt(db, &sql, to_args(args))
}

/// Combined icons whose drawing was built in the browser keep their columns from that build, not a push.
pub const BUILT_IN_BROWSER: &str = "family IN ('side_combination64', 'container_combination64', 'combination-72') \
    AND EXISTS (SELECT 1 FROM revisions r WHERE r.svg_sha256 = icons.svg_sha256 AND r.origin = 'combination-build')";

/// Store what the list reads of a record (`guard`: an extra condition on the row, e.g. NOT BUILT_IN_BROWSER).
pub fn index_statement(db: &D1Database, key: &str, record: &Value, guard: Option<&str>) -> Result<D1PreparedStatement> {
    let i: IconIndex = index(record, None);
    let sql = format!("UPDATE icons SET card = ?, search = ?, sort_name = ?, keyshape = ?, author = ?, side_role = ?, stroke_count = ?, \
        segment_count = ?, created_ms = ?, modified_ms = ?, version_group = ?, version = ?, variant = ?, has_original = ?, \
        artwork_source = ? WHERE key = ?{}", guard.map(|g| format!(" AND {g}")).unwrap_or_default());
    db::stmt(db, &sql, args![i.card, i.search, i.sort_name, i.keyshape, i.author, i.side_role, i.stroke_count, i.segment_count,
                             i.created_ms, i.modified_ms, i.version_group, i.version, i.variant, i.has_original, i.artwork_source, key])
}

/// The measured mirror axes of an icon (a review-facets.json entry `{axes, svg_sha256}`, or null to clear).
pub fn symmetry_statement(db: &D1Database, key: &str, facet: &Value) -> Result<D1PreparedStatement> {
    let i = index(&json!({}), facet.is_object().then_some(facet));
    db::stmt(db, "UPDATE icons SET symmetry = ?, symmetry_sha = ? WHERE key = ?", args![i.symmetry, i.symmetry_sha, key])
}

fn params(ctx: &Ctx) -> Params {
    Params::from_query(|name| ctx.param(name).map(str::to_string))
}

/// A list row's work claim as /api/work reports it for the current drawing (`workClaims`), or null.
fn work_of(row: &Row) -> Value {
    let text = |name: &str| row.get(name).and_then(Value::as_str).map(str::to_string);
    let Some(status) = text("row_status") else { return Value::Null };
    let review = ReviewRow { icon: text("key").unwrap_or_default(), svg_sha256: text("svg_sha256").unwrap_or_default(), status,
                             updated_at: text("row_at"), updated_by: None, worker: text("worker"), claimed_at: text("claimed_at"),
                             note: text("note") };
    match work::work_state(Some(&review), chrono::Utc::now()) {
        Some(state) => json!({"state": state, "worker": review.worker, "note": review.note.clone().unwrap_or_default(),
                              "claimed_at": review.claimed_at, "updated_at": review.updated_at,
                              "expires_at": work::expires_at(Some(&review)), "svg_sha256": review.svg_sha256}),
        None => Value::Null,
    }
}

fn items(rows: Vec<Row>) -> Vec<Value> {
    rows.into_iter().map(|row| {
        let work = work_of(&row);
        let mut item = icon_query::item(&row, work);
        // A pick made since the push is shown from the Worker, like the artwork overlay's preview.
        if row.get("picked").is_some_and(|p| !p.is_null()) {
            let key = row.get("key").and_then(Value::as_str).unwrap_or("");
            let sha = row.get("svg_sha256").and_then(Value::as_str).unwrap_or("");
            item["preview_url"] = json!(format!("../api/icon-artwork/svg?icon={}&v={sha}", http::percent_encode(key)));
        } else if let Some(url) = row.get("preview_url").filter(|u| !u.is_null()) {
            item["preview_url"] = url.clone();
        }
        item
    }).collect()
}

/// Rows `{data}` (and `part`, `seq`) whose `data` is a JSON object, parsed.
fn parsed(rows: Vec<Row>) -> Vec<(String, i64, Row)> {
    rows.into_iter().filter_map(|r| {
        let data: Row = serde_json::from_str(r.get("data")?.as_str()?).ok()?;
        let part = r.get("part").and_then(Value::as_str).unwrap_or("item").to_string();
        Some((part, r.get("seq").and_then(Value::as_f64).unwrap_or(0.0) as i64, data))
    }).collect()
}

async fn query(ctx: &Ctx, p: &Params) -> Result<(Row, Vec<Row>, Map<String, Value>, Map<String, Value>)> {
    let rows: Vec<Row> = statement(&ctx.db, icon_query::list(p))?.all().await?.results()?;
    let (mut total, mut page, mut states, mut categories) = (Row::new(), Vec::new(), Map::new(), Map::new());
    for (part, seq, data) in parsed(rows) {
        match part.as_str() {
            "total" => total = data,
            "state" => { if let (Some(Value::String(k)), Some(n)) = (data.get("state"), data.get("n")) { states.insert(k.clone(), n.clone()); } }
            "category" => { if let (Some(Value::String(k)), Some(n)) = (data.get("category"), data.get("n")) { categories.insert(k.clone(), n.clone()); } }
            _ => page.push((seq, data)),
        }
    }
    page.sort_by_key(|(seq, _)| *seq);
    Ok((total, page.into_iter().map(|(_, row)| row).collect(), states, categories))
}

/// GET /api/icons?family=&q=&status=&…&sort=&view=&offset=&limit= (the page's URL filters), or ?keys=k1,k2 (≤ 200):
/// `{items, total, versions, offset, limit, states, categories}`; with keys, `{items}`. One statement reads the icons
/// once for the page and every count.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    if let Some(keys) = ctx.param("keys") {
        let keys: Vec<String> = keys.split(',').filter(|k| !k.is_empty()).map(str::to_string).collect();
        if keys.is_empty() || keys.len() > 200 {
            return http::error(400, "Ask for 1 to 200 icon keys.");
        }
        let rows: Vec<Row> = statement(&ctx.db, icon_query::by_keys(&keys))?.all().await?.results()?;
        return http::json(200, &json!({"items": items(parsed(rows).into_iter().map(|(_, _, row)| row).collect())}));
    }
    let mut p = params(ctx);
    let (mut total, mut page, mut states, mut categories) = query(ctx, &p).await?;
    let number = |row: &Row, field: &str| row.get(field).and_then(Value::as_f64).unwrap_or(0.0) as i64;
    let units = number(&total, "total");
    // Past the end: the last page, as the page clamps it.
    if p.offset >= units && units > 0 {
        p.offset = (units - 1) / p.limit * p.limit;
        (total, page, states, categories) = query(ctx, &p).await?;
    }
    http::json(200, &json!({"items": items(page), "total": number(&total, "total"), "versions": number(&total, "versions"),
                            "offset": p.offset, "limit": p.limit, "states": states, "categories": categories}))
}

/// GET /api/icons/facets: the filter choices with counts `{authors, keyshapes, categories, families}` and how many
/// icons are built (`total`, failed builds not included).
pub async fn facets(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Facet { kind: String, value: Option<String>, n: f64 }
    let rows: Vec<Facet> = db::all(&ctx.db, icon_query::FACETS, vec![]).await?;
    let mut out: Map<String, Value> = ["authors", "keyshapes", "categories", "families"].iter().map(|k| (k.to_string(), json!({}))).collect();
    let mut total = 0;
    for row in rows {
        let Some(value) = row.value else { continue };
        let list = match row.kind.as_str() { "author" => "authors", "keyshape" => "keyshapes", "category" => "categories",
                                             "family" => "families", _ => { total = row.n as i64; continue } };
        out[list][value] = json!(row.n as i64);
    }
    out.insert("total".into(), json!(total));
    http::json(200, &Value::Object(out))
}

/// GET /api/icon?key=: one icon's full record as the gallery shows it (a pick made since the push applied), with its
/// review and work state.
pub async fn detail(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("key").unwrap_or("").to_string();
    let rows: Vec<Row> = statement(&ctx.db, icon_query::by_keys(std::slice::from_ref(&key)))?.all().await?.results()?;
    let Some((_, _, row)) = parsed(rows).into_iter().next() else { return http::error(404, "Unknown icon") };
    #[derive(Deserialize)]
    struct Stored { record: String }
    let stored: Option<Stored> = db::first(&ctx.db, "SELECT record FROM icons WHERE key = ?", args![key.clone()]).await?;
    let mut record: Value = match super::combinations::record_of(ctx, &key).await? {
        Some(built) => built,
        None => stored.and_then(|s| serde_json::from_str(&s.record).ok()).filter(Value::is_object).unwrap_or_else(|| json!({})),
    };
    if let Some(Value::Object(overlay)) = super::edits::override_of(ctx, &key).await? {
        for (field, value) in overlay {
            record[field] = value;
        }
    }
    let item = items(vec![row]).remove(0);
    for field in ["svg_sha256", "build_failed", "review", "work", "stroke_count", "segment_count", "symmetry_axes", "uploaded_icon",
                  "artwork_source", "preview_url", "name", "icon_id", "family", "category", "key"] {
        if let Some(value) = item.get(field).filter(|v| !v.is_null() || record.get(field).is_none()) {
            record[field] = value.clone();
        }
    }
    record.as_object_mut().map(|r| r.remove("add"));
    http::json(200, &record)
}

/// POST /api/icons/reindex {offset, limit} (push token): the list columns of stored rows again, from their stored
/// records (uploads, combined icons built in the browser, pushed rows with a record) → `{indexed, next_offset}`.
pub async fn reindex(ctx: &Ctx, data: &Value) -> Result<Response> {
    let offset = data["offset"].as_i64().unwrap_or(0).max(0);
    let limit = data["limit"].as_i64().unwrap_or(500).clamp(1, 2000);
    #[derive(Deserialize)]
    struct Stored { key: String, record: String, built: f64 }
    let rows: Vec<Stored> = db::all(&ctx.db, &format!("SELECT key, record, CASE WHEN {BUILT_IN_BROWSER} THEN 1 ELSE 0 END AS built \
        FROM icons ORDER BY rowid LIMIT ? OFFSET ?"), args![limit, offset]).await?;
    let mut statements = Vec::new();
    for row in &rows {
        let record = if row.built != 0.0 {
            super::combinations::record_of(ctx, &row.key).await?
        } else {
            serde_json::from_str::<Value>(&row.record).ok().filter(|r| r.as_object().is_some_and(|o| !o.is_empty()))
        };
        if let Some(record) = record {
            statements.push(index_statement(&ctx.db, &row.key, &record, None)?);
        }
    }
    let indexed = statements.len();
    for chunk in statements.chunks(100) {
        db::batch(&ctx.db, chunk.to_vec()).await?;
    }
    let next = (rows.len() as i64 == limit).then_some(offset + limit);
    http::json(200, &json!({"indexed": indexed, "next_offset": next}))
}
