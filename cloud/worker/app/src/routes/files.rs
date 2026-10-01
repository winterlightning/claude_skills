//! Files served from R2: the built gallery site, original primitives, reference images.

use crate::args;
use crate::auth::current_user;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use base64::Engine;
use futures_util::{stream, StreamExt};
use pictographic_core::refimg;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Value};
use worker::{Headers, HttpMetadata, Range, Response, Result};

pub const SITE: &str = "site";
pub const ICONS_JSON: &str = "site/gallery/icons.json";
pub const PREVIEW_ICONS_JSON: &str = "site/gallery/preview-icons.json";
pub const SIDE_COMPONENTS_JSON: &str = "site/gallery/side-components.json";

fn content_type(path: &str) -> Option<&'static str> {
    let extension = path.rsplit('.').next()?.to_ascii_lowercase();
    Some(match extension.as_str() {
        "html" => "text/html; charset=utf-8",
        "json" => "application/json",
        "svg" => "image/svg+xml",
        "png" => "image/png",
        "css" => "text/css; charset=utf-8",
        "js" => "text/javascript; charset=utf-8",
        _ => return None,
    })
}

/// No hidden segments, traversal or directory listings — the checks of deploy.py `send_head`.
fn safe_relative(path: &str) -> Option<String> {
    let relative = path.trim_start_matches('/');
    if relative.is_empty() || relative.split('/').any(|part| part.is_empty() || part.starts_with('.')) {
        return None;
    }
    Some(relative.to_string())
}

/// GET of any other path: the static gallery build, from R2 under `site/`.
pub async fn static_file(ctx: &Ctx) -> Result<Response> {
    if ctx.path == "/" {
        return http::redirect("/gallery/home.html");
    }
    if ctx.path == "/gallery/generate.html" && current_user(ctx).await.is_none() {
        return http::redirect("/gallery/login.html");
    }
    let Some(relative) = safe_relative(&ctx.path) else { return http::error(404, "Not found") };
    let Some(mime) = content_type(&relative) else { return http::error(404, "Not found") };
    let key = format!("{SITE}/{relative}");
    if key == ICONS_JSON {
        return icons_json(ctx).await;
    }
    if key == PREVIEW_ICONS_JSON {
        return preview_icons_json(ctx).await;
    }
    if let Some(pair_id) = relative.strip_prefix("gallery/combination-previews/").and_then(|n| n.strip_suffix(".svg")) {
        if let Some(response) = super::combinations::built_preview(ctx, pair_id).await? {
            return Ok(response);
        }
    }
    if key == SIDE_COMPONENTS_JSON {
        return super::edits::side_components(ctx).await;
    }
    if let Some(response) = drawing(ctx, &relative).await? {
        return Ok(response);
    }
    if let Some(response) = reference_copy(ctx, &relative).await? {
        return Ok(response);
    }
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(&key).execute().await? else { return http::error(404, "Not found") };
    let etag = object.http_etag();
    let headers = Headers::new();
    headers.set("Content-Type", mime)?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    // Static files revalidate so a grid of hundreds of SVGs is not refetched on every view.
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").as_deref() == Some(etag.as_str()) {
        return Ok(Response::empty()?.with_status(304).with_headers(headers));
    }
    let Some(body) = object.body() else { return http::error(404, "Not found") };
    Ok(Response::from_stream(body.stream()?)?.with_headers(headers))
}

