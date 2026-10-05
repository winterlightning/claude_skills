//! Fix-queue claims — deploy.py `work_read`, `work_action`, `work_one`, `work_claim_many`.
//! A claim is one conditional UPDATE, so two machines can never both win.

use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use crate::routes::reviews::tidy;
use pictographic_core::catalog::Icon;
use pictographic_core::reviews::{public_status, Decision, ReviewRow};
use pictographic_core::time::iso_utc;
use pictographic_core::work::{self as rules, WorkData, WorkError};
use serde::Deserialize;
use serde_json::{json, Value};
use worker::{Response, Result};

fn refuse(error: WorkError) -> Result<Response> {
    http::json(error.status, &error.payload())
}

/// `release_expired`: claims older than the lease go back to Disapproved, each logged.
async fn release_expired(ctx: &Ctx, now: chrono::DateTime<chrono::Utc>) -> Result<usize> {
    let stale = rules::stale_before(now);
    let rows: Vec<ReviewRow> = db::all(&ctx.db, "SELECT icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note \
        FROM reviews WHERE status = 'claimed' AND claimed_at <= ?", args![stale]).await?;
    let mut statements = Vec::new();
    for row in &rows {
        statements.push(db::stmt(&ctx.db, "UPDATE reviews SET status = 'pending', worker = NULL, claimed_at = NULL, note = '' \
            WHERE icon = ? AND svg_sha256 = ? AND status = 'claimed' AND claimed_at = ?",
            args![row.icon.clone(), row.svg_sha256.clone(), row.claimed_at.clone()])?);
        statements.push(db::activity_if_changed(&ctx.db, "system", "work_expired", Some(&row.icon), details(vec![
            ("svg_sha256", json!(row.svg_sha256)), ("worker", json!(row.worker)), ("claimed_at", json!(row.claimed_at))]))?);
        statements.extend(super::icon_list::recalc(&ctx.db, &row.icon)?);
    }
    db::batch(&ctx.db, statements).await?;
    Ok(rows.len())
}

/// GET /api/work, /api/work/queue, /disapproved, /review, /history, /result.
pub async fn read(ctx: &Ctx) -> Result<Response> {
    let now = chrono::Utc::now();
    release_expired(ctx, now).await?;
    if ctx.path == "/api/work/fixes" {
        // Every uploaded after result; the gallery shows it while that revision is current. Needs no catalog.
        #[derive(Deserialize, serde::Serialize)]
        struct Fix { icon: String, svg_sha256: String, worker: Option<String>, saved_at: Option<String> }
        let fixes: Vec<Fix> = db::all(&ctx.db, "SELECT icon, svg_sha256, worker, saved_at FROM work_results \
            WHERE stage = 'after' ORDER BY icon, svg_sha256", vec![]).await?;
        return http::json(200, &json!({"fixes": fixes}));
    }
    let catalog = data::catalog(&ctx.db, true).await?;
    let (rows, _, decisions) = data::decisions(&ctx.db, &catalog).await?;
    let path = ctx.path.as_str();
    let row_map = data::row_map(&rows);
    if matches!(path, "/api/work/queue" | "/api/work/disapproved" | "/api/work/review") {
        let feedback = data::latest_feedback(&ctx.db).await?;
        let types = data::icon_types(&ctx.db).await?;
        let (events, notes, fixes) = count_inputs(ctx).await?;
        let empty = Default::default();
        let base = WorkData { catalog: &catalog, decisions: &decisions, rows: &row_map, feedback: &feedback, types: &types,
                              disapprovals: &empty, now };
        let counts = rules::disapproval_counts(&base, &rules::CountInputs { events: &events, feedback: &notes, fixes: &fixes });
        let work = WorkData { disapprovals: &counts, ..base };
        let result = if path == "/api/work/review" {
            let summaries = rules::result_summaries(&result_rows(ctx, None).await?);
            rules::review_listing(&work, &ctx.query, &summaries)
        } else {
            rules::queue(&work, &ctx.query, path.ends_with("/queue"))
        };
        return match result { Ok(value) => http::json(200, &value), Err(error) => refuse(error) };
    }
    let key = ctx.param("icon").unwrap_or("").to_string();
    if path == "/api/work/history" || path == "/api/work/result" {
        let Some(icon) = catalog.get(&key) else { return http::error(404, "Unknown icon") };
        if path == "/api/work/history" {
            return history(ctx, icon, &decisions, &rows, now).await;
        }
        let stage = ctx.param("stage").unwrap_or("");
        let part = ctx.param("part").unwrap_or("svg");
        #[derive(Deserialize)]
        struct Row { svg: String, python_source: Option<String>, validation: Option<String> }
        let row: Option<Row> = db::first(&ctx.db, "SELECT svg, python_source, validation FROM work_results \
            WHERE icon = ? AND svg_sha256 = ? AND stage = ?", args![key.clone(), ctx.param("svg_sha256").unwrap_or(""), stage]).await?;
        let Some(row) = row.filter(|_| matches!(part, "svg" | "python" | "validation")) else {
            return http::error(404, "No uploaded result for this revision and stage.");
        };
        let text = match part { "svg" => Some(row.svg), "python" => row.python_source, _ => row.validation };
        let Some(text) = text else { return http::error(404, &format!("The {stage} result has no {part} part.")) };
        return if part == "svg" { http::svg(&text) } else { http::text(200, &text, "text/plain; charset=utf-8") };
    }
    if path != "/api/work" {
        return http::error(404, "Unknown work route.");
    }
    if !key.is_empty() {
        let Some(icon) = catalog.get(&key) else { return http::error(404, "Unknown icon") };
        let detail = data::detail(&ctx.db, &key, &icon.svg_sha256).await?;
        let row = row_map.get(&(key.clone(), icon.svg_sha256.clone()));
        let state = rules::work_state(row, now);
        return http::json(200, &json!({"icon": key, "svg_sha256": icon.svg_sha256, "status": public_status(&detail.status),
                                       "work": rules::work_field(row, state)}));
    }
    let feedback = Default::default();
    let types = Default::default();
    let disapprovals = Default::default();
    let work = WorkData { catalog: &catalog, decisions: &decisions, rows: &row_map, feedback: &feedback, types: &types,
                          disapprovals: &disapprovals, now };
    http::json(200, &rules::listing(&work))
}

