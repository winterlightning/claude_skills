//! Reviewer dashboard numbers, ported from reviewer_stats.py.
//! Each icon's current decision counts once, on the local day it was made, for whoever made it.

use crate::catalog::Catalog;
use crate::query::{first, Query};
use crate::reviews::{current_decisions, ActiveSplit, Decision, ReviewRow};
use crate::time::parse_time;
use chrono::{DateTime, Duration, NaiveDate, TimeZone, Utc};
use chrono_tz::Tz;
use serde_json::{json, Map, Value};
use std::collections::{BTreeMap, BTreeSet, HashSet};

fn outcome(status: &str) -> Option<&'static str> {
    match status {
        "approve" => Some("approved"),
        "pending" | "disapprove" | "claimed" => Some("disapproved"),
        "rejected" => Some("rejected"),
        _ => None,
    }
}

#[derive(Clone, Default)]
struct Counts {
    total: i64,
    approved: i64,
    disapproved: i64,
    rejected: i64,
    ready: i64,
}

impl Counts {
    fn add(&mut self, outcome: &str) {
        match outcome {
            "approved" => self.approved += 1,
            "disapproved" => self.disapproved += 1,
            "rejected" => self.rejected += 1,
            _ => self.ready += 1,
        }
        self.total += 1;
    }

    /// `blank_counts()` (with ready) or `empty_counts()` (without), in Python's key order.
    fn fields(&self, with_ready: bool) -> Map<String, Value> {
        let mut map = Map::new();
        map.insert("total".into(), json!(self.total));
        map.insert("approved".into(), json!(self.approved));
        map.insert("disapproved".into(), json!(self.disapproved));
        map.insert("rejected".into(), json!(self.rejected));
        if with_ready {
            map.insert("ready".into(), json!(self.ready));
        }
        map
    }
}

fn labelled(label: &str, name: &str, counts: &Counts, with_ready: bool) -> Value {
    let mut map = Map::new();
    map.insert(label.into(), json!(name));
    map.extend(counts.fields(with_ready));
    Value::Object(map)
}

fn family_of(catalog: &Catalog, key: &str) -> String {
    catalog.get(key).and_then(|icon| icon.family.clone()).filter(|f| !f.is_empty()).unwrap_or_else(|| "other".into())
}

/// reviewer_stats.py `current_status`.
pub fn current_status(catalog: &Catalog, reviewer: &str, decisions: &[(String, Decision)]) -> Value {
    let mut totals = Counts::default();
    let mut families: BTreeMap<String, Counts> = BTreeMap::new();
    let mut reviewers: BTreeMap<String, Counts> = BTreeMap::new();
    for (key, decision) in decisions {
        let result = outcome(&decision.status).unwrap_or("ready");
        let actor = match (&decision.actor, result) {
            (Some(actor), result) if result != "ready" && !actor.is_empty() => actor.clone(),
            _ => String::new(),
        };
        if !reviewer.is_empty() && actor != reviewer {
            continue;
        }
        totals.add(result);
        families.entry(family_of(catalog, key)).or_default().add(result);
        if !actor.is_empty() {
            reviewers.entry(actor).or_default().add(result);
        }
    }
    let mut ranked: Vec<_> = reviewers.into_iter().collect();
    ranked.sort_by(|a, b| b.1.total.cmp(&a.1.total).then(a.0.cmp(&b.0)));
    json!({
        "totals": Value::Object(totals.fields(true)),
        "families": families.iter().map(|(name, c)| labelled("family", name, c, true)).collect::<Vec<_>>(),
        "reviewers": ranked.iter().map(|(name, c)| labelled("reviewer", name, c, true)).collect::<Vec<_>>(),
    })
}

