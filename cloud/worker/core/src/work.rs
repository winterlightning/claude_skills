//! Who is fixing which disapproved icon — ported from icon_set/scripts/work_claims.py.
//!
//! Claims live on the `reviews` row (`status='claimed'`, `worker`, `claimed_at`, `note`).
//! The API's `work.state` is derived from that row and the clock:
//! working (claimed < LEASE_HOURS ago), done (ready with a worker), cannot-fix (pending with a worker).
//! These functions are pure: callers load rows from D1, and write with conditional SQL.

use crate::catalog::{Catalog, Icon};
use crate::query::{first, Query};
use crate::reviews::{public_status, Decision, ReviewRow};
use crate::time::{iso, parse_time};
use chrono::{DateTime, Duration, FixedOffset, Utc};
use serde_json::{json, Map, Value};
use std::collections::{BTreeMap, HashMap};

pub const LEASE_HOURS: i64 = 6;
pub const MAX_WORKER: usize = 120;
pub const MAX_NOTE: usize = 4000;
pub const MAX_QUEUE: i64 = 500;
pub const MAX_RESULT_TEXT: usize = 512 * 1024;
const STATES: [&str; 3] = ["working", "done", "cannot-fix"];

/// A refused transition: HTTP status, message and the revision's current `work` field.
#[derive(Debug, Clone, PartialEq)]
pub struct WorkError {
    pub status: u16,
    pub message: String,
    pub work: Option<Value>,
}

impl WorkError {
    pub fn new(message: impl Into<String>, status: u16) -> Self {
        WorkError { status, message: message.into(), work: None }
    }

    pub fn with_work(message: impl Into<String>, status: u16, work: Value) -> Self {
        WorkError { status, message: message.into(), work: Some(work) }
    }

    pub fn payload(&self) -> Value {
        let mut map = Map::new();
        map.insert("error".into(), json!(self.message));
        if let Some(work) = &self.work {
            map.insert("work".into(), work.clone());
        }
        Value::Object(map)
    }
}

pub fn validate_worker(worker: &Value) -> Result<String, WorkError> {
    let bad = || WorkError::new(format!("worker must be a name of 1-{MAX_WORKER} characters, e.g. \"hostname/agent\"."), 400);
    let text = worker.as_str().ok_or_else(bad)?.trim().to_string();
    let count = text.chars().count();
    if count == 0 || count > MAX_WORKER || text.chars().any(|c| (c as u32) < 0x20 || c as u32 == 0x7f) {
        return Err(bad());
    }
    Ok(text)
}

pub fn validate_note(note: &Value, required: bool) -> Result<String, WorkError> {
    let text = match note {
        Value::Null => String::new(),
        Value::String(text) if text.chars().count() <= MAX_NOTE => text.clone(),
        _ => return Err(WorkError::new(format!("note must be a string of at most {MAX_NOTE} characters."), 400)),
    };
    if required && text.trim().is_empty() {
        return Err(WorkError::new("A note explaining why the icon cannot be fixed is required.", 400));
    }
    Ok(text.trim().to_string())
}

/// `validate_text`: None for missing/empty; at most MAX_RESULT_TEXT bytes.
pub fn validate_text(value: &Value, name: &str, required: bool) -> Result<Option<String>, WorkError> {
    match value {
        Value::Null => {}
        Value::String(text) if text.is_empty() => {}
        Value::String(text) if text.len() <= MAX_RESULT_TEXT => return Ok(Some(text.clone())),
        _ => return Err(WorkError::new(format!("{name} must be text of at most {} KB.", MAX_RESULT_TEXT / 1024), 400)),
    }
    if required {
        return Err(WorkError::new(format!("{name} is required."), 400));
    }
    Ok(None)
}

fn lease() -> Duration {
    Duration::hours(LEASE_HOURS)
}

/// The stamp before which a claim has expired.
pub fn stale_before(now: DateTime<Utc>) -> String {
    crate::time::iso_utc(now - lease())
}

pub fn expires_at(row: Option<&ReviewRow>) -> Option<String> {
    let claimed = row?.claimed_at.as_deref().and_then(parse_time)?;
    Some(iso(&(claimed + lease())))
}