/// The rows `rules::disapproval_counts` reads: activity in id order, feedback shas, uploaded fixes.
async fn count_inputs(ctx: &Ctx) -> Result<(Vec<rules::CountEvent>, Vec<(String, String)>, Vec<(String, String)>)> {
    #[derive(Deserialize)]
    struct Event { icon: String, action: String, status: Option<String>, svg_sha256: Option<String>, created_at: String }
    #[derive(Deserialize)]
    struct Pair { icon: String, svg_sha256: String }
    let events: Vec<Event> = db::all(&ctx.db, "SELECT icon, action, \
        CASE WHEN json_valid(details) THEN json_extract(details, '$.status') END AS status, \
        CASE WHEN json_valid(details) THEN json_extract(details, '$.svg_sha256') END AS svg_sha256, created_at FROM activity_log \
        WHERE icon IS NOT NULL AND action IN ('work_done', 'upload', 'review', 'feedback') ORDER BY id", vec![]).await?;
    let notes: Vec<Pair> = db::all(&ctx.db, "SELECT DISTINCT icon, svg_sha256 FROM feedback", vec![]).await?;
    let fixes: Vec<Pair> = db::all(&ctx.db, "SELECT DISTINCT icon, svg_sha256 FROM work_results WHERE stage = 'after'", vec![]).await?;
    Ok((events.into_iter().map(|e| rules::CountEvent { icon: e.icon, action: e.action, status: e.status,
                                                       svg_sha256: e.svg_sha256, at: e.created_at }).collect(),
        notes.into_iter().map(|p| (p.icon, p.svg_sha256)).collect(),
        fixes.into_iter().map(|p| (p.icon, p.svg_sha256)).collect()))
}

#[derive(Deserialize)]
struct ResultRow {
    icon: String,
    svg_sha256: String,
    stage: String,
    worker: String,
    python_path: Option<String>,
    note: Option<String>,
    saved_at: String,
    has_python: f64,
    has_validation: f64,
}

