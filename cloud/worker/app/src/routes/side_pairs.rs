//! Side pairs saved on the cloud with a main (a solo icon) and a sub (a sub icon) picked by a reviewer:
//!
//! * made from a primitive classified as a combination on the primitives review page (key `<primitive uuid>`).
//!   Such a reference is not in the published `experiment-combination.json`, so it never reached the side page;
//!   its main / sub are prefilled from the classification's briefs.
//! * a published pair given another main / sub on the side page (key `<pair id>`, `published: true`). It replaces
//!   the published row until it is removed, which restores the icon and layout it had (`restore`).
//!
//! * store `side-pairs`: the pair row, shaped like a published one (side.rs reads it through `pair_rows`), with
//!   `custom: true`, `main_id` / `sub_id` set to the chosen icon keys (or `draw:` plus a name still to draw) and one
//!   unmeasured item per role. The graphics service measures both from their current drawings on every render.
//! * icon `side_combination64/<id>`: its Side combination 64 icon, drawn by side.rs `save`, listed in Icon review
//!   through `records` (icons.json only changes on a catalog push).

use super::side::{self, Parts};
use crate::args;
use crate::data;
use crate::db::{self, details};
use crate::http::{self, Ctx};
use pictographic_core::catalog::Icon;
use pictographic_core::time::iso_utc;
use serde::Deserialize;
use serde_json::{json, Value};
use std::collections::HashMap;
use worker::{Response, Result};

const STORE: &str = "side-pairs";
const FAMILY: &str = "side_combination64";
const POSITIONS: [(&str, &str); 8] = [("br", "Bottom-right"), ("bl", "Bottom-left"), ("tr", "Top-right"), ("tl", "Top-left"),
                                      ("ri", "Right"), ("le", "Left"), ("bo", "Bottom"), ("to", "Top")];
/// The review page's sub positions (primitives.html SUB_POSITIONS); `center` has no side position.
const SUB_POSITIONS: [(&str, &str); 8] = [("bottom-right", "br"), ("bottom-left", "bl"), ("top-right", "tr"), ("top-left", "tl"),
                                          ("right", "ri"), ("left", "le"), ("bottom", "bo"), ("top", "to")];
const CANDIDATES: usize = 10;
/// Words that name no subject in a brief ("Idea lightbulb", "Three-person team").
const FILLER: [&str; 12] = ["the", "and", "with", "icon", "small", "simple", "shape", "symbol", "outline", "mark", "for", "of"];

fn position_label(code: &str) -> &'static str {
    POSITIONS.iter().find(|(c, _)| *c == code).map(|(_, label)| *label).unwrap_or("Side")
}

/// The saved pair rows with these ids (primitive uuids).
pub async fn rows(ctx: &Ctx, ids: &[&str]) -> Result<HashMap<String, Value>> {
    #[derive(Deserialize)]
    struct Row { key: String, document: String }
    let ids: Vec<&str> = ids.iter().copied().filter(|id| id.len() == 36).collect();
    if ids.is_empty() {
        return Ok(HashMap::new());
    }
    let marks = vec!["?"; ids.len()].join(", ");
    let mut values = args![STORE];
    values.extend(ids.iter().map(|id| db::Arg::from(*id)));
    let rows: Vec<Row> = db::all(&ctx.db, &format!("SELECT key, document FROM store_documents WHERE store = ? AND key IN ({marks})"),
                                 values).await?;
    Ok(rows.into_iter().filter_map(|r| Some((r.key, serde_json::from_str(&r.document).ok()?))).collect())
}

