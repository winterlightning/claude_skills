//! Icon metadata routes: runtime, families, categories, types, flags, uploads, drawings.

use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::reviews::public_status;
use pictographic_core::time::iso_utc;
use pictographic_core::work as rules;
use serde::Deserialize;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::collections::BTreeSet;
use worker::{Response, Result};

pub fn runtime() -> Result<Response> {
    // The cloud is the single production authority; generation and editing run on local machines.
    http::json(200, &json!({"mode": "production", "can_generate": false, "can_edit": true, "can_upload": true,
                            "production_api": "", "storage": "cloudflare"}))
}

/// Built-in families from the BUILTIN_FAMILIES variable (`[["sub", 32], ...]`), then custom ones.
async fn families(ctx: &Ctx) -> Result<Vec<Value>> {
    let builtins: Vec<(String, i64)> = ctx.var("BUILTIN_FAMILIES").and_then(|t| serde_json::from_str(&t).ok()).unwrap_or_default();
    let mut result: Vec<Value> = builtins.into_iter().map(|(key, size)| {
        let title = key.replace('_', " ").split(' ').map(|w| {
            let mut chars = w.chars();
            chars.next().map(|c| c.to_uppercase().collect::<String>() + &chars.as_str().to_lowercase()).unwrap_or_default()
        }).collect::<Vec<_>>().join(" ");
        json!({"id": key, "name": title, "canvas_size": size, "builtin": true})
    }).collect();
    #[derive(Deserialize)]
    struct Row { id: String, name: String, canvas_size: f64 }
    let custom: Vec<Row> = db::all(&ctx.db, "SELECT id, name, canvas_size FROM upload_families ORDER BY name, id", vec![]).await?;
    result.extend(custom.into_iter().map(|r| json!({"id": r.id, "name": r.name, "canvas_size": r.canvas_size as i64, "builtin": false})));
    Ok(result)
}

pub async fn get_families(ctx: &Ctx) -> Result<Response> {
    http::json(200, &json!({"families": families(ctx).await?}))
}

pub async fn post_family(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let key = data.get("id").and_then(Value::as_str).unwrap_or("");
    let valid_key = !key.is_empty() && key.len() <= 64 && key.as_bytes()[0].is_ascii_lowercase()
        && key.bytes().all(|b| b.is_ascii_lowercase() || b.is_ascii_digit() || b == b'_' || b == b'-');
    if !valid_key {
        return http::error(400, "Family id must be 1–64 lowercase letters, digits, underscores or hyphens, starting with a letter.");
    }
    let name = data.get("name").and_then(Value::as_str).map(str::trim).filter(|n| (1..=120).contains(&n.chars().count()));
    let Some(name) = name else { return http::error(400, "Enter a family name up to 120 characters.") };
    let canvas = data.get("canvas_size").filter(|v| v.is_i64()).and_then(Value::as_i64).filter(|c| (16..=256).contains(c));
    let Some(canvas) = canvas else { return http::error(400, "canvas_size must be an integer from 16 to 256.") };
    if families(ctx).await?.iter().any(|f| f["id"] == key) {
        return http::error(409, "Family id already exists. Choose it for your upload or use a different id.");
    }
    let inserted = db::run(&ctx.db, "INSERT OR IGNORE INTO upload_families VALUES (?, ?, ?, ?, ?)",
                           args![key, name, canvas, iso_utc(chrono::Utc::now()), user]).await?;
    if inserted == 0 {
        return http::error(409, "Family id already exists.");
    }
    http::json(201, &json!({"family": {"id": key, "name": name, "canvas_size": canvas, "builtin": false}}))
}

pub async fn get_categories(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { category: Option<String> }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT DISTINCT category FROM icons", vec![]).await?;
    let mut categories: BTreeSet<String> = rows.into_iter().filter_map(|r| r.category)
        .map(|c| c.trim().to_string()).filter(|c| !c.is_empty()).collect();
    categories.insert("manual_upload".into());
    let mut sorted: Vec<String> = categories.into_iter().collect();
    sorted.sort_by(|a, b| (a.to_lowercase(), a).cmp(&(b.to_lowercase(), b)));
    http::json(200, &json!({"categories": sorted}))
}