async fn result_rows(ctx: &Ctx, key: Option<&str>) -> Result<Vec<rules::ResultRow>> {
    let base = "SELECT icon, svg_sha256, stage, worker, python_path, note, saved_at, python_source IS NOT NULL AS has_python, \
                validation IS NOT NULL AS has_validation FROM work_results";
    let rows: Vec<ResultRow> = match key {
        Some(key) => db::all(&ctx.db, &format!("{base} WHERE icon = ?"), args![key]).await?,
        None => db::all(&ctx.db, base, vec![]).await?,
    };
    Ok(rows.into_iter().map(|r| rules::ResultRow {
        icon: r.icon, svg_sha256: r.svg_sha256, stage: r.stage, worker: r.worker, python_path: r.python_path,
        note: r.note.unwrap_or_default(), saved_at: r.saved_at, has_python: r.has_python != 0.0, has_validation: r.has_validation != 0.0,
    }).collect())
}

async fn history(ctx: &Ctx, icon: &Icon, decisions: &[(String, Decision)], rows: &[ReviewRow],
                 now: chrono::DateTime<chrono::Utc>) -> Result<Response> {
    #[derive(Deserialize)]
    struct Feedback { id: f64, svg_sha256: String, reason: Option<String>, feedback: String, author: Option<String>,
                      created_at: String, edited_by: Option<String>, edited_at: Option<String> }
    #[derive(Deserialize)]
    struct Event { username: String, action: String, details: Option<String>, created_at: String }
    let feedback: Vec<Feedback> = db::all(&ctx.db, "SELECT id, svg_sha256, reason, feedback, author, created_at, edited_by, edited_at \
        FROM feedback WHERE icon = ? ORDER BY id", args![icon.key.clone()]).await?;
    let events: Vec<Event> = db::all(&ctx.db, "SELECT username, action, details, created_at FROM activity_log WHERE icon = ? ORDER BY id",
                                     args![icon.key.clone()]).await?;
    let summaries = rules::result_summaries(&result_rows(ctx, Some(&icon.key)).await?);
    let decision = decisions.iter().find(|(k, _)| *k == icon.key).map(|(_, d)| d);
    let feedback: Vec<rules::HistoryFeedback> = feedback.into_iter().map(|f| rules::HistoryFeedback {
        id: f.id as i64, svg_sha256: f.svg_sha256, reason: f.reason, feedback: f.feedback, author: f.author,
        created_at: f.created_at, edited_by: f.edited_by, edited_at: f.edited_at }).collect();
    let events: Vec<rules::HistoryEvent> = events.into_iter().map(|e| rules::HistoryEvent {
        username: e.username, action: e.action, details: e.details.unwrap_or_default(), created_at: e.created_at }).collect();
    http::json(200, &tidy(rules::history(icon, decision, rows, &feedback, &summaries, &events, now)))
}

/// POST /api/work/claim|done|cannot-fix|abandon|result.
pub async fn action(ctx: &Ctx, route: &str, data: &Value, user: &str) -> Result<Response> {
    let action = route.rsplit('/').next().unwrap_or("");
    if action == "claim" && data.get("icons").is_some() {
        return claim_many(ctx, data, user).await;
    }
    let (status, payload) = work_one(ctx, action, data.get("icon"), data.get("svg_sha256"), data, user, true).await?;
    http::json(status, &payload)
}

async fn claim_many(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let icons = data.get("icons").and_then(Value::as_array).filter(|l| !l.is_empty() && l.len() as i64 <= rules::MAX_QUEUE);
    let Some(icons) = icons else {
        return http::error(400, &format!("icons must be a list of 1-{} icon keys or {{icon, svg_sha256}} objects.", rules::MAX_QUEUE));
    };
    let worker = match rules::validate_worker(data.get("worker").unwrap_or(&Value::Null)) {
        Ok(worker) => worker,
        Err(error) => return refuse(error),
    };
    let (mut claimed, mut refused, mut seen) = (Vec::new(), Vec::new(), Vec::<String>::new());
    let mut body = data.clone();
    body["worker"] = json!(worker);
    for entry in icons {
        let (key, sha) = match entry {
            Value::String(key) => (Some(key.clone()), None),
            Value::Object(map) => (map.get("icon").and_then(Value::as_str).map(str::to_string), map.get("svg_sha256").cloned()),
            _ => (None, None),
        };
        let Some(key) = key.filter(|k| !k.is_empty()) else {
            refused.push(json!({"icon": entry.as_str(), "status": 400, "error": "Each entry needs an icon key."}));
            continue;
        };
        if seen.contains(&key) {
            continue;
        }
        seen.push(key.clone());
        let require = sha.is_some();
        let (status, payload) = work_one(ctx, "claim", Some(&json!(key)), sha.as_ref(), &body, user, require).await?;
        if status == 201 {
            claimed.push(payload["item"].clone());
        } else {
            let mut item = payload.clone();
            item["icon"] = json!(key);
            item["status"] = json!(status);
            refused.push(item);
        }
    }
    http::json(200, &json!({"saved": !claimed.is_empty(), "worker": worker, "claimed": claimed, "refused": refused}))
}

