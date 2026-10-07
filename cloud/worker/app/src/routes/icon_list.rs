//! Icon review's list from D1 (core icon_query): a page of icon cards with the counts its tabs and categories show,
//! the filter choices, one icon's full record, and the stored columns those read (core icon_index).

use crate::args;
use crate::db::{self, Arg};
use crate::http::{self, Ctx};
use pictographic_core::icon_index::{index, IconIndex};
use pictographic_core::icon_query::{self, Params};
use pictographic_core::reviews::ReviewRow;
use pictographic_core::time::iso_utc;
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
    let sql = format!("UPDATE icons SET card = ?, search = ?, sort_name = ?, keyshape = ?, author = ?, side_role = ?, style = ?, style_of = ?, stroke_count = ?, \
        segment_count = ?, created_ms = ?, modified_ms = ?, version_group = ?, version = ?, variant = ?, has_original = ?, \
        artwork_source = ? WHERE key = ?{}", guard.map(|g| format!(" AND {g}")).unwrap_or_default());
    db::stmt(db, &sql, args![i.card, i.search, i.sort_name, i.keyshape, i.author, i.side_role, i.style, i.style_of, i.stroke_count, i.segment_count,
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

async fn query(ctx: &Ctx, p: &Params) -> Result<(Row, Vec<Row>, Map<String, Value>, Map<String, Value>, Map<String, Value>)> {
    let rows: Vec<Row> = statement(&ctx.db, icon_query::list(p))?.all().await?.results()?;
    let (mut total, mut page, mut states, mut categories, mut families) = (Row::new(), Vec::new(), Map::new(), Map::new(), Map::new());
    for (part, seq, data) in parsed(rows) {
        match part.as_str() {
            "total" => total = data,
            "state" => { if let (Some(Value::String(k)), Some(n)) = (data.get("state"), data.get("n")) { states.insert(k.clone(), n.clone()); } }
            "category" => { if let (Some(Value::String(k)), Some(n)) = (data.get("category"), data.get("n")) { categories.insert(k.clone(), n.clone()); } }
            "family" => { if let (Some(Value::String(k)), Some(n)) = (data.get("family"), data.get("n")) { families.insert(k.clone(), n.clone()); } }
            _ => page.push((seq, data)),
        }
    }
    page.sort_by_key(|(seq, _)| *seq);
    Ok((total, page.into_iter().map(|(_, row)| row).collect(), states, categories, families))
}

/// GET /api/icons?family=&q=&status=&…&sort=&view=&offset=&limit= (the page's URL filters), or ?keys=k1,k2 (≤ 200):
/// `{items, total, versions, offset, limit, states, categories}`; with keys or ?group=<version group>, `{items}`. One statement reads the icons
/// once for the page and every count.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    if let Some(group) = ctx.param("group") {
        let rows: Vec<Row> = statement(&ctx.db, icon_query::by_group(group))?.all().await?.results()?;
        return http::json(200, &json!({"items": items(parsed(rows).into_iter().map(|(_, _, row)| row).collect())}));
    }
    if let Some(keys) = ctx.param("keys") {
        let keys: Vec<String> = keys.split(',').filter(|k| !k.is_empty()).map(str::to_string).collect();
        if keys.is_empty() || keys.len() > 200 {
            return http::error(400, "Ask for 1 to 200 icon keys.");
        }
        let rows: Vec<Row> = statement(&ctx.db, icon_query::by_keys(&keys))?.all().await?.results()?;
        return http::json(200, &json!({"items": items(parsed(rows).into_iter().map(|(_, _, row)| row).collect())}));
    }
    let mut p = params(ctx);
    let (mut total, mut page, mut states, mut categories, mut families) = query(ctx, &p).await?;
    let number = |row: &Row, field: &str| row.get(field).and_then(Value::as_f64).unwrap_or(0.0) as i64;
    let units = number(&total, "total");
    // Past the end: the last page, as the page clamps it.
    if p.offset >= units && units > 0 {
        p.offset = (units - 1) / p.limit * p.limit;
        (total, page, states, categories, families) = query(ctx, &p).await?;
    }
    http::json(200, &json!({"items": items(page), "total": number(&total, "total"), "versions": number(&total, "versions"),
                            "offset": p.offset, "limit": p.limit, "states": states, "categories": categories, "families": families}))
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

/// POST /api/icons/reindex {offset, limit} (push token): the list columns of stored rows again from their stored
/// records (uploads, combined icons built in the browser, pushed rows with a record), their review state (view
/// icon_state) and search rows. `offset` is a row id cursor → `{indexed, next_offset}`; the counts are rebuilt with
/// the last page.
pub async fn reindex(ctx: &Ctx, data: &Value) -> Result<Response> {
    let after = data["offset"].as_i64().unwrap_or(0).max(0);
    let limit = data["limit"].as_i64().unwrap_or(500).clamp(1, 2000);
    #[derive(Deserialize)]
    struct Stored { rowid: f64, key: String, record: String, built: f64 }
    let rows: Vec<Stored> = db::all(&ctx.db, &format!("SELECT rowid, key, record, CASE WHEN {BUILT_IN_BROWSER} THEN 1 ELSE 0 END AS built \
        FROM icons WHERE rowid > ? ORDER BY rowid LIMIT ?"), args![after, limit]).await?;
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
    let last = rows.last().map(|r| r.rowid as i64);
    if let (Some(first), Some(last)) = (rows.first().map(|r| r.rowid as i64), last) {
        refresh_range(ctx, first, last + 1).await?;
    }
    let next = last.filter(|_| rows.len() as i64 == limit);
    if next.is_none() {
        rebuild_counts(ctx, None).await?;
    }
    http::json(200, &json!({"indexed": indexed, "next_offset": next}))
}

/// Before a write that changes one icon's review state, drawing, row or build (a review, feedback, split, artwork
/// pick, claim, upload, build, push or discard): the statements that take the icon out of the count rows it is in
/// (core `UNCOUNT_ICON`). Put them in the write's batch ahead of the write, and `recount` after it.
pub fn uncount(db: &D1Database, key: &str) -> Result<Vec<D1PreparedStatement>> {
    icon_query::UNCOUNT_ICON.iter().map(|sql| db::stmt(db, sql, args![key])).collect()
}

/// After such a write: the icon's stored review state again from the view and the icon counted in the rows of its
/// new state (core `REFRESH_KEY`, `RECOUNT_ICON`). With `search`, its search row again too (an inserted or renamed
/// icon). An icon the write deleted has no row left, so this adds nothing for it.
pub fn recount(db: &D1Database, key: &str, search: bool) -> Result<Vec<D1PreparedStatement>> {
    let mut statements = vec![db::stmt(db, icon_query::REFRESH_KEY, args![key])?];
    for sql in icon_query::RECOUNT_ICON.iter().chain(if search { icon_query::SEARCH_KEY.iter() } else { [].iter() }) {
        statements.push(db::stmt(db, sql, args![key])?);
    }
    Ok(statements)
}

/// Both, for a write that leaves the icon's row in place (a review, feedback, split, artwork choice or claim).
pub fn recalc(db: &D1Database, key: &str) -> Result<Vec<D1PreparedStatement>> {
    let mut statements = uncount(db, key)?;
    statements.extend(recount(db, key, false)?);
    Ok(statements)
}

/// After a part's review changed (approved, disapproved, rejected): the combined icons built from it say again
/// whether their build failed (core `combined_parts`), so a pair whose main and sub were approved after it was
/// built leaves "failed" for its own review, and one whose part was disapproved goes back. Returns how many changed.
pub async fn recheck_combined(db: &D1Database, part: &str) -> Result<usize> {
    use pictographic_core::combined_parts;
    #[derive(Deserialize)]
    struct Key { key: String }
    let using: Vec<Key> = db::all(db, combined_parts::USING_PART, args![part]).await?;
    if using.is_empty() {
        return Ok(0);
    }
    let keys = json!(using.iter().map(|k| k.key.as_str()).collect::<Vec<_>>()).to_string();
    let changed: Vec<Key> = db::all(db, combined_parts::CHANGED, args![keys]).await?;
    for chunk in changed.chunks(25) {
        let list = json!(chunk.iter().map(|k| k.key.as_str()).collect::<Vec<_>>()).to_string();
        let mut statements = Vec::new();
        for k in chunk {
            statements.extend(uncount(db, &k.key)?);
        }
        for sql in combined_parts::UPDATE {
            statements.push(db::stmt(db, sql, args![list.clone()])?);
        }
        for k in chunk {
            statements.extend(recount(db, &k.key, false)?);
        }
        db::batch(db, statements).await?;
    }
    Ok(changed.len())
}

/// Before a write that deletes the icon's row: the icon out of its count rows and its search row gone.
pub fn remove(db: &D1Database, key: &str) -> Result<Vec<D1PreparedStatement>> {
    let mut statements = uncount(db, key)?;
    for sql in &icon_query::SEARCH_KEY[..2] {
        statements.push(db::stmt(db, sql, args![key])?);
    }
    Ok(statements)
}

/// After a write that deleted rows by condition (a final catalog push's removals): the search rows of icons that
/// no longer exist dropped, and the counts rebuilt from one pass over icons.
pub async fn after_bulk_delete(ctx: &Ctx) -> Result<()> {
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "DELETE FROM icon_search WHERE rowid IN (SELECT k.search_rowid FROM icon_search_keys k \
            WHERE NOT EXISTS (SELECT 1 FROM icons i WHERE i.key = k.key))", vec![])?,
        db::stmt(&ctx.db, "DELETE FROM icon_search_keys WHERE NOT EXISTS (SELECT 1 FROM icons i WHERE i.key = icon_search_keys.key)", vec![])?,
    ]).await?;
    rebuild_counts(ctx, None).await?;
    Ok(())
}