pub fn work_state(row: Option<&ReviewRow>, now: DateTime<Utc>) -> Option<&'static str> {
    let row = row?;
    row.worker.as_ref().filter(|w| !w.is_empty())?;
    match row.status.as_str() {
        "claimed" => {
            let claimed: Option<DateTime<FixedOffset>> = row.claimed_at.as_deref().and_then(parse_time);
            match claimed {
                Some(claimed) if now < claimed + lease() => Some("working"),
                _ => None,
            }
        }
        "ready" => Some("done"),
        "pending" => Some("cannot-fix"),
        _ => None,
    }
}

pub fn work_field(row: Option<&ReviewRow>, state: Option<&str>) -> Value {
    let mut field = Map::new();
    field.insert("state".into(), json!(state));
    if let (Some(row), Some(_)) = (row, state) {
        if row.worker.as_deref().is_some_and(|w| !w.is_empty()) {
            field.insert("worker".into(), json!(row.worker));
            field.insert("note".into(), json!(row.note.clone().unwrap_or_default()));
            field.insert("claimed_at".into(), json!(row.claimed_at));
            field.insert("updated_at".into(), json!(row.updated_at));
            field.insert("svg_sha256".into(), json!(row.svg_sha256));
            if row.status == "claimed" {
                field.insert("expires_at".into(), json!(expires_at(Some(row))));
            }
        }
    }
    Value::Object(field)
}

/// Newest feedback per (icon, sha): reason, feedback, feedback_by, feedback_at.
#[derive(Clone, Debug, Default)]
pub struct FeedbackSummary {
    pub reason: Option<String>,
    pub feedback: Option<String>,
    pub feedback_by: Option<String>,
    pub feedback_at: Option<String>,
}

pub type RowMap = HashMap<(String, String), ReviewRow>;
pub type FeedbackMap = HashMap<(String, String), FeedbackSummary>;

pub fn queue_item(icon: &Icon, icon_type: Option<&str>, decision: &Decision, feedback: Option<&FeedbackSummary>,
                  row: Option<&ReviewRow>, state: Option<&str>) -> Value {
    json!({
        "key": icon.key, "icon_id": icon.icon_id, "name": icon.name,
        "family": icon.family, "category": icon.category,
        "svg_sha256": icon.svg_sha256, "python_source": icon.python_source,
        "preview_url": icon.preview_url,
        "original_sources": if icon.original_sources.is_null() { json!([]) } else { icon.original_sources.clone() },
        "status": public_status(&decision.status),
        "disapproved_by": decision.actor, "disapproved_at": decision.stamp,
        "reason": feedback.and_then(|f| f.reason.clone()), "feedback": feedback.and_then(|f| f.feedback.clone()),
        "feedback_by": feedback.and_then(|f| f.feedback_by.clone()),
        "icon_type": icon_type, "work": work_field(row, state),
    })
}

pub struct Paging<'a> {
    pub query: &'a Query,
    pub limit: i64,
    pub offset: i64,
}

impl<'a> Paging<'a> {
    pub fn one(&self, name: &str) -> Option<&'a str> {
        first(self.query, name)
    }
}

pub fn paging(query: &Query, default_limit: i64) -> Result<Paging<'_>, WorkError> {
    let parse = |name: &str, default: i64| match first(query, name) {
        None => Ok(default),
        Some(text) => text.trim().parse::<i64>().map_err(|_| WorkError::new("limit and offset must be integers.", 400)),
    };
    let limit = parse("limit", default_limit)?;
    let offset = parse("offset", 0)?;
    if !(1..=MAX_QUEUE).contains(&limit) || offset < 0 {
        return Err(WorkError::new(format!("limit must be 1-{MAX_QUEUE} and offset nonnegative."), 400));
    }
    Ok(Paging { query, limit, offset })
}

pub struct Filters<'a> {
    pub family: Option<&'a str>,
    pub category: Option<&'a str>,
    pub icon_type: Option<&'a str>,
    pub reason: Option<&'a str>,
}

/// Everything the queue pages need, loaded once per request.
pub struct WorkData<'a> {
    pub catalog: &'a Catalog,
    pub decisions: &'a [(String, Decision)],
    pub rows: &'a RowMap,
    pub feedback: &'a FeedbackMap,
    pub types: &'a HashMap<String, String>,
    pub now: DateTime<Utc>,
}