/// The primitive (from primitives.json) and its classification: only a combination can become a pair.
async fn primitive(ctx: &Ctx, uuid: &str) -> Result<std::result::Result<(String, Value, Value), Response>> {
    let (resolved, _) = super::primitives::canonical(ctx, &[json!(uuid)]).await?;
    let uid = resolved[0].as_str().unwrap_or("").trim().to_lowercase();
    let Some(row) = super::primitives::rows(ctx).await?.iter().find(|r| r["uuid"].as_str() == Some(uid.as_str())).cloned() else {
        return Ok(Err(http::error(400, "Choose an existing primitive.")?));
    };
    #[derive(Deserialize)]
    struct Status { reason: String, main_brief: Option<String>, sub_brief: Option<String>, sub_position: Option<String> }
    let status: Option<Status> = db::first(&ctx.db, "SELECT reason, main_brief, sub_brief, sub_position FROM primitive_status WHERE uuid = ?",
                                           args![uid.clone()]).await?;
    let Some(status) = status.filter(|s| s.reason == "combination") else {
        return Ok(Err(http::error(409, "Classify this icon as a combination first.")?));
    };
    let brief = |text: &Option<String>| text.as_deref().and_then(|t| serde_json::from_str::<Value>(t).ok()).unwrap_or(Value::Null);
    let classification = json!({"main_brief": brief(&status.main_brief), "sub_brief": brief(&status.sub_brief),
                                "sub_position": status.sub_position});
    Ok(Ok((uid, row, classification)))
}

/// What a pair is saved for: a combination primitive (`uuid`), or a published pair (`pair_id`) given another
/// main / sub, with what prefills its form.
struct Target { id: String, concept: String, reference_url: Option<String>, published: bool,
                main_query: String, sub_query: String, position: Option<String>, sub_position: Value }

async fn target(ctx: &Ctx, uuid: &str, pair_id: &str) -> Result<std::result::Result<Target, Response>> {
    if !pair_id.is_empty() {
        let Some(row) = side::published_rows(ctx, &[pair_id]).await?.remove(pair_id) else {
            return Ok(Err(http::error(404, "Choose an available side pair.")?));
        };
        if row["native_text"] == json!(true) {
            return Ok(Err(http::error(409, "A native text pair keeps its typeface layout.")?));
        }
        let name = |group: &str| row[group][0]["icon"].as_str().unwrap_or("").replace('-', " ");
        return Ok(Ok(Target { id: pair_id.to_string(), concept: row["concept"].as_str().unwrap_or(pair_id).to_string(),
            reference_url: None, published: true, main_query: name("mains"), sub_query: name("subs"),
            position: row["position"].as_str().map(str::to_string), sub_position: Value::Null }));
    }
    let (uid, row, classification) = match primitive(ctx, uuid).await? {
        Ok(found) => found,
        Err(response) => return Ok(Err(response)),
    };
    let position = classification["sub_position"].as_str()
        .and_then(|p| SUB_POSITIONS.iter().find(|(name, _)| *name == p)).map(|(_, code)| code.to_string());
    Ok(Ok(Target { concept: row["concept"].as_str().unwrap_or(&uid).to_string(), reference_url: reference_url(&row), published: false,
        main_query: classification["main_brief"]["name"].as_str().unwrap_or("").to_string(),
        sub_query: classification["sub_brief"]["name"].as_str().unwrap_or("").to_string(),
        position, sub_position: classification["sub_position"].clone(), id: uid }))
}

fn reference_url(row: &Value) -> Option<String> {
    let path = row["path"].as_str()?;
    Some(format!("/primitives/{}", path.split('/').map(http::percent_encode).collect::<Vec<_>>().join("/")))
}

fn words(query: &str) -> Vec<String> {
    let mut out: Vec<String> = Vec::new();
    for word in query.to_lowercase().split(|c: char| !c.is_ascii_alphanumeric()) {
        // A plural matches its singular icon: "busts" searches "bust".
        let word = if word.len() > 3 && word.ends_with('s') && !word.ends_with("ss") { &word[..word.len() - 1] } else { word };
        if word.len() >= 3 && !FILLER.contains(&word) && !noise(word) && !out.iter().any(|w| w == word) {
            out.push(word.to_string());
        }
    }
    out.truncate(6);
    out
}

fn noise(part: &str) -> bool {
    part == "sub32" || part.bytes().all(|b| b.is_ascii_digit()) || (part.len() > 1 && part.starts_with('v') && part[1..].bytes().all(|b| b.is_ascii_digit()))
        || (part.len() >= 4 && part.bytes().all(|b| b.is_ascii_hexdigit()) && part.bytes().any(|b| b.is_ascii_digit()))
}

