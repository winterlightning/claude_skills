//! Loading catalog and workflow rows from D1 into the core types.

use crate::args;
use crate::db::{self, Arg};
use pictographic_core::catalog::{Catalog, Icon};
use pictographic_core::reviews::{current_decisions, review_detail, ActiveSplit, Decision, ReviewRow};
use pictographic_core::work::{FeedbackMap, FeedbackSummary, RowMap};
use serde::Deserialize;
use serde_json::{json, Value};
use std::collections::HashMap;
use worker::{D1Database, Result};

#[derive(Deserialize)]
struct IconRow {
    key: String,
    icon_id: Option<String>,
    name: Option<String>,
    family: Option<String>,
    category: Option<String>,
    svg_sha256: Option<String>,
    python_source: Option<String>,
    preview_url: Option<String>,
    original_sources: Option<String>,
    canvas_size: Option<f64>,
    build_failed: Option<f64>,
    uploaded: Option<f64>,
}

impl From<IconRow> for Icon {
    fn from(row: IconRow) -> Self {
        Icon {
            key: row.key,
            icon_id: row.icon_id,
            name: row.name,
            family: row.family,
            category: row.category,
            svg_sha256: row.svg_sha256.unwrap_or_default(),
            python_source: row.python_source.and_then(|t| serde_json::from_str(&t).ok()).unwrap_or(Value::Null),
            preview_url: row.preview_url,
            original_sources: row.original_sources.and_then(|t| serde_json::from_str(&t).ok()).unwrap_or(Value::Array(vec![])),
            canvas_size: row.canvas_size.map(|n| n as i64),
            build_failed: row.build_failed.unwrap_or(0.0) != 0.0,
            uploaded: row.uploaded.unwrap_or(0.0) != 0.0,
        }
    }
}

const ICON_COLUMNS: &str = "key, icon_id, name, family, category, svg_sha256, python_source, preview_url, \
                            original_sources, canvas_size, build_failed, uploaded";

/// deploy.py `catalog(include_failed=...)`: built icons, then uploads, then failed builds.
pub async fn catalog(db: &D1Database, include_failed: bool) -> Result<Catalog> {
    let sql = format!("SELECT {ICON_COLUMNS} FROM icons {} ORDER BY build_failed, uploaded, rowid",
                      if include_failed { "" } else { "WHERE build_failed = 0" });
    let rows: Vec<IconRow> = db::all(db, &sql, vec![]).await?;
    Ok(Catalog::new(rows.into_iter().map(Icon::from).collect(), include_failed))
}

/// Every icon's stored decision and who made it (`icons.decision`, `actor`), for `GET /api/reviews`: one pass over icons,
/// in table order (sorting would read every row twice; the answer is a map).
pub async fn stored_decisions(db: &D1Database) -> Result<Vec<(String, Decision)>> {
    #[derive(Deserialize)]
    struct Row { key: String, decision: Option<String>, actor: Option<String> }
    let rows: Vec<Row> = db::all(db, "SELECT key, decision, actor FROM icons", vec![]).await?;
    Ok(rows.into_iter().map(|row| (row.key, Decision::stored(row.decision.as_deref(), row.actor, None))).collect())
}

/// deploy.py `catalog(...).get(key)` for a single key.
pub async fn icon(db: &D1Database, key: &str, include_failed: bool) -> Result<Option<Icon>> {
    let sql = format!("SELECT {ICON_COLUMNS} FROM icons WHERE key = ?{}", if include_failed { "" } else { " AND build_failed = 0" });
    Ok(db::first::<IconRow>(db, &sql, args![key]).await?.map(Icon::from))
}

pub async fn review_rows(db: &D1Database) -> Result<Vec<ReviewRow>> {
    db::all(db, "SELECT icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note FROM reviews ORDER BY updated_at", vec![]).await
}

pub async fn active_splits(db: &D1Database) -> Result<Vec<ActiveSplit>> {
    db::all(db, "SELECT icon, svg_sha256, created_by, created_at FROM split_requests WHERE active = 1", vec![]).await
}