/// Every icon whose current revision needs a fix (pending, claimed, cannot-fix) or was just fixed (done).
pub fn disapproved_items(data: &WorkData, filters: &Filters) -> Vec<Value> {
    let mut items = Vec::new();
    for (key, decision) in data.decisions {
        let Some(icon) = data.catalog.get(key) else { continue };
        let sha = icon.svg_sha256.clone();
        let mut row = data.rows.get(&(key.clone(), sha.clone())).cloned();
        let status = if decision.status == "disapprove" { "pending" } else { decision.status.as_str() };
        if status == "pending" || status == "claimed" {
            if row.is_none() {
                row = Some(ReviewRow {
                    icon: key.clone(), svg_sha256: sha.clone(), status: status.into(), worker: None,
                    note: Some(String::new()), claimed_at: None,
                    updated_at: decision.stamp.clone(), updated_by: decision.actor.clone(),
                });
            }
        } else if !(status == "ready" && row.as_ref().is_some_and(|r| r.worker.as_deref().is_some_and(|w| !w.is_empty()))) {
            continue;
        }
        let icon_type = data.types.get(key).map(String::as_str);
        if filters.family.is_some_and(|f| icon.family.as_deref() != Some(f)) { continue; }
        if filters.category.is_some_and(|c| icon.category.as_deref() != Some(c)) { continue; }
        if filters.icon_type.is_some_and(|t| icon_type != Some(t)) { continue; }
        let feedback = data.feedback.get(&(key.clone(), sha.clone()));
        if filters.reason.is_some_and(|r| feedback.and_then(|f| f.reason.as_deref()) != Some(r)) { continue; }
        let state = work_state(row.as_ref(), data.now);
        items.push(queue_item(icon, icon_type, decision, feedback, row.as_ref(), state));
    }
    items
}

fn state_of(item: &Value) -> Option<&str> {
    item["work"]["state"].as_str()
}

fn text(item: &Value, field: &str) -> String {
    item[field].as_str().unwrap_or("").to_string()
}

fn page(rows: Vec<Value>, offset: i64, limit: i64) -> (Vec<Value>, Value) {
    let total = rows.len() as i64;
    let next = if offset + limit < total { json!(offset + limit) } else { Value::Null };
    let page = rows.into_iter().skip(offset as usize).take(limit as usize).collect();
    (page, next)
}

/// `/api/work/queue` (claimable only) and `/api/work/disapproved` (all with work state).
pub fn queue(data: &WorkData, query: &Query, claimable_only: bool) -> Result<Value, WorkError> {
    let paging = paging(query, 50)?;
    let filters = Filters { family: paging.one("family"), category: paging.one("category"),
                            icon_type: paging.one("type"), reason: paging.one("reason") };
    let wanted_state = paging.one("state");
    let mut rows: Vec<Value> = disapproved_items(data, &filters).into_iter().filter(|item| {
        let status = item["status"].as_str().unwrap_or("");
        (status == "disapprove" || status == "claimed")
            && (!claimable_only || state_of(item).is_none())
            && wanted_state.is_none_or(|s| state_of(item) == Some(s))
    }).collect();
    rows.sort_by_key(|item| (text(item, "disapproved_at"), text(item, "key")));
    let total = rows.len();
    let (items, next) = page(rows, paging.offset, paging.limit);
    Ok(json!({"total": total, "offset": paging.offset, "next_offset": next, "items": items}))
}

/// `/api/work`: every current revision carrying a worker, for the gallery badges.
pub fn listing(data: &WorkData) -> Value {
    let decisions: HashMap<&str, &Decision> = data.decisions.iter().map(|(k, d)| (k.as_str(), d)).collect();
    let mut keys: Vec<&(String, String)> = data.rows.keys().collect();
    keys.sort();
    let mut claims = Vec::new();
    for pair in keys {
        let row = &data.rows[pair];
        let Some(icon) = data.catalog.get(&pair.0) else { continue };
        if icon.svg_sha256 != pair.1 || !row.worker.as_deref().is_some_and(|w| !w.is_empty()) {
            continue;
        }
        let Some(state) = work_state(Some(row), data.now) else { continue };
        let mut field = work_field(Some(row), Some(state));
        let status = decisions.get(pair.0.as_str()).map(|d| d.status.clone()).unwrap_or_else(|| row.status.clone());
        let map = field.as_object_mut().unwrap();
        map.insert("icon".into(), json!(pair.0));
        map.insert("current".into(), json!(true));
        map.insert("status".into(), json!(public_status(&status)));
        claims.push(field);
    }
    json!({"claims": claims})
}

/// Stage summaries of uploaded fix results, keyed by (icon, sha).
pub type ResultSummaries = HashMap<(String, String), BTreeMap<String, Value>>;