/// reviewer_stats.py `reviewer_stats`. Errors are the user-facing 400 messages.
pub fn reviewer_stats(rows: &[ReviewRow], splits: &[ActiveSplit], params: &Query, users: &[String],
                      catalog: &Catalog, now: DateTime<Utc>) -> Result<Value, String> {
    let zone_name = first(params, "timezone").unwrap_or("Asia/Ho_Chi_Minh").to_string();
    let zone: Tz = zone_name.parse().map_err(|_| "Choose a valid time zone.".to_string())?;
    let family = first(params, "family").unwrap_or("").to_string();
    if !family.is_empty() && !catalog.iter().any(|icon| icon.family.as_deref() == Some(family.as_str())) {
        return Err("Choose a known family.".into());
    }
    let catalog = catalog.filtered(|icon| family.is_empty() || icon.family.as_deref() == Some(family.as_str()));
    let decisions = current_decisions(rows, splits, &catalog);
    let mut decided: Vec<(NaiveDate, String, String, &'static str)> = Vec::new();
    for (key, decision) in &decisions {
        if let Some(result) = outcome(&decision.status) {
            if let Some(when) = decision.stamp.as_deref().and_then(parse_time) {
                let day = when.with_timezone(&zone).date_naive();
                decided.push((day, decision.actor.clone().unwrap_or_default(), key.clone(), result));
            }
        }
    }
    let today = now.with_timezone(&zone).date_naive();
    let first_day = decided.iter().map(|(day, ..)| *day).min().unwrap_or(today);
    let parse_day = |text: &str| NaiveDate::parse_from_str(text, "%Y-%m-%d").map_err(|_| "Choose valid start and end dates.".to_string());
    let end = match first(params, "end") { Some(text) => parse_day(text)?, None => today };
    let all = params.get("period").map(|v| v == &vec!["all".to_string()]).unwrap_or(false);
    let default_start = if all { first_day.min(end) } else { end - Duration::days(6) };
    let start = match first(params, "start") { Some(text) => parse_day(text)?, None => default_start };
    let span = (end - start).num_days();
    if !(0..366).contains(&span) || end == NaiveDate::MAX {
        return Err("Choose a date range between 1 and 366 days.".into());
    }
    let reviewer = first(params, "reviewer").unwrap_or("").to_string();
    let mut names: BTreeSet<String> = users.iter().cloned().collect();
    names.extend(decided.iter().filter(|(_, actor, ..)| !actor.is_empty()).map(|(_, actor, ..)| actor.clone()));
    let reviewers: Vec<String> = names.into_iter().collect();
    if !reviewer.is_empty() && !reviewers.contains(&reviewer) {
        return Err("Choose a known reviewer.".into());
    }
    let days: Vec<String> = (0..=span).map(|offset| (start + Duration::days(offset)).format("%Y-%m-%d").to_string()).collect();
    let day_set: HashSet<&str> = days.iter().map(String::as_str).collect();
    let listed: Vec<String> = reviewers.iter().filter(|user| reviewer.is_empty() || **user == reviewer).cloned().collect();
    let mut daily: BTreeMap<String, Counts> = BTreeMap::new();
    let mut by_reviewer: BTreeMap<String, Counts> = listed.iter().map(|u| (u.clone(), Counts::default())).collect();
    let mut reviewer_daily: BTreeMap<(String, String), Counts> = BTreeMap::new();
    let mut totals = Counts::default();
    let mut active: BTreeSet<(String, String)> = BTreeSet::new();
    let family_names: BTreeSet<String> = catalog.iter().map(|icon| family_of(&catalog, &icon.key)).collect();
    let mut families: BTreeMap<String, Counts> = family_names.iter().map(|f| (f.clone(), Counts::default())).collect();
    for (local_day, actor, key, result) in &decided {
        let day = local_day.format("%Y-%m-%d").to_string();
        if !day_set.contains(day.as_str()) || (!reviewer.is_empty() && *actor != reviewer) {
            continue;
        }
        totals.add(result);
        daily.entry(day.clone()).or_default().add(result);
        families.entry(family_of(&catalog, key)).or_default().add(result);
        if !actor.is_empty() {
            by_reviewer.entry(actor.clone()).or_default().add(result);
            reviewer_daily.entry((day.clone(), actor.clone())).or_default().add(result);
            active.insert((actor.clone(), day));
        }
    }
    let mut active_days: BTreeMap<String, i64> = BTreeMap::new();
    for (actor, _) in &active {
        *active_days.entry(actor.clone()).or_default() += 1;
    }
    let empty = Counts::default();
    let daily_rows: Vec<Value> = days.iter().map(|day| labelled("date", day, daily.get(day).unwrap_or(&empty), false)).collect();
    let mut reviewer_daily_rows = Vec::new();
    for day in &days {
        for user in &listed {
            let counts = reviewer_daily.get(&(day.clone(), user.clone())).unwrap_or(&empty);
            let mut map = Map::new();
            map.insert("date".into(), json!(day));
            map.insert("reviewer".into(), json!(user));
            map.extend(counts.fields(false));
            reviewer_daily_rows.push(Value::Object(map));
        }
    }
    let mut reviewer_rows: Vec<(String, Counts)> = listed.iter().map(|u| (u.clone(), by_reviewer[u].clone())).collect();
    reviewer_rows.sort_by(|a, b| b.1.total.cmp(&a.1.total).then(a.0.cmp(&b.0)));
    let reviewer_values: Vec<Value> = reviewer_rows.iter().map(|(name, counts)| {
        let mut map = Map::new();
        map.insert("reviewer".into(), json!(name));
        map.insert("active_days".into(), json!(active_days.get(name).copied().unwrap_or(0)));
        map.extend(counts.fields(false));
        Value::Object(map)
    }).collect();
    let history_since = if decided.is_empty() {
        Value::Null
    } else {
        let midnight = first_day.and_hms_opt(0, 0, 0).unwrap();
        match zone.from_local_datetime(&midnight).earliest() {
            Some(when) => json!(crate::time::iso(&when)),
            None => Value::Null,
        }
    };
    Ok(json!({
        "start": start.format("%Y-%m-%d").to_string(), "end": end.format("%Y-%m-%d").to_string(),
        "timezone": zone_name, "reviewer": reviewer, "family": family,
        "available_reviewers": reviewers, "totals": Value::Object(totals.fields(false)),
        "unique_icons": totals.total,
        "families": families.iter().map(|(name, c)| labelled("family", name, c, false)).collect::<Vec<_>>(),
        "daily": daily_rows, "reviewer_daily": reviewer_daily_rows, "reviewers": reviewer_values,
        "history_since": history_since,
        "current": current_status(&catalog, &reviewer, &decisions),
        "counting": "Each icon's current decision, on the day it was made, for the reviewer who made it.",
    }))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::catalog::Icon;
    use crate::query::parse_qs;

    fn fixture() -> (Catalog, Vec<ReviewRow>) {
        let icon = |key: &str, family: &str| Icon { key: key.into(), svg_sha256: "s".into(), family: Some(family.into()), ..Default::default() };
        let row = |key: &str, status: &str, by: &str, at: &str| ReviewRow {
            icon: key.into(), svg_sha256: "s".into(), status: status.into(),
            updated_by: Some(by.into()), updated_at: Some(at.into()), ..Default::default() };
        (Catalog::new(vec![icon("solo/a", "solo"), icon("sub/b", "sub"), icon("solo/c", "solo")], false),
         vec![row("solo/a", "approve", "ray", "2026-09-20T02:00:00+00:00"),
              row("sub/b", "pending", "hina", "2026-09-20T18:00:00+00:00")])
    }

    #[test]
    fn counts_on_local_day() {
        let (catalog, rows) = fixture();
        let now = Utc.with_ymd_and_hms(2026, 9, 21, 0, 0, 0).unwrap();
        let users = vec!["ray".to_string(), "hina".to_string()];
        let stats = reviewer_stats(&rows, &[], &parse_qs("start=2026-09-20&end=2026-09-21"), &users, &catalog, now).unwrap();
        // 18:00 UTC is already the 21st in Ho Chi Minh City (UTC+7).
        assert_eq!(stats["daily"][0]["approved"], 1);
        assert_eq!(stats["daily"][1]["disapproved"], 1);
        assert_eq!(stats["totals"]["total"], 2);
        assert_eq!(stats["current"]["totals"]["ready"], 1);
        assert_eq!(stats["reviewers"][0]["active_days"], 1);
        assert_eq!(stats["history_since"], "2026-09-20T00:00:00+07:00");
    }

    #[test]
    fn rejects_bad_parameters() {
        let (catalog, rows) = fixture();
        let now = Utc::now();
        assert!(reviewer_stats(&rows, &[], &parse_qs("timezone=Mars/Base"), &[], &catalog, now).is_err());
        assert!(reviewer_stats(&rows, &[], &parse_qs("family=nope"), &[], &catalog, now).is_err());
        assert!(reviewer_stats(&rows, &[], &parse_qs("start=2026-09-21&end=2026-09-20"), &[], &catalog, now).is_err());
        assert!(reviewer_stats(&rows, &[], &parse_qs("reviewer=ghost"), &[], &catalog, now).is_err());
    }
}
