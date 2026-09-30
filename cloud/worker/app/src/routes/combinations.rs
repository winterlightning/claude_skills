//! Combinations from the one set of combination tables (migration 0009): a `"references"` row with
//! kind = 'combination', its `reference_parts` (role, the part's reference, the icon drawn for it,
//! position, layout boxes, the drawing it was last built from) and its combined icon
//! (`side_combination64/<reference_id>` or `container_combination64/<reference_id>`).
//!
//! A combination is `unbuilt` when no part records a build, `stale` when a part's icon has been redrawn
//! since (its `built_sha` is not the icon's current drawing), else `built`.

use crate::args;
use crate::db::{self, Arg};
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use sha2::{Digest, Sha256};
use std::collections::HashMap;
use worker::{Response, Result};

const DEFAULT_LIMIT: i64 = 100;
const SIDE_POSITIONS: [&str; 8] = ["tl", "tr", "bl", "br", "ri", "le", "bo", "to"];
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
              review: Option<String>, updated_at: Option<String>, updated_by: Option<String>, form: Option<String> }

#[derive(Deserialize)]
struct Count { kind: String, state: String, n: f64 }

fn preview_url(key: &str, sha: &str) -> String {
    format!("/api/icon-artwork/svg?icon={}&v={}", http::percent_encode(key), &sha[..12.min(sha.len())])
}