/// `<profile>/<icon_id>.svg` and `failed/<profile>/<icon_id>.svg`: the page URLs of icon images.
/// Family/profile is just a field of the icon row, so the folder name selects the profile and the
/// current drawing comes from D1 — the same revision the review status is attached to.
async fn drawing(ctx: &Ctx, relative: &str) -> Result<Option<Response>> {
    let (failed, rest) = match relative.strip_prefix("failed/") { Some(rest) => (1i64, rest), None => (0, relative) };
    let Some((folder, file)) = rest.split_once('/') else { return Ok(None) };
    let Some(icon_id) = file.strip_suffix(".svg") else { return Ok(None) };
    let profile_like = !folder.is_empty() && folder.bytes().all(|b| b.is_ascii_lowercase() || b.is_ascii_digit() || b == b'_')
        && folder.bytes().last().is_some_and(|b| b.is_ascii_digit());
    if !profile_like || icon_id.contains('/') {
        return Ok(None);
    }
    #[derive(Deserialize)]
    struct Row { svg: String, svg_sha256: String }
    let profile = folder.to_ascii_uppercase();
    let mut row: Option<Row> = db::first(&ctx.db, "SELECT r.svg, r.svg_sha256 FROM icons i JOIN revisions r ON r.svg_sha256 = i.svg_sha256 \
        WHERE i.profile = ? AND i.icon_id = ? AND i.build_failed = ? AND i.uploaded = 0 LIMIT 1", args![profile.clone(), icon_id, failed]).await?;
    if row.is_none() {
        row = db::first(&ctx.db, "SELECT r.svg, r.svg_sha256 FROM extra_drawings e JOIN revisions r ON r.svg_sha256 = e.svg_sha256 \
            WHERE e.profile = ? AND e.icon_id = ? AND e.failed = ?", args![profile, icon_id, failed]).await?;
    }
    let Some(row) = row else { return Ok(Some(http::error(404, "Not found")?)) };
    let etag = format!("\"{}\"", row.svg_sha256);
    let headers = Headers::new();
    headers.set("Content-Type", "image/svg+xml")?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").as_deref() == Some(etag.as_str()) {
        return Ok(Some(Response::empty()?.with_status(304).with_headers(headers)));
    }
    Ok(Some(Response::from_bytes(row.svg.into_bytes())?.with_headers(headers)))
}

/// `gallery/originals/<sha256>.<ext>` and `gallery/combination-originals/<reference id>.svg`: the
/// reference shown next to an icon, served from the one stored copy under references/.
async fn reference_copy(ctx: &Ctx, relative: &str) -> Result<Option<Response>> {
    #[derive(Deserialize)]
    struct Row { r2_key: String }
    let row: Option<Row> = if let Some(name) = relative.strip_prefix("gallery/originals/") {
        db::first(&ctx.db, "SELECT r2_key FROM \"references\" WHERE sha256 = ? AND r2_key IS NOT NULL LIMIT 1", args![name]).await?
    } else if let Some(name) = relative.strip_prefix("gallery/combination-originals/") {
        let Some(id) = name.strip_suffix(".svg") else { return Ok(None) };
        db::first(&ctx.db, "SELECT r2_key FROM \"references\" WHERE reference_id = ? AND r2_key IS NOT NULL", args![id]).await?
    } else {
        return Ok(None);
    };
    let Some(row) = row else { return Ok(Some(http::error(404, "Not found")?)) };
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(&row.r2_key).execute().await? else { return Ok(Some(http::error(404, "Not found")?)) };
    let etag = object.http_etag();
    let headers = Headers::new();
    headers.set("Content-Type", content_type(relative).unwrap_or("application/octet-stream"))?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").as_deref() == Some(etag.as_str()) {
        return Ok(Some(Response::empty()?.with_status(304).with_headers(headers)));
    }
    let Some(body) = object.body() else { return Ok(Some(http::error(404, "Not found")?)) };
    Ok(Some(Response::from_stream(body.stream()?)?.with_headers(headers)))
}

/// Details of the last catalog push: where the icons list ends in icons.json.
#[derive(Deserialize, Default)]
struct IconsJsonLayout {
    #[serde(default)]
    tail: u64,
    #[serde(default)]
    count: u64,
}