fn same_word(part: &str, word: &str) -> bool {
    part == word || (part.len() >= 4 && word.starts_with(part)) || (word.len() >= 4 && part.starts_with(word) && part.len() <= word.len() + 2)
}

/// Icons of `family` whose id or name shares the most words with `query`, approved and passing drawings first.
async fn search(ctx: &Ctx, family: &str, query: &str) -> Result<Vec<Value>> {
    let words = words(query);
    if words.is_empty() {
        return Ok(vec![]);
    }
    #[derive(Deserialize)]
    struct Row { key: String, icon_id: Option<String>, name: Option<String>, preview_url: Option<String>, build_failed: f64, review: Option<String> }
    let mut values = args![family];
    let mut conditions = Vec::new();
    for word in &words {
        // "lightbulb" also finds light-bulb.
        conditions.push("replace(i.icon_id, '-', '') LIKE ? OR i.name LIKE ?");
        values.push(db::Arg::from(format!("%{word}%")));
        values.push(db::Arg::from(format!("%{word}%")));
    }
    let rows: Vec<Row> = db::all(&ctx.db, &format!(
        "SELECT i.key, i.icon_id, i.name, i.preview_url, i.build_failed, \
         (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review \
         FROM icons i WHERE i.family = ? AND i.uploaded = 0 AND ({}) LIMIT 500", conditions.join(" OR ")), values).await?;
    let slug = words.join("-");
    let mut scored: Vec<(i64, Value)> = rows.into_iter().map(|r| {
        let id = r.icon_id.clone().unwrap_or_default();
        let text = format!("{} {} {}", id, id.replace('-', ""), r.name.clone().unwrap_or_default()).to_lowercase();
        let parts: Vec<&str> = id.split('-').filter(|part| !part.is_empty() && !noise(part)).collect();
        // A word that is a whole part of the id ("note" in music-note) counts more than one inside a part
        // ("note" in notebook); "music" stands for "musical", and "lightbulb" for light-bulb.
        let whole = words.iter().filter(|w| parts.iter().any(|part| same_word(part, w))
            || parts.windows(2).any(|pair| pair.concat() == **w)).count() as i64;
        let matched = words.iter().filter(|w| text.contains(w.as_str())).count() as i64 - whole;
        // The last word names the subject ("Open Padlock" is a padlock, not something open).
        let head = words.last().is_some_and(|w| parts.iter().any(|part| same_word(part, w)));
        // Other words in the id make a different subject; uuid, sub32 and version parts do not.
        let extra = id.split('-').filter(|part| !part.is_empty() && !noise(part)
            && !words.iter().any(|w| w.contains(part) || part.contains(w.as_str()))).count() as i64;
        let approved = r.review.as_deref() == Some("approve");
        let failed = r.build_failed != 0.0;
        // An approved drawing beats an unapproved one with the same words: only approved parts make a Ready pair.
        let score = whole * 25 + if head { 12 } else { 0 } + matched * 8 - (words.len() as i64 - whole - matched) * 6 + if id == slug { 30 } else if id.starts_with(&slug) { 10 } else { 0 }
            + if approved { 18 } else { 0 } - if failed { 18 } else { 0 } - extra * 4;
        (score, json!({"key": r.key, "icon_id": id, "name": r.name, "preview_url": r.preview_url,
                       "approved": approved, "build_failed": failed, "review": r.review}))
    }).collect();
    scored.sort_by(|a, b| b.0.cmp(&a.0).then_with(|| a.1["icon_id"].as_str().map(str::len).cmp(&b.1["icon_id"].as_str().map(str::len))));
    Ok(scored.into_iter().take(CANDIDATES).map(|(_, v)| v).collect())
}