/// GET /api/combinations?kind=side|container&state=built|stale|unbuilt&q=&offset=&limit=&forms=1 →
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
    // `forms=1` adds what the side engine combines for each part (the page builds from it).
    let forms = ctx.param("forms") == Some("1");
    let parts: Vec<Part> = db::all(&ctx.db, "SELECT p.reference_id, p.role, p.part_reference_id, p.position, p.icon, p.layout,
            p.built_sha, i.svg_sha256 AS current_sha, p.updated_at, p.updated_by, CASE WHEN ? THEN p.form END AS form,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon
        WHERE p.reference_id IN (SELECT value FROM json_each(?)) ORDER BY p.reference_id, p.role", vec![forms.into(), ids.into()]).await?;
    let mut parts_of: HashMap<String, Vec<Value>> = HashMap::new();
    for p in parts {
        let layout = p.layout.as_deref().and_then(|l| serde_json::from_str::<Value>(l).ok()).unwrap_or(Value::Null);
        let stale = matches!((&p.built_sha, &p.current_sha), (Some(built), Some(current)) if built != current);
        let mut part = json!({
            "role": p.role, "part_reference_id": p.part_reference_id, "position": p.position, "icon": p.icon,
            "layout": layout, "built_sha": p.built_sha, "current_sha": p.current_sha, "stale": stale,
            "review": p.review, "updated_at": p.updated_at, "updated_by": p.updated_by,
        });
        if forms {
            part["form"] = p.form.as_deref().and_then(|f| serde_json::from_str::<Value>(f).ok()).unwrap_or(Value::Null);
        }
        parts_of.entry(p.reference_id).or_default().push(part);
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

// ---- the parts' drawings, picks and builds: the browser composes (combine.js), the Worker checks and stores

const MAX_KEYS: usize = 100;
const MAX_BUILDS: usize = 50;

/// The families an icon for each part may come from.
fn fits_role(role: &str, key: &str) -> bool {
    let family = key.split_once('/').map_or("", |(family, _)| family);
    match role {
        "container" => family == "container",
        "symbol" => family == "symbol",
        "main" => matches!(family, "solo" | "combination_main"),
        "sub" => family == "sub",
        _ => false,
    }
}

fn kind_of(roles: &[String]) -> &'static str {
    if roles.iter().any(|r| r == "container" || r == "symbol") { "container" } else { "side" }
}

/// Layout boxes as reference_parts stores them: a list of {x, y, w, h} (and `paths` for a group), numbers on the grid.
fn layout_ok(layout: &Value) -> bool {
    let number = |v: &Value| v.as_f64().is_some_and(|n| n.is_finite() && (-64.0..=128.0).contains(&n));
    layout.is_null() || layout.as_array().is_some_and(|boxes| !boxes.is_empty() && boxes.len() <= 64 && boxes.iter().all(|b| {
        ["x", "y", "w", "h"].iter().all(|k| number(&b[*k]))
            && (b["paths"].is_null() || b["paths"].as_array().is_some_and(|p| p.iter().all(|i| i.as_u64().is_some())))
    }))
}

#[derive(Deserialize)]
struct Drawing { key: String, svg_sha256: String, svg: Option<String>, review: Option<String> }

/// The current drawing, sha and review status of each icon key (one query).
async fn drawings_of(ctx: &Ctx, keys: &[String]) -> Result<HashMap<String, Drawing>> {
    let rows: Vec<Drawing> = db::all(&ctx.db, "SELECT i.key, i.svg_sha256,
            CASE WHEN i.uploaded THEN (SELECT svg FROM uploaded_icons u WHERE u.icon = i.key)
                 ELSE (SELECT svg FROM revisions r WHERE r.svg_sha256 = i.svg_sha256) END AS svg,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM icons i WHERE i.key IN (SELECT value FROM json_each(?))", vec![json!(keys).to_string().into()]).await?;
    Ok(rows.into_iter().map(|d| (d.key.clone(), d)).collect())
}

/// GET /api/combinations/drawings?keys=k1,k2 (at most 100) → {key: {svg_sha256, svg, review}}: what combine.js builds from.
pub async fn drawings(ctx: &Ctx) -> Result<Response> {
    let keys: Vec<String> = ctx.param("keys").unwrap_or("").split(',').filter(|k| !k.is_empty()).map(str::to_string).collect();
    if keys.is_empty() || keys.len() > MAX_KEYS {
        return http::error(400, &format!("Ask for 1 to {MAX_KEYS} icon keys."));
    }
    let found = drawings_of(ctx, &keys).await?;
    let out: Map<String, Value> = found.into_values()
        .map(|d| (d.key, json!({"svg_sha256": d.svg_sha256, "svg": d.svg, "review": d.review}))).collect();
    http::json(200, &Value::Object(out))
}

#[derive(Deserialize)]
struct RefPart { reference_id: String, role: String, icon: Option<String> }

/// The parts (role, current icon) of each combination reference among `ids` (one query).
async fn roles_of(ctx: &Ctx, ids: &[&str]) -> Result<HashMap<String, Vec<(String, Option<String>)>>> {
    let rows: Vec<RefPart> = db::all(&ctx.db, "SELECT p.reference_id, p.role, p.icon FROM reference_parts p
        JOIN \"references\" r ON r.reference_id = p.reference_id AND r.kind = 'combination'
        WHERE p.reference_id IN (SELECT value FROM json_each(?))", vec![json!(ids).to_string().into()]).await?;
    let mut roles: HashMap<String, Vec<(String, Option<String>)>> = HashMap::new();
    for row in rows {
        roles.entry(row.reference_id).or_default().push((row.role, row.icon));
    }
    Ok(roles)
}

/// The square canvas of a combined drawing: 64, or larger for a native text side pair.
fn canvas_of(svg: &str) -> Option<i64> {
    let start = svg.find("<svg")?;
    let head = &svg[start..start + svg[start..].find('>')?];
    let view = head.split("viewBox=\"").nth(1)?.split('"').next()?;
    let n: Vec<f64> = view.split(|c: char| c == ' ' || c == ',').filter(|v| !v.is_empty()).filter_map(|v| v.parse().ok()).collect();
    (n.len() == 4 && n[0] == 0.0 && n[1] == 0.0 && n[2] == n[3] && n[2].fract() == 0.0 && (64.0..=256.0).contains(&n[2]))
        .then(|| n[2] as i64)
}

/// POST /api/combinations/parts {reference_id, role, icon?, layout?}: pick the icon drawn for a part and/or
/// its boxes, without building. The combination shows as stale until it is built again.
pub async fn post_part(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to change combinations.");
    }
    let (Some(id), Some(role)) = (data["reference_id"].as_str(), data["role"].as_str()) else {
        return http::error(400, "reference_id and role are required.");
    };
    if !roles_of(ctx, &[id]).await?.get(id).is_some_and(|roles| roles.iter().any(|(r, _)| r == role)) {
        return http::error(404, "That combination has no such part.");
    }
    let icon = data.get("icon").filter(|v| !v.is_null());
    let layout = data.get("layout");
    if icon.is_none() && layout.is_none() {
        return http::error(400, "Send an icon, a layout or both.");
    }
    if let Some(icon) = icon {
        let Some(key) = icon.as_str().filter(|k| fits_role(role, k)) else {
            return http::error(400, &format!("The {role} must be an icon of its family."));
        };
        if !drawings_of(ctx, &[key.to_string()]).await?.contains_key(key) {
            return http::error(404, "No icon with that key.");
        }
    }
    if layout.is_some_and(|l| !layout_ok(l)) {
        return http::error(400, "layout must be null or a list of {x, y, w, h} boxes on the grid.");
    }
    let now = iso_utc(chrono::Utc::now());
    let mut sets = vec!["updated_at = ?", "updated_by = ?"];
    let mut values: Vec<Arg> = vec![now.clone().into(), user.into()];
    if let Some(icon) = icon {
        sets.push("icon = ?");
        values.push(icon.as_str().into());
    }
    if let Some(layout) = layout {
        sets.push("layout = ?");
        values.push(if layout.is_null() { Arg::Null } else { layout.to_string().into() });
    }
    values.push(id.into());
    values.push(role.into());
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, &format!("UPDATE reference_parts SET {} WHERE reference_id = ? AND role = ?", sets.join(", ")), values)?,
        db::activity(&ctx.db, user, "combination_part", Some(id), db::details(vec![
            ("role", json!(role)), ("icon", icon.cloned().unwrap_or(Value::Null)), ("layout", layout.cloned().unwrap_or(Value::Null))]))?,
    ]).await?;
    http::json(200, &json!({"reference_id": id, "role": role, "updated_at": now}))
}