/// The stored state and search rows of the icons with rowid in [from, to).
async fn refresh_range(ctx: &Ctx, from: i64, to: i64) -> Result<()> {
    #[derive(Deserialize)]
    struct Key { key: String }
    let keys: Vec<Key> = db::all(&ctx.db, "SELECT key FROM icons WHERE rowid >= ? AND rowid < ?", args![from, to]).await?;
    db::run(&ctx.db, icon_query::REFRESH_RANGE, args![from, to]).await?;
    refresh_search(ctx, &keys.into_iter().map(|k| k.key).collect::<Vec<_>>()).await
}

/// The search rows of the named icons again (core `SEARCH_REFRESH`), 100 keys at a time.
async fn refresh_search(ctx: &Ctx, keys: &[String]) -> Result<()> {
    for chunk in keys.chunks(100) {
        let list = Value::Array(chunk.iter().map(|k| json!(k)).collect()).to_string();
        let [delete_rows, delete_keys, insert_rows, remember] = icon_query::SEARCH_REFRESH;
        db::batch(&ctx.db, vec![
            db::stmt(&ctx.db, delete_rows, args![list.clone()])?,
            db::stmt(&ctx.db, delete_keys, args![list.clone()])?,
            db::stmt(&ctx.db, insert_rows, args![list])?,
            db::stmt(&ctx.db, remember, vec![])?,
        ]).await?;
    }
    Ok(())
}