/// Which icons a fix-queue read starts from. The stored review state picks them by index, so a read touches the
/// disapproved and worked-on icons, never the whole catalog.
#[derive(Clone, Copy, PartialEq)]
pub enum WorkScope {
    /// Disapproved or claimed (`/api/work/queue`, `/disapproved`).
    Fix,
    /// Those and every icon whose current drawing carries a worker: done, cannot-fix (`/api/work/review`).
    Review,
    /// Only icons whose current drawing carries a worker (`/api/work`).
    Worked,
}

/// Disapproved and claimed icons are stored with state `pending` (index icons_list_state). A claimed side or container
/// combination whose build failed is stored as `failed`; its review row has a worker (partial index reviews_worker).
const PENDING_KEYS: &str = "SELECT key FROM icons WHERE state = 'pending'";
const CURRENT_WORKER: &str = "FROM reviews r JOIN icons i ON i.key = r.icon AND i.svg_sha256 = r.svg_sha256 WHERE r.worker IS NOT NULL";

/// The icons of one scope as the work rules read them: catalog rows without the large `python_source` and
/// `original_sources` (`with_sources` adds them to a page), the current drawing's review row, the decision and
/// disapproval count the writes stored, and the stored feedback reason (`feedback`: reason only; a page or a text
/// search loads the notes themselves with `latest_feedback_for`).
pub struct WorkSet {
    pub catalog: Catalog,
    pub rows: Vec<ReviewRow>,
    pub decisions: Vec<(String, Decision)>,
    pub feedback: FeedbackMap,
    pub disapprovals: HashMap<String, u32>,
}

impl WorkSet {
    /// The keys as a JSON array, for the `json_each(?)` loaders below.
    pub fn keys(&self) -> String {
        json!(self.catalog.iter().map(|icon| icon.key.as_str()).collect::<Vec<_>>()).to_string()
    }
}

pub async fn work_set(db: &D1Database, scope: WorkScope) -> Result<WorkSet> {
    #[derive(Deserialize)]
    struct Row {
        #[serde(flatten)]
        icon: IconRow,
        decision: Option<String>,
        reason: Option<String>,
        disapprovals: Option<f64>,
        status: Option<String>,
        updated_at: Option<String>,
        updated_by: Option<String>,
        worker: Option<String>,
        claimed_at: Option<String>,
        note: Option<String>,
    }
    let keys = match scope {
        WorkScope::Fix => format!("{PENDING_KEYS} UNION ALL SELECT r.icon {CURRENT_WORKER} AND r.status = 'claimed' \
            AND COALESCE(i.state, '') != 'pending'"),
        WorkScope::Review => format!("{PENDING_KEYS} UNION ALL SELECT r.icon {CURRENT_WORKER} AND COALESCE(i.state, '') != 'pending'"),
        WorkScope::Worked => format!("SELECT r.icon {CURRENT_WORKER}"),
    };
    let rows: Vec<Row> = db::all(db, &format!("WITH k(key) AS ({keys}) SELECT i.{}, NULL AS python_source, NULL AS original_sources, \
        i.decision, i.reason, i.disapprovals, r.status, r.updated_at, r.updated_by, r.worker, r.claimed_at, r.note \
        FROM k JOIN icons i ON i.key = k.key LEFT JOIN reviews r ON r.icon = i.key AND r.svg_sha256 = i.svg_sha256",
        SLIM_COLUMNS.replace(", ", ", i.")), vec![]).await?;
    let mut set = WorkSet { catalog: Catalog::default(), rows: Vec::new(), decisions: Vec::new(), feedback: FeedbackMap::new(),
                            disapprovals: HashMap::new() };
    let mut icons = Vec::new();
    for row in rows {
        let icon = Icon::from(row.icon);
        let key = icon.key.clone();
        set.decisions.push((key.clone(), Decision::stored(row.decision.as_deref(), row.updated_by.clone(), row.updated_at.clone())));
        if let Some(status) = row.status {
            set.rows.push(ReviewRow { icon: key.clone(), svg_sha256: icon.svg_sha256.clone(), status, updated_at: row.updated_at,
                                      updated_by: row.updated_by, worker: row.worker, claimed_at: row.claimed_at, note: row.note });
        }
        // The stored reason says `missing` when the current drawing has no feedback.
        if let Some(reason) = row.reason.filter(|r| r != "missing") {
            set.feedback.insert((key.clone(), icon.svg_sha256.clone()), FeedbackSummary { reason: Some(reason), ..Default::default() });
        }
        set.disapprovals.insert(key, row.disapprovals.unwrap_or(0.0) as u32);
        icons.push(icon);
    }
    set.catalog = Catalog::new(icons, true);
    Ok(set)
}