/// GET /api/combinations/side/suggest?uuid=<primitive>|pair_id=<published pair>[&role=main|sub&q=<name>]: the main
/// (solo) and sub (sub) candidates, searched from the primitive's brief names or the published pair's icon names,
/// or from `q` for one role.
pub async fn suggest(ctx: &Ctx) -> Result<Response> {
    let t = match target(ctx, ctx.param("uuid").unwrap_or(""), ctx.param("pair_id").unwrap_or("")).await? {
        Ok(found) => found,
        Err(response) => return Ok(response),
    };
    if let (Some(role), Some(query)) = (ctx.param("role"), ctx.param("q")) {
        let family = match role { "main" => "solo", "sub" => "sub", _ => return http::error(400, "Choose main or sub.") };
        return http::json(200, &json!({"role": role, "query": query, "candidates": search(ctx, family, query).await?}));
    }
    let pair = rows(ctx, &[t.id.as_str()]).await?.remove(&t.id);
    http::json(200, &json!({
        "uuid": t.id, "concept": t.concept, "reference_url": t.reference_url, "published": t.published,
        "sub_position": t.sub_position, "position": t.position,
        "main": {"query": t.main_query, "candidates": search(ctx, "solo", &t.main_query).await?},
        "sub": {"query": t.sub_query, "candidates": search(ctx, "sub", &t.sub_query).await?},
        "pair": pair,
    }))
}

fn item(icon: &Icon, role: &str) -> Value {
    let mut item = json!({"icon": icon.icon_id.clone().unwrap_or_default(), "family": icon.family, "model_key": icon.key,
                          "preview_url": icon.preview_url});
    if role == "sub" {
        item["sizing_kind"] = json!("symbol");
    }
    item
}

/// The Side combination 64 icon row of a pair (recombine_side_pairs.py family_record's columns).
fn icon_row(ctx: &Ctx, pair: &Value, parts: &Parts, now: &str) -> Result<worker::D1PreparedStatement> {
    let id = pair["id"].as_str().unwrap_or("");
    let key = format!("{FAMILY}/{id}");
    let sources = pair["reference_url"].as_str().map(|url| json!([{"url": url, "format": "SVG", "source_path": url}])).unwrap_or(json!([]));
    let record = json!({"main_key": parts.main_key, "sub_key": parts.sub_key, "errors": []});
    db::stmt(&ctx.db, "INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, \
        original_sources, build_failed, uploaded, record, pushed_at) VALUES (?, ?, ?, ?, ?, 'SIDE_COMBINATION64', 64, '', ?, ?, 1, 0, ?, ?) \
        ON CONFLICT(key) DO UPDATE SET name = excluded.name, category = excluded.category, \
        original_sources = CASE WHEN excluded.original_sources = '[]' THEN icons.original_sources ELSE excluded.original_sources END \
        WHERE icons.family = 'side_combination64' AND icons.uploaded = 0",
        args![key.clone(), id, pair["concept"].as_str().unwrap_or(""), FAMILY, position_label(pair["position"].as_str().unwrap_or("")),
              format!("combination-previews/{id}.svg"), sources.to_string(), record.to_string(), now])
}

/// What was generated: the main, sub and position the pair's icon was drawn from.
fn generated_mark(pair: &Value, now: &str) -> Value {
    json!({"main": pair["main_id"], "sub": pair["sub_id"], "position": pair["position"], "at": now})
}

/// Statements side.rs `save` adds for a pair made here: its icon row (created on the first drawing) and
/// the mark of what was generated. Any save counts: Generate here, or Recombine / a layout on the side page.
pub(super) fn saving(ctx: &Ctx, pair: &Value, parts: &Parts, now: &str) -> Result<Vec<worker::D1PreparedStatement>> {
    Ok(vec![
        icon_row(ctx, pair, parts, now)?,
        db::stmt(&ctx.db, "UPDATE store_documents SET document = json_set(document, '$.generated', json(?)) WHERE store = ? AND key = ?",
                 args![generated_mark(pair, now).to_string(), STORE, pair["id"].as_str().unwrap_or("")])?,
    ])
}

