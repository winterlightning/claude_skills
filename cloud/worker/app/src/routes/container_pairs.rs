//! Container combination 64: a container pair's combined icon, made on the Container pairs page.
//!
//! * icon `container_combination64/<pair id>`: the container with its symbol placed at the pair's center and
//!   size, rendered by the graphics service (`/container/render`, container_combination_render.py) from both
//!   parts' current drawings. Its revision holds the SVG; it is listed in Icon review through `records`
//!   (icons.json only changes on a catalog push, and these rows are never part of one).
//! * Like a side combination, it fails its check (Failed check, cannot be approved) while its container or
//!   symbol is not approved; saving it again re-checks.

use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use sha2::{Digest, Sha256};
use worker::{Response, Result};

pub const FAMILY: &str = "container_combination64";
const PROFILE: &str = "CONTAINER_COMBINATION64";

macro_rules! try_response {
    ($value:expr) => {
        match $value {
            Ok(value) => value,
            Err(response) => return Ok(response),
        }
    };
}

fn valid_id(id: &str) -> bool {
    !id.is_empty() && id.len() <= 200 && id.chars().all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '_')
}

fn preview_url(key: &str, sha: &str) -> String {
    format!("../api/icon-artwork/svg?icon={}&variant=use_org&v={}", key.replace('/', "%2F"), &sha[..12.min(sha.len())])
}

/// Why a part is not approved, or None: approved in Icon review on its current drawing (uploads count),
/// and not a failed build unless a picked version replaced it.
async fn not_approved(ctx: &Ctx, key: &str) -> Result<Option<String>> {
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return Ok(Some("has no drawing".into())) };
    let status = data::detail(&ctx.db, key, &icon.svg_sha256).await?.status;
    if status != "approve" {
        let word = match status.as_str() {
            "pending" | "disapprove" => "disapproved", "claimed" => "being fixed", "rejected" => "rejected", _ => "not reviewed",
        };
        return Ok(Some(format!("not approved in Icon review ({word})")));
    }
    if icon.build_failed && !icon.uploaded && !super::edits::picked(ctx, &icon).await? {
        return Ok(Some("fails the build check".into()));
    }
    Ok(None)
}

async fn reasons(ctx: &Ctx, main: &str, symbol: &str) -> Result<Vec<String>> {
    let mut out = Vec::new();
    for (role, key) in [("Container", main), ("Symbol", symbol)] {
        if let Some(why) = not_approved(ctx, key).await? {
            out.push(format!("{role} {} {why}", key.split_once('/').map(|(_, id)| id).unwrap_or(key)));
        }
    }
    Ok(out)
}

/// POST /api/container-pairs/icon {pair_id, concept, main_key, symbol_key, center: [x, y], ink: [w, h] | null,
/// reference_url?}: (re)make the pair's combined icon from both parts' current drawings.
pub async fn save(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to combine container pairs.");
    }
    let Some(pair_id) = data["pair_id"].as_str().filter(|id| valid_id(id)) else { return http::error(400, "Choose a container pair.") };
    let (Some(main_key), Some(symbol_key)) = (data["main_key"].as_str(), data["symbol_key"].as_str()) else {
        return http::error(400, "The pair needs a container and a symbol.");
    };
    if !main_key.starts_with("container/") || !symbol_key.starts_with("symbol/") {
        return http::error(400, "Choose a container icon and a symbol icon.");
    }
    let Some((main_sha, main_svg)) = super::edits::current_drawing(ctx, main_key).await? else {
        return http::error(404, "The container has no drawing yet.");
    };
    let Some((symbol_sha, symbol_svg)) = super::edits::current_drawing(ctx, symbol_key).await? else {
        return http::error(404, "The symbol has no drawing yet.");
    };
    let body = json!({"main": main_svg, "symbol": symbol_svg, "center": data["center"], "ink": data["ink"]});
    let result = try_response!(super::edits::graphics(ctx, "/container/render", &body).await?);
    let svg = result["svg"].as_str().unwrap_or("").to_string();
    if svg.is_empty() {
        return http::error(502, "The graphics service returned no drawing.");
    }
    let sha = hex::encode(Sha256::digest(svg.as_bytes()));
    let key = format!("{FAMILY}/{pair_id}");
    let errors = reasons(ctx, main_key, symbol_key).await?;
    let now = iso_utc(chrono::Utc::now());
    let record = json!({"main_key": main_key, "symbol_key": symbol_key, "center": result["center"], "ink": result["ink"],
                        "drawings": {"main": main_sha, "symbol": symbol_sha}, "placements": result["placements"],
                        "errors": errors, "updated_at": now, "updated_by": user});
    let sources = data["reference_url"].as_str().map(|url| json!([{"url": url, "format": "SVG", "source_path": url}])).unwrap_or(json!([]));
    let concept = data["concept"].as_str().unwrap_or(pair_id);
    let mut statements = vec![
        db::stmt(&ctx.db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'container-combination', ?)",
                 args![sha.clone(), key.clone(), svg.clone(), now.clone()])?,
        db::stmt(&ctx.db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, \
            original_sources, build_failed, uploaded, record, pushed_at) VALUES (?, ?, ?, ?, 'Container', ?, 64, ?, ?, ?, ?, 0, ?, ?) \
            ON CONFLICT(key) DO UPDATE SET name = excluded.name, svg_sha256 = excluded.svg_sha256, preview_url = excluded.preview_url, \
            original_sources = CASE WHEN excluded.original_sources = '[]' THEN icons.original_sources ELSE excluded.original_sources END, \
            build_failed = excluded.build_failed, record = excluded.record WHERE icons.family = ?",
            args![key.clone(), pair_id, concept, FAMILY, PROFILE, sha.clone(), preview_url(&key, &sha), sources.to_string(),
                  !errors.is_empty(), record.to_string(), now.clone(), FAMILY])?,
        db::stmt(&ctx.db, "INSERT INTO activity_log(username, action, icon, details, created_at) VALUES (?, 'container_combination', ?, ?, ?)",
                 args![user, key.clone(), Value::Object(details(vec![("svg_sha256", json!(sha)), ("main", json!(main_key)),
                     ("symbol", json!(symbol_key)), ("center", result["center"].clone()), ("ink", result["ink"].clone())])).to_string(), now])?,
    ];
    // The drawing's stroke geometry (svg_graph.py), so the geometry editor can select the container and symbol strokes.
    if let Value::Object(mut graph) = result["graph"].clone() {
        graph.insert("key".into(), json!(key));
        // The validator wants a slug that starts with a letter; pair ids are UUIDs.
        graph.insert("icon_id".into(), json!(format!("pair-{pair_id}")));
        graph.insert("name".into(), json!(concept));
        graph.insert("svg_sha256".into(), json!(sha));
        graph.insert("python_source".into(), Value::Null);
        graph.insert("validation".into(), json!({"status": if errors.is_empty() { "pass" } else { "fail" }}));
        statements.push(db::stmt(&ctx.db, "INSERT OR REPLACE INTO icon_graphs(svg_sha256, icon, graph) VALUES (?, ?, ?)",
                                 args![sha.clone(), key.clone(), Value::Object(graph).to_string()])?);
    }
    db::batch(&ctx.db, statements).await?;
    http::json(200, &json!({"key": key, "svg_sha256": sha, "build_failed": !errors.is_empty(), "record": record,
                            "preview_url": preview_url(&key, &sha), "svg": svg, "placements": result["placements"]}))
}