/// POST /api/combinations/build {builds: [{reference_id, svg, parts: {role: {icon, svg_sha256, layout, position?}}}]} (at most 50):
/// store combinations the browser built. Each is checked (its parts are that combination's, each part's
/// drawing is still the icon's current one, the SVG is a clean 64x64 drawing) and stored as the combined
/// icon's new drawing, with every part's icon, boxes and built drawing. A part not approved in Icon review
/// makes the combined icon fail its check (it cannot be approved until the parts are).
/// → {results: [{reference_id, ok, key, svg_sha256, build_failed, errors} | {reference_id, ok: false, error}]}
pub async fn build(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to build combinations.");
    }
    let Some(builds) = data["builds"].as_array().filter(|b| !b.is_empty() && b.len() <= MAX_BUILDS) else {
        return http::error(400, &format!("Send 1 to {MAX_BUILDS} builds."));
    };
    let ids: Vec<&str> = builds.iter().filter_map(|b| b["reference_id"].as_str()).collect();
    let roles = roles_of(ctx, &ids).await?;
    let keys: Vec<String> = builds.iter().filter_map(|b| b["parts"].as_object())
        .flat_map(|parts| parts.values().filter_map(|p| p["icon"].as_str().map(str::to_string))).collect();
    let current = if keys.is_empty() { HashMap::new() } else { drawings_of(ctx, &keys).await? };
    let now = iso_utc(chrono::Utc::now());
    let mut statements = Vec::new();
    let mut results = Vec::new();
    for b in builds {
        let id = b["reference_id"].as_str().unwrap_or("");
        let failed = |error: String| json!({"reference_id": id, "ok": false, "error": error});
        let Some(own) = roles.get(id) else { results.push(failed("Not a combination.".into())); continue };
        let names: Vec<&str> = own.iter().map(|(r, _)| r.as_str()).collect();
        let Some(parts) = b["parts"].as_object().filter(|p| p.len() == own.len() && names.iter().all(|r| p.contains_key(*r))) else {
            results.push(failed(format!("Send every part: {}.", names.join(", "))));
            continue;
        };
        let mut problem = None;
        let mut errors = Vec::new();
        for (role, part) in parts {
            // A native text sub is drawn from the typeface: no icon, nothing to have been redrawn.
            let textual = part["icon"].is_null() && own.iter().any(|(r, icon)| r == role && icon.is_none());
            if textual {
                continue;
            }
            let icon = part["icon"].as_str().unwrap_or("");
            let Some(drawing) = current.get(icon).filter(|_| fits_role(role, icon)) else {
                problem = Some(format!("The {role} must be an existing icon of its family."));
                break;
            };
            if part["svg_sha256"].as_str() != Some(drawing.svg_sha256.as_str()) {
                problem = Some(format!("The {role} {icon} was redrawn since it was loaded. Reload and build again."));
                break;
            }
            if !layout_ok(&part["layout"]) {
                problem = Some(format!("The {role} layout must be a list of {{x, y, w, h}} boxes."));
                break;
            }
            if !part["position"].is_null() && !(role == "sub" && part["position"].as_str().is_some_and(|p| SIDE_POSITIONS.contains(&p))) {
                problem = Some("A side sub's position is one of tl, tr, bl, br, ri, le, bo, to.".into());
                break;
            }
            if drawing.review.as_deref() != Some("approve") {
                let name = icon.split_once('/').map_or(icon, |(_, n)| n);
                errors.push(format!("{} {name} is not approved in Icon review", capitalize(role)));
            }
        }
        if let Some(problem) = problem {
            results.push(failed(problem));
            continue;
        }
        let kind = kind_of(&own.iter().map(|(r, _)| r.clone()).collect::<Vec<_>>());
        // Checked by the sanitizer (which refuses anything outside its allowlist) and stored as the browser
        // made it, so a pair rebuilt from unchanged parts keeps its drawing's sha.
        let svg = b["svg"].as_str().unwrap_or("").to_string();
        let Some(canvas) = canvas_of(&svg).filter(|c| kind == "side" || *c == 64) else {
            results.push(failed("The combined drawing needs a square viewBox from 0 0 (64 × 64, or larger for native text).".into()));
            continue;
        };
        if let Err(error) = pictographic_core::svg::safe_svg(&svg, canvas) {
            results.push(failed(error));
            continue;
        }
        let sha = hex::encode(Sha256::digest(svg.as_bytes()));
        let key = format!("{kind}_combination64/{id}");
        let (profile, category) = if kind == "container" { ("CONTAINER_COMBINATION64", "Container") } else { ("SIDE_COMBINATION64", "Side") };
        let record = json!({"parts": parts.iter().map(|(role, p)| (role.clone(), p["icon"].clone())).collect::<Map<_, _>>(),
                            "errors": errors, "built_by": user, "built_at": now});
        statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) \
            VALUES (?, ?, ?, 'combination-build', ?)", args![sha.clone(), key.clone(), svg, now.clone()])?);
        statements.push(db::stmt(&ctx.db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, \
            preview_url, build_failed, uploaded, record, pushed_at) \
            VALUES (?, ?, (SELECT concept FROM \"references\" WHERE reference_id = ?), ?, ?, ?, ?, ?, ?, ?, 0, ?, ?) \
            ON CONFLICT(key) DO UPDATE SET svg_sha256 = excluded.svg_sha256, preview_url = excluded.preview_url, \
            canvas_size = excluded.canvas_size, build_failed = excluded.build_failed, record = excluded.record WHERE icons.uploaded = 0",
            args![key.clone(), id, id, format!("{kind}_combination64"), category, profile, canvas, sha.clone(), preview_url(&key, &sha),
                  !errors.is_empty(), record.to_string(), now.clone()])?);
        statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO icon_references(icon, reference_id) VALUES (?, ?)",
                                 args![key.clone(), id])?);
        for (role, part) in parts {
            let layout = if part["layout"].is_null() { Arg::Null } else { part["layout"].to_string().into() };
            statements.push(db::stmt(&ctx.db, "UPDATE reference_parts SET icon = ?, layout = ?, built_sha = ?, \
                position = COALESCE(?, position), updated_at = ?, updated_by = ? WHERE reference_id = ? AND role = ?",
                args![part["icon"].as_str(), layout, part["svg_sha256"].as_str(), part["position"].as_str(), now.clone(), user, id,
                      role.as_str()])?);
        }
        statements.push(db::activity(&ctx.db, user, "combination_build", Some(&key), db::details(vec![
            ("svg_sha256", json!(sha)), ("errors", json!(errors))]))?);
        results.push(json!({"reference_id": id, "ok": true, "key": key, "svg_sha256": sha, "build_failed": !errors.is_empty(),
                            "errors": errors, "preview_url": preview_url(&key, &sha)}));
    }
    if !statements.is_empty() {
        db::batch(&ctx.db, statements).await?;
    }
    http::json(200, &json!({"results": results}))
}

