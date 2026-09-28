//! Request context and the response shapes deploy.py sends.

use pictographic_core::query::{parse_qs, Query};
use serde_json::{json, Value};
use worker::{Env, Headers, Method, Request, Response, Result};

pub struct Ctx {
    pub req: Request,
    pub env: Env,
    pub method: Method,
    pub path: String,
    pub query: Query,
    pub db: worker::D1Database,
}

impl Ctx {
    pub fn new(req: Request, env: Env) -> Result<Self> {
        let url = req.url()?;
        let raw_query = url.query().unwrap_or("").to_string();
        let path = percent_decode(url.path());
        let db = env.d1("DB")?;
        Ok(Ctx { method: req.method(), path, query: parse_qs(&raw_query), req, env, db })
    }

    pub fn header(&self, name: &str) -> Option<String> {
        self.req.headers().get(name).ok().flatten()
    }

    pub fn var(&self, name: &str) -> Option<String> {
        self.env.var(name).ok().map(|v| v.to_string())
    }

    pub fn param(&self, name: &str) -> Option<&str> {
        pictographic_core::query::first(&self.query, name)
    }
}

pub fn percent_decode(text: &str) -> String {
    let bytes = text.as_bytes();
    let mut out = Vec::with_capacity(bytes.len());
    let mut index = 0;
    while index < bytes.len() {
        if bytes[index] == b'%' && index + 2 < bytes.len() {
            if let Ok(value) = u8::from_str_radix(std::str::from_utf8(&bytes[index + 1..index + 3]).unwrap_or("zz"), 16) {
                out.push(value);
                index += 3;
                continue;
            }
        }
        out.push(bytes[index]);
        index += 1;
    }
    String::from_utf8_lossy(&out).into_owned()
}

fn base_headers(content_type: &str, cache: &str) -> Result<Headers> {
    let headers = Headers::new();
    headers.set("Content-Type", content_type)?;
    headers.set("X-Content-Type-Options", "nosniff")?;
    headers.set("Cache-Control", cache)?;
    Ok(headers)
}

/// `json_response(data, status)`: UTF-8 JSON, never cached.
pub fn json(status: u16, value: &Value) -> Result<Response> {
    let body = serde_json::to_vec(value).map_err(|e| worker::Error::RustError(e.to_string()))?;
    Ok(Response::from_bytes(body)?.with_status(status)
        .with_headers(base_headers("application/json; charset=utf-8", "no-store")?))
}

pub fn error(status: u16, message: &str) -> Result<Response> {
    json(status, &json!({"error": message}))
}

/// Untrusted SVG, displayed sandboxed exactly like deploy.py.
pub fn svg(document: &str) -> Result<Response> {
    let headers = base_headers("image/svg+xml", "no-store")?;
    headers.set("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; sandbox")?;
    Ok(Response::from_bytes(document.as_bytes().to_vec())?.with_headers(headers))
}

pub fn text(status: u16, body: &str, content_type: &str) -> Result<Response> {
    Ok(Response::from_bytes(body.as_bytes().to_vec())?.with_status(status)
        .with_headers(base_headers(content_type, "no-store")?))
}

/// Prebuilt response bytes (e.g. JSON spliced around a stored file), never cached.
pub fn bytes(status: u16, body: Vec<u8>, content_type: &str) -> Result<Response> {
    Ok(Response::from_bytes(body)?.with_status(status).with_headers(base_headers(content_type, "no-store")?))
}

pub fn redirect(location: &str) -> Result<Response> {
    let headers = Headers::new();
    headers.set("Location", location)?;
    Ok(Response::empty()?.with_status(302).with_headers(headers))
}

pub fn not_found() -> Result<Response> {
    error(404, "Not found")
}

/// Read a JSON object body with deploy.py's checks. Err is the response to send.
pub async fn json_body(ctx: &mut Ctx, limit: usize, too_large: &str) -> std::result::Result<Value, Response> {
    let fail = |status: u16, message: &str| error(status, message).unwrap_or_else(|_| Response::error("error", status).unwrap());
    let content_type = ctx.header("Content-Type").unwrap_or_default();
    let mime = content_type.split(';').next().unwrap_or("").trim().to_ascii_lowercase();
    if mime != "application/json" {
        return Err(fail(415, "Expected application/json"));
    }
    let bytes = ctx.req.bytes().await.map_err(|_| fail(400, "Invalid feedback or review status"))?;
    if bytes.is_empty() || bytes.len() > limit {
        return Err(fail(413, too_large));
    }
    match serde_json::from_slice::<Value>(&bytes) {
        Ok(value @ Value::Object(_)) => Ok(value),
        _ => Err(fail(400, "Invalid feedback or review status")),
    }
}

/// deploy.py refuses cross-origin writes: an Origin header must match Host.
pub fn same_origin(ctx: &Ctx) -> bool {
    let Some(origin) = ctx.header("Origin") else { return true };
    let host = ctx.header("Host").unwrap_or_default();
    match origin.split_once("://") {
        Some((scheme, rest)) if scheme == "http" || scheme == "https" => rest.split('/').next() == Some(host.as_str()),
        _ => false,
    }
}