#[derive(Deserialize)]
struct Row { key: String, icon_id: String, name: Option<String>, svg_sha256: String, build_failed: f64,
             original_sources: String, record: String, review: Option<String> }

async fn rows(ctx: &Ctx) -> Result<Vec<Row>> {
    db::all(&ctx.db, "SELECT i.key, i.icon_id, i.name, i.svg_sha256, i.build_failed, i.original_sources, i.record, \
        (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review \
        FROM icons i WHERE i.family = ? AND i.svg_sha256 != ''", args![FAMILY]).await
}

/// GET /api/container-pairs/icons → {pair id: {key, svg_sha256, build_failed, review, preview_url, record}}.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    let mut out = Map::new();
    for r in rows(ctx).await? {
        let record: Value = serde_json::from_str(&r.record).unwrap_or(json!({}));
        out.insert(r.icon_id.clone(), json!({"key": r.key, "svg_sha256": r.svg_sha256, "build_failed": r.build_failed != 0.0,
            "review": r.review, "preview_url": preview_url(&r.key, &r.svg_sha256), "record": record}));
    }
    http::json(200, &Value::Object(out))
}

/// GET /api/container-pairs/current?keys=k1,k2,… (at most 100): {key: {row, drawing}} — each part's catalog
/// revision (what a review names) and current drawing (its picked artwork, else the catalog drawing), so the page
/// can review a part and tell a combined icon built from an older drawing.
pub async fn current(ctx: &Ctx) -> Result<Response> {
    let keys: Vec<String> = ctx.param("keys").unwrap_or("").split(',').filter(|k| !k.is_empty()).map(str::to_string).collect();
    if keys.len() > 100 {
        return http::error(400, "Ask for at most 100 icons at a time.");
    }
    let mut out = Map::new();
    for key in keys {
        let Some(icon) = data::icon(&ctx.db, &key, true).await? else { continue };
        let drawing = super::edits::current_drawing(ctx, &key).await?.map(|(sha, _svg)| sha);
        // `row` is what a review names (reviews.rs compares it); `drawing` is what a combination is made from.
        out.insert(key, json!({"row": icon.svg_sha256, "drawing": drawing}));
    }
    http::json(200, &Value::Object(out))
}

/// Icon review records: complete records (`add`), since icons.json never lists these.
pub async fn records(ctx: &Ctx) -> Result<Vec<Value>> {
    Ok(rows(ctx).await?.into_iter().map(|r| {
        let record: Value = serde_json::from_str(&r.record).unwrap_or(json!({}));
        let errors = record["errors"].as_array().cloned().unwrap_or_default();
        json!({"add": true, "key": r.key, "icon_id": r.icon_id, "name": r.name, "family": FAMILY, "profile": PROFILE,
               "category": "Container", "canvas_size": 64, "svg_sha256": r.svg_sha256, "preview_url": preview_url(&r.key, &r.svg_sha256),
               "build_failed": r.build_failed != 0.0,
               "validation": {"status": if errors.is_empty() { "valid" } else { "invalid" }, "automatic_status": if errors.is_empty() { "pass" } else { "fail" },
                              "errors": errors},
               "original_sources": serde_json::from_str::<Value>(&r.original_sources).unwrap_or(json!([])),
               "main_key": record["main_key"], "sub_key": record["symbol_key"], "tags": [], "keywords": [], "aliases": [],
               "description": "", "created_at": record["updated_at"], "created_at_source": "container-pair"})
    }).collect())
}