/// POST /api/icons/refresh — the gallery's "Refresh stats" button (a logged-in reviewer, or the push token).
/// Recomputes the stored review state and the search row of every icon the activity log names since the last
/// refresh, then rebuilds the tab and filter counts from one pass over icons → `{refreshed, counts, activity_id}`.
/// `{full: true, offset, limit}` instead recomputes every icon a page at a time (a repair after writes that bypass
/// the log, such as local pushes to /api/store) → `{refreshed, next_offset}`; the counts are rebuilt with the last page.
pub async fn refresh(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" && !super::internal::authorized(ctx) {
        return http::error(401, "Log in, or send the push token, to refresh the list.");
    }
    if data["full"] == json!(true) {
        let after = data["offset"].as_i64().unwrap_or(0).max(0);
        let limit = data["limit"].as_i64().unwrap_or(500).clamp(1, 2000);
        #[derive(Deserialize)]
        struct Range { first: Option<f64>, last: Option<f64>, n: f64 }
        let range: Option<Range> = db::first(&ctx.db, "SELECT MIN(rowid) AS first, MAX(rowid) AS last, COUNT(*) AS n \
            FROM (SELECT rowid FROM icons WHERE rowid > ? ORDER BY rowid LIMIT ?)", args![after, limit]).await?;
        let (mut refreshed, mut next) = (0, None);
        if let Some(Range { first: Some(first), last: Some(last), n }) = range {
            refresh_range(ctx, first as i64, last as i64 + 1).await?;
            refreshed = n as i64;
            next = Some(last as i64).filter(|_| n as i64 == limit);
        }
        if next.is_none() {
            // Search rows of icons deleted since: their keys are no longer in icons.
            after_bulk_delete(ctx).await?;
            db::run(&ctx.db, "UPDATE list_refresh SET refreshed_at = ?, refreshed_by = ?, refreshed_icons = ? WHERE id = 1",
                    args![iso_utc(chrono::Utc::now()), user, refreshed]).await?;
        }
        return http::json(200, &json!({"refreshed": refreshed, "next_offset": next}));
    }
    #[derive(Deserialize)]
    struct Since { last_activity_id: f64 }
    #[derive(Deserialize)]
    struct Changed { icon: String }
    #[derive(Deserialize)]
    struct Latest { id: f64 }
    let since: Option<Since> = db::first(&ctx.db, "SELECT last_activity_id FROM list_refresh WHERE id = 1", vec![]).await?;
    let since = since.map(|s| s.last_activity_id as i64).unwrap_or(0);
    let latest: Option<Latest> = db::first(&ctx.db, "SELECT COALESCE(MAX(id), 0) AS id FROM activity_log", vec![]).await?;
    let latest = latest.map(|l| l.id as i64).unwrap_or(0);
    let changed: Vec<Changed> = db::all(&ctx.db, "SELECT DISTINCT icon FROM activity_log WHERE id > ? AND id <= ? AND icon IS NOT NULL \
        AND icon LIKE '%/%'", args![since, latest]).await?;
    let keys: Vec<String> = changed.into_iter().map(|c| c.icon).collect();
    for chunk in keys.chunks(100) {
        let list = Value::Array(chunk.iter().map(|k| json!(k)).collect()).to_string();
        db::run(&ctx.db, icon_query::REFRESH_KEYS, args![list]).await?;
    }
    refresh_search(ctx, &keys).await?;
    let counts = rebuild_counts(ctx, Some((user, keys.len() as i64))).await?;
    db::run(&ctx.db, "UPDATE list_refresh SET last_activity_id = ? WHERE id = 1", args![latest]).await?;
    http::json(200, &json!({"refreshed": keys.len(), "counts": counts, "activity_id": latest}))
}