pub async fn get_icon_types(ctx: &Ctx) -> Result<Response> {
    let wanted = ctx.param("type");
    let wanted_status = ctx.param("status");
    let catalog = data::catalog(&ctx.db, true).await?;
    #[derive(Deserialize)]
    struct Row { icon: String, icon_type: String, updated_at: String, updated_by: String }
    let types: Vec<Row> = db::all(&ctx.db, "SELECT icon, icon_type, updated_at, updated_by FROM icon_types WHERE icon_type != ''", vec![]).await?;
    let rows = data::review_rows(&ctx.db).await?;
    let splits = data::active_splits(&ctx.db).await?;
    let index = data::DetailIndex::new(&rows, &splits);
    let row_map = data::row_map(&rows);
    let feedback = data::latest_feedback(&ctx.db).await?;
    let now = chrono::Utc::now();
    let mut result = Vec::new();
    for row in types {
        let Some(icon) = catalog.get(&row.icon) else { continue };
        if wanted.is_some_and(|t| t != row.icon_type) {
            continue;
        }
        let detail = index.detail(&row.icon, &icon.svg_sha256);
        let status = public_status(&detail.status);
        if wanted_status.is_some_and(|s| s != status) {
            continue;
        }
        let pair = (row.icon.clone(), icon.svg_sha256.clone());
        let latest = feedback.get(&pair);
        let review_row = row_map.get(&pair);
        result.push(json!({"icon": row.icon, "icon_type": row.icon_type, "status": status,
            "python_source": icon.python_source, "svg_sha256": icon.svg_sha256,
            "reason": latest.and_then(|f| f.reason.clone()), "feedback": latest.and_then(|f| f.feedback.clone()),
            "updated_at": row.updated_at, "updated_by": row.updated_by,
            "work": rules::work_field(review_row, rules::work_state(review_row, now))}));
    }
    http::json(200, &json!({"icons": result}))
}

pub async fn get_icon_type(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("");
    if data::icon(&ctx.db, key, false).await?.is_none() {
        return http::error(404, "Unknown icon");
    }
    #[derive(Deserialize)]
    struct Row { icon_type: String, updated_by: String, updated_at: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT icon_type, updated_by, updated_at FROM icon_types WHERE icon = ?", args![key]).await?;
    http::json(200, &match row {
        Some(r) => json!({"icon_type": r.icon_type, "updated_by": r.updated_by, "updated_at": r.updated_at}),
        None => json!({"icon_type": "", "updated_by": null, "updated_at": null}),
    })
}

pub async fn post_icon_type(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let key = data.get("icon").and_then(Value::as_str);
    let icon_type = data.get("icon_type").and_then(Value::as_str).filter(|t| t.chars().count() <= 200);
    let (Some(key), Some(icon_type)) = (key, icon_type) else { return http::error(400, "Enter an icon type of up to 200 characters.") };
    let icon_type = icon_type.trim();
    if data::icon(&ctx.db, key, false).await?.is_none() {
        return http::error(404, "Unknown icon");
    }
    let now = iso_utc(chrono::Utc::now());
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "INSERT INTO icon_types(icon, icon_type, updated_at, updated_by) VALUES (?, ?, ?, ?) \
            ON CONFLICT(icon) DO UPDATE SET icon_type = excluded.icon_type, updated_at = excluded.updated_at, updated_by = excluded.updated_by",
            args![key, icon_type, now.clone(), user])?,
        db::activity(&ctx.db, user, "icon_type", Some(key), details(vec![("icon_type", json!(icon_type))]))?,
    ]).await?;
    http::json(200, &json!({"icon_type": icon_type, "updated_by": user, "updated_at": now}))
}