/// One icon's review rows of every revision and the decision `current_decisions` gives it, read by key.
pub async fn icon_decisions(db: &D1Database, icon: &Icon) -> Result<(Vec<ReviewRow>, Vec<(String, Decision)>)> {
    let rows: Vec<ReviewRow> = db::all(db, "SELECT icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note FROM reviews \
        WHERE icon = ? ORDER BY updated_at", args![icon.key.clone()]).await?;
    let splits: Vec<ActiveSplit> = db::all(db, "SELECT icon, svg_sha256, created_by, created_at FROM split_requests \
        WHERE active = 1 AND icon = ?", args![icon.key.clone()]).await?;
    let decisions = current_decisions(&rows, &splits, &Catalog::new(vec![icon.clone()], true));
    Ok((rows, decisions))
}

const SLIM_COLUMNS: &str = "key, icon_id, name, family, category, svg_sha256, preview_url, canvas_size, build_failed, uploaded";

/// `python_source` and `original_sources` of the listed items (a page), as the full catalog row gives them.
pub async fn with_sources(db: &D1Database, items: &mut [Value]) -> Result<()> {
    #[derive(Deserialize)]
    struct Row { key: String, python_source: Option<String>, original_sources: Option<String> }
    let keys: Vec<&str> = items.iter().filter_map(|item| item["key"].as_str()).collect();
    if keys.is_empty() {
        return Ok(());
    }
    let rows: Vec<Row> = db::all(db, "SELECT key, python_source, original_sources FROM icons WHERE key IN (SELECT value FROM json_each(?))",
                                 args![json!(keys).to_string()]).await?;
    let sources: HashMap<String, Row> = rows.into_iter().map(|row| (row.key.clone(), row)).collect();
    for item in items.iter_mut() {
        let Some(row) = item["key"].as_str().and_then(|key| sources.get(key)) else { continue };
        item["python_source"] = row.python_source.as_deref().and_then(|t| serde_json::from_str(t).ok()).unwrap_or(Value::Null);
        let original = row.original_sources.as_deref().and_then(|t| serde_json::from_str(t).ok()).unwrap_or(Value::Array(vec![]));
        item["original_sources"] = if original.is_null() { Value::Array(vec![]) } else { original };
    }
    Ok(())
}

/// `latest_feedback` for the listed keys.
pub async fn latest_feedback_for(db: &D1Database, keys: &str) -> Result<FeedbackMap> {
    let rows: Vec<FeedbackRow> = db::all(db, "SELECT icon, svg_sha256, reason, feedback, author, created_at FROM feedback \
        WHERE icon IN (SELECT value FROM json_each(?)) ORDER BY id", args![keys]).await?;
    Ok(fold_latest(rows))
}

/// `icon_types` for the listed keys.
pub async fn icon_types_for(db: &D1Database, keys: &str) -> Result<HashMap<String, String>> {
    let rows: Vec<TypeRow> = db::all(db, "SELECT icon, icon_type FROM icon_types WHERE icon_type != '' \
        AND icon IN (SELECT value FROM json_each(?))", args![keys]).await?;
    Ok(rows.into_iter().map(|r| (r.icon, r.icon_type)).collect())
}

pub fn row_map(rows: &[ReviewRow]) -> RowMap {
    rows.iter().map(|row| ((row.icon.clone(), row.svg_sha256.clone()), row.clone())).collect()
}

#[derive(Deserialize)]
struct FeedbackRow {
    icon: String,
    svg_sha256: String,
    reason: Option<String>,
    feedback: Option<String>,
    author: Option<String>,
    created_at: Option<String>,
}

