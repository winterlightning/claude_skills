//! Reviews and feedback — deploy.py's review routes, `do_POST` tail, feedback edit/delete, reviewer stats.

use crate::args;
use crate::data::{self, admin_users};
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::refimg;
use pictographic_core::reviews::current_reviews;
use pictographic_core::stats::reviewer_stats;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use worker::{Response, Result};

/// D1 hands numbers back as floats; make integral ones integers again, like sqlite3 rows.
pub fn tidy(value: Value) -> Value {
    match value {
        Value::Number(n) if n.as_f64().is_some_and(|f| f.fract() == 0.0 && f.abs() < 9e15) && !n.is_i64() => json!(n.as_f64().unwrap() as i64),
        Value::Array(items) => Value::Array(items.into_iter().map(tidy).collect()),
        Value::Object(map) => Value::Object(map.into_iter().map(|(k, v)| (k, tidy(v))).collect()),
        other => other,
    }
}

/// deploy.py `feedback_row`: reference_images decoded from JSON text.
fn feedback_row(row: Map<String, Value>) -> Value {
    let mut row = row;
    let images = row.get("reference_images").and_then(Value::as_str).and_then(|t| serde_json::from_str::<Value>(t).ok())
        .unwrap_or_else(|| json!([]));
    row.insert("reference_images".into(), images);
    tidy(Value::Object(row))
}

pub async fn get_reviews(ctx: &Ctx) -> Result<Response> {
    let catalog = data::catalog(&ctx.db, true).await?;
    let (_, _, decisions) = data::decisions(&ctx.db, &catalog).await?;
    let reviews = current_reviews(&decisions);
    if ctx.query.get("include_approvers").map(|v| v == &vec!["1".to_string()]).unwrap_or(false) {
        #[derive(Deserialize)]
        struct Row { icon: String, author: String }
        let authors: Vec<Row> = db::all(&ctx.db, "SELECT DISTINCT icon, author FROM feedback WHERE author IS NOT NULL ORDER BY icon, author", vec![]).await?;
        let mut feedback_by: Map<String, Value> = Map::new();
        for row in authors {
            if catalog.contains(&row.icon) && !row.author.is_empty() {
                feedback_by.entry(row.icon).or_insert_with(|| json!([])).as_array_mut().unwrap().push(json!(row.author));
            }
        }
        return http::json(200, &json!({"statuses": reviews.statuses, "approved_by": reviews.approved_by,
            "rejected_by": reviews.rejected_by, "disapproved_by": reviews.disapproved_by, "feedback_by": feedback_by}));
    }
    http::json(200, &Value::Object(reviews.statuses))
}

pub async fn get_review_detail(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("");
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return http::error(404, "Unknown icon") };
    let decision = data::detail(&ctx.db, key, &icon.svg_sha256).await?;
    let row = data::review_row(&ctx.db, key, &icon.svg_sha256).await?;
    let now = chrono::Utc::now();
    let state = pictographic_core::work::work_state(row.as_ref(), now);
    let mut detail = decision.detail();
    detail["work"] = pictographic_core::work::work_field(row.as_ref(), state);
    http::json(200, &detail)
}

pub async fn get_feedback(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("");
    if data::icon(&ctx.db, key, true).await?.is_none() {
        return http::error(404, "Unknown icon");
    }
    let rows: Vec<Map<String, Value>> = db::all(&ctx.db, "SELECT id, feedback, svg_sha256, created_at, reference_images, author, \
        edited_by, edited_at, reason FROM feedback WHERE icon = ? ORDER BY id DESC LIMIT 100", args![key]).await?;
    http::json(200, &Value::Array(rows.into_iter().map(feedback_row).collect()))
}

pub async fn get_feedback_feed(ctx: &Ctx) -> Result<Response> {
    let rows: Vec<Map<String, Value>> = db::all(&ctx.db, "SELECT f.*, COALESCE(t.icon_type, '') AS icon_type FROM feedback f \
        LEFT JOIN icon_types t ON t.icon = f.icon ORDER BY f.id DESC", vec![]).await?;
    http::json(200, &Value::Array(rows.into_iter().map(feedback_row).collect()))
}

pub async fn get_reviewer_stats(ctx: &Ctx) -> Result<Response> {
    let catalog = data::catalog(&ctx.db, true).await?;
    let rows = data::review_rows(&ctx.db).await?;
    let splits = data::active_splits(&ctx.db).await?;
    let users: Vec<String> = admin_users(&ctx.env).into_iter().map(|(name, _)| name).collect();
    match reviewer_stats(&rows, &splits, &ctx.query, &users, &catalog, chrono::Utc::now()) {
        Ok(result) => http::json(200, &result),
        Err(message) => http::error(400, &message),
    }
}