pub async fn get_icon_flag(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("");
    if data::icon(&ctx.db, key, false).await?.is_none() {
        return http::error(404, "Unknown icon");
    }
    #[derive(Deserialize)]
    struct Row { flag: String, updated_by: Option<String>, updated_at: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT flag, updated_by, updated_at FROM icon_flags WHERE icon = ?", args![key]).await?;
    http::json(200, &match row {
        Some(r) => json!({"flag": r.flag, "updated_by": r.updated_by, "updated_at": r.updated_at}),
        None => json!({"flag": "", "updated_by": null, "updated_at": null}),
    })
}

const FLAGS: [&str; 7] = ["", "container_combination", "combination", "text", "number", "other", "exception"];

pub async fn post_icon_flag(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let key = data.get("icon").and_then(Value::as_str);
    let flag = data.get("flag").and_then(Value::as_str).filter(|f| FLAGS.contains(f));
    let (Some(key), Some(flag)) = (key, flag) else { return http::error(400, "Choose a valid icon flag.") };
    if data::icon(&ctx.db, key, false).await?.is_none() {
        return http::error(404, "Unknown icon");
    }
    let now = iso_utc(chrono::Utc::now());
    let write = if flag.is_empty() {
        db::stmt(&ctx.db, "DELETE FROM icon_flags WHERE icon = ?", args![key])?
    } else {
        db::stmt(&ctx.db, "INSERT INTO icon_flags(icon, flag, updated_at, updated_by) VALUES (?, ?, ?, ?) \
            ON CONFLICT(icon) DO UPDATE SET flag = excluded.flag, updated_at = excluded.updated_at, updated_by = excluded.updated_by",
            args![key, flag, now.clone(), user])?
    };
    db::batch(&ctx.db, vec![write,
        db::activity(&ctx.db, user, if flag.is_empty() { "unflag" } else { "flag" }, Some(key), details(vec![("flag", json!(flag))]))?]).await?;
    http::json(200, &json!({"flag": flag, "updated_by": if flag.is_empty() { Value::Null } else { json!(user) },
                            "updated_at": if flag.is_empty() { Value::Null } else { json!(now) }}))
}

fn hex_token(bytes: usize) -> Result<String> {
    let mut buffer = vec![0u8; bytes];
    getrandom::getrandom(&mut buffer).map_err(|e| worker::Error::RustError(e.to_string()))?;
    Ok(hex::encode(buffer))
}

/// POST /api/icons/upload: a persistent SVG-only icon and its initial Ready review, atomically.
pub async fn post_upload(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let name = data.get("name").and_then(Value::as_str).filter(|n| (1..=120).contains(&n.trim().chars().count()));
    let Some(name) = name else { return http::error(400, "Enter an icon name up to 120 characters.") };
    let all = families(ctx).await?;
    let family_id = data.get("family").and_then(Value::as_str);
    let Some(family) = family_id.and_then(|f| all.iter().find(|row| row["id"] == f)) else {
        return http::error(400, "Unknown family. Create it with POST /api/icon-families first.");
    };
    let family_id = family_id.unwrap();
    let category = match data.get("category") {
        None => "manual_upload".to_string(),
        Some(Value::String(c)) if c.chars().count() <= 100 => c.clone(),
        _ => return http::error(400, "Enter a category up to 100 characters."),
    };
    let bypass = match data.get("bypass_validation") {
        None => true,
        Some(Value::Bool(b)) => *b,
        _ => return http::error(400, "bypass_validation must be a JSON boolean: true or false."),
    };
    // Optional: approve at once, and stand in for a combination component that has no drawing yet.
    let approve = data.get("approve") == Some(&json!(true));
    let reference = match data.get("reference") {
        None | Some(Value::Null) => None,
        Some(r) => {
            let id = r["id"].as_str().filter(|id| (1..=64).contains(&id.len())
                && id.chars().all(|c| c.is_ascii_alphanumeric() || c == '-'));
            match (id, r["role"].as_str()) {
                (Some(id), Some(role)) if matches!(role, "container" | "symbol") && role == family_id => Some((id.to_lowercase(), role)),
                _ => return http::error(400, "reference must be {id, role} with role container or symbol matching the family."),
            }
        }
    };
    // Optional: the reference the drawing was made from, linked like a built icon (original_sources and
    // icon_references). A combination part's `reference.id` links too when it is a known reference.
    let reference_id = match data.get("reference_id") {
        None | Some(Value::Null) => None,
        Some(Value::String(id)) if (1..=64).contains(&id.len()) && id.chars().all(|c| c.is_ascii_alphanumeric() || c == '-') => Some(id.to_lowercase()),
        _ => return http::error(400, "reference_id must be a reference id (letters, digits and hyphens, up to 64 characters)."),
    };
    if let (Some(id), Some((part, _))) = (&reference_id, &reference) {
        if id != part {
            return http::error(400, "reference_id and reference.id name different references.");
        }
    }
    let original = match reference_id.clone().or_else(|| reference.as_ref().map(|(id, _)| id.clone())) {
        None => None,
        Some(id) => match original_reference(ctx, &id).await? {
            Some(sources) => Some((id, sources)),
            None if reference_id.is_some() => return http::error(400, "Unknown reference_id: no reference has this id."),
            None => None,
        },
    };
    let original_sources = original.as_ref().map(|(_, sources)| sources.clone()).unwrap_or_else(|| json!([]));
    let status = if approve { "approve" } else { "ready" };
    let canvas = family["canvas_size"].as_i64().unwrap_or(48);
    let svg_input = data.get("svg").and_then(Value::as_str).unwrap_or("");
    // Uploads for a combination part (with `reference`, container-pairs.html) keep whatever canvas they were drawn on.
    let cleaned = if reference.is_some() { pictographic_core::svg::safe_svg_any_canvas(svg_input) }
                  else { pictographic_core::svg::safe_svg(svg_input, canvas) };
    let document = match cleaned {
        Ok(document) => document,
        Err(message) => return http::error(400, &message),
    };
    let digest = hex::encode(Sha256::digest(document.as_bytes()));
    let now = iso_utc(chrono::Utc::now());
    // A reference that already has an icon in this family gets no second icon: the upload is that icon's picked
    // candidate and the icon returns to Ready, whatever its review was (the generated icon before an earlier upload).
    if let Some((id, _)) = &original {
        if let Some(existing) = existing_icon(ctx, id, family_id).await? {
            let statements = super::edits::pick_upload(ctx, &existing, &document, &digest, user, &now).await?;
            db::batch(&ctx.db, statements).await?;
            let record = json!({"key": existing.key, "icon_id": existing.icon_id, "name": existing.name, "family": family_id,
                                "svg_sha256": digest, "preview_url": format!("../api/icon-artwork/svg?icon={}&v={digest}", http::percent_encode(&existing.key)),
                                "artwork_source": "use_upload"});
            return http::json(200, &json!({"record": record, "status": "ready", "candidate_of": existing.key}));
        }
    }
    let mut validation = json!({
        "status": "not-run", "bypassed": bypass, "checks_run": ["static SVG", "canvas"], "errors": [],
        "warnings": ["Uploaded artwork requires human review."],
        "scope": "Uploaded SVG safety and rendering; optional rendered holes/pinches QA.",
        "checks_not_run": ["render (runs on local machines)", "authored primitive grid/style", "keyshape fit", "vector spacing", "geometry symmetry"],
        "svg_sha256": digest, "checked_at": now});
    if !bypass {
        validation["status"] = json!("error");
        validation["errors"] = json!(["Holes/pinches validation renders the SVG, which runs on local machines. \
            Upload through a local gallery (deploy.py --cloud-api) or choose bypass."]);
        return http::json(503, &json!({"error": "Upload validation is unavailable.", "validation": validation}));
    }
    let slug: String = {
        let lowered = name.to_lowercase();
        let mut slug = String::new();
        let mut dash = false;
        for c in lowered.chars() {
            if c.is_ascii_lowercase() || c.is_ascii_digit() { slug.push(c); dash = false; }
            else if !dash { slug.push('-'); dash = true; }
        }
        let trimmed: String = slug.trim_matches('-').chars().take(80).collect();
        if trimmed.is_empty() { "icon".into() } else { trimmed }
    };
    let icon_id = format!("{slug}-upload-{}", hex_token(8)?);
    let key = format!("{family_id}/{icon_id}");
    let category = if category.trim().is_empty() { "manual_upload".to_string() } else { category.trim().to_string() };
    let preview_url = format!("../api/icon-artwork/svg?icon={key}&v={digest}");
    let record = json!({
        "key": key, "icon_id": icon_id, "name": name.trim(), "family": family_id,
        "profile": format!("{}{}", family_id.to_uppercase(), canvas), "canvas_size": canvas,
        "category": category, "icon_type": "uploaded", "keywords": [], "aliases": [],
        "svg_sha256": digest, "uploaded_icon": true, "artwork_source": "use_org",
        "preview_url": preview_url, "author": user, "created_at": now, "modified_at": now, "original_sources": original_sources,
        "primitives": [], "contours": [], "relationships": [], "anchors": {},
        "style": {"stroke_width": 4}, "keyshape": "FREE", "keyshape_bounds": [0, 0, canvas, canvas],
        "bypass_validation": bypass, "validation": validation});
    let record_text = serde_json::to_string(&record).unwrap();
    let db = &ctx.db;
    let mut statements = vec![
        db::stmt(db, "INSERT INTO uploaded_icons VALUES (?, ?, ?)", args![key.clone(), record_text.clone(), document.clone()])?,
        db::stmt(db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, \
            original_sources, uploaded, record, pushed_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?)",
            args![key.clone(), icon_id.clone(), name.trim(), family_id, category.clone(), record["profile"].as_str(), canvas,
                  digest.clone(), preview_url.clone(), original_sources.to_string(), record_text, now.clone()])?,
        super::icon_list::index_statement(db, &key, &record, None)?,
        db::stmt(db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'upload', ?)",
                 args![digest.clone(), key.clone(), document, now.clone()])?,
        db::stmt(db, "INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, ?, ?, ?, ?)",
                 args![key.clone(), digest.clone(), status, now.clone(), user])?,
        db::stmt(db, "INSERT INTO icon_types(icon, icon_type, updated_at, updated_by) VALUES (?, 'uploaded', ?, ?)",
                 args![key.clone(), now.clone(), user])?,
        db::activity(db, user, "upload", Some(&key), details(vec![("svg_sha256", json!(digest)), ("status", json!(status)),
            ("category", json!(category)), ("icon_type", json!("uploaded"))]))?,
    ];
    if let Some((id, _)) = &original {
        statements.push(db::stmt(db, "INSERT OR IGNORE INTO icon_references(icon, reference_id) VALUES (?, ?)", args![key.clone(), id.clone()])?);
    }
    // A 72 side pair part (main-54 / sub-36) drawn from a part's reference fills that part's 72 pick in every side
    // pair that uses the reference and has none yet; the pair then shows as ready to build.
    let pair_role = match family_id { "main-54" => Some("main"), "sub-36" => Some("sub"), _ => None };
    if let (Some(role), Some((id, _))) = (pair_role, &original) {
        statements.push(db::stmt(db, "INSERT INTO reference_part_sizes(reference_id, role, size, icon, updated_at, updated_by) \
            SELECT p.reference_id, p.role, 72, ?, ?, ? FROM reference_parts p WHERE p.part_reference_id = ? AND p.role = ? \
              AND NOT EXISTS (SELECT 1 FROM reference_parts c WHERE c.reference_id = p.reference_id AND c.role IN ('container', 'symbol')) \
            ON CONFLICT(reference_id, role, size) DO UPDATE SET icon = excluded.icon, updated_at = excluded.updated_at, \
              updated_by = excluded.updated_by WHERE reference_part_sizes.icon IS NULL",
            args![key.clone(), now.clone(), user, id.clone(), role])?);
    }
    if approve {
        statements.push(db::activity(db, user, "review", Some(&key), details(vec![("status", json!("approve")), ("svg_sha256", json!(digest))]))?);
    }
    db::batch(db, statements).await?;
    #[derive(Deserialize)]
    struct Picked { reference_id: String, role: String }
    let picked: Vec<Picked> = if pair_role.is_some() {
        db::all(db, "SELECT reference_id, role FROM reference_part_sizes WHERE icon = ? AND size = 72 ORDER BY reference_id", args![key.clone()]).await?
    } else { vec![] };
    let mut answer = json!({"record": record, "status": status});
    if pair_role.is_some() {
        answer["combination_parts"] = json!(picked.iter().map(|p| json!({"reference_id": p.reference_id, "role": p.role, "size": 72})).collect::<Vec<_>>());
    }
    http::json(201, &answer)
}

