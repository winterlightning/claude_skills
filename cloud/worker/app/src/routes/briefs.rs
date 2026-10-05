//! Rejected combinations and their two component briefs — deploy.py `brief_action`, brief_queue.py.

use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use crate::routes::reviews::tidy;
use pictographic_core::briefs::validate_split;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use worker::{Response, Result};

/// GET /api/pending-briefs — brief_queue.py `list_briefs`.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    let rows: Vec<Map<String, Value>> = db::all(&ctx.db, "SELECT b.id, b.split_id, b.position, b.name, b.family, b.description, \
        b.status, b.generated_icon, s.icon, s.svg_sha256, s.combination_type, s.reason, s.reference_path, s.created_at, \
        s.created_by, b.completed_by, b.completed_at \
        FROM pending_briefs b JOIN split_requests s ON s.id = b.split_id WHERE s.active = 1 ORDER BY s.id DESC, b.position", vec![]).await?;
    http::json(200, &tidy(Value::Array(rows.into_iter().map(Value::Object).collect())))
}

pub async fn action(ctx: &Ctx, route: &str, data: &Value, user: &str) -> Result<Response> {
    let db = &ctx.db;
    if route == "/api/pending-briefs/complete" {
        let brief_id = data.get("brief_id").filter(|v| v.is_i64()).and_then(Value::as_i64);
        let key = data.get("generated_icon").and_then(Value::as_str);
        let (Some(brief_id), Some(key)) = (brief_id, key) else { return http::error(400, "Choose a generated component icon.") };
        #[derive(Deserialize)]
        struct Brief { family: String, icon: String }
        let brief: Option<Brief> = db::first(db, "SELECT b.family AS family, s.icon AS icon FROM pending_briefs b \
            JOIN split_requests s ON s.id = b.split_id WHERE b.id = ? AND s.active = 1", args![brief_id]).await?;
        let icon = data::icon(db, key, false).await?;
        let (Some(brief), Some(icon)) = (brief, icon) else {
            return http::error(400, "Choose a built standalone icon in this component family, not the rejected combination.");
        };
        if icon.family.as_deref() != Some(brief.family.as_str()) || key == brief.icon {
            return http::error(400, "Choose a built standalone icon in this component family, not the rejected combination.");
        }
        if data::is_rejected(db, key, &icon.svg_sha256).await? {
            return http::error(400, "A rejected icon cannot fulfill a component brief.");
        }
        db::batch(db, vec![
            db::stmt(db, "UPDATE pending_briefs SET status = 'generated', generated_icon = ?, completed_by = ?, completed_at = ? WHERE id = ?",
                     args![key, user, iso_utc(chrono::Utc::now()), brief_id])?,
            db::activity(db, user, "brief_complete", Some(&brief.icon), details(vec![("brief_id", json!(brief_id)), ("generated_icon", json!(key))]))?,
        ]).await?;
        return http::json(200, &json!({"saved": true}));
    }
    let key = data.get("icon").and_then(Value::as_str);
    let icon = match key { Some(key) => data::icon(db, key, route == "/api/reject-combination/restore").await?, None => None };
    let (Some(key), Some(icon)) = (key, icon) else { return http::error(404, "Unknown icon") };
    let sha = icon.svg_sha256.clone();
    if data.get("svg_sha256").and_then(Value::as_str) != Some(sha.as_str()) {
        return http::error(409, "Icon changed. Refresh before rejecting or restoring.");
    }
    let now = iso_utc(chrono::Utc::now());
    if route == "/api/reject-combination/restore" {
        let mut statements = vec![
            db::stmt(db, "UPDATE split_requests SET active = 0, restored_by = ?, restored_at = ? WHERE icon = ? AND svg_sha256 = ? AND active = 1",
                     args![user, now.clone(), key, sha.clone()])?,
            db::stmt(db, "UPDATE reviews SET status = 'ready', updated_by = ?, updated_at = ? WHERE icon = ? AND status = 'rejected'",
                     args![user, now.clone(), key])?,
            // Explicit restore returns the icon to review, never silently approves it.
            db::stmt(db, "INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, 'ready', ?, ?) \
                ON CONFLICT(icon, svg_sha256) DO UPDATE SET status = 'ready', updated_at = excluded.updated_at, updated_by = excluded.updated_by",
                args![key, sha.clone(), now.clone(), user])?,
            db::stmt(db, "DELETE FROM feedback WHERE icon = ?", args![key])?,
            db::activity_with_placeholders(db, user, "feedback_resolved", Some(key), details(vec![("deleted_count", json!("__CHANGES__"))]))?,
            db::activity(db, user, "restore", Some(key), details(vec![("svg_sha256", json!(sha))]))?,
        ];
        statements.extend(super::icon_list::recalc(db, key)?);
        db::batch(db, statements).await?;
        return http::json(200, &json!({"saved": true, "status": "ready"}));
    }
    let split = match validate_split(data) { Ok(split) => split, Err(message) => return http::error(400, &message) };
    let reference = icon.original_sources.as_array().and_then(|s| s.first())
        .and_then(|s| s.get("source_path")).and_then(Value::as_str).unwrap_or("").to_string();
    #[derive(Deserialize)]
    struct Existing { id: f64, active: f64 }
    let existing: Option<Existing> = db::first(db, "SELECT id, active FROM split_requests WHERE icon = ? AND svg_sha256 = ?",
                                               args![key, sha.clone()]).await?;
    if let Some(existing) = &existing {
        if existing.active != 0.0 {
            // Repeated clicks and retries cannot duplicate or reset work, and record nothing.
            return http::json(201, &json!({"saved": true, "status": "rejected", "split_id": existing.id as i64}));
        }
    }
    let mut statements = Vec::new();
    match &existing {
        Some(existing) => {
            statements.push(db::stmt(db, "UPDATE split_requests SET active = 1, combination_type = ?, reason = ?, reference_path = ?, \
                created_at = ?, created_by = ?, restored_by = NULL, restored_at = NULL WHERE id = ?",
                args![split.kind.clone(), split.reason.clone(), reference.clone(), now.clone(), user, existing.id as i64])?);
            statements.push(db::stmt(db, "DELETE FROM pending_briefs WHERE split_id = ?", args![existing.id as i64])?);
        }
        None => statements.push(db::stmt(db, "INSERT INTO split_requests(icon, svg_sha256, combination_type, reason, reference_path, created_at, created_by) \
            VALUES (?, ?, ?, ?, ?, ?, ?)", args![key, sha.clone(), split.kind.clone(), split.reason.clone(), reference.clone(), now.clone(), user])?),
    }
    for (index, part) in split.parts.iter().enumerate() {
        statements.push(db::stmt(db, "INSERT INTO pending_briefs(split_id, position, name, family, description) \
            VALUES ((SELECT id FROM split_requests WHERE icon = ? AND svg_sha256 = ?), ?, ?, ?, ?)",
            args![key, sha.clone(), (index + 1) as i64, part["name"].as_str(), part["family"].as_str(), part["description"].as_str()])?);
    }
    statements.extend(super::icon_list::recalc(db, key)?);
    db::batch(db, statements).await?;
    #[derive(Deserialize)]
    struct Id { id: f64 }
    let split_id = db::first::<Id>(db, "SELECT id FROM split_requests WHERE icon = ? AND svg_sha256 = ?", args![key, sha.clone()])
        .await?.map(|r| r.id as i64).unwrap_or(0);
    db::batch(db, vec![db::activity(db, user, "reject_combination", Some(key), details(vec![
        ("split_id", json!(split_id)), ("combination_type", json!(split.kind))]))?]).await?;
    http::json(201, &json!({"saved": true, "status": "rejected", "split_id": split_id}))
}