/// Where the pair stands: a part still to be drawn, both picked but not (or not like this) generated, or generated.
fn status(pair: &Value) -> &'static str {
    let (main, sub) = (pair["mains"].as_array().is_some_and(|m| !m.is_empty()), pair["subs"].as_array().is_some_and(|s| !s.is_empty()));
    let generated = &pair["generated"];
    match (main, sub) {
        (false, false) => "needs_both",
        (false, true) => "needs_main",
        (true, false) => "needs_sub",
        _ if generated.is_object() && generated["main"] == pair["main_id"] && generated["sub"] == pair["sub_id"]
            && generated["position"] == pair["position"] => "generated",
        _ => "waiting",
    }
}

/// POST /api/combinations/side/pairs {uuid, main, sub, main_name, sub_name, position, generate}: save the primitive's pair.
/// Each part is a picked icon (`main` / `sub`: a solo / sub icon key) or, when none fits yet, the name of the icon to
/// draw (`main_name` / `sub_name`). `generate: true` also draws its combined icon, which needs both icons and a position.
/// {uuid, remove: true} deletes the pair, its saved layout and its icon.
pub async fn post(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" {
        return http::error(401, "Log in to make side pairs.");
    }
    let t = match target(ctx, data["uuid"].as_str().unwrap_or(""), data["pair_id"].as_str().unwrap_or("")).await? {
        Ok(found) => found,
        Err(response) => return Ok(response),
    };
    let uid = t.id.clone();
    let key = format!("{FAMILY}/{uid}");
    let now = iso_utc(chrono::Utc::now());
    let previous = side::document(ctx, STORE, &uid).await?;
    // The icon and layout of an earlier drawing that no longer matches the pair.
    let forget = |ctx: &Ctx| -> Result<Vec<worker::D1PreparedStatement>> { Ok(vec![
        db::stmt(&ctx.db, "DELETE FROM store_documents WHERE store = 'side-layouts' AND key = ?", args![uid.clone()])?,
        db::stmt(&ctx.db, "DELETE FROM icons WHERE key = ? AND family = ? AND uploaded = 0", args![key.clone(), FAMILY])?,
    ]) };
    if data["remove"] == json!(true) && t.published {
        // Back to the published pair: the icon and layout it had before it was first changed.
        let restore = previous.as_ref().map(|p| p["restore"].clone()).unwrap_or(Value::Null);
        let mut statements = vec![db::stmt(&ctx.db, "DELETE FROM store_documents WHERE store = ? AND key = ?", args![STORE, uid.clone()])?];
        let icon = &restore["icon"];
        if icon.is_object() {
            statements.push(db::stmt(&ctx.db, "UPDATE icons SET svg_sha256 = ?, build_failed = ?, record = ? WHERE key = ? AND family = ? AND uploaded = 0",
                args![icon["svg_sha256"].as_str().unwrap_or(""), icon["build_failed"].as_f64().unwrap_or(0.0) != 0.0,
                      icon["record"].as_str().unwrap_or("{}"), key.clone(), FAMILY])?);
        }
        statements.push(super::internal::put_statement(&ctx.db, "side-layouts", &uid, &restore["layout"], None, user, &now)?);
        statements.push(db::activity(&ctx.db, user, "side_pair_restored", Some(&key), details(vec![("pair", json!(uid))]))?);
        db::batch(&ctx.db, statements).await?;
        return http::json(200, &json!({"uuid": uid, "removed": true, "restored": true}));
    }
    if data["remove"] == json!(true) {
        let mut statements = forget(ctx)?;
        statements.push(db::stmt(&ctx.db, "DELETE FROM store_documents WHERE store = ? AND key = ?", args![STORE, uid.clone()])?);
        statements.push(db::activity(&ctx.db, user, "side_pair_removed", Some(&key), details(vec![("primitive", json!(uid))]))?);
        db::batch(&ctx.db, statements).await?;
        return http::json(200, &json!({"uuid": uid, "removed": true}));
    }
    let generate = data["generate"] == json!(true);
    let position = data["position"].as_str().unwrap_or("");
    if !(position.is_empty() || POSITIONS.iter().any(|(code, _)| *code == position)) || (generate && position.is_empty()) {
        return http::error(400, "Choose where the sub sits: one of the eight side positions.");
    }
    let mut pair = json!({"id": uid, "concept": t.concept, "type": "side", "custom": true, "published": t.published,
        "position": position, "reference_url": t.reference_url, "mains": [], "subs": [],
        "created_by": user, "created_at": now, "updated_by": user, "updated_at": now});
    let mut to_draw = Vec::new();
    for (role, group, family, label) in [("main", "mains", "solo", "main"), ("sub", "subs", "sub", "sub")] {
        let wanted = data[role].as_str().unwrap_or("").trim();
        let name = data[format!("{role}_name")].as_str().unwrap_or("").trim();
        if !wanted.is_empty() {
            let Some(icon) = data::icon(&ctx.db, wanted, true).await?.filter(|i| !i.uploaded && i.family.as_deref() == Some(family)) else {
                return http::error(400, &format!("{wanted} is not a {family} icon. Pick the {label} from the list."));
            };
            pair[group] = json!([item(&icon, role)]);
            pair[format!("{role}_id")] = json!(icon.key);
        } else if !name.is_empty() && name.chars().count() <= 120 {
            // Not drawn yet: tracked by name until an icon is picked.
            pair[format!("{role}_id")] = json!(format!("draw:{uid}:{role}"));
            pair[format!("{role}_name")] = json!(name);
            to_draw.push(format!("the {label} ({name})"));
        } else {
            return http::error(400, &format!("Pick the {label} icon, or type the name of the {label} to draw (up to 120 characters)."));
        }
    }
    if generate && !to_draw.is_empty() {
        return http::error(400, &format!("Pick both icons before generating: {} still needs drawing.", to_draw.join(" and ")));
    }
    if let Some(previous) = &previous {
        pair["created_at"] = previous["created_at"].clone();
        pair["created_by"] = previous["created_by"].clone();
        pair["generated"] = previous["generated"].clone();
        pair["restore"] = previous["restore"].clone();
    } else if t.published {
        // First change of a published pair: what it had, so that removing the change restores it.
        #[derive(Deserialize)]
        struct IconRow { svg_sha256: String, build_failed: f64, record: String }
        let icon: Option<IconRow> = db::first(&ctx.db, "SELECT svg_sha256, build_failed, record FROM icons WHERE key = ? AND family = ?",
                                              args![key.clone(), FAMILY]).await?;
        pair["restore"] = json!({
            "icon": icon.map(|i| json!({"svg_sha256": i.svg_sha256, "build_failed": i.build_failed, "record": i.record})),
            "layout": side::document(ctx, "side-layouts", &uid).await?,
        });
    }
    let action = if previous.is_some() { "side_pair_changed" } else { "side_pair_created" };
    let log = |ctx: &Ctx, pair: &Value| db::activity(&ctx.db, user, action, Some(&key), details(vec![
        ("main", pair["main_id"].clone()), ("sub", pair["sub_id"].clone()), ("position", json!(position)), ("generate", json!(generate))]));
    if !generate {
        let mut statements = vec![super::internal::put_statement(&ctx.db, STORE, &uid, &pair, None, user, &now)?, log(ctx, &pair)?];
        // Saved differently from its drawing: the old combined icon goes, until the pair is generated again.
        if pair["generated"].is_object() && status(&pair) != "generated" {
            if !t.published {
                statements.extend(forget(ctx)?);
            }
            pair["generated"] = Value::Null;
            statements[0] = super::internal::put_statement(&ctx.db, STORE, &uid, &pair, None, user, &now)?;
        }
        db::batch(&ctx.db, statements).await?;
        return http::json(200, &json!({"pair": pair, "status": status(&pair)}));
    }
    let parts = match side::parts(ctx, &pair, None, None).await? {
        Ok(parts) => parts,
        Err(response) => return Ok(response),
    };
    for role in ["main", "sub"] {
        if parts.documents[role].is_null() {
            return http::error(422, &format!("The {role} has no drawing on production yet."));
        }
    }
    // Render before storing anything: a pair the engine cannot combine is not saved.
    let result = match side::render(ctx, &pair, &parts, &Value::Null, false).await? {
        Ok(result) => result,
        Err(response) => return Ok(response),
    };
    db::batch(&ctx.db, vec![super::internal::put_statement(&ctx.db, STORE, &uid, &pair, None, user, &now)?, log(ctx, &pair)?]).await?;
    // A changed main or sub starts from automatic placement again; `saving` creates the icon and marks it generated.
    let saved = side::save(ctx, &pair, &parts, &Value::Null, &result, user).await?;
    let reasons = side::pair_reasons(ctx, &parts).await?;
    pair["generated"] = generated_mark(&pair, &now);
    http::json(200, &json!({"pair": pair, "status": status(&pair), "result": result, "saved": saved, "errors": reasons}))
}

