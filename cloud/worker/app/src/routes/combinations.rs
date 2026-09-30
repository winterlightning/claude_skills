//! Combinations from the one set of combination tables (migration 0009): a `"references"` row with
//! kind = 'combination', its `reference_parts` (role, the part's reference, the icon drawn for it,
//! position, layout boxes, the drawing it was last built from) and its combined icon
//! (`side_combination64/<reference_id>` or `container_combination64/<reference_id>`).
//!
//! A combination is `unbuilt` when no part records a build, `stale` when a part's icon has been redrawn
//! since (its `built_sha` is not the icon's current drawing), else `built`.

use crate::db::{self, Arg};
use crate::http::{self, Ctx};
use serde::Deserialize;
use serde_json::{json, Map, Value};
use std::collections::HashMap;
use worker::{Response, Result};

const DEFAULT_LIMIT: i64 = 100;
const MAX_LIMIT: i64 = 500;

/// One row per combination: its kind and build state, from its parts.
const COMBINATIONS: &str = "WITH parts AS (
    SELECT p.reference_id, p.role, p.built_sha, i.svg_sha256 AS current_sha
    FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon),
combos AS (
    SELECT r.reference_id, r.concept,
        CASE WHEN max(pt.role IN ('container', 'symbol')) THEN 'container' ELSE 'side' END AS kind,
        CASE WHEN count(pt.built_sha) = 0 THEN 'unbuilt'
             WHEN max(pt.built_sha IS NOT NULL AND pt.current_sha IS NOT NULL AND pt.built_sha != pt.current_sha) THEN 'stale'
             ELSE 'built' END AS state
    FROM \"references\" r JOIN parts pt ON pt.reference_id = r.reference_id
    WHERE r.kind = 'combination' GROUP BY r.reference_id)";

#[derive(Deserialize)]
struct Combo { reference_id: String, concept: Option<String>, kind: String, state: String,
               icon_sha: Option<String>, review: Option<String> }

#[derive(Deserialize)]
struct Part { reference_id: String, role: String, part_reference_id: String, position: Option<String>,
              icon: Option<String>, layout: Option<String>, built_sha: Option<String>, current_sha: Option<String>,
              review: Option<String>, updated_at: Option<String>, updated_by: Option<String> }

#[derive(Deserialize)]
struct Count { kind: String, state: String, n: f64 }

fn preview_url(key: &str, sha: &str) -> String {
    format!("/api/icon-artwork/svg?icon={}&v={}", http::percent_encode(key), &sha[..12.min(sha.len())])
}