/// One work transition; returns (HTTP status, JSON payload).
async fn work_one(ctx: &Ctx, action: &str, key: Option<&Value>, sha_given: Option<&Value>, data: &Value, user: &str,
                  require_sha: bool) -> Result<(u16, Value)> {
    let Some(key) = key.and_then(Value::as_str).filter(|k| !k.is_empty()) else { return Ok((400, json!({"error": "Choose an icon."}))) };
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return Ok((404, json!({"error": "Unknown icon"}))) };
    let sha = icon.svg_sha256.clone();
    let given = sha_given.filter(|v| !v.is_null());
    if (require_sha || given.is_some()) && given.and_then(Value::as_str).unwrap_or("") != sha {
        return Ok((409, json!({"error": "Icon changed on production; refresh the queue and use its svg_sha256. \
            If your build is ahead of production, wait for the production pull.", "svg_sha256": sha})));
    }
    if data::is_rejected(&ctx.db, key, &sha).await? {
        return Ok((409, json!({"error": "Restore this rejected icon before working on it."})));
    }
    let now = chrono::Utc::now();
    release_expired(ctx, now).await?;
    let decision = data::detail(&ctx.db, key, &sha).await?;
    let row = data::review_row(&ctx.db, key, &sha).await?;
    let outcome = match action {
        "claim" => claim(ctx, &icon, &decision, row.as_ref(), data, user, now).await?,
        "done" | "cannot-fix" => finish(ctx, key, &sha, action, row.as_ref(), data, user, now).await?,
        "result" => save_result(ctx, &icon, row.as_ref(), data, user, now).await?,
        _ => abandon(ctx, key, &sha, row.as_ref(), data, user, now).await?,
    };
    match outcome {
        Ok(mut result) => {
            result["saved"] = json!(true);
            result["icon"] = json!(key);
            result["svg_sha256"] = json!(sha);
            Ok((if action == "claim" { 201 } else { 200 }, result))
        }
        Err(error) => Ok((error.status, error.payload())),
    }
}

type Outcome = std::result::Result<Value, WorkError>;

async fn claim(ctx: &Ctx, icon: &Icon, decision: &Decision, row: Option<&ReviewRow>, data: &Value, user: &str,
               now: chrono::DateTime<chrono::Utc>) -> Result<Outcome> {
    let worker = match rules::validate_worker(data.get("worker").unwrap_or(&Value::Null)) { Ok(w) => w, Err(e) => return Ok(Err(e)) };
    if let Err(error) = rules::check_claim(&decision.status, row, now, &worker) {
        return Ok(Err(error));
    }
    let (key, sha) = (icon.key.as_str(), icon.svg_sha256.as_str());
    let stamp = iso_utc(now);
    let stale = rules::stale_before(now);
    let expires = iso_utc(now + chrono::Duration::hours(rules::LEASE_HOURS));
    let mut statements = vec![db::stmt(&ctx.db, "UPDATE reviews SET status = 'claimed', worker = ?, claimed_at = ?, note = '' \
        WHERE icon = ? AND svg_sha256 = ? AND ((status = 'pending' AND worker IS NULL) OR (status = 'claimed' AND claimed_at <= ?))",
        args![worker.clone(), stamp.clone(), key, sha, stale])?];
    if let Some(previous) = row.filter(|r| r.status == "claimed") {
        statements.push(db::activity_if_changed(&ctx.db, user, "work_expired", Some(key), details(vec![
            ("svg_sha256", json!(sha)), ("worker", json!(previous.worker)), ("claimed_at", json!(previous.claimed_at)),
            ("taken_by", json!(worker))]))?);
    }
    statements.push(db::stmt(&ctx.db, "INSERT INTO activity_log(username, action, icon, details, created_at) \
        SELECT ?, 'work_claim', ?, ?, ? WHERE EXISTS (SELECT 1 FROM reviews WHERE icon = ? AND svg_sha256 = ? AND status = 'claimed' \
        AND worker = ? AND claimed_at = ?)",
        args![user, key, pictographic_core::primitives::python_json(&json!({"svg_sha256": sha, "worker": worker, "expires_at": expires})),
              stamp.clone(), key, sha, worker.clone(), stamp.clone()])?);
    statements.extend(super::icon_list::recalc(&ctx.db, key)?);
    let results = db::batch(&ctx.db, statements).await?;
    let fresh = data::review_row(&ctx.db, key, sha).await?;
    if db::changes(&results[0]) == 0 {
        let state = rules::work_state(fresh.as_ref(), now);
        return Ok(Err(WorkError::with_work("Another worker claimed this icon just now.", 409, rules::work_field(fresh.as_ref(), state))));
    }
    let feedback = data::feedback_for(&ctx.db, key, sha).await?;
    let icon_type = data::icon_type(&ctx.db, key).await?;
    let item = rules::queue_item(icon, icon_type.as_deref(), decision, feedback.as_ref(), fresh.as_ref(), Some("working"));
    Ok(Ok(json!({"work": rules::work_field(fresh.as_ref(), Some("working")), "item": item})))
}