/// `/gallery/icons.json`: the pushed catalog, with uploaded icons appended to its `icons` list.
/// The push writes `icons` last, so the file ends with `]}` and the uploads splice in before it.
async fn icons_json(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Push { details: String }
    let push: Option<Push> = db::first(&ctx.db, "SELECT details FROM catalog_pushes ORDER BY id DESC LIMIT 1", vec![]).await?;
    let layout: IconsJsonLayout = push.and_then(|p| serde_json::from_str::<Value>(&p.details).ok())
        .and_then(|d| serde_json::from_value(d["icons_json"].clone()).ok()).unwrap_or_default();
    let bucket = ctx.env.bucket("FILES")?;
    let Some(head) = bucket.head(ICONS_JSON).await? else { return http::error(503, "Artwork storage is unavailable.") };
    // The file changes only with a push (the R2 object) or an upload: a browser that has this version gets a 304
    // instead of the ~90 MB again.
    #[derive(Deserialize)]
    struct Version { n: f64, last: Option<f64> }
    let version: Option<Version> = db::first(&ctx.db, "SELECT COUNT(*) AS n, MAX(rowid) AS last FROM uploaded_icons", vec![]).await?;
    let etag = format!("\"{}-{}-{}\"", head.etag(), version.as_ref().map_or(0.0, |v| v.n) as i64,
                       version.and_then(|v| v.last).unwrap_or(0.0) as i64);
    let headers = Headers::new();
    headers.set("Content-Type", "application/json; charset=utf-8")?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", "no-cache")?;
    headers.set("ETag", &etag)?;
    if ctx.header("If-None-Match").is_some_and(|given| given.split(',').any(|t| t.trim().trim_start_matches("W/") == etag)) {
        return Ok(Response::empty()?.with_status(304).with_headers(headers));
    }
    #[derive(Deserialize)]
    struct Upload { record: String }
    let uploads: Vec<Upload> = db::all(&ctx.db, "SELECT record FROM uploaded_icons ORDER BY rowid", vec![]).await?;
    let size = head.size();
    if uploads.is_empty() || layout.tail == 0 || layout.tail > size {
        let object = bucket.get(ICONS_JSON).execute().await?.ok_or_else(|| worker::Error::RustError("icons.json vanished".into()))?;
        let body = object.body().ok_or_else(|| worker::Error::RustError("empty icons.json".into()))?;
        return Ok(Response::from_stream(body.stream()?)?.with_headers(headers));
    }
    let object = bucket.get(ICONS_JSON).range(Range::OffsetWithLength { offset: 0, length: size - layout.tail })
        .execute().await?.ok_or_else(|| worker::Error::RustError("icons.json vanished".into()))?;
    let prefix = object.body().ok_or_else(|| worker::Error::RustError("empty icons.json".into()))?.stream()?;
    let tail_object = bucket.get(ICONS_JSON).range(Range::Suffix { suffix: layout.tail }).execute().await?
        .ok_or_else(|| worker::Error::RustError("icons.json vanished".into()))?;
    let tail = tail_object.body().ok_or_else(|| worker::Error::RustError("empty icons.json".into()))?.bytes().await?;
    let mut appended = Vec::new();
    for (index, upload) in uploads.iter().enumerate() {
        if index > 0 || layout.count > 0 {
            appended.push(b',');
        }
        appended.extend_from_slice(upload.record.as_bytes());
    }
    appended.extend_from_slice(&tail);
    let combined = prefix.chain(stream::once(async move { Ok::<Vec<u8>, worker::Error>(appended) }));
    Ok(Response::from_stream(combined)?.with_headers(headers))
}

/// `/gallery/preview-icons.json`: the built preview list lacks uploads; append them (deploy.py does the same).
async fn preview_icons_json(ctx: &Ctx) -> Result<Response> {
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(PREVIEW_ICONS_JSON).execute().await? else { return http::error(404, "Not found") };
    let bytes = object.body().ok_or_else(|| worker::Error::RustError("empty preview-icons.json".into()))?.bytes().await?;
    let Ok(mut data) = serde_json::from_slice::<Value>(&bytes) else { return http::error(503, "Artwork storage is unavailable.") };
    #[derive(Deserialize)]
    struct Upload { record: String }
    let uploads: Vec<Upload> = db::all(&ctx.db, "SELECT record FROM uploaded_icons ORDER BY rowid", vec![]).await?;
    if let Some(Value::Array(icons)) = data.get_mut("icons") {
        for upload in uploads {
            let Ok(record) = serde_json::from_str::<Value>(&upload.record) else { continue };
            let mut row = serde_json::Map::new();
            for field in ["icon_id", "name", "family", "preview_url", "category"] {
                row.insert(field.into(), record.get(field).cloned().filter(|v| !v.is_null()).unwrap_or(json!("")));
            }
            icons.push(Value::Object(row));
        }
    }
    http::json(200, &data)
}


