//! Route table: the same paths, methods and error shapes as icon_set/scripts/deploy.py.

pub mod briefs;
pub mod combinations;
pub mod edits;
pub mod files;
pub mod icons;
pub mod internal;
pub mod side;
pub mod side_pairs;
pub mod primitives;
pub mod reviews;
pub mod work;

use crate::auth;
use crate::http::{self, Ctx};
use serde_json::json;
use worker::{Method, Response, Result};

const MAX_BODY: usize = 65536;
const MAX_REFERENCE_BODY: usize = 2 * 1024 * 1024 * 4 / 3 + 4096;
const MAX_WORK_RESULT_BODY: usize = 1536 * 1024;
const MAX_PUSH_BODY: usize = 32 * 1024 * 1024;

/// deploy.py `production_blocked`: development-workspace actions production never ran.
fn production_blocked(path: &str) -> bool {
    path.starts_with("/api/generation") || path.starts_with("/api/ai-feedback")
        || matches!(path, "/api/icons/discard" | "/api/combinations/side/keep-sub" | "/api/feedback-db/sync"
                          | "/api/combination-refresh" | "/api/symbols/copy-from-sub")
}

/// Graphics processing (rendering, validation, geometry) and file packaging stay on local machines.
fn local_only(path: &str) -> bool {
    path.starts_with("/api/qa-evidence") || path.starts_with("/api/combinations/container/")
        || matches!(path, "/api/primitives/generation-queue" | "/api/combinations/generation-queue"
                          | "/api/pending-briefs/download" | "/api/feedback-db/export" | "/api/review-data/export")
}

fn local_response() -> Result<Response> {
    http::json(501, &json!({"error": "This action runs on the local gallery (deploy.py --cloud-api); the cloud stores data only.",
                            "local": true}))
}

fn is_internal(path: &str) -> bool {
    path == "/api/catalog/push" || path.starts_with("/api/store/") || path.starts_with("/api/files/") || path == "/api/icons/discard-record" || path == "/api/activity"
}

pub async fn dispatch(ctx: &mut Ctx) -> Result<Response> {
    let path = ctx.path.clone();
    if is_internal(&path) && !internal::authorized(ctx) {
        return http::error(401, "A valid push token is required.");
    }
    if production_blocked(&path) {
        return http::error(403, "This action belongs to the development workspace.");
    }
    if local_only(&path) {
        return local_response();
    }
    if path.starts_with("/api/files/") {
        return match ctx.method {
            Method::Put | Method::Delete => internal::file(ctx).await,
            _ => http::error(405, "Method not allowed"),
        };
    }
    match ctx.method {
        Method::Get | Method::Head => get(ctx, &path).await,
        Method::Post => post(ctx, &path).await,
        _ => http::error(405, "Method not allowed"),
    }
}

async fn get(ctx: &Ctx, path: &str) -> Result<Response> {
    match path {
        "/api/runtime" => icons::runtime(),
        "/api/auth/session" => http::json(200, &json!({"user": auth::current_user(ctx).await})),
        "/api/icon-families" => icons::get_families(ctx).await,
        "/api/icon-categories" => icons::get_categories(ctx).await,
        "/api/icon-types" => icons::get_icon_types(ctx).await,
        "/api/icon-type" => icons::get_icon_type(ctx).await,
        "/api/icon-flag" => icons::get_icon_flag(ctx).await,
        "/api/icon-artwork/svg" => icons::get_artwork_svg(ctx).await,
        "/api/icon-artwork" => edits::get_artwork(ctx).await,
        "/api/icon-artwork/overrides" => edits::get_overrides(ctx).await,
        "/api/stroke-edits" => edits::get_stroke_edits(ctx).await,
        "/api/uploaded-icons" => icons::get_uploaded(ctx).await,
        "/api/reference-images" => files::get_reference_image(ctx).await,
        "/api/reviews" => reviews::get_reviews(ctx).await,
        "/api/review-detail" => reviews::get_review_detail(ctx).await,
        "/api/feedback" => reviews::get_feedback(ctx).await,
        "/api/feedback-feed" => reviews::get_feedback_feed(ctx).await,
        "/api/reviewer-stats" => reviews::get_reviewer_stats(ctx).await,
        "/api/pending-briefs" => briefs::list(ctx).await,
        "/api/primitives" | "/api/primitives/status" | "/api/primitives/summary" | "/api/primitives/briefs"
        | "/api/primitives/symbol-links" | "/api/primitives/prompt" | "/api/primitives/state" => primitives::get(ctx).await,
        "/api/combinations" => combinations::list(ctx).await,
        "/api/combinations/drawings" => combinations::drawings(ctx).await,
        "/api/combinations/candidates" => combinations::candidates(ctx).await,
        "/api/side-components" => edits::side_components(ctx).await,
        "/api/combinations/side/layouts" => side::layouts(ctx).await,
        "/api/combinations/side/pairs" => side_pairs::list(ctx).await,
        "/api/combinations/side/suggest" => side_pairs::suggest(ctx).await,
        _ if path == "/api/work" || path.starts_with("/api/work/") => work::read(ctx).await,
        _ if path.starts_with("/api/store/") => internal::store(ctx, None, "system").await,
        "/api/activity" => internal::read_activity(ctx).await,
        _ if path.starts_with("/primitives/") => files::primitive(ctx).await,
        _ if path.starts_with("/api/") => http::error(404, "Not found"),
        _ => files::static_file(ctx).await,
    }
}