/// `ReferenceStore.resolve`: validated metadata for up to four reference image ids.
pub async fn resolve_references(ctx: &Ctx, ids: &Value) -> std::result::Result<Vec<Value>, String> {
    if ids.is_null() {
        return Ok(vec![]);
    }
    let list = ids.as_array().filter(|l| l.len() <= refimg::MAX_IMAGES && l.iter().all(Value::is_string))
        .ok_or_else(|| format!("Attach up to {} reference images.", refimg::MAX_IMAGES))?;
    let mut seen = Vec::new();
    for id in list.iter().filter_map(Value::as_str) {
        if !seen.contains(&id.to_string()) {
            seen.push(id.to_string());
        }
    }
    let mut result = Vec::new();
    for id in seen {
        if !refimg::is_id(&id) {
            return Err("Unknown reference image.".into());
        }
        #[derive(Deserialize)]
        struct Row { id: String, name: String, mime: String }
        let row: Option<Row> = db::first(&ctx.db, "SELECT id, name, mime FROM reference_images WHERE id = ?", args![id.clone()])
            .await.map_err(|_| "Unknown reference image.".to_string())?;
        let row = row.ok_or("Unknown reference image.")?;
        let kind = if row.mime == "image/png" { "png" } else { "svg" };
        result.push(json!({"id": row.id, "kind": kind, "name": row.name}));
    }
    Ok(result)
}

const LABELS: [(&str, &str); 3] = [("bad-stroke", "Bad stroke drawn"), ("meaning", "Does not convey the intended meaning"),
                                   ("manual-fix-request", "Manual fix request")];
const REASONS: [&str; 4] = ["bad-stroke", "meaning", "manual-fix-request", "other"];

