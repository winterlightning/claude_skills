//! TODO / SKIP decisions for reference primitives — ported from primitive_status.py
//! and primitive_briefs.py. Catalog rows (`primitives.json`) are passed through as JSON.

use serde::Deserialize;
use serde_json::{json, Map, Value};
use std::collections::{HashMap, HashSet};

pub const REASONS: [&str; 4] = ["combination", "container", "text_number", "other"];
pub const MAX_BATCH: usize = 500;
pub const MAX_NOTE: usize = 2000;
pub const SUB_POSITIONS: [&str; 9] = ["top-left", "top", "top-right", "left", "center", "right", "bottom-left", "bottom", "bottom-right"];
pub const BRIEF_FAMILIES: [&str; 5] = ["sub", "solo", "container", "avatar", "symbol"];
pub const MAX_BRIEF: usize = 20000;
const TODO_REFERENCES: &str = "icon_set/work/todo-references";
const MAKE_RAY_NOTE: &str = "Most of these already have a primitive-make-ray run that failed validation. Do not skip a file because a result.json exists: author a fresh run in a new RESULT_DIR for every file, unless its newest existing run is already valid, in which case report it as done and move on.";

pub fn is_uuid(text: &str) -> bool {
    let groups: Vec<&str> = text.split('-').collect();
    groups.len() == 5
        && groups.iter().zip([8, 4, 4, 4, 12]).all(|(g, n)| g.len() == n && g.bytes().all(|b| b.is_ascii_digit() || (b'a'..=b'f').contains(&b)))
}

pub fn python_repr(value: &Value) -> String {
    match value {
        Value::String(text) => format!("'{text}'"),
        Value::Null => "None".into(),
        other => other.to_string(),
    }
}

/// `validate(uuids, status, reason, note, known)` → (uuids, reason, note).
pub fn validate(uuids: &Value, status: &str, reason: &Value, note: &Value, known: Option<&HashSet<String>>)
                -> Result<(Vec<String>, Option<String>, String), String> {
    if status != "todo" && status != "skip" {
        return Err("Status must be 'todo' or 'skip'.".into());
    }
    let list = uuids.as_array().filter(|l| !l.is_empty()).ok_or("Choose at least one primitive.")?;
    if list.len() > MAX_BATCH {
        return Err(format!("Update at most {MAX_BATCH} primitives at a time."));
    }
    let mut cleaned: Vec<String> = Vec::new();
    for item in list {
        let uid = item.as_str().map(|s| s.trim().to_lowercase()).filter(|s| is_uuid(s))
            .ok_or_else(|| format!("Invalid primitive id: {}", python_repr(item)))?;
        if known.is_some_and(|k| !k.contains(&uid)) {
            return Err(format!("Unknown primitive: {uid}"));
        }
        if !cleaned.contains(&uid) {
            cleaned.push(uid);
        }
    }
    let note = match note {
        Value::Null => String::new(),
        Value::String(text) if text.chars().count() <= MAX_NOTE => text.trim().to_string(),
        Value::String(text) if text.is_empty() => String::new(),
        _ => return Err(format!("Notes must be text of at most {MAX_NOTE} characters.")),
    };
    if status == "skip" {
        let reason = reason.as_str().filter(|r| REASONS.contains(r))
            .ok_or_else(|| format!("Choose a skip reason: {}.", REASONS.join(", ")))?;
        if reason == "other" && note.is_empty() {
            return Err("A skip for 'other' needs a note explaining why.".into());
        }
        Ok((cleaned, Some(reason.to_string()), note))
    } else {
        Ok((cleaned, None, String::new()))
    }
}

fn component_fields(component: &Value, family: &str) -> Result<Value, String> {
    let mut item = Map::new();
    item.insert("family".into(), json!(family));
    for (key, limit) in [("name", 200usize), ("description", MAX_NOTE)] {
        let value = component.get(key).and_then(Value::as_str)
            .filter(|v| !v.trim().is_empty() && v.chars().count() <= limit)
            .ok_or_else(|| format!("Component {key} must be nonempty text of at most {limit} characters."))?;
        item.insert(key.into(), json!(value.trim()));
    }
    Ok(Value::Object(item))
}