#[allow(clippy::too_many_arguments)]
async fn finish(ctx: &Ctx, key: &str, sha: &str, outcome: &str, row: Option<&ReviewRow>, data: &Value, user: &str,
                now: chrono::DateTime<chrono::Utc>) -> Result<Outcome> {
    let worker = match rules::validate_worker(data.get("worker").unwrap_or(&Value::Null)) { Ok(w) => w, Err(e) => return Ok(Err(e)) };
    let note = match rules::validate_note(data.get("note").unwrap_or(&Value::Null), outcome == "cannot-fix") { Ok(n) => n, Err(e) => return Ok(Err(e)) };
    if let Err(error) = rules::check_own_claim(row, now, &worker, "finish") {
        return Ok(Err(error));
    }
    let stamp = iso_utc(now);
    let claimed_at = row.and_then(|r| r.claimed_at.clone());
    // Only while the same claim is still held: guards against a concurrent release.
    let held = "icon = ? AND svg_sha256 = ? AND status = 'claimed' AND worker = ? AND claimed_at = ?";
    let mut statements = if outcome == "done" {
        vec![
            db::stmt(&ctx.db, &format!("UPDATE reviews SET status = 'ready', note = ?, updated_at = ?, updated_by = ? WHERE {held}"),
                     args![note.clone(), stamp, worker.clone(), key, sha, worker.clone(), claimed_at.clone()])?,
            db::activity_if_changed(&ctx.db, user, "work_done", Some(key), details(vec![
                ("svg_sha256", json!(sha)), ("worker", json!(worker)), ("note", json!(note))]))?,
            db::activity(&ctx.db, &worker, "review", Some(key), details(vec![("status", json!("ready")), ("svg_sha256", json!(sha)),
                ("source", json!("work_done")), ("feedback_kept", json!(true))]))?,
        ]
    } else {
        vec![
            db::stmt(&ctx.db, &format!("UPDATE reviews SET status = 'pending', note = ? WHERE {held}"),
                     args![note.clone(), key, sha, worker.clone(), claimed_at.clone()])?,
            db::activity_if_changed(&ctx.db, user, "work_cannot_fix", Some(key), details(vec![
                ("svg_sha256", json!(sha)), ("worker", json!(worker)), ("note", json!(note))]))?,
        ]
    };
    statements.extend(super::icon_list::recalc(&ctx.db, key)?);
    let results = db::batch(&ctx.db, statements).await?;
    let fresh = data::review_row(&ctx.db, key, sha).await?;
    if db::changes(&results[0]) == 0 {
        let state = rules::work_state(fresh.as_ref(), now);
        return Ok(Err(WorkError::with_work("The claim changed while finishing; refresh and retry.", 409, rules::work_field(fresh.as_ref(), state))));
    }
    if outcome == "done" {
        Ok(Ok(json!({"work": rules::work_field(fresh.as_ref(), Some("done")), "status": "ready"})))
    } else {
        Ok(Ok(json!({"work": rules::work_field(fresh.as_ref(), Some("cannot-fix"))})))
    }
}