/// `/api/work/review`: everything a reviewer may follow, newest activity first.
pub fn review_listing(data: &WorkData, query: &Query, summaries: &ResultSummaries) -> Result<Value, WorkError> {
    let mut query = query.clone();
    query.entry("limit".into()).or_insert_with(|| vec![MAX_QUEUE.to_string()]);
    let paging = paging(&query, MAX_QUEUE)?;
    let filters = Filters { family: paging.one("family"), category: None, icon_type: None, reason: paging.one("reason") };
    let mut items = disapproved_items(data, &filters);
    for item in items.iter_mut() {
        let key = (text(item, "key"), text(item, "svg_sha256"));
        let stages: Vec<String> = summaries.get(&key).map(|s| s.keys().cloned().collect()).unwrap_or_default();
        item["work"]["results"] = json!(stages);
    }
    let sort_key = |item: &Value| {
        let stamp = item["work"]["claimed_at"].as_str().filter(|s| !s.is_empty()).map(str::to_string)
            .unwrap_or_else(|| text(item, "disapproved_at"));
        (stamp, text(item, "key"))
    };
    let mut ordered = items.clone();
    ordered.sort_by_key(|item| std::cmp::Reverse(sort_key(item)));
    if let Some(state) = paging.one("state") {
        ordered.retain(|item| state_of(item) == Some(state));
    }
    if let Some(status) = paging.one("status") {
        ordered.retain(|item| item["status"].as_str() == Some(status));
    }
    let mut counts = Map::new();
    for state in STATES {
        counts.insert(state.into(), json!(items.iter().filter(|item| state_of(item) == Some(state)).count()));
    }
    let total = ordered.len();
    let (page_items, next) = page(ordered, paging.offset, paging.limit);
    Ok(json!({"total": total, "offset": paging.offset, "next_offset": next, "counts": counts, "items": page_items}))
}

// ---- transition checks; the caller runs the conditional SQL when these pass ----

/// Checks before `claim`; `status` is the current decision's status.
pub fn check_claim(status: &str, row: Option<&ReviewRow>, now: DateTime<Utc>, worker: &str) -> Result<(), WorkError> {
    let state = work_state(row, now);
    if !matches!(status, "pending" | "claimed" | "disapprove") {
        return Err(WorkError::with_work(
            format!("Only disapproved icons can be claimed; this revision is {}.", public_status(status)), 409, work_field(row, state)));
    }
    if let Some(state) = state {
        let holder = row.and_then(|r| r.worker.clone()).unwrap_or_default();
        if state == "working" && holder == worker {
            return Err(WorkError::with_work("You already hold this claim.", 409, work_field(row, Some(state))));
        }
        let message = match state {
            "working" => format!("{holder} is working on this icon."),
            "cannot-fix" => format!("{holder} reported this revision cannot be fixed."),
            other => format!("This revision is {other}."),
        };
        return Err(WorkError::with_work(message, 409, work_field(row, Some(state))));
    }
    Ok(())
}

/// `_own_claim`: the worker must hold a live claim.
pub fn check_own_claim(row: Option<&ReviewRow>, now: DateTime<Utc>, worker: &str, verb: &str) -> Result<(), WorkError> {
    let state = work_state(row, now);
    if state != Some("working") {
        return Err(WorkError::with_work(
            format!("No active claim to {verb}; this revision is {}.", state.unwrap_or("not claimed")), 409, work_field(row, state)));
    }
    let holder = row.and_then(|r| r.worker.clone()).unwrap_or_default();
    if holder != worker {
        return Err(WorkError::with_work(format!("This claim belongs to {holder}, not {worker}."), 409, work_field(row, state)));
    }
    Ok(())
}

pub fn check_result(stage: &str, row: Option<&ReviewRow>, now: DateTime<Utc>, worker: &str) -> Result<(), WorkError> {
    if stage != "before" && stage != "after" {
        return Err(WorkError::new("stage must be before or after.", 400));
    }
    let state = work_state(row, now);
    let allowed: &[&str] = if stage == "before" { &["working"] } else { &["working", "done", "cannot-fix"] };
    if !state.is_some_and(|s| allowed.contains(&s)) {
        let shown = state.map(str::to_string).unwrap_or_else(|| "None".into());
        return Err(WorkError::with_work(
            format!("Upload the {stage} result while you hold the claim; this revision is {shown}."), 409, work_field(row, state)));
    }
    let holder = row.and_then(|r| r.worker.clone()).unwrap_or_default();
    if holder != worker {
        return Err(WorkError::with_work(format!("This claim belongs to {holder}, not {worker}."), 409, work_field(row, state)));
    }
    Ok(())
}