/// POST /api/reviews and /api/feedback — the tail of deploy.py `do_POST`.
pub async fn post_review(ctx: &Ctx, original_route: &str, data: &Value, user: &str) -> Result<Response> {
    let invalid = || http::error(400, "Invalid feedback or review status");
    let mut route = original_route.to_string();
    let key = data.get("icon").and_then(Value::as_str);
    let mut feedback = data.get("feedback").cloned().unwrap_or(Value::Null);
    let status_value = data.get("status").cloned().unwrap_or(json!(""));
    let reason_value = data.get("reason").cloned().unwrap_or(json!("other"));
    let (Some(status), Some(reason)) = (status_value.as_str(), reason_value.as_str()) else { return invalid() };
    let mut status = match status { "disapprove" => "pending", "re-generated" => "ready", other => other }.to_string();
    let reason = if reason == "bad-draw" { "bad-stroke" } else { reason }.to_string();
    let Some(key) = key else { return invalid() };
    if route == "/api/reviews" && status == "pending" && (data.get("reason").is_some() || data.get("feedback").is_some()) {
        let details_text = data.get("feedback").cloned().unwrap_or(json!(""));
        let Some(details_text) = details_text.as_str() else {
            return http::error(400, "Choose a disapproval reason; Other requires feedback.");
        };
        if !REASONS.contains(&reason.as_str()) || (reason == "other" && details_text.trim().is_empty()) {
            return http::error(400, "Choose a disapproval reason; Other requires feedback.");
        }
        let label = LABELS.iter().find(|(r, _)| *r == reason).map(|(_, l)| *l);
        let parts: Vec<&str> = [label, Some(details_text.trim())].into_iter().flatten().filter(|p| !p.is_empty()).collect();
        feedback = json!(parts.join("\n\n"));
        route = "/api/feedback".into();
    }
    let mut references = Vec::new();
    let feedback_id = data.get("feedback_id").cloned().unwrap_or(Value::Null);
    if route == "/api/feedback" {
        if !feedback_id.is_null() && (!feedback_id.is_i64() || !data.get("previous_feedback").is_some_and(Value::is_string)) {
            return invalid();
        }
        if !REASONS.contains(&reason.as_str()) {
            return http::error(400, "Choose a valid disapproval reason.");
        }
        let length = feedback.as_str().map(|f| f.trim().chars().count()).unwrap_or(0);
        if !(1..=10000).contains(&length) {
            return invalid();
        }
        references = match resolve_references(ctx, data.get("reference_images").unwrap_or(&Value::Null)).await {
            Ok(refs) => refs,
            Err(message) => return http::error(400, &message),
        };
        status = "pending".into();
    } else if !["ready", "pending", "re-generated", "approve", "rejected"].contains(&status.as_str()) {
        return invalid();
    }
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return http::error(404, "Unknown icon") };
    // A combined side / container icon cannot be approved while one of its parts (reference_parts) is not
    // approved on its current drawing.
    if status == "approve" && matches!(icon.family.as_deref(), Some("side_combination64" | "container_combination64")) {
        let reference = key.split_once('/').map_or("", |(_, id)| id);
        if let Some(waiting) = super::combinations::unapproved_parts(&ctx.db, reference).await? {
            return http::error(409, &format!("Approve {waiting} first: this combined icon uses parts that are not approved."));
        }
    }
    let sha = icon.svg_sha256.clone();
    if data.get("svg_sha256").and_then(Value::as_str).unwrap_or("") != sha {
        return http::error(409, "Icon changed; reload the gallery before submitting");
    }
    let db = &ctx.db;
    if original_route == "/api/reviews"
        && data::exists(db, "SELECT 1 FROM split_requests WHERE icon = ? AND svg_sha256 = ? AND active = 1", args![key, sha.clone()]).await? {
        return http::error(409, "This combined icon is rejected. Restore it before changing its review status.");
    }
    if data::is_rejected(db, key, &sha).await? {
        if original_route == "/api/feedback" {
            status = "rejected".into();
        } else if status != "rejected" {
            return http::error(409, "Restore this rejected icon before changing its review status.");
        }
    }
    let now = iso_utc(chrono::Utc::now());
    let held = data::exists(db, "SELECT 1 FROM reviews WHERE icon = ? AND svg_sha256 = ? AND status = 'claimed'", args![key, sha.clone()]).await?;
    let keep_claim = held && route == "/api/feedback";
    if keep_claim {
        status = "claimed".into(); // more feedback while a worker is on it does not take the icon away
    }
    let mut statements = Vec::new();
    let feedback_text = feedback.as_str().unwrap_or("").trim().to_string();
    let reference_ids: Vec<Value> = references.iter().map(|r| r["id"].clone()).collect();
    let references_json = pictographic_core::primitives::python_json(&Value::Array(references.clone()));
    if route == "/api/feedback" {
        if let Some(id) = feedback_id.as_i64() {
            let previous = data["previous_feedback"].as_str().unwrap_or("");
            statements.push(db::stmt(db, "UPDATE feedback SET feedback = ?, reason = ?, reference_images = ?, edited_by = ?, edited_at = ? \
                WHERE id = ? AND icon = ? AND svg_sha256 = ? AND feedback = ? AND author = ?",
                args![feedback_text.clone(), reason.clone(), references_json.clone(), user, now.clone(), id, key, sha.clone(), previous, user])?);
            statements.push(db::activity_if_changed(db, user, "feedback_edit", Some(key), details(vec![
                ("feedback_id", json!(id)), ("status", json!(status)), ("reason", json!(reason)), ("reference_images", json!(reference_ids))]))?);
        } else {
            statements.push(db::stmt(db, "INSERT INTO feedback(icon, feedback, svg_sha256, created_at, reference_images, author, reason) \
                VALUES (?, ?, ?, ?, ?, ?, ?)", args![key, feedback_text.clone(), sha.clone(), now.clone(), references_json.clone(), user, reason.clone()])?);
            statements.push(db::activity_with_placeholders(db, user, "feedback", Some(key), details(vec![
                ("feedback_id", json!("__ROWID__")), ("status", json!(status)), ("reason", json!(reason)),
                ("reference_images", json!(reference_ids))]))?);
        }
    } else {
        statements.push(db::activity(db, user, "review", Some(key), details(vec![("status", json!(status)), ("svg_sha256", json!(sha))]))?);
    }
    // Guarded so a failed feedback edit (no row changed) leaves the review alone.
    let guard = if route == "/api/feedback" && feedback_id.is_i64() {
        " WHERE EXISTS (SELECT 1 FROM feedback WHERE id = ? AND edited_at = ? AND edited_by = ?)"
    } else { " WHERE 1" };
    let upsert = format!("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) SELECT ?, ?, ?, ?, ?{guard} \
        ON CONFLICT(icon, svg_sha256) DO UPDATE SET \
        status = excluded.status, updated_at = excluded.updated_at, updated_by = excluded.updated_by, \
        worker = CASE WHEN ? THEN worker END, claimed_at = CASE WHEN ? THEN claimed_at END, \
        note = CASE WHEN ? THEN note ELSE '' END");
    let mut upsert_args = args![key, sha.clone(), status.clone(), now.clone(), user];
    if guard != " WHERE 1" {
        upsert_args.extend(args![feedback_id.as_i64().unwrap(), now.clone(), user]);
    }
    upsert_args.extend(args![keep_claim, keep_claim, keep_claim]);
    statements.push(db::stmt(db, &upsert, upsert_args)?);
    if status == "ready" {
        // clear_ready_feedback: resolve every saved request when the icon returns to Ready.
        statements.push(db::stmt(db, "DELETE FROM feedback WHERE icon = ?", args![key])?);
        statements.push(db::activity_with_placeholders(db, user, "feedback_resolved", Some(key),
            details(vec![("deleted_count", json!("__CHANGES__"))]))?);
    }
    let results = db::batch(db, statements).await?;
    let mut result = json!({"saved": true, "status": status, "updated_by": user});
    if route == "/api/feedback" {
        let id = match feedback_id.as_i64() {
            Some(id) => {
                if db::changes(&results[0]) == 0 {
                    return http::error(409, "Feedback changed. Reopen the icon before editing again.");
                }
                id
            }
            None => db::last_row_id(&results[0]).unwrap_or(0),
        };
        result["id"] = json!(id);
        result["feedback"] = json!(feedback_text);
    }
    http::json(201, &result)
}