/// `validate_component`: null clears; main is solo/container, sub is sub.
pub fn validate_component(component: &Value, field: &str) -> Result<Option<Value>, String> {
    if component.is_null() {
        return Ok(None);
    }
    let allowed: &[&str] = if field == "sub_brief" { &["sub"] } else { &["solo", "container"] };
    let family = component.get("family").and_then(Value::as_str).filter(|f| allowed.contains(f))
        .ok_or("The main brief must be solo/container; the sub brief must be sub.")?;
    component_fields(component, family).map(Some)
}

/// `validate_brief`: the legacy paired brief → (main, sub).
pub fn validate_brief(brief: &Value) -> Result<Option<(Value, Value)>, String> {
    if brief.is_null() {
        return Ok(None);
    }
    let kind = brief.get("combination_type").and_then(Value::as_str).filter(|k| *k == "container" || *k == "side")
        .ok_or("Choose a container + sub or main + sub combination brief.")?;
    let components = brief.get("components").and_then(Value::as_array).filter(|c| c.len() == 2)
        .ok_or("A combination brief needs exactly two components.")?;
    let mut cleaned = Vec::new();
    for (index, component) in components.iter().enumerate() {
        let allowed: &[&str] = if index == 1 { &["sub"] } else if kind == "container" { &["container"] } else { &["solo", "container"] };
        let family = component.get("family").and_then(Value::as_str).filter(|f| allowed.contains(f))
            .ok_or("Choose the correct family for each component: container/main first, sub second.")?;
        cleaned.push(component_fields(component, family)?);
    }
    let sub = cleaned.pop().unwrap();
    Ok(Some((cleaned.pop().unwrap(), sub)))
}

/// One `primitive_status` row.
#[derive(Clone, Debug, Default, Deserialize, PartialEq)]
pub struct StatusRow {
    pub uuid: String,
    pub status: String,
    pub reason: String,
    #[serde(default)]
    pub note: String,
    pub updated_by: String,
    pub updated_at: String,
    #[serde(default)]
    pub main_brief: Option<String>,
    #[serde(default)]
    pub sub_brief: Option<String>,
    #[serde(default)]
    pub sub_position: Option<String>,
}

/// Python's `json.dumps(value, ensure_ascii=False, sort_keys=True)` for the small brief objects.
pub fn encode_sorted(value: &Value) -> String {
    fn sort(value: &Value) -> Value {
        match value {
            Value::Object(map) => {
                let mut keys: Vec<&String> = map.keys().collect();
                keys.sort();
                Value::Object(keys.into_iter().map(|k| (k.clone(), sort(&map[k]))).collect())
            }
            Value::Array(items) => Value::Array(items.iter().map(sort).collect()),
            other => other.clone(),
        }
    }
    python_json(&sort(value))
}

/// `json.dumps` default separators (`, ` and `: `) — how stored JSON text looks in the database.
pub fn python_json(value: &Value) -> String {
    match value {
        Value::Object(map) => format!("{{{}}}", map.iter()
            .map(|(k, v)| format!("{}: {}", serde_json::to_string(k).unwrap(), python_json(v))).collect::<Vec<_>>().join(", ")),
        Value::Array(items) => format!("[{}]", items.iter().map(python_json).collect::<Vec<_>>().join(", ")),
        other => serde_json::to_string(other).unwrap(),
    }
}

/// Optional component fields of a status update; `None` = omitted (keep the saved value).
#[derive(Clone, Debug, Default)]
pub struct BriefUpdates {
    pub main: Option<Option<Value>>,
    pub sub: Option<Option<Value>>,
    pub sub_position: Option<Option<String>>,
}