/// GET /api/combinations/side/pairs: every pair made from a primitive, with its status and its main / sub drawings'
/// current previews and check state (for the side page and the review cards).
pub async fn list(ctx: &Ctx) -> Result<Response> {
    #[derive(Deserialize)]
    struct Row { document: String }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT document FROM store_documents WHERE store = ? ORDER BY updated_at DESC", args![STORE]).await?;
    #[derive(Deserialize)]
    struct Drawing { key: String, preview_url: Option<String>, svg_sha256: String, build_failed: f64, review: Option<String> }
    let drawings: Vec<Drawing> = db::all(&ctx.db, "SELECT i.key, i.preview_url, i.svg_sha256, i.build_failed, \
        (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review FROM icons i \
        WHERE i.key IN (SELECT json_extract(document, '$.main_id') FROM store_documents WHERE store = ?1 \
                        UNION SELECT json_extract(document, '$.sub_id') FROM store_documents WHERE store = ?1)", args![STORE]).await?;
    let drawings: HashMap<String, Value> = drawings.into_iter().map(|d| (d.key.clone(), json!({
        "key": d.key, "preview_url": d.preview_url, "svg_sha256": d.svg_sha256, "build_failed": d.build_failed != 0.0, "review": d.review,
    }))).collect();
    let pairs: Vec<Value> = rows.into_iter().filter_map(|r| serde_json::from_str::<Value>(&r.document).ok()).map(|pair| {
        let drawing = |field: &str| pair[field].as_str().and_then(|k| drawings.get(k)).cloned().unwrap_or(Value::Null);
        json!({"row": pair, "status": status(&pair), "main": drawing("main_id"), "sub": drawing("sub_id")})
    }).collect();
    http::json(200, &json!({"pairs": pairs}))
}

