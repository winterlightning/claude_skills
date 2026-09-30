//! Container symbol centers saved from the Container pairs page (migrations/0006_container_centers.sql),
//! with an optional symbol box width and height (0008; absent = the standard 32).
//! Defaults live in gallery/container-centers.json (combination_catalog.write_container_centers).

use crate::args;
use crate::db;
use crate::http::{self, Ctx};
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Map, Value};
use worker::{Response, Result};

/// GET /api/container-centers → {containers: {main: entry}, pairs: {main: {sub: entry}}}.
pub async fn list(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { main: String, sub: String, x: f64, y: f64, width: Option<f64>, height: Option<f64>, updated_at: String, updated_by: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT main, sub, x, y, width, height, updated_at, updated_by FROM container_centers", vec![]).await?;
    let (mut containers, mut pairs) = (Map::new(), Map::new());
    for r in rows {
        let mut entry = json!({"center": [r.x, r.y], "user": r.updated_by, "updated_at": r.updated_at});
        if r.width.is_some() || r.height.is_some() {
            entry["size"] = json!([r.width.unwrap_or(32.0), r.height.unwrap_or(32.0)]);
        }
        if r.sub.is_empty() {
            containers.insert(r.main, entry);
        } else if let Value::Object(subs) = pairs.entry(r.main).or_insert_with(|| json!({})) {
            subs.insert(r.sub, entry);
        }
    }
    http::json(200, &json!({"containers": containers, "pairs": pairs}))
}

/// POST /api/container-centers {main, sub?, center: [x, y] | null, size?: [width, height]}: save, or reset
/// when center is null. `size` is the symbol box (each side even, 8–64, so its edges sit on the grid); omitted means 32 × 32.
pub async fn save(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to save container centers.");
    }
    let valid_id = |id: &str| !id.is_empty() && id.len() <= 200 && id.chars().all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '_');
    let Some(main) = data["main"].as_str().filter(|m| valid_id(m)) else { return http::error(400, "Choose a container.") };
    let sub = data["sub"].as_str().unwrap_or("");
    if !sub.is_empty() && !valid_id(sub) {
        return http::error(400, "Choose a symbol.");
    }
    if data["center"].is_null() {
        db::run(&ctx.db, "DELETE FROM container_centers WHERE main = ? AND sub = ?", args![main, sub]).await?;
        return http::json(200, &json!({"main": main, "sub": sub, "center": null}));
    }
    let point: Option<Vec<f64>> = data["center"].as_array().map(|a| a.iter().filter_map(Value::as_f64).collect());
    let Some([x, y]) = point.as_deref().and_then(|p| <[f64; 2]>::try_from(p).ok()) else {
        return http::error(400, "Center must be [x, y].");
    };
    // Half-unit steps inside the 64x64 canvas.
    if ![x, y].iter().all(|v| (0.0..=64.0).contains(v) && (v * 2.0).fract() == 0.0) {
        return http::error(400, "Center values must be 0–64 in steps of 0.5.");
    }
    let (width, height) = match &data["size"] {
        Value::Null => (None, None),
        value => {
            let sides: Option<Vec<f64>> = value.as_array().map(|a| a.iter().filter_map(Value::as_f64).collect());
            match sides.as_deref().and_then(|s| <[f64; 2]>::try_from(s).ok()) {
                Some(sides) if sides.iter().all(|s| (8.0..=64.0).contains(s) && (s / 2.0).fract() == 0.0) => {
                    let standard = |s: f64| (s != 32.0).then_some(s);
                    (standard(sides[0]), standard(sides[1]))
                }
                _ => return http::error(400, "Symbol size must be [width, height], each an even number from 8 to 64."),
            }
        }
    };
    let now = iso_utc(chrono::Utc::now());
    db::run(&ctx.db, "INSERT INTO container_centers(main, sub, x, y, width, height, updated_at, updated_by) VALUES (?, ?, ?, ?, ?, ?, ?, ?) \
        ON CONFLICT(main, sub) DO UPDATE SET x = excluded.x, y = excluded.y, width = excluded.width, \
        height = excluded.height, updated_at = excluded.updated_at, updated_by = excluded.updated_by",
        args![main, sub, x, y, width, height, now.clone(), user]).await?;
    let mut saved = json!({"main": main, "sub": sub, "center": [x, y], "user": user, "updated_at": now});
    if width.is_some() || height.is_some() {
        saved["size"] = json!([width.unwrap_or(32.0), height.unwrap_or(32.0)]);
    }
    http::json(200, &saved)
}