/// Parse `combination_brief` / `main_brief` / `sub_brief` / `sub_position` from a request body.
pub fn brief_updates(data: &Value, status: &str, reason: Option<&str>, count: usize) -> Result<BriefUpdates, String> {
    let mut updates = BriefUpdates::default();
    let has = |key: &str| data.get(key).is_some();
    let (mut main, mut sub) = (None, None);
    if has("combination_brief") {
        if has("main_brief") || has("sub_brief") {
            return Err("Use separate component fields or the legacy paired brief, not both.".into());
        }
        match validate_brief(&data["combination_brief"])? {
            Some((m, s)) => { main = Some(m); sub = Some(s); }
            None => { main = Some(Value::Null); sub = Some(Value::Null); }
        }
    } else {
        if has("main_brief") { main = Some(data["main_brief"].clone()); }
        if has("sub_brief") { sub = Some(data["sub_brief"].clone()); }
    }
    if let Some(value) = main { updates.main = Some(validate_component(&value, "main_brief")?); }
    if let Some(value) = sub { updates.sub = Some(validate_component(&value, "sub_brief")?); }
    if (updates.main.is_some() || updates.sub.is_some())
        && (status != "skip" || !matches!(reason, Some("container" | "combination")) || count != 1) {
        return Err("Save a component brief for one skipped container or combination at a time.".into());
    }
    if has("sub_position") {
        let position = &data["sub_position"];
        let position = match position {
            Value::Null => None,
            Value::String(p) if SUB_POSITIONS.contains(&p.as_str()) => Some(p.clone()),
            _ => return Err("Choose a valid sub-icon position relative to the main icon.".into()),
        };
        if status != "skip" || reason != Some("combination") || count != 1 {
            return Err("Set a sub-icon position for one skipped side combination at a time.".into());
        }
        updates.sub_position = Some(position);
    }
    Ok(updates)
}

/// What to do for one uuid of a status update.
#[derive(Clone, Debug, PartialEq)]
pub enum StatusWrite {
    Delete,
    Upsert { reason: String, note: String, main: Option<String>, sub: Option<String>, position: Option<String> },
}

#[derive(Clone, Debug, PartialEq)]
pub struct StatusChange {
    pub write: Option<StatusWrite>,
    /// (action, details) for the activity log.
    pub record: Option<(String, Value)>,
    pub changed: bool,
}

/// `set_status` for one uuid, given its current row.
pub fn status_change(current: Option<&StatusRow>, status: &str, reason: Option<&str>, note: &str,
                     updates: &BriefUpdates, authority: &str) -> StatusChange {
    let mut audit = Map::new();
    audit.insert("previous_classification".into(), json!(current.map(|c| c.reason.as_str()).unwrap_or("todo")));
    audit.insert("classification".into(), json!(if status == "skip" { reason.unwrap_or("") } else { "todo" }));
    audit.insert("authority".into(), json!(authority));
    audit.insert("previous_note".into(), json!(current.map(|c| c.note.as_str()).unwrap_or("")));
    let confirmed = || StatusChange {
        write: None, changed: false,
        record: (authority == "user").then(|| ("primitive_classification_confirmed".to_string(), Value::Object(audit.clone()))),
    };
    if status == "todo" {
        let Some(current) = current else { return confirmed() };
        let mut details = Map::new();
        details.insert("previous_reason".into(), json!(current.reason));
        details.extend(audit.clone());
        return StatusChange { write: Some(StatusWrite::Delete), changed: true,
                              record: Some(("primitive_todo".into(), Value::Object(details))) };
    }
    let reason = reason.unwrap_or("other");
    let (mut main, mut sub, mut position) = match current {
        Some(c) => (c.main_brief.clone(), c.sub_brief.clone(), c.sub_position.clone()),
        None => (None, None, None),
    };
    if let Some(p) = &updates.sub_position { position = p.clone(); }
    if reason != "combination" { position = None; }
    let encode = |value: &Option<Value>| value.as_ref().map(encode_sorted);
    if let Some(m) = &updates.main { main = encode(m); }
    if let Some(s) = &updates.sub { sub = encode(s); }
    if reason != "container" && reason != "combination" { main = None; sub = None; }
    if let Some(c) = current {
        if (c.reason.as_str(), c.note.as_str(), &c.main_brief, &c.sub_brief, &c.sub_position)
            == (reason, note, &main, &sub, &position) {
            return confirmed();
        }
    }
    let decode = |text: &Option<String>| text.as_deref().and_then(|t| serde_json::from_str::<Value>(t).ok()).unwrap_or(Value::Null);
    let mut details = Map::new();
    details.insert("reason".into(), json!(reason));
    details.insert("note".into(), json!(note));
    details.insert("main_brief".into(), decode(&main));
    details.insert("sub_brief".into(), decode(&sub));
    details.insert("sub_position".into(), json!(position));
    details.extend(audit);
    StatusChange {
        write: Some(StatusWrite::Upsert { reason: reason.into(), note: note.into(), main, sub, position }),
        record: Some(("primitive_skip".into(), Value::Object(details))),
        changed: true,
    }
}