/// The icon this family already has for a reference (icon_references), the generated one before an upload, or None.
async fn existing_icon(ctx: &Ctx, reference_id: &str, family: &str) -> Result<Option<pictographic_core::catalog::Icon>> {
    #[derive(Deserialize)]
    struct Row { key: String }
    let row: Option<Row> = db::first(&ctx.db, "SELECT i.key FROM icon_references r JOIN icons i ON i.key = r.icon \
        WHERE r.reference_id = ? AND i.family = ? ORDER BY i.uploaded, i.pushed_at LIMIT 1", args![reference_id, family]).await?;
    match row {
        Some(row) => data::icon(&ctx.db, &row.key, true).await,
        None => Ok(None),
    }
}

/// The original_sources value a built icon drawn from this reference carries, or None for an unknown id.
async fn original_reference(ctx: &Ctx, id: &str) -> Result<Option<Value>> {
    #[derive(Deserialize)]
    struct Row { folder: Option<String>, file: Option<String>, r2_key: Option<String>, sha256: Option<String> }
    let row: Option<Row> = db::first(&ctx.db, "SELECT folder, file, r2_key, sha256 FROM \"references\" WHERE reference_id = ?",
                                     args![id]).await?;
    Ok(row.and_then(|row| {
        let sha = row.sha256?;
        let root = if row.r2_key.as_deref().unwrap_or("").starts_with("references/combinations/") { "pictographic-combinations" }
                   else { "pictographic-primitives" };
        Some(json!([{"url": format!("originals/{sha}"), "format": "SVG",
                     "source_path": format!("{root}/{}/{}", row.folder.unwrap_or_default(), row.file.unwrap_or_default())}]))
    }))
}