/// GET /primitives/<path>: original reference SVGs, sandboxed like deploy.py `serve_primitive`.
pub async fn primitive(ctx: &Ctx) -> Result<Response> {
    let relative = ctx.path.trim_start_matches("/primitives/");
    let Some(relative) = safe_relative(relative).filter(|r| r.to_ascii_lowercase().ends_with(".svg")) else {
        return http::error(404, "Not found");
    };
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(format!("references/primitives/{relative}")).execute().await? else {
        return http::error(404, "Not found");
    };
    let text = object.body().ok_or_else(|| worker::Error::RustError("empty".into()))?.text().await?;
    http::svg(&text)
}

pub async fn get_reference_image(ctx: &Ctx) -> Result<Response> {
    let id = ctx.param("id").unwrap_or("");
    #[derive(Deserialize)]
    struct Row { mime: String, r2_key: String }
    let row: Option<Row> = if refimg::is_id(id) {
        db::first(&ctx.db, "SELECT mime, r2_key FROM reference_images WHERE id = ?", args![id]).await?
    } else { None };
    let Some(row) = row else { return http::error(404, "Unknown reference image.") };
    let bucket = ctx.env.bucket("FILES")?;
    let Some(object) = bucket.get(&row.r2_key).execute().await? else { return http::error(404, "Unknown reference image.") };
    let bytes = object.body().ok_or_else(|| worker::Error::RustError("empty".into()))?.bytes().await?;
    let headers = Headers::new();
    headers.set("Content-Type", &row.mime)?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", "no-store")?;
    headers.set("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; sandbox")?;
    Ok(Response::from_bytes(bytes)?.with_headers(headers))
}

/// POST /api/reference-images: store by content hash in R2, metadata in D1.
pub async fn post_reference_image(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let Some(encoded) = data.get("data").and_then(Value::as_str) else { return http::error(400, "Choose an SVG or PNG file.") };
    let Ok(bytes) = base64::engine::general_purpose::STANDARD.decode(encoded) else {
        return http::error(400, "Could not read the uploaded file.");
    };
    if bytes.is_empty() {
        return http::error(400, "Choose an SVG or PNG file.");
    }
    let kind = match refimg::kind(&bytes) { Ok(kind) => kind, Err(message) => return http::error(400, &message) };
    if bytes.len() > refimg::limit(kind) {
        return http::error(400, &format!("{} references must be at most {} MB.", kind.to_uppercase(), refimg::limit(kind) / (1024 * 1024)));
    }
    let id = refimg::id(&bytes);
    let name = refimg::name(data.get("name").and_then(Value::as_str), kind);
    let key = format!("stores/reference-images/{id}.{kind}");
    let bucket = ctx.env.bucket("FILES")?;
    let size = bytes.len() as i64;
    if bucket.head(&key).await?.is_none() {
        bucket.put(&key, bytes).http_metadata(HttpMetadata { content_type: Some(refimg::mime(kind).into()), ..Default::default() })
            .execute().await?;
    }
    db::batch(&ctx.db, vec![
        db::stmt(&ctx.db, "INSERT INTO reference_images(id, name, mime, size, r2_key, uploaded_by, uploaded_at) VALUES (?, ?, ?, ?, ?, ?, ?) \
            ON CONFLICT(id) DO UPDATE SET name = excluded.name",
            args![id.clone(), name.clone(), refimg::mime(kind), size, key, user, iso_utc(chrono::Utc::now())])?,
        db::activity(&ctx.db, user, "reference_upload", None, details(vec![("image", json!(id)), ("name", json!(name))]))?,
    ]).await?;
    http::json(201, &json!({"id": id, "kind": kind, "name": name}))
}