/// `load_status`: uuid → decision object.
pub fn load_status(rows: &[StatusRow]) -> Map<String, Value> {
    let mut result = Map::new();
    for row in rows {
        let parse = |text: &Option<String>| text.as_deref().and_then(|t| serde_json::from_str::<Value>(t).ok());
        let (main, sub) = (parse(&row.main_brief), parse(&row.sub_brief));
        let combination = match (&main, &sub) {
            (Some(m), Some(s)) if !m.is_null() && !s.is_null() => json!({
                "combination_type": if row.reason == "container" { "container" } else { "side" },
                "components": [m, s]}),
            _ => Value::Null,
        };
        result.insert(row.uuid.clone(), json!({
            "status": row.status, "reason": row.reason, "note": row.note,
            "updated_by": row.updated_by, "updated_at": row.updated_at,
            "main_brief": main, "sub_brief": sub, "sub_position": row.sub_position,
            "combination_brief": combination}));
    }
    result
}

fn effective(row: &Value, decision: &Value) -> &'static str {
    let state = row.get("state").and_then(Value::as_str);
    if state == Some("generated") {
        return "generated";
    }
    if !decision.is_null() {
        return "skip";
    }
    let has_models = row.get("models").is_some_and(|m| match m {
        Value::Array(a) => !a.is_empty(),
        Value::Null | Value::Bool(false) => false,
        Value::String(s) => !s.is_empty(),
        _ => true,
    });
    if has_models || matches!(state, Some("model_only" | "build_failed" | "work_only")) {
        return "drawn";
    }
    "todo"
}

fn row_decision(row: &Value, statuses: &Map<String, Value>) -> Value {
    if let Some(decision) = row.get("uuid").and_then(Value::as_str).and_then(|u| statuses.get(u)) {
        return decision.clone();
    }
    for alias in row.get("aliases").and_then(Value::as_array).into_iter().flatten() {
        if let Some(uid) = alias.get("uuid").and_then(Value::as_str) {
            if let Some(Value::Object(decision)) = statuses.get(uid) {
                let mut tagged = decision.clone();
                tagged.insert("from_uuid".into(), json!(uid));
                return Value::Object(tagged);
            }
        }
    }
    Value::Null
}

/// `merge`: each catalog row plus status, decision and conflict.
pub fn merge(rows: &[Value], statuses: &Map<String, Value>) -> Vec<Value> {
    rows.iter().map(|row| {
        let decision = row_decision(row, statuses);
        let mut merged = row.as_object().cloned().unwrap_or_default();
        let conflict = !decision.is_null() && row.get("state").and_then(Value::as_str) == Some("generated");
        merged.insert("status".into(), json!(effective(row, &decision)));
        merged.insert("decision".into(), decision);
        merged.insert("conflict".into(), json!(conflict));
        Value::Object(merged)
    }).collect()
}

/// Every uuid the catalog knows (canonical or folded alias) → its canonical uuid.
pub fn canonical_map(rows: &[Value]) -> HashMap<String, String> {
    let mut result = HashMap::new();
    for row in rows {
        let Some(uid) = row.get("uuid").and_then(Value::as_str).filter(|u| !u.is_empty()) else { continue };
        result.insert(uid.to_string(), uid.to_string());
        for alias in row.get("aliases").and_then(Value::as_array).into_iter().flatten() {
            if let Some(alias_uid) = alias.get("uuid").and_then(Value::as_str) {
                result.insert(alias_uid.to_string(), uid.to_string());
            }
        }
    }
    result
}

fn bump(counts: &mut Map<String, Value>, key: &str, by: i64) {
    let current = counts.get(key).and_then(Value::as_i64).unwrap_or(0);
    counts.insert(key.to_string(), json!(current + by));
}