/// work_claims.py `latest_feedback`: the newest entry per (icon, sha), from rows in id order.
fn fold_latest(rows: Vec<FeedbackRow>) -> FeedbackMap {
    let mut latest = FeedbackMap::new();
    for row in rows {
        latest.insert((row.icon, row.svg_sha256), FeedbackSummary {
            reason: row.reason, feedback: row.feedback, feedback_by: row.author, feedback_at: row.created_at,
        });
    }
    latest
}

pub async fn feedback_for(db: &D1Database, key: &str, sha: &str) -> Result<Option<FeedbackSummary>> {
    let row: Option<FeedbackRow> = db::first(db, "SELECT icon, svg_sha256, reason, feedback, author, created_at FROM feedback \
        WHERE icon = ? AND svg_sha256 = ? ORDER BY id DESC LIMIT 1", args![key, sha]).await?;
    Ok(row.map(|r| FeedbackSummary { reason: r.reason, feedback: r.feedback, feedback_by: r.author, feedback_at: r.created_at }))
}

#[derive(Deserialize)]
struct TypeRow {
    icon: String,
    icon_type: String,
}

pub async fn icon_type(db: &D1Database, key: &str) -> Result<Option<String>> {
    let row: Option<TypeRow> = db::first(db, "SELECT icon, icon_type FROM icon_types WHERE icon = ? AND icon_type != ''", args![key]).await?;
    Ok(row.map(|r| r.icon_type))
}

pub async fn review_row(db: &D1Database, key: &str, sha: &str) -> Result<Option<ReviewRow>> {
    db::first(db, "SELECT icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note FROM reviews \
        WHERE icon = ? AND svg_sha256 = ?", args![key, sha]).await
}

#[derive(Deserialize)]
struct ByAt {
    by: Option<String>,
    at: Option<String>,
}

/// deploy.py `review_detail(connection, key, sha)`.
pub async fn detail(db: &D1Database, key: &str, sha: &str) -> Result<Decision> {
    let split: Option<ByAt> = db::first(db, "SELECT created_by AS by, created_at AS at FROM split_requests \
        WHERE icon = ? AND svg_sha256 = ? AND active = 1", args![key, sha]).await?;
    let rejected: Option<ByAt> = if split.is_some() { None } else {
        db::first(db, "SELECT updated_by AS by, updated_at AS at FROM reviews WHERE icon = ? AND +status = 'rejected' \
            ORDER BY updated_at DESC LIMIT 1", args![key]).await?
    };
    let row = review_row(db, key, sha).await?;
    Ok(review_detail(split.map(|s| (s.by, s.at)), rejected.map(|r| (r.by, r.at)),
                     row.map(|r| (r.status, r.updated_by, r.updated_at))))
}

/// deploy.py `is_rejected`: any rejected revision, or an active split of this revision.
pub async fn is_rejected(db: &D1Database, key: &str, sha: &str) -> Result<bool> {
    #[derive(Deserialize)]
    struct One { #[allow(dead_code)] one: f64 }
    let hit: Option<One> = db::first(db, "SELECT 1 AS one FROM reviews WHERE icon = ? AND +status = 'rejected' \
        UNION ALL SELECT 1 AS one FROM split_requests WHERE icon = ? AND svg_sha256 = ? AND active = 1 LIMIT 1",
        args![key, key, sha]).await?;
    Ok(hit.is_some())
}

pub async fn exists(db: &D1Database, sql: &str, args: Vec<Arg>) -> Result<bool> {
    #[derive(Deserialize)]
    struct Any {}
    Ok(db::first::<Any>(db, sql, args).await?.is_some())
}

/// Admin users: `{"name": "password"}` from the ADMIN_USERS variable.
pub fn admin_users(env: &worker::Env) -> Vec<(String, String)> {
    let text = env.var("ADMIN_USERS").map(|v| v.to_string()).unwrap_or_default();
    let map: serde_json::Map<String, Value> = serde_json::from_str(&text).unwrap_or_default();
    map.into_iter().map(|(k, v)| (k, v.as_str().unwrap_or("").to_string())).collect()
}
