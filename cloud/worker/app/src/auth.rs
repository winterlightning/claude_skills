//! Reviewer sessions — deploy.py `current_user` and `auth_action`, same cookie and users.

use crate::args;
use crate::data::admin_users;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use base64::Engine;
use serde::Deserialize;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use worker::{Headers, Response, Result};

pub const SESSION_TTL: f64 = 12.0 * 60.0 * 60.0;
const COOKIE: &str = "pictographic_session";

fn now_seconds() -> f64 {
    worker::js_sys::Date::now() / 1000.0
}

fn digest(token: &str) -> String {
    hex::encode(Sha256::digest(token.as_bytes()))
}

fn session_cookie(ctx: &Ctx) -> Option<String> {
    let header = ctx.header("Cookie")?;
    header.split(';').filter_map(|part| part.trim().split_once('='))
        .find(|(name, _)| *name == COOKIE).map(|(_, value)| value.trim_matches('"').to_string())
        .filter(|value| !value.is_empty())
}

/// The signed-in reviewer, if any.
pub async fn current_user(ctx: &Ctx) -> Option<String> {
    let token = session_cookie(ctx)?;
    #[derive(Deserialize)]
    struct Row { username: String }
    db::first::<Row>(&ctx.db, "SELECT username FROM admin_sessions WHERE token = ? AND expires > ?",
                     args![digest(&token), now_seconds()]).await.ok().flatten().map(|r| r.username)
}

/// `secrets.token_urlsafe(32)`.
fn new_token() -> Result<String> {
    let mut bytes = [0u8; 32];
    getrandom::getrandom(&mut bytes).map_err(|e| worker::Error::RustError(e.to_string()))?;
    Ok(base64::engine::general_purpose::URL_SAFE_NO_PAD.encode(bytes))
}

/// POST /api/auth/login and /api/auth/logout.
pub async fn auth_action(ctx: &Ctx, login: bool, data: &Value) -> Result<Response> {
    let username = data.get("username").and_then(Value::as_str).map(str::to_string);
    if login {
        let password = data.get("password").and_then(Value::as_str);
        let users = admin_users(&ctx.env);
        let valid = match (&username, password) {
            (Some(name), Some(password)) => users.iter().any(|(user, secret)| user == name && constant_eq(secret, password)),
            _ => false,
        };
        if !valid {
            return http::error(401, "Incorrect username or password.");
        }
    }
    let db = &ctx.db;
    let mut statements = vec![db::stmt(db, "DELETE FROM admin_sessions WHERE expires <= ?", args![now_seconds()])?];
    if let Some(old) = session_cookie(ctx) {
        let old = digest(&old);
        if !login {
            #[derive(Deserialize)]
            struct Row { username: String }
            let ended = db::first::<Row>(db, "SELECT username FROM admin_sessions WHERE token = ?", args![old.clone()]).await?;
            statements.push(db::stmt(db, "DELETE FROM admin_sessions WHERE token = ?", args![old])?);
            if let Some(ended) = ended {
                statements.push(db::activity(db, &ended.username, "logout", None, details(vec![]))?);
            }
        } else {
            statements.push(db::stmt(db, "DELETE FROM admin_sessions WHERE token = ?", args![old])?);
        }
    }
    let token = if login { new_token()? } else { String::new() };
    if login {
        let name = username.clone().unwrap_or_default();
        statements.push(db::stmt(db, "INSERT INTO admin_sessions VALUES (?, ?, ?)", args![digest(&token), name.clone(), now_seconds() + SESSION_TTL])?);
        statements.push(db::activity(db, &name, "login", None, details(vec![]))?);
    }
    db::batch(db, statements).await?;
    let body = json!({"user": if login { username.map(Value::String).unwrap_or(Value::Null) } else { Value::Null }});
    let headers = Headers::new();
    headers.set("Set-Cookie", &format!("{COOKIE}={token}; Path=/; HttpOnly; SameSite=Strict; Max-Age={}",
                                       if login { SESSION_TTL as i64 } else { 0 }))?;
    headers.set("Content-Type", "application/json")?;
    headers.set("Cache-Control", "no-store")?;
    Ok(Response::from_bytes(serde_json::to_vec(&body).unwrap())?.with_headers(headers))
}

fn constant_eq(a: &str, b: &str) -> bool {
    let (a, b) = (a.as_bytes(), b.as_bytes());
    if a.len() != b.len() {
        return false;
    }
    a.iter().zip(b).fold(0u8, |acc, (x, y)| acc | (x ^ y)) == 0
}