pub async fn post_feedback_delete(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let id = data.get("id").and_then(Value::as_i64).filter(|id| *id > 0 && data["id"].is_i64());
    let previous = data.get("previous_feedback").and_then(Value::as_str);
    let edited_at = data.get("previous_edited_at").cloned().unwrap_or(Value::Null);
    let (Some(id), Some(previous)) = (id, previous) else { return http::error(400, "Choose a feedback entry to remove.") };
    if !(edited_at.is_null() || edited_at.is_string()) {
        return http::error(400, "Choose a feedback entry to remove.");
    }
    #[derive(Deserialize)]
    struct Row { icon: String, feedback: String, edited_at: Option<String> }
    let Some(row) = db::first::<Row>(&ctx.db, "SELECT icon, feedback, edited_at FROM feedback WHERE id = ?", args![id]).await? else {
        return http::error(404, "Feedback not found. Refresh the page.");
    };
    if row.feedback != previous || row.edited_at.as_deref() != edited_at.as_str() {
        return http::error(409, "Feedback changed. Refresh before removing it.");
    }
    let results = db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "DELETE FROM feedback WHERE id = ? AND feedback = ? AND edited_at IS ?", args![id, previous, edited_at.as_str()])?,
        db::activity_if_changed(&ctx.db, user, "feedback_delete", Some(&row.icon), details(vec![("feedback_id", json!(id))]))?,
    ]).await?;
    if db::changes(&results[0]) == 0 {
        return http::error(409, "Feedback changed. Refresh before removing it.");
    }
    http::json(200, &json!({"deleted": true, "id": id, "icon": row.icon}))
}

pub async fn post_feedback_edit(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let id = data.get("id").filter(|v| v.is_i64()).and_then(Value::as_i64);
    let feedback = data.get("feedback").and_then(Value::as_str).filter(|f| (1..=10000).contains(&f.trim().chars().count()));
    let previous = data.get("previous_feedback").and_then(Value::as_str);
    let (Some(id), Some(feedback), Some(previous)) = (id, feedback, previous) else {
        return http::error(400, "Enter feedback between 1 and 10,000 characters.");
    };
    #[derive(Deserialize)]
    struct Row { icon: String }
    let Some(row) = db::first::<Row>(&ctx.db, "SELECT icon FROM feedback WHERE id = ?", args![id]).await? else {
        return http::error(404, "Feedback not found.");
    };
    let now = iso_utc(chrono::Utc::now());
    let results = db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "UPDATE feedback SET feedback = ?, edited_by = ?, edited_at = ? WHERE id = ? AND feedback = ?",
                 args![feedback.trim(), user, now.clone(), id, previous])?,
        db::activity_if_changed(&ctx.db, user, "feedback_edit", Some(&row.icon),
            details(vec![("feedback_id", json!(id)), ("previous_feedback", json!(previous))]))?,
    ]).await?;
    if db::changes(&results[0]) == 0 {
        return http::error(409, "Feedback changed. Refresh before editing again.");
    }
    http::json(200, &json!({"saved": true, "feedback": feedback.trim(), "edited_by": user, "edited_at": now}))
}