/// icon_counts and icon_facet_counts again from one pass over icons (core `GROUPS`, split by `count_rows`), with the
/// refresh bookkeeping when `stamp` names who refreshed how many → how many count rows were written.
async fn rebuild_counts(ctx: &Ctx, stamp: Option<(&str, i64)>) -> Result<usize> {
    let groups: Vec<icon_query::Group> = db::all(&ctx.db, icon_query::GROUPS, vec![]).await?;
    let (counts, facets) = icon_query::count_rows(&groups);
    let mut statements = vec![db::stmt(&ctx.db, icon_query::COUNTS_CLEAR[0], vec![])?, db::stmt(&ctx.db, icon_query::COUNTS_CLEAR[1], vec![])?];
    // D1 binds at most 100 values per statement.
    for chunk in counts.chunks(14) {
        let values = vec!["(?, ?, ?, ?, ?, ?, ?)"; chunk.len()].join(", ");
        let mut values_args = Vec::new();
        for (family, side_role, style, state, category, failed, n) in chunk {
            values_args.extend(args![family, side_role, style, state, category, *failed, *n]);
        }
        statements.push(db::stmt(&ctx.db, &format!("{}{values}", icon_query::COUNTS_INSERT), values_args)?);
    }
    for chunk in facets.chunks(33) {
        let values = vec!["(?, ?, ?)"; chunk.len()].join(", ");
        let mut values_args = Vec::new();
        for (kind, value, n) in chunk {
            values_args.extend(args![*kind, value, *n]);
        }
        statements.push(db::stmt(&ctx.db, &format!("{}{values}", icon_query::FACETS_INSERT), values_args)?);
    }
    if let Some((user, refreshed)) = stamp {
        statements.push(db::stmt(&ctx.db, "UPDATE list_refresh SET refreshed_at = ?, refreshed_by = ?, refreshed_icons = ? WHERE id = 1",
                                 args![iso_utc(chrono::Utc::now()), user, refreshed])?);
    }
    db::batch(&ctx.db, statements).await?;
    Ok(counts.len() + facets.len())
}

/// POST /api/icons/records {records: [record…], facets: {key: facet}} (push token, ≤ 300 records): store the full record
/// of icons already in D1 (rows pushed before migration 0015 have none) with their list columns and symmetry. Only
/// those columns change, so a drawing picked since the push keeps its svg_sha256 → `{stored}`.
pub async fn records(ctx: &Ctx, data: &Value) -> Result<Response> {
    let Some(records) = data["records"].as_array().filter(|r| r.len() <= 300) else {
        return http::error(400, "Send up to 300 records.");
    };
    let guard = format!("uploaded = 0 AND NOT ({BUILT_IN_BROWSER})");
    let (mut statements, mut record_rows) = (Vec::new(), Vec::new());
    for record in records {
        let Some(key) = record["key"].as_str() else { continue };
        let mut stored = record.clone();
        stored.as_object_mut().map(|r| r.remove("uploaded_svg"));
        record_rows.push(statements.len());
        statements.push(db::stmt(&ctx.db, &format!("UPDATE icons SET record = ? WHERE key = ? AND {guard}"),
                                 args![stored.to_string(), key])?);
        statements.push(index_statement(&ctx.db, key, &stored, Some(&guard))?);
        if let Some(facet) = data["facets"].get(key) {
            statements.push(symmetry_statement(&ctx.db, key, facet)?);
        }
        // The record changes the card's keyshape, author, measured axes and search text.
        statements.extend(uncount(&ctx.db, key)?);
        statements.extend(recount(&ctx.db, key, true)?);
    }
    // One batch: the record statements are every one that starts an icon's group.
    let results = db::batch(&ctx.db, statements).await?;
    let stored: usize = record_rows.iter().map(|&i| results.get(i).map(db::changes).unwrap_or(0)).sum();
    http::json(200, &json!({"stored": stored}))
}
