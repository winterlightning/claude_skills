//! Pictographic review server on Cloudflare Workers: D1 holds the data and review status,
//! R2 holds references and large files. Graphics processing stays on local machines.

mod auth;
mod data;
mod db;
mod http;
mod routes;

use worker::{console_error, event, Context, Env, Request, Response, Result};

#[event(fetch)]
async fn fetch(req: Request, env: Env, _ctx: Context) -> Result<Response> {
    let mut ctx = match http::Ctx::new(req, env) {
        Ok(ctx) => ctx,
        Err(error) => {
            console_error!("setup failed: {error}");
            return http::error(503, "The service is temporarily unavailable. Please retry.");
        }
    };
    match routes::dispatch(&mut ctx).await {
        Ok(response) => Ok(response),
        Err(error) => {
            console_error!("{} {} failed: {error}", ctx.method, ctx.path);
            http::error(503, "The service is temporarily unavailable. Please retry.")
        }
    }
}