/// GET /api/uploaded-icons: upload records for the gallery catalog (without the SVG text).
pub async fn get_uploaded(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { record: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT record FROM uploaded_icons ORDER BY rowid", vec![]).await?;
    let records: Vec<Value> = rows.into_iter().filter_map(|r| serde_json::from_str(&r.record).ok()).collect();
    http::json(200, &json!({"icons": records}))
}

/// GET /api/icon-artwork/svg: the current drawing, stored inline in D1.
pub async fn get_artwork_svg(ctx: &Ctx) -> Result<Response> {
    let key = ctx.param("icon").unwrap_or("");
    if let Some(variant) = ctx.param("variant") {
        let variant = variant.to_string();
        return super::edits::get_artwork_variant(ctx, &variant).await;
    }
    let Some(icon) = data::icon(&ctx.db, key, true).await? else { return http::error(404, "Icon not found.") };
    // A picked version (browser edit or manual SVG) is what the gallery shows, before a worker's fix.
    if let Some(response) = super::edits::picked_drawing(ctx, &icon).await? {
        return Ok(response);
    }
    #[derive(Deserialize)]
    struct Row { svg: String }
    let row: Option<Row> = if icon.uploaded {
        db::first(&ctx.db, "SELECT svg FROM uploaded_icons WHERE icon = ?", args![key]).await?
    } else {
        // A worker's uploaded fix of the current revision is what the gallery shows (deploy.py `serve_work_fix`);
        // an artwork choice gives the icon a different svg_sha256, so it never matches a fix.
        let fix: Option<Row> = db::first(&ctx.db, "SELECT svg FROM work_results WHERE icon = ? AND svg_sha256 = ? AND stage = 'after'",
                                         args![key, icon.svg_sha256.clone()]).await?;
        match fix {
            Some(fix) => Some(fix),
            None => db::first(&ctx.db, "SELECT svg FROM revisions WHERE svg_sha256 = ?", args![icon.svg_sha256.clone()]).await?,
        }
    };
    match row {
        Some(row) => http::svg(&row.svg),
        None => http::error(503, "Artwork is unavailable on this server."),
    }
}