fn capitalize(text: &str) -> String {
    let mut chars = text.chars();
    chars.next().map(|c| c.to_uppercase().collect::<String>() + chars.as_str()).unwrap_or_default()
}

#[derive(Deserialize)]
struct Candidate { key: String, name: Option<String>, svg_sha256: String, review: Option<String> }

/// GET /api/combinations/candidates?role=container|symbol|main|sub&q= → [{key, name, svg_sha256, review}]:
/// icons that can be picked for a part (at most 40, approved first).
pub async fn candidates(ctx: &Ctx) -> Result<Response> {
    let role = ctx.param("role").unwrap_or("");
    let families: &[&str] = match role {
        "container" => &["container"], "symbol" => &["symbol"], "main" => &["solo", "combination_main"], "sub" => &["sub"],
        _ => return http::error(400, "role must be container, symbol, main or sub."),
    };
    let words: Vec<String> = ctx.param("q").unwrap_or("").to_lowercase().split(|c: char| !c.is_ascii_alphanumeric())
        .filter(|w| w.len() >= 2).take(6).map(str::to_string).collect();
    let mut values: Vec<Arg> = vec![json!(families).to_string().into()];
    let mut filter = String::new();
    for word in &words {
        filter.push_str(" AND (lower(i.key) LIKE ? OR lower(COALESCE(i.name, '')) LIKE ?)");
        values.push(format!("%{word}%").into());
        values.push(format!("%{word}%").into());
    }
    let rows: Vec<Candidate> = db::all(&ctx.db, &format!("SELECT i.key, i.name, i.svg_sha256,
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM icons i WHERE i.family IN (SELECT value FROM json_each(?)) AND i.svg_sha256 != ''{filter}
        ORDER BY (review = 'approve') DESC, length(i.key), i.key LIMIT 40"), values).await?;
    http::json(200, &json!(rows.into_iter().map(|c| json!({"key": c.key, "name": c.name, "svg_sha256": c.svg_sha256,
        "review": c.review, "preview_url": preview_url(&c.key, &c.svg_sha256)})).collect::<Vec<_>>()))
}

/// The parts of a combination not approved in Icon review on their current drawing, as "container x and
/// symbol y", or None when every part is approved.
pub async fn unapproved_parts(db: &worker::D1Database, reference_id: &str) -> Result<Option<String>> {
    #[derive(Deserialize)]
    struct Waiting { role: String, icon: Option<String> }
    let rows: Vec<Waiting> = db::all(db, "SELECT p.role, p.icon FROM reference_parts p LEFT JOIN icons i ON i.key = p.icon
        WHERE p.reference_id = ? AND COALESCE((SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256), '') != 'approve'
        ORDER BY p.role", args![reference_id]).await?;
    Ok((!rows.is_empty()).then(|| rows.iter().map(|w| format!("the {} {}", w.role,
        w.icon.as_deref().map_or("(none picked)", |k| k.split_once('/').map_or(k, |(_, n)| n)))).collect::<Vec<_>>().join(" and ")))
}

/// Icon review records for combined icons built in the browser: complete records (`add`, merged into icons.json's
/// record when it has one), since a catalog push never carries them.
pub async fn records(ctx: &Ctx) -> Result<Vec<Value>> {
    #[derive(Deserialize)]
    struct Row { key: String, icon_id: String, name: Option<String>, family: String, category: Option<String>, canvas_size: Option<f64>,
                 svg_sha256: String, build_failed: f64, original_sources: String, record: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT i.key, i.icon_id, i.name, i.family, i.category, i.canvas_size, i.svg_sha256,
            i.build_failed, i.original_sources, i.record
        FROM icons i JOIN revisions r ON r.svg_sha256 = i.svg_sha256 AND r.origin = 'combination-build'
        WHERE i.family IN ('side_combination64', 'container_combination64')", vec![]).await?;
    Ok(rows.into_iter().map(|r| {
        let record: Value = serde_json::from_str(&r.record).unwrap_or(json!({}));
        let errors = record["errors"].as_array().cloned().unwrap_or_default();
        let container = r.family == "container_combination64";
        let (main, sub) = if container { ("container", "symbol") } else { ("main", "sub") };
        json!({"add": true, "key": r.key, "icon_id": r.icon_id, "name": r.name, "family": r.family,
               "profile": if container { "CONTAINER_COMBINATION64" } else { "SIDE_COMBINATION64" },
               "category": r.category, "canvas_size": r.canvas_size.unwrap_or(64.0), "svg_sha256": r.svg_sha256,
               "preview_url": preview_url(&r.key, &r.svg_sha256), "build_failed": r.build_failed != 0.0,
               "validation": {"status": if errors.is_empty() { "valid" } else { "invalid" },
                              "automatic_status": if errors.is_empty() { "pass" } else { "fail" }, "errors": errors},
               "original_sources": serde_json::from_str::<Value>(&r.original_sources).unwrap_or(json!([])),
               "main_key": record["parts"][main], "sub_key": record["parts"][sub], "created_at": record["built_at"],
               "created_at_source": if container { "container-pair" } else { "side-pair" }})
    }).collect())
}

/// `gallery/combination-previews/<id>.svg`: a side pair's drawing once it was built in the browser (the published
/// file is the catalog build's). None: serve the published file.
pub async fn built_preview(ctx: &Ctx, reference_id: &str) -> Result<Option<Response>> {
    #[derive(Deserialize)]
    struct Row { svg: String, svg_sha256: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT r.svg, r.svg_sha256 FROM icons i
        JOIN revisions r ON r.svg_sha256 = i.svg_sha256 AND r.origin = 'combination-build' WHERE i.key = ?",
        args![format!("side_combination64/{reference_id}")]).await?;
    let Some(row) = row else { return Ok(None) };
    let etag = format!("\"{}\"", row.svg_sha256);
    let headers = worker::Headers::new();
    headers.set("Content-Type", "image/svg+xml")?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; sandbox")?;
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").as_deref() == Some(etag.as_str()) {
        return Ok(Some(Response::empty()?.with_status(304).with_headers(headers)));
    }
    Ok(Some(Response::from_bytes(row.svg.into_bytes())?.with_headers(headers)))
}

/// POST /api/combinations/pair {reference_id, position, remove?}: make a side pair of a reference (a primitive
/// classified as a combination): the reference becomes a combination with a main and a sub part, the icons
/// picked afterwards on the side page (POST /api/combinations/parts, /build). `remove: true` undoes it for a
/// pair made this way: its parts and combined icon go, and the reference is a single again.
pub async fn post_pair(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to make side pairs.");
    }
    let Some(id) = data["reference_id"].as_str().filter(|id| !id.is_empty()) else { return http::error(400, "reference_id is required.") };
    #[derive(Deserialize)]
    struct Reference { kind: String }
    let Some(reference) = db::first::<Reference>(&ctx.db, "SELECT kind FROM \"references\" WHERE reference_id = ?", args![id]).await? else {
        return http::error(404, "No reference with that id.");
    };
    let roles = roles_of(ctx, &[id]).await?.remove(id).unwrap_or_default();
    let now = iso_utc(chrono::Utc::now());
    if data["remove"] == json!(true) {
        if roles.iter().any(|(r, _)| r == "container" || r == "symbol") {
            return http::error(409, "Only a side pair made from a reference can be removed.");
        }
        db::batch(&ctx.db, vec![
            db::stmt(&ctx.db, "DELETE FROM reference_parts WHERE reference_id = ? AND role IN ('main', 'sub')", args![id])?,
            db::stmt(&ctx.db, "DELETE FROM icons WHERE key = ? AND uploaded = 0", args![format!("side_combination64/{id}")])?,
            db::stmt(&ctx.db, "DELETE FROM icon_references WHERE icon = ?", args![format!("side_combination64/{id}")])?,
            db::stmt(&ctx.db, "UPDATE \"references\" SET kind = 'single' WHERE reference_id = ?", args![id])?,
            db::activity(&ctx.db, user, "side_pair_removed", Some(id), db::details(vec![]))?,
        ]).await?;
        return http::json(200, &json!({"reference_id": id, "removed": true}));
    }
    let position = data["position"].as_str().unwrap_or("br");
    if !SIDE_POSITIONS.contains(&position) {
        return http::error(400, "position is one of tl, tr, bl, br, ri, le, bo, to.");
    }
    if roles.iter().any(|(r, _)| r == "container" || r == "symbol") {
        return http::error(409, "This reference is a container combination.");
    }
    if reference.kind == "combination" && roles.len() == 2 {
        return http::json(200, &json!({"reference_id": id, "created": false}));
    }
    // A part to draw is a placeholder reference until an icon is picked for it.
    let mut statements = vec![db::stmt(&ctx.db, "UPDATE \"references\" SET kind = 'combination' WHERE reference_id = ?", args![id])?];
    for role in ["main", "sub"] {
        statements.push(db::stmt(&ctx.db, "INSERT OR IGNORE INTO reference_parts(reference_id, role, part_reference_id, position, updated_at, updated_by) \
            VALUES (?, ?, ?, ?, ?, ?)", args![id, role, format!("draw:{id}:{role}"), (role == "sub").then_some(position), now.clone(), user])?);
    }
    statements.push(db::activity(&ctx.db, user, "side_pair_created", Some(id), db::details(vec![("position", json!(position))]))?);
    db::batch(&ctx.db, statements).await?;
    http::json(200, &json!({"reference_id": id, "created": true}))
}