/// GET /api/combinations?kind=side|container&state=built|stale|unbuilt&q=&offset=&limit= →
/// {total, offset, next_offset, counts: {kind: {state: n}}, items: [{reference_id, concept, kind, state, icon, parts}]}.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    let kind = ctx.param("kind").filter(|k| !k.is_empty());
    let state = ctx.param("state").filter(|s| !s.is_empty());
    let needle = ctx.param("q").map(str::trim).filter(|q| !q.is_empty());
    if kind.is_some_and(|k| !matches!(k, "side" | "container")) {
        return http::error(400, "kind must be side or container.");
    }
    if state.is_some_and(|s| !matches!(s, "built" | "stale" | "unbuilt")) {
        return http::error(400, "state must be built, stale or unbuilt.");
    }
    let number = |name: &str, default: i64| ctx.param(name).map(|v| v.parse::<i64>().ok()).unwrap_or(Some(default));
    let (Some(offset), Some(limit)) = (number("offset", 0), number("limit", DEFAULT_LIMIT)) else {
        return http::error(400, "offset and limit must be integers.");
    };
    if offset < 0 || !(1..=MAX_LIMIT).contains(&limit) {
        return http::error(400, &format!("offset must be 0 or more and limit from 1 to {MAX_LIMIT}."));
    }

    let mut filters = Vec::new();
    let mut values: Vec<Arg> = Vec::new();
    if let Some(kind) = kind {
        filters.push("c.kind = ?");
        values.push(kind.into());
    }
    if let Some(state) = state {
        filters.push("c.state = ?");
        values.push(state.into());
    }
    if let Some(needle) = needle {
        filters.push("(c.concept LIKE ? OR c.reference_id LIKE ?)");
        values.push(format!("%{needle}%").into());
        values.push(format!("{needle}%").into());
    }
    let filter = if filters.is_empty() { String::new() } else { format!("WHERE {}", filters.join(" AND ")) };

    // Page one extra row to know whether there is a next page without counting.
    let mut page_values = values.clone();
    page_values.push((limit + 1).into());
    page_values.push(offset.into());
    let mut combos: Vec<Combo> = db::all(&ctx.db, &format!("{COMBINATIONS}
        SELECT c.reference_id, c.concept, c.kind, c.state, i.svg_sha256 AS icon_sha,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM combos c LEFT JOIN icons i ON i.key = c.kind || '_combination64/' || c.reference_id
        {filter} ORDER BY c.reference_id LIMIT ? OFFSET ?"), page_values).await?;
    let next = (combos.len() as i64 > limit).then(|| offset + limit);
    combos.truncate(limit as usize);

    let counts: Vec<Count> = db::all(&ctx.db, &format!("{COMBINATIONS} SELECT kind, state, count(*) AS n FROM combos GROUP BY 1, 2"),
                                     vec![]).await?;
    let mut by_kind: Map<String, Value> = Map::new();
    for c in &counts {
        let entry = by_kind.entry(c.kind.clone()).or_insert_with(|| json!({"built": 0, "stale": 0, "unbuilt": 0}));
        entry[c.state.as_str()] = json!(c.n as u64);
    }
    let total: u64 = if needle.is_some() {
        #[derive(Deserialize)]
        struct Total { n: f64 }
        db::first::<Total>(&ctx.db, &format!("{COMBINATIONS} SELECT count(*) AS n FROM combos c {filter}"), values).await?
            .map_or(0, |t| t.n as u64)
    } else {
        counts.iter().filter(|c| kind.is_none_or(|k| k == c.kind) && state.is_none_or(|s| s == c.state)).map(|c| c.n as u64).sum()
    };

    // One JSON parameter for the ids: D1 allows 100 bound parameters per query.
    let ids = json!(combos.iter().map(|c| c.reference_id.as_str()).collect::<Vec<_>>()).to_string();
    let parts: Vec<Part> = db::all(&ctx.db, "SELECT p.reference_id, p.role, p.part_reference_id, p.position, p.icon, p.layout,
            p.built_sha, i.svg_sha256 AS current_sha, p.updated_at, p.updated_by,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon
        WHERE p.reference_id IN (SELECT value FROM json_each(?)) ORDER BY p.reference_id, p.role", vec![ids.into()]).await?;
    let mut parts_of: HashMap<String, Vec<Value>> = HashMap::new();
    for p in parts {
        let layout = p.layout.as_deref().and_then(|l| serde_json::from_str::<Value>(l).ok()).unwrap_or(Value::Null);
        let stale = matches!((&p.built_sha, &p.current_sha), (Some(built), Some(current)) if built != current);
        parts_of.entry(p.reference_id).or_default().push(json!({
            "role": p.role, "part_reference_id": p.part_reference_id, "position": p.position, "icon": p.icon,
            "layout": layout, "built_sha": p.built_sha, "current_sha": p.current_sha, "stale": stale,
            "review": p.review, "updated_at": p.updated_at, "updated_by": p.updated_by,
        }));
    }
    let items: Vec<Value> = combos.into_iter().map(|c| {
        let key = format!("{}_combination64/{}", c.kind, c.reference_id);
        let icon = c.icon_sha.as_deref().filter(|s| !s.is_empty())
            .map(|sha| json!({"key": key, "svg_sha256": sha, "review": c.review, "preview_url": preview_url(&key, sha)}))
            .unwrap_or(Value::Null);
        let parts = parts_of.remove(&c.reference_id).unwrap_or_default();
        json!({"reference_id": c.reference_id, "concept": c.concept, "kind": c.kind, "state": c.state,
               "icon": icon, "parts": parts})
    }).collect();
    http::json(200, &json!({"total": total, "offset": offset, "next_offset": next, "counts": by_kind, "items": items}))
}