async fn abandon(ctx: &Ctx, key: &str, sha: &str, row: Option<&ReviewRow>, data: &Value, user: &str,
                 now: chrono::DateTime<chrono::Utc>) -> Result<Outcome> {
    let worker = match rules::validate_worker(data.get("worker").unwrap_or(&Value::Null)) { Ok(w) => w, Err(e) => return Ok(Err(e)) };
    let state = match rules::check_abandon(row, now) { Ok(s) => s, Err(e) => return Ok(Err(e)) };
    let holder = row.and_then(|r| r.worker.clone());
    let mut statements = vec![
        db::stmt(&ctx.db, "UPDATE reviews SET status = 'pending', worker = NULL, claimed_at = NULL, note = '' WHERE icon = ? AND svg_sha256 = ?",
                 args![key, sha])?,
        db::activity(&ctx.db, user, "work_abandon", Some(key), details(vec![("svg_sha256", json!(sha)), ("worker", json!(holder)),
            ("released_by", json!(worker)), ("previous_state", json!(state))]))?,
    ];
    statements.extend(super::icon_list::recalc(&ctx.db, key)?);
    db::batch(&ctx.db, statements).await?;
    Ok(Ok(json!({"work": rules::work_field(None, None)})))
}

async fn save_result(ctx: &Ctx, icon: &Icon, row: Option<&ReviewRow>, data: &Value, user: &str,
                     now: chrono::DateTime<chrono::Utc>) -> Result<Outcome> {
    let canvas = icon.canvas_size.unwrap_or(48);
    let svg_input = data.get("svg").and_then(Value::as_str).unwrap_or("");
    let svg = match pictographic_core::svg::safe_svg(svg_input, canvas) {
        Ok(svg) => svg,
        Err(error) => return Ok(Err(WorkError::new(format!("Result SVG refused: {error}"), 400))),
    };
    let stage = data.get("stage").and_then(Value::as_str).unwrap_or("");
    if stage != "before" && stage != "after" {
        return Ok(Err(WorkError::new("stage must be before or after.", 400)));
    }
    let worker = match rules::validate_worker(data.get("worker").unwrap_or(&Value::Null)) { Ok(w) => w, Err(e) => return Ok(Err(e)) };
    let checked = (|| -> std::result::Result<_, WorkError> {
        let svg = rules::validate_text(&json!(svg), "svg", true)?;
        let python_source = rules::validate_text(data.get("python_source").unwrap_or(&Value::Null), "python_source", false)?;
        let validation = rules::validate_text(data.get("validation").unwrap_or(&Value::Null), "validation", false)?;
        let python_path = match data.get("python_path") {
            None | Some(Value::Null) => None,
            Some(Value::String(p)) if p.chars().count() <= 512 => Some(p.clone()),
            _ => return Err(WorkError::new("python_path must be a short path string.", 400)),
        };
        let note = rules::validate_note(data.get("note").unwrap_or(&Value::Null), false)?;
        Ok((svg.unwrap_or_default(), python_source, validation, python_path, note))
    })();
    let (svg, python_source, validation, python_path, note) = match checked { Ok(v) => v, Err(e) => return Ok(Err(e)) };
    if let Err(error) = rules::check_result(stage, row, now, &worker) {
        return Ok(Err(error));
    }
    let stamp = iso_utc(now);
    let (key, sha) = (icon.key.as_str(), icon.svg_sha256.as_str());
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "INSERT INTO work_results(icon, svg_sha256, stage, worker, svg, python_path, python_source, validation, note, saved_at) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(icon, svg_sha256, stage) DO UPDATE SET worker = excluded.worker, svg = excluded.svg, \
            python_path = excluded.python_path, python_source = excluded.python_source, validation = excluded.validation, \
            note = excluded.note, saved_at = excluded.saved_at",
            args![key, sha, stage, worker.clone(), svg, python_path.clone(), python_source.clone(), validation.clone(), note.clone(), stamp.clone()])?,
        db::activity(&ctx.db, user, "work_result", Some(key), details(vec![("svg_sha256", json!(sha)), ("stage", json!(stage)),
            ("worker", json!(worker)), ("python_path", json!(python_path)), ("has_python", json!(python_source.is_some())),
            ("has_validation", json!(validation.is_some())), ("note", json!(note))]))?,
    ]).await?;
    let fresh = data::review_row(&ctx.db, key, sha).await?;
    let state = rules::work_state(fresh.as_ref(), now);
    Ok(Ok(json!({
        "result": {"stage": stage, "worker": worker, "saved_at": stamp, "python_path": python_path, "note": note,
                   "has_python": python_source.is_some(), "has_validation": validation.is_some()},
        "work": rules::work_field(fresh.as_ref(), state)})))
}