/// Icon review records for pairs made here: complete records (`add`), since icons.json lists them only
/// after a catalog push. side.rs `overlays` then sets their drawing and check state like any saved pair.
pub async fn records(ctx: &Ctx) -> Result<Vec<Value>> {
    #[derive(Deserialize)]
    struct Row { key: String, icon_id: String, name: Option<String>, category: Option<String>, svg_sha256: String,
                 original_sources: String, record: String, created_at: Option<String> }
    let rows: Vec<Row> = db::all(&ctx.db, "SELECT i.key, i.icon_id, i.name, i.category, i.svg_sha256, i.original_sources, i.record, \
        json_extract(s.document, '$.created_at') AS created_at FROM icons i JOIN store_documents s ON s.store = ? AND s.key = i.icon_id \
        WHERE i.family = ? AND i.svg_sha256 != ''", args![STORE, FAMILY]).await?;
    Ok(rows.into_iter().map(|r| {
        let record: Value = serde_json::from_str(&r.record).unwrap_or(json!({}));
        json!({"add": true, "key": r.key, "icon_id": r.icon_id, "name": r.name, "family": FAMILY, "profile": "SIDE_COMBINATION64",
               "category": r.category, "canvas_size": 64, "svg_sha256": r.svg_sha256,
               "preview_url": format!("combination-previews/{}.svg?v={}", r.icon_id, &r.svg_sha256[..12.min(r.svg_sha256.len())]),
               "original_sources": serde_json::from_str::<Value>(&r.original_sources).unwrap_or(json!([])),
               "main_key": record["main_key"], "sub_key": record["sub_key"], "tags": [], "keywords": [], "aliases": [], "description": "",
               "created_at": r.created_at, "created_at_source": "side-pair"})
    }).collect())
}
