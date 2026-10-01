//! Loading catalog and workflow rows from D1 into the core types.

use crate::args;
use crate::db::{self, Arg};
use pictographic_core::catalog::{Catalog, Icon};
use pictographic_core::reviews::{current_decisions, review_detail, ActiveSplit, Decision, ReviewRow};
use pictographic_core::work::{FeedbackMap, FeedbackSummary, RowMap};
use serde::Deserialize;
use serde_json::Value;
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

/// Only what `current_decisions` reads (key, drawing hash and the order flags), for `GET /api/reviews`:
/// loading every column of every icon there ran the Worker out of memory when page loads overlapped.
pub async fn review_catalog(db: &D1Database) -> Result<Catalog> {
    let rows: Vec<IconRow> = db::all(db, "SELECT key, svg_sha256, build_failed, uploaded FROM icons \
        ORDER BY build_failed, uploaded, rowid", vec![]).await?;
    Ok(Catalog::new(rows.into_iter().map(Icon::from).collect(), true))
}

/// `decisions` reading only the review columns a decision keeps (no worker, claim time or note).
pub async fn review_decisions(db: &D1Database, catalog: &Catalog) -> Result<Vec<(String, Decision)>> {
    let rows: Vec<ReviewRow> = db::all(db, "SELECT icon, svg_sha256, status, updated_at, updated_by FROM reviews \
        ORDER BY updated_at", vec![]).await?;
    let splits = active_splits(db).await?;
    Ok(current_decisions(&rows, &splits, catalog))
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

pub async fn decisions(db: &D1Database, catalog: &Catalog) -> Result<(Vec<ReviewRow>, Vec<ActiveSplit>, Vec<(String, Decision)>)> {
    let rows = review_rows(db).await?;
    let splits = active_splits(db).await?;
    let decisions = current_decisions(&rows, &splits, catalog);
    Ok((rows, splits, decisions))
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

/// work_claims.py `latest_feedback`: the newest entry per (icon, sha).
pub async fn latest_feedback(db: &D1Database) -> Result<FeedbackMap> {
    let rows: Vec<FeedbackRow> = db::all(db, "SELECT icon, svg_sha256, reason, feedback, author, created_at FROM feedback ORDER BY id", vec![]).await?;
    let mut latest = FeedbackMap::new();
    for row in rows {
        latest.insert((row.icon, row.svg_sha256), FeedbackSummary {
            reason: row.reason, feedback: row.feedback, feedback_by: row.author, feedback_at: row.created_at,
        });
    }
    Ok(latest)
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

pub async fn icon_types(db: &D1Database) -> Result<HashMap<String, String>> {
    let rows: Vec<TypeRow> = db::all(db, "SELECT icon, icon_type FROM icon_types WHERE icon_type != ''", vec![]).await?;
    Ok(rows.into_iter().map(|r| (r.icon, r.icon_type)).collect())
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
        db::first(db, "SELECT updated_by AS by, updated_at AS at FROM reviews WHERE icon = ? AND status = 'rejected' \
            ORDER BY updated_at DESC LIMIT 1", args![key]).await?
    };
    let row = review_row(db, key, sha).await?;
    Ok(review_detail(split.map(|s| (s.by, s.at)), rejected.map(|r| (r.by, r.at)),
                     row.map(|r| (r.status, r.updated_by, r.updated_at))))
}

/// In-memory `review_detail` for many icons at once, from rows already loaded.
pub struct DetailIndex {
    splits: HashMap<(String, String), (Option<String>, Option<String>)>,
    rejected: HashMap<String, (Option<String>, Option<String>, String)>,
    rows: RowMap,
}

impl DetailIndex {
    pub fn new(rows: &[ReviewRow], splits: &[ActiveSplit]) -> Self {
        let mut rejected: HashMap<String, (Option<String>, Option<String>, String)> = HashMap::new();
        for row in rows.iter().filter(|r| r.status == "rejected") {
            let stamp = row.updated_at.clone().unwrap_or_default();
            let newer = rejected.get(&row.icon).is_none_or(|(_, _, seen)| stamp > *seen);
            if newer {
                rejected.insert(row.icon.clone(), (row.updated_by.clone(), row.updated_at.clone(), stamp));
            }
        }
        DetailIndex {
            splits: splits.iter().map(|s| ((s.icon.clone(), s.svg_sha256.clone()), (s.created_by.clone(), s.created_at.clone()))).collect(),
            rejected,
            rows: row_map(rows),
        }
    }

    pub fn detail(&self, key: &str, sha: &str) -> Decision {
        let pair = (key.to_string(), sha.to_string());
        review_detail(self.splits.get(&pair).cloned(),
                      self.rejected.get(key).map(|(by, at, _)| (by.clone(), at.clone())),
                      self.rows.get(&pair).map(|r| (r.status.clone(), r.updated_by.clone(), r.updated_at.clone())))
    }
}

/// deploy.py `is_rejected`: any rejected revision, or an active split of this revision.
pub async fn is_rejected(db: &D1Database, key: &str, sha: &str) -> Result<bool> {
    #[derive(Deserialize)]
    struct One { #[allow(dead_code)] one: f64 }
    let hit: Option<One> = db::first(db, "SELECT 1 AS one FROM reviews WHERE icon = ? AND status = 'rejected' \
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