pub fn check_abandon(row: Option<&ReviewRow>, now: DateTime<Utc>) -> Result<&'static str, WorkError> {
    let state = work_state(row, now);
    match state {
        Some(state @ ("working" | "cannot-fix")) => Ok(state),
        _ => Err(WorkError::with_work(
            format!("There is no claim to release; this revision is {}.", state.unwrap_or("not claimed")),
            if row.is_some() { 409 } else { 404 }, work_field(row, state))),
    }
}

/// One fix-result row without its large text fields.
#[derive(Clone, Debug, Default)]
pub struct ResultRow {
    pub icon: String,
    pub svg_sha256: String,
    pub stage: String,
    pub worker: String,
    pub python_path: Option<String>,
    pub note: String,
    pub saved_at: String,
    pub has_python: bool,
    pub has_validation: bool,
}

pub fn result_summaries(rows: &[ResultRow]) -> ResultSummaries {
    let mut summaries: ResultSummaries = HashMap::new();
    for row in rows {
        summaries.entry((row.icon.clone(), row.svg_sha256.clone())).or_default().insert(row.stage.clone(), json!({
            "worker": row.worker, "python_path": row.python_path, "note": row.note, "saved_at": row.saved_at,
            "has_python": row.has_python, "has_validation": row.has_validation,
        }));
    }
    summaries
}

/// One feedback row as `/api/work/history` lists it.
#[derive(Clone, Debug, Default)]
pub struct HistoryFeedback {
    pub id: i64,
    pub svg_sha256: String,
    pub reason: Option<String>,
    pub feedback: String,
    pub author: Option<String>,
    pub created_at: String,
    pub edited_by: Option<String>,
    pub edited_at: Option<String>,
}

/// One activity-log row for the icon.
#[derive(Clone, Debug, Default)]
pub struct HistoryEvent {
    pub username: String,
    pub action: String,
    pub details: String,
    pub created_at: String,
}

struct HistoryEntry {
    value: Map<String, Value>,
    first_seen: Option<String>,
}

/// The history entry of one revision, created on first use (in first-use order).
fn revision(revisions: &mut HashMap<String, HistoryEntry>, order: &mut Vec<String>, sha: &str, current_sha: &str) -> String {
    if !revisions.contains_key(sha) {
        let mut value = Map::new();
        value.insert("svg_sha256".into(), json!(sha));
        value.insert("current".into(), json!(sha == current_sha));
        value.insert("review".into(), Value::Null);
        value.insert("claim".into(), Value::Null);
        value.insert("feedback".into(), json!([]));
        value.insert("results".into(), json!({}));
        revisions.insert(sha.to_string(), HistoryEntry { value, first_seen: None });
        order.push(sha.to_string());
    }
    sha.to_string()
}

fn seen(entry: &mut HistoryEntry, stamp: Option<&str>) {
    if let Some(stamp) = stamp.filter(|s| !s.is_empty()) {
        if entry.first_seen.as_deref().is_none_or(|first| stamp < first) {
            entry.first_seen = Some(stamp.to_string());
        }
    }
}