/// `summarize`: counts overall and per category (Counter semantics, zero entries kept).
pub fn summarize(merged: &[Value]) -> Value {
    let mut categories: Map<String, Value> = Map::new();
    for row in merged {
        let category = row["category"].as_str().unwrap_or("").to_string();
        let counts = categories.entry(category).or_insert_with(|| json!({})).as_object_mut().unwrap();
        bump(counts, "total", 1);
        bump(counts, row["status"].as_str().unwrap_or(""), 1);
        bump(counts, "build_failed", (row.get("state").and_then(Value::as_str) == Some("build_failed")) as i64);
        bump(counts, "conflict", row["conflict"].as_bool().unwrap_or(false) as i64);
        if row["status"] == "skip" {
            let reason = row["decision"]["reason"].as_str().unwrap_or("");
            bump(counts, &format!("skip_{reason}"), 1);
        }
    }
    let mut overall = Map::new();
    for counts in categories.values() {
        for (key, value) in counts.as_object().unwrap() {
            bump(&mut overall, key, value.as_i64().unwrap_or(0));
        }
    }
    json!({"overall": overall, "categories": categories})
}

/// `filter_rows`.
pub fn filter_rows<'a>(merged: &'a [Value], category: Option<&str>, status: Option<&str>, batch: Option<&str>,
                       reason: Option<&str>) -> Vec<&'a Value> {
    let category = category.unwrap_or("").to_lowercase();
    merged.iter().filter(|row| {
        if !category.is_empty() && row["category"].as_str().unwrap_or("").to_lowercase() != category { return false; }
        if let Some(status) = status.filter(|s| !s.is_empty() && *s != "all") {
            if row["status"].as_str() != Some(status) { return false; }
        }
        if let Some(batch) = batch.filter(|b| !b.is_empty()) {
            if row.get("batch").and_then(Value::as_str) != Some(batch) { return false; }
        }
        if let Some(reason) = reason.filter(|r| !r.is_empty()) {
            if row["decision"].get("reason").and_then(Value::as_str) != Some(reason) { return false; }
        }
        true
    }).collect()
}

/// `make_ray_prompt`: the next `count` TODO primitives of a category as a primitive-make-ray prompt.
pub fn make_ray_prompt(merged: &[Value], category: &str, count: i64, offset: i64) -> Value {
    let todo = filter_rows(merged, Some(category), Some("todo"), None, None);
    let picked: Vec<&Value> = todo.iter().skip(offset.max(0) as usize).take(count.max(0) as usize).copied().collect();
    let files: Vec<String> = picked.iter().map(|row| {
        let path = row["path"].as_str().unwrap_or("");
        format!("{TODO_REFERENCES}/{}", path.rsplit('/').next().unwrap_or(path))
    }).collect();
    let label = if category.trim().is_empty() { "all".to_string() } else { category.trim().to_string() };
    let mut lines = vec![format!("Run $primitive-make-ray draw each of these {} reference files in order. (tp:{label})", files.len()),
                         format!("  {MAKE_RAY_NOTE}")];
    lines.extend(files.iter().map(|file| format!("  {file}")));
    let icons: Vec<Value> = picked.iter().zip(&files).map(|(row, file)| {
        let concept = row.get("concept").and_then(Value::as_str).filter(|c| !c.is_empty())
            .or_else(|| row.get("old_concept").and_then(Value::as_str)).unwrap_or("");
        json!({"uuid": row["uuid"], "concept": concept, "file": file})
    }).collect();
    json!({"category": label, "count": files.len(), "offset": offset, "todo_total": todo.len(),
           "remaining": (todo.len() as i64 - offset - files.len() as i64).max(0),
           "icons": icons, "files": files, "prompt": lines.join("\n") + "\n"})
}

/// `save_primitive_brief` validation → (family, trimmed brief).
pub fn validate_primitive_brief(uid: &Value, family: &Value, brief: &Value, known: &HashSet<String>)
                                -> Result<(String, String, String), String> {
    let uid = uid.as_str().filter(|u| known.contains(*u)).ok_or("Choose a known primitive.")?;
    let family = family.as_str().filter(|f| BRIEF_FAMILIES.contains(f))
        .ok_or("Choose an icon family: sub, solo, container, avatar or symbol.")?;
    let brief = brief.as_str().filter(|b| !b.trim().is_empty() && b.chars().count() <= MAX_BRIEF)
        .ok_or_else(|| format!("Enter a brief of 1–{} characters.", "20,000"))?;
    Ok((uid.to_string(), family.to_string(), brief.trim().to_string()))
}

#[cfg(test)]
mod tests {
    use super::*;