const POST_ROUTES: &[&str] = &["/api/icon-families", "/api/icons/upload", "/api/reference-images", "/api/auth/login",
    "/api/auth/logout", "/api/icon-type", "/api/icon-flag", "/api/feedback/delete", "/api/feedback/edit", "/api/feedback",
    "/api/reviews", "/api/reject-combination", "/api/pending-briefs/complete", "/api/reject-combination/restore",
    "/api/primitives/status", "/api/primitives/briefs", "/api/primitives/symbol-link", "/api/work/claim", "/api/work/done",
    "/api/work/cannot-fix", "/api/work/abandon", "/api/work/result", "/api/catalog/push", "/api/icons/discard-record", "/api/activity",
    "/api/icon-artwork", "/api/stroke-edits", "/api/stroke-edits/validate", "/api/combination-experiment",
    "/api/combinations/side/recombine", "/api/combinations/side/preview", "/api/combinations/side/layout",
    "/api/combinations/side/layout/apply", "/api/combinations/side/pairs",
    "/api/combinations/parts", "/api/combinations/build"];

async fn post(ctx: &mut Ctx, path: &str) -> Result<Response> {
    if !POST_ROUTES.contains(&path) && !path.starts_with("/api/store/") {
        return http::not_found();
    }
    // Login identifies a human reviewer; sessionless API calls are system actions.
    let user = auth::current_user(ctx).await.unwrap_or_else(|| "system".to_string());
    if !http::same_origin(ctx) {
        return http::error(403, "Cross-origin feedback is not allowed");
    }
    let limit = match path {
        "/api/icons/upload" | "/api/icon-artwork" | "/api/combinations/build" => 2 * 1024 * 1024,
        "/api/reference-images" => MAX_REFERENCE_BODY,
        "/api/work/result" => MAX_WORK_RESULT_BODY,
        "/api/catalog/push" => MAX_PUSH_BODY,
        _ if path.starts_with("/api/store/") => 4 * 1024 * 1024,
        _ => MAX_BODY,
    };
    let too_large = if path == "/api/reference-images" { "Reference image is too large." } else { "Invalid request size" };
    let data = match http::json_body(ctx, limit, too_large).await {
        Ok(data) => data,
        Err(response) => return Ok(response),
    };
    let user = user.as_str();
    match path {
        "/api/auth/login" => auth::auth_action(ctx, true, &data).await,
        "/api/auth/logout" => auth::auth_action(ctx, false, &data).await,
        "/api/icon-families" => icons::post_family(ctx, &data, user).await,
        "/api/icons/upload" => icons::post_upload(ctx, &data, user).await,
        "/api/reference-images" => files::post_reference_image(ctx, &data, user).await,
        "/api/icon-type" => icons::post_icon_type(ctx, &data, user).await,
        "/api/icon-flag" => icons::post_icon_flag(ctx, &data, user).await,
        "/api/feedback/delete" => reviews::post_feedback_delete(ctx, &data, user).await,
        "/api/feedback/edit" => reviews::post_feedback_edit(ctx, &data, user).await,
        "/api/reject-combination" | "/api/pending-briefs/complete" | "/api/reject-combination/restore" =>
            briefs::action(ctx, path, &data, user).await,
        "/api/primitives/status" => primitives::post_status(ctx, &data, user).await,
        "/api/primitives/briefs" => primitives::post_brief(ctx, &data, user).await,
        "/api/primitives/symbol-link" => primitives::post_symbol_link(ctx, &data, user).await,
        "/api/catalog/push" => internal::catalog_push(ctx, &data, user).await,
        "/api/icons/discard-record" => internal::discard_record(ctx, &data, user).await,
        "/api/activity" => internal::activity(ctx, &data).await,
        "/api/icon-artwork" => edits::post_artwork(ctx, &data, user).await,
        "/api/stroke-edits" => edits::post_stroke_edits(ctx, &data, user, false).await,
        "/api/stroke-edits/validate" => edits::post_stroke_edits(ctx, &data, user, true).await,
        "/api/combination-experiment" => side::experiment(ctx, &data).await,
        "/api/combinations/side/preview" => side::preview(ctx, &data).await,
        "/api/combinations/side/recombine" => side::recombine(ctx, &data, user).await,
        "/api/combinations/side/layout" => side::save_layout(ctx, &data, user).await,
        "/api/combinations/side/layout/apply" => side::apply_layout(ctx, &data, user).await,
        "/api/combinations/side/pairs" => side_pairs::post(ctx, &data, user).await,
        "/api/combinations/parts" => combinations::post_part(ctx, &data, user).await,
        "/api/combinations/build" => combinations::build(ctx, &data, user).await,
        _ if path.starts_with("/api/work/") => work::action(ctx, path, &data, user).await,
        _ if path.starts_with("/api/store/") => internal::store(ctx, Some(&data), user).await,
        _ => reviews::post_review(ctx, path, &data, user).await,
    }
}