/// `/api/work/history`: revisions, reviews, feedback, claims, results and the event log of one icon.
pub fn history(icon: &Icon, decision: Option<&Decision>, rows: &[ReviewRow], feedback: &[HistoryFeedback],
               results: &ResultSummaries, events: &[HistoryEvent], now: DateTime<Utc>) -> Value {
    let current_sha = icon.svg_sha256.clone();
    let decision = decision.cloned().unwrap_or_else(Decision::ready);
    let mut order: Vec<String> = Vec::new();
    let mut revisions: HashMap<String, HistoryEntry> = HashMap::new();
    let mut sorted_rows: Vec<&ReviewRow> = rows.iter().filter(|r| r.icon == icon.key).collect();
    sorted_rows.sort_by(|a, b| a.svg_sha256.cmp(&b.svg_sha256));
    for row in sorted_rows {
        let sha = revision(&mut revisions, &mut order, &row.svg_sha256, &current_sha);
        let entry = revisions.get_mut(&sha).unwrap();
        entry.value.insert("review".into(), json!({"status": public_status(&row.status),
            "updated_by": row.updated_by, "updated_at": row.updated_at}));
        seen(entry, row.updated_at.as_deref());
        if let Some(state) = work_state(Some(row), now) {
            entry.value.insert("claim".into(), work_field(Some(row), Some(state)));
            seen(entry, row.claimed_at.as_deref());
        }
    }
    for item in feedback {
        let sha = revision(&mut revisions, &mut order, &item.svg_sha256, &current_sha);
        let entry = revisions.get_mut(&sha).unwrap();
        entry.value["feedback"].as_array_mut().unwrap().push(json!({
            "id": item.id, "reason": item.reason, "feedback": item.feedback, "author": item.author,
            "created_at": item.created_at, "edited_by": item.edited_by, "edited_at": item.edited_at}));
        seen(entry, Some(&item.created_at));
    }
    let mut result_keys: Vec<&(String, String)> = results.keys().filter(|(k, _)| *k == icon.key).collect();
    result_keys.sort();
    for pair in result_keys {
        let stages = &results[pair];
        let sha = revision(&mut revisions, &mut order, &pair.1, &current_sha);
        let entry = revisions.get_mut(&sha).unwrap();
        entry.value.insert("results".into(), json!(stages));
        for summary in stages.values() {
            seen(entry, summary["saved_at"].as_str());
        }
    }
    let current = revision(&mut revisions, &mut order, &current_sha, &current_sha);
    {
        let entry = revisions.get_mut(&current).unwrap();
        if entry.value["review"].is_null() || decision.status == "rejected" {
            entry.value.insert("review".into(), json!({"status": public_status(&decision.status),
                "updated_by": decision.actor, "updated_at": decision.stamp}));
        }
    }
    let current_entry = revisions[&current].value.clone();
    let history_events: Vec<Value> = events.iter().map(|event| {
        let details: Value = serde_json::from_str(&event.details).unwrap_or_else(|_| json!({}));
        json!({"at": event.created_at, "user": event.username, "action": event.action, "details": details})
    }).collect();
    let mut ordered: Vec<(bool, String, Map<String, Value>)> = order.iter().map(|sha| {
        let entry = &revisions[sha];
        (entry.value["current"].as_bool().unwrap_or(false), entry.first_seen.clone().unwrap_or_default(), entry.value.clone())
    }).collect();
    ordered.sort_by(|a, b| (a.0, &a.1).cmp(&(b.0, &b.1)));
    let review = &current_entry["review"];
    json!({
        "icon": icon.key, "name": icon.name, "family": icon.family, "preview_url": icon.preview_url,
        "python_source": icon.python_source,
        "current": {"svg_sha256": current_sha, "status": review["status"], "updated_by": review["updated_by"],
                    "updated_at": review["updated_at"],
                    "work": if current_entry["claim"].is_null() { json!({"state": null}) } else { current_entry["claim"].clone() }},
        "revisions": ordered.into_iter().map(|(_, _, value)| Value::Object(value)).collect::<Vec<_>>(),
        "events": history_events,
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::query::parse_qs;
    use chrono::TimeZone;

    fn now() -> DateTime<Utc> {
        Utc.with_ymd_and_hms(2026, 9, 25, 12, 0, 0).unwrap()
    }

    fn row(status: &str, worker: Option<&str>, claimed_hours_ago: Option<i64>) -> ReviewRow {
        ReviewRow {
            icon: "solo/a".into(), svg_sha256: "s".into(), status: status.into(),
            updated_at: Some("2026-09-24T00:00:00+00:00".into()), updated_by: Some("ray".into()),
            worker: worker.map(Into::into), note: Some(String::new()),
            claimed_at: claimed_hours_ago.map(|h| crate::time::iso_utc(now() - Duration::hours(h))),
        }
    }

    #[test]
    fn states_follow_row_and_clock() {
        assert_eq!(work_state(Some(&row("claimed", Some("w"), Some(1))), now()), Some("working"));
        assert_eq!(work_state(Some(&row("claimed", Some("w"), Some(7))), now()), None, "lease expired");
        assert_eq!(work_state(Some(&row("ready", Some("w"), Some(1))), now()), Some("done"));
        assert_eq!(work_state(Some(&row("pending", Some("w"), Some(1))), now()), Some("cannot-fix"));
        assert_eq!(work_state(Some(&row("pending", None, None)), now()), None);
        assert_eq!(work_state(None, now()), None);
    }

    #[test]
    fn claim_checks() {
        assert!(check_claim("pending", Some(&row("pending", None, None)), now(), "w").is_ok());
        assert!(check_claim("pending", None, now(), "w").is_ok());
        let mine = row("claimed", Some("w"), Some(1));
        assert_eq!(check_claim("claimed", Some(&mine), now(), "w").unwrap_err().message, "You already hold this claim.");
        assert_eq!(check_claim("claimed", Some(&mine), now(), "x").unwrap_err().message, "w is working on this icon.");
        assert!(check_claim("claimed", Some(&row("claimed", Some("w"), Some(8))), now(), "x").is_ok(), "expired claim is open");
        let approved = check_claim("approve", None, now(), "w").unwrap_err();
        assert_eq!(approved.status, 409);
        assert!(approved.message.contains("this revision is approve"));
        let cannot = check_claim("pending", Some(&row("pending", Some("w"), Some(1))), now(), "x").unwrap_err();
        assert_eq!(cannot.message, "w reported this revision cannot be fixed.");
    }

    #[test]
    fn own_claim_and_abandon() {
        let mine = row("claimed", Some("w"), Some(1));
        assert!(check_own_claim(Some(&mine), now(), "w", "finish").is_ok());
        assert!(check_own_claim(Some(&mine), now(), "x", "finish").unwrap_err().message.contains("belongs to w"));
        assert_eq!(check_own_claim(None, now(), "w", "finish").unwrap_err().message,
                   "No active claim to finish; this revision is not claimed.");
        assert_eq!(check_abandon(Some(&mine), now()), Ok("working"));
        assert_eq!(check_abandon(None, now()).unwrap_err().status, 404);
        assert_eq!(check_abandon(Some(&row("pending", None, None)), now()).unwrap_err().status, 409);
    }

    #[test]
    fn result_stage_rules() {
        let done = row("ready", Some("w"), Some(1));
        assert!(check_result("after", Some(&done), now(), "w").is_ok());
        assert!(check_result("before", Some(&done), now(), "w").is_err());
        assert_eq!(check_result("middle", Some(&done), now(), "w").unwrap_err().status, 400);
    }

    #[test]
    fn work_field_shape() {
        let field = work_field(Some(&row("claimed", Some("w"), Some(1))), Some("working"));
        assert_eq!(field["state"], "working");
        assert_eq!(field["expires_at"], "2026-09-25T17:00:00+00:00");
        assert_eq!(work_field(None, None), json!({"state": null}));
    }

    #[test]
    fn validation_messages() {
        assert!(validate_worker(&json!("  thuan-mac  ")).unwrap() == "thuan-mac");
        assert!(validate_worker(&json!("")).is_err());
        assert!(validate_worker(&json!("a\u{7}b")).is_err());
        assert!(validate_worker(&json!(5)).is_err());
        assert!(validate_note(&json!("  "), true).is_err());
        assert_eq!(validate_note(&Value::Null, false).unwrap(), "");
        assert_eq!(validate_text(&json!(""), "svg", false).unwrap(), None);
        assert!(validate_text(&json!(""), "svg", true).is_err());
    }

    #[test]
    fn queue_orders_oldest_disapproval_first_and_pages() {
        let icon = |key: &str| Icon { key: key.into(), svg_sha256: "s".into(), family: Some("solo".into()), ..Default::default() };
        let catalog = Catalog::new(vec![icon("solo/a"), icon("solo/b"), icon("solo/c")], false);
        let decision = |at: &str| Decision { status: "pending".into(), actor: Some("ray".into()), stamp: Some(at.into()) };
        let decisions = vec![("solo/a".to_string(), decision("2026-09-03")), ("solo/b".to_string(), decision("2026-09-01")),
                             ("solo/c".to_string(), Decision::ready())];
        let rows = RowMap::new();
        let data = WorkData { catalog: &catalog, decisions: &decisions, rows: &rows, feedback: &FeedbackMap::new(),
                              types: &HashMap::new(), now: now() };
        let result = queue(&data, &parse_qs("limit=1"), true).unwrap();
        assert_eq!(result["total"], 2);
        assert_eq!(result["items"][0]["key"], "solo/b");
        assert_eq!(result["next_offset"], 1);
        assert_eq!(result["items"][0]["status"], "disapprove");
        assert!(queue(&data, &parse_qs("limit=0"), true).is_err());
        assert!(queue(&data, &parse_qs("offset=x"), true).is_err());
    }
}