    const A: &str = "bd456324-64d7-46c8-a153-b39382cfb4fa";
    const B: &str = "ac0c8839-9020-4a65-9a30-af5a45d63503";

    fn rows() -> Vec<Value> {
        vec![
            json!({"uuid": A, "category": "accessories", "batch": "batch-01", "path": "accessories/batch-01/x_a.svg",
                   "concept": "Necklace", "state": "none", "aliases": [{"uuid": B}]}),
            json!({"uuid": "00000000-0000-0000-0000-000000000001", "category": "accessories", "path": "accessories/y.svg",
                   "old_concept": "ring", "state": "generated", "models": ["ring"]}),
        ]
    }

    #[test]
    fn validates_like_python() {
        assert!(validate(&json!([A]), "skip", &json!("other"), &json!(""), None).is_err());
        let (ids, reason, note) = validate(&json!([A.to_uppercase(), A]), "skip", &json!("text_number"), &json!(" n "), None).unwrap();
        assert_eq!((ids.len(), reason.as_deref(), note.as_str()), (1, Some("text_number"), "n"));
        assert_eq!(validate(&json!(["nope"]), "skip", &json!("other"), &json!("x"), None).unwrap_err(), "Invalid primitive id: 'nope'");
        assert_eq!(validate(&json!([A]), "todo", &json!("other"), &json!("x"), None).unwrap(), (vec![A.to_string()], None, String::new()));
    }

    #[test]
    fn merge_uses_aliases_and_conflicts() {
        let mut statuses = Map::new();
        statuses.insert(B.into(), json!({"status": "skip", "reason": "container"}));
        statuses.insert("00000000-0000-0000-0000-000000000001".into(), json!({"status": "skip", "reason": "other"}));
        let merged = merge(&rows(), &statuses);
        assert_eq!(merged[0]["status"], "skip");
        assert_eq!(merged[0]["decision"]["from_uuid"], B);
        assert_eq!(merged[1]["status"], "generated");
        assert_eq!(merged[1]["conflict"], true);
        let summary = summarize(&merged);
        assert_eq!(summary["overall"]["total"], 2);
        assert_eq!(summary["overall"]["skip_container"], 1);
        assert_eq!(summary["overall"]["conflict"], 1);
        assert_eq!(summary["overall"]["build_failed"], 0);
        assert_eq!(canonical_map(&rows())[B], A);
    }

    #[test]
    fn status_changes() {
        let updates = BriefUpdates::default();
        let skip = status_change(None, "skip", Some("container"), "", &updates, "user");
        assert!(skip.changed);
        assert_eq!(skip.record.as_ref().unwrap().0, "primitive_skip");
        let current = StatusRow { uuid: A.into(), status: "skip".into(), reason: "container".into(), ..Default::default() };
        let same = status_change(Some(&current), "skip", Some("container"), "", &updates, "user");
        assert_eq!((same.changed, same.record.unwrap().0.as_str()), (false, "primitive_classification_confirmed"));
        let todo = status_change(Some(&current), "todo", None, "", &updates, "agent");
        assert_eq!(todo.write, Some(StatusWrite::Delete));
        assert_eq!(status_change(None, "todo", None, "", &updates, "agent").record, None);
    }

    #[test]
    fn briefs_encode_like_python() {
        let main = json!({"family": "container", "name": "Shield", "description": "A shield"});
        assert_eq!(encode_sorted(&main), r#"{"description": "A shield", "family": "container", "name": "Shield"}"#);
        let updates = brief_updates(&json!({"main_brief": main}), "skip", Some("container"), 1).unwrap();
        assert!(updates.main.is_some());
        assert!(brief_updates(&json!({"main_brief": main}), "skip", Some("other"), 1).is_err());
        assert!(brief_updates(&json!({"sub_position": "top"}), "skip", Some("container"), 1).is_err());
    }

    #[test]
    fn make_ray_prompt_pages_todo_rows() {
        let merged = merge(&rows(), &Map::new());
        let prompt = make_ray_prompt(&merged, "accessories", 4, 0);
        assert_eq!(prompt["count"], 1);
        assert_eq!(prompt["files"][0], "icon_set/work/todo-references/x_a.svg");
        assert!(prompt["prompt"].as_str().unwrap().starts_with("Run $primitive-make-ray draw each of these 1 reference files in order. (tp:accessories)"));
    }
}
