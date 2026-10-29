//! Fill side pairs (migration 0023): the 64 side pairs combined from fill variants of their main and sub.
//!
//! Every read is bounded: lists are keyset pages on (state, sort_key) indexes with LIMIT (no OFFSET, no COUNT(*)),
//! picks are primary-key lookups, a part's fill variants come through icons_style_of (style_of, style), and the
//! totals are fill_counts rows that each write keeps in step. Each response says what it read in X-D1-Rows-Read, so
//! cloud/worker/tests/side_fill checks the budget on every route.
//!
//! GET  /api/side-fill/pairs?state=&after=&limit=&q=&original=1   a page of fill pairs with their picks (original=1: and
//!      each pair's normal Side combination 64 icon, side_combination64/<id>, by key)
//! GET  /api/side-fill/pair?id=                          one pair, its picks, its parts' variants, its neighbours
//! GET  /api/side-fill/parts?role=main|sub&status=&after=&limit=&q=   a page of the mains / subs the pairs use
//! POST /api/side-fill/pick {reference_id, rank?, append?|insert?, main, sub, layout?: {main, sub}, options?, version?}
//!      a pair's pick (main / sub: a fill variant icon of the part, or the part's own solo / sub icon for its outline):
//!      append: true adds it after the last (refused at 9 picks); insert: true puts it in at `rank`, the picks from there
//!      moving down one; otherwise it replaces the pick at `rank`, which must exist
//! POST /api/side-fill/build {reference_id, rank, version, svg, main: {icon, svg_sha256}, sub: {icon, svg_sha256}}
//!      save the pick's combined drawing (made in the browser by side-fill-combine.js) as its icon, Ready in Icon review
//! POST /api/side-fill/unpick {reference_id, rank, version?}       drop a pick (later ranks move up)
//! POST /api/side-fill/move {reference_id, rank, to, version?}      move a pick to another rank (the ones between shift)
//! Every pick / move / unpick gives the pair a new `version` and marks it edited on the site (the import leaves its
//! picks alone). A build names the version it combined, and is refused (409, nothing written) when the pair has
//! changed since; a pick / move / unpick that names one is refused the same way.

use std::cell::Cell;
use std::collections::HashMap;

use crate::args;
use crate::db::{self, Arg};
use crate::http::{self, Ctx};
use pictographic_core::side_fill as sql;
use pictographic_core::time::iso_utc;
use serde::de::DeserializeOwned;
use serde::Deserialize;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use worker::{Response, Result};

// A part's fill variants are icons of style fill in its own family (POST /api/icons/styled): solo/<name>--fill,
// solo/<name>--fill-region-3…, sub/<name>--fill, style_of the solo / sub icon, which is itself the outline.
const PART_STYLE: &str = "fill";
// A pick's combined icon is a Side combination 64 icon of style fill (as round / sharp icons are styles of a
// normal icon, migration 0019): key side_combination64/<reference_id>--fill[-n], style_of the pair's normal key.
const COMBINED_FAMILY: &str = "side_combination64";
const COMBINED_STYLE: &str = "fill";
const MAX_LIMIT: i64 = 120;
const MAX_RANK: i64 = 9;
const PAIR_STATES: [&str; 3] = ["picked", "unpicked", "uncombined"];
const PART_STATUSES: [&str; 7] = ["ready", "outline", "redrawn", "no-source", "no-fill", "not-drawn", "text"];

/// Statements that add up what D1 read for one request.
struct Reads<'a> { ctx: &'a Ctx, rows: Cell<usize> }

impl<'a> Reads<'a> {
    fn new(ctx: &'a Ctx) -> Self { Reads { ctx, rows: Cell::new(0) } }
    async fn all<T: DeserializeOwned>(&self, sql: &str, args: Vec<Arg>) -> Result<Vec<T>> {
        let result = db::stmt(&self.ctx.db, sql, args)?.all().await?;
        let read = result.meta().ok().flatten().and_then(|m| m.rows_read).unwrap_or(0);
        self.rows.set(self.rows.get() + read);
        result.results::<T>()
    }
    async fn first<T: DeserializeOwned>(&self, sql: &str, args: Vec<Arg>) -> Result<Option<T>> {
        Ok(self.all::<T>(sql, args).await?.into_iter().next())
    }
    /// The JSON answer, with the rows this request read.
    fn answer(&self, value: &Value) -> Result<Response> {
        let response = http::json(200, value)?;
        response.headers().set("X-D1-Rows-Read", &self.rows.get().to_string())?;
        Ok(response)
    }
}

fn limit_param(ctx: &Ctx, default: i64) -> Option<i64> {
    match ctx.param("limit") {
        None | Some("") => Some(default),
        Some(v) => v.parse::<i64>().ok().filter(|n| (1..=MAX_LIMIT).contains(n)),
    }
}
/// A concept / name prefix as a sort_key range (the same index as the page order).
fn prefix_range(q: Option<&str>) -> Option<(String, String)> {
    let q = q.map(str::trim).filter(|q| !q.is_empty())?.to_lowercase();
    Some((q.clone(), format!("{q}\u{ffff}")))
}

#[derive(Deserialize)]
struct PairRow { reference_id: String, sort_key: String, state: String, main_source: Option<String>, sub_source: Option<String>,
                 main_layout: Option<String>, sub_layout: Option<String>, note: Option<String>, concept: Option<String>, version: f64 }
#[derive(Deserialize)]
struct PickRow { reference_id: String, role: String, rank: f64, icon: Option<String>, layout: Option<String>, built_sha: Option<String>,
                 options: Option<String>, combined: Option<String>, icon_sha: Option<String>, icon_of: Option<String> }

// The pick's icon read once with it (by key): its current drawing and, for a fill variant, its label.
const PICK_COLUMNS: &str = "p.reference_id, p.role, p.rank, p.icon, p.layout, p.built_sha, p.options, p.combined, \
    i.svg_sha256 AS icon_sha, i.style_of AS icon_of";
const PICK_FROM: &str = "reference_part_fills p LEFT JOIN icons i ON i.key = p.icon";
#[derive(Deserialize)]
struct VariantRow { key: String, style_of: Option<String>, svg_sha256: Option<String>, review: Option<String> }

/// The fill variants of some solo / sub icons with their review status, by style_of (icons_style_of).
async fn variants_of(reads: &Reads<'_>, sources: &[&str]) -> Result<HashMap<String, Vec<Value>>> {
    let mut variants: HashMap<String, Vec<Value>> = HashMap::new();
    if sources.is_empty() { return Ok(variants); }
    let rows: Vec<VariantRow> = reads.all("SELECT i.key, i.style_of, i.svg_sha256, \
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review \
        FROM icons i WHERE i.style_of IN (SELECT value FROM json_each(?)) AND i.style = ?",
        args![json!(sources).to_string(), PART_STYLE]).await?;
    for row in rows {
        let Some(of) = row.style_of else { continue };
        let Some(label) = super::styled::fill_variant(&row.key, &of) else { continue };
        variants.entry(of.clone()).or_default().push(json!({"key": row.key, "variant": label, "svg_sha256": row.svg_sha256,
            "review": row.review.unwrap_or_else(|| "ready".into())}));
    }
    Ok(variants)
}
#[derive(Deserialize)]
struct CombinedRow { key: String, svg_sha256: Option<String>, build_failed: Option<f64>, review: Option<String> }
#[derive(Deserialize)]
struct CountRow { status: String, n: f64 }

const PAIR_COLUMNS: &str = "f.reference_id, f.sort_key, f.state, f.main_source, f.sub_source, f.main_layout, f.sub_layout, f.note, f.version, \
    (SELECT concept FROM \"references\" r WHERE r.reference_id = f.reference_id) AS concept";

async fn counts(reads: &Reads<'_>, scope: &str) -> Result<Value> {
    let rows: Vec<CountRow> = reads.all("SELECT status, n FROM fill_counts WHERE scope = ?", args![scope]).await?;
    Ok(Value::Object(rows.into_iter().map(|r| (r.status, json!(r.n as i64))).collect()))
}

/// The picks and their combined icons of some pairs, by key; with `variants` (the pair page) also every fill variant
/// of their parts with its review status. The grid leaves the variants out: a pick names its own label. With
/// `originals`, each pair's normal Side combination 64 icon (the outline pair the fill one is a style of).
async fn details(reads: &Reads<'_>, pairs: &[PairRow], variants_too: bool, originals: bool) -> Result<Vec<Value>> {
    let ids: Vec<&str> = pairs.iter().map(|p| p.reference_id.as_str()).collect();
    let picks: Vec<PickRow> = if ids.is_empty() { vec![] } else {
        reads.all(&format!("SELECT {PICK_COLUMNS} FROM {PICK_FROM} \
            WHERE p.reference_id IN (SELECT value FROM json_each(?)) ORDER BY p.reference_id, p.rank, p.role"),
            args![json!(ids).to_string()]).await?
    };
    let mains: Vec<&str> = pairs.iter().filter_map(|p| p.main_source.as_deref()).collect();
    let subs: Vec<&str> = pairs.iter().filter_map(|p| p.sub_source.as_deref()).collect();
    let variants = if variants_too { variants_of(reads, &[mains, subs].concat()).await? } else { HashMap::new() };
    let mut combined_keys: Vec<String> = picks.iter().filter_map(|p| p.combined.clone()).collect();
    if originals { combined_keys.extend(pairs.iter().map(|p| format!("{COMBINED_FAMILY}/{}", p.reference_id))); }
    let combined: HashMap<String, CombinedRow> = if combined_keys.is_empty() { HashMap::new() } else {
        reads.all::<CombinedRow>("SELECT i.key, i.svg_sha256, i.build_failed, \
                (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review \
            FROM icons i WHERE i.key IN (SELECT value FROM json_each(?))", args![json!(combined_keys).to_string()]).await?
            .into_iter().map(|r| (r.key.clone(), r)).collect()
    };
    let mut by_pair: HashMap<&str, Vec<&PickRow>> = HashMap::new();
    for pick in &picks { by_pair.entry(pick.reference_id.as_str()).or_default().push(pick); }
    Ok(pairs.iter().map(|p| {
        let mut ranks: Vec<Value> = vec![];
        let rows = by_pair.get(p.reference_id.as_str()).cloned().unwrap_or_default();
        let mut numbers: Vec<i64> = rows.iter().map(|r| r.rank as i64).collect();
        numbers.sort();numbers.dedup();
        for rank in numbers {
            let row_of = |role: &str| rows.iter().find(|r| r.rank as i64 == rank && r.role == role);
            let part = |role: &str| row_of(role).map(|r| json!({"icon": r.icon, "svg_sha256": r.icon_sha,
                "label": if r.icon == if role == "main" { p.main_source.clone() } else { p.sub_source.clone() } { Some("outline".to_string()) }
                         else { r.icon.as_deref().zip(r.icon_of.as_deref()).and_then(|(k, of)| super::styled::fill_variant(k, of)).map(str::to_string) },
                "layout": r.layout.as_deref().and_then(|l| serde_json::from_str::<Value>(l).ok()), "built_sha": r.built_sha}));
            let main = row_of("main");
            let options = main.and_then(|r| r.options.as_deref()).and_then(|o| serde_json::from_str::<Value>(o).ok());
            let built = main.and_then(|r| r.combined.as_ref()).and_then(|key| combined.get(key)).map(|c| json!({"key": c.key,
                "svg_sha256": c.svg_sha256, "build_failed": c.build_failed.unwrap_or(0.0) != 0.0,
                "review": c.review.clone().unwrap_or_else(|| "ready".into())}));
            ranks.push(json!({"rank": rank, "main": part("main"), "sub": part("sub"), "options": options, "combined": built}));
        }
        json!({"id": p.reference_id, "concept": p.concept, "state": p.state, "note": p.note, "sort_key": p.sort_key, "version": p.version as i64,
               "main": p.main_source, "sub": p.sub_source, "picks": ranks,
               "original": if originals { combined.get(&format!("{COMBINED_FAMILY}/{}", p.reference_id)).map(|c| json!({"key": c.key,
                   "svg_sha256": c.svg_sha256, "review": c.review.clone().unwrap_or_else(|| "ready".into())})) } else { None },
               "layout": {"main": p.main_layout.as_deref().and_then(|l| serde_json::from_str::<Value>(l).ok()),
                          "sub": p.sub_layout.as_deref().and_then(|l| serde_json::from_str::<Value>(l).ok())},
               "main_variants": p.main_source.as_ref().and_then(|m| variants.get(m)).cloned().unwrap_or_default(),
               "sub_variants": p.sub_source.as_ref().and_then(|s| variants.get(s)).cloned().unwrap_or_default()})
    }).collect())
}

/// A key for a pick's combined icon: the pair's `--fill` key when no other pick of the pair holds it, else `--fill-2`,
/// `--fill-3`… (kept on the pick, so a key never changes hands when ranks move up).
fn free_combined_key(reference_id: &str, taken: &[String]) -> String {
    let base = format!("{COMBINED_FAMILY}/{reference_id}--{COMBINED_STYLE}");
    if !taken.contains(&base) { return base; }
    (2..).map(|n| format!("{base}-{n}")).find(|k| !taken.contains(k)).unwrap()
}

/// Whether an icon key is a fill side pair's combined icon (side_combination64/<id>--fill[-n]).
pub fn is_fill_combined(key: &str) -> bool {
    key.strip_prefix("side_combination64/").and_then(|rest| rest.split_once("--fill")).is_some_and(|(id, n)| {
        !id.is_empty() && (n.is_empty() || n.strip_prefix('-').is_some_and(|d| !d.is_empty() && d.bytes().all(|b| b.is_ascii_digit())))
    })
}

/// GET /api/side-fill/pairs?state=&after=&limit=&q= → {pairs, next, counts}
pub async fn pairs(ctx: &Ctx) -> Result<Response> {
    let reads = Reads::new(ctx);
    let Some(limit) = limit_param(ctx, 60) else { return http::error(400, &format!("limit must be 1 to {MAX_LIMIT}.")) };
    let state = ctx.param("state").filter(|s| !s.is_empty() && *s != "all");
    if state.is_some_and(|s| !PAIR_STATES.contains(&s)) {
        return http::error(400, "state must be picked, unpicked or uncombined.");
    }
    let mut filters = vec![];
    let mut values: Vec<Arg> = vec![];
    if let Some(s) = state { filters.push("f.state = ?"); values.push(s.into()); }
    if let Some((from, to)) = prefix_range(ctx.param("q")) { filters.push("f.sort_key >= ? AND f.sort_key < ?"); values.push(from.into()); values.push(to.into()); }
    if let Some(after) = ctx.param("after").filter(|a| !a.is_empty()) { filters.push("f.sort_key > ?"); values.push(after.into()); }
    values.push((limit + 1).into());
    let filter = if filters.is_empty() { String::new() } else { format!("WHERE {}", filters.join(" AND ")) };
    let mut rows: Vec<PairRow> = reads.all(&format!("SELECT {PAIR_COLUMNS} FROM fill_pairs f {filter} ORDER BY f.sort_key LIMIT ?"), values).await?;
    let next = if rows.len() as i64 > limit { rows.truncate(limit as usize); rows.last().map(|r| r.sort_key.clone()) } else { None };
    let items = details(&reads, &rows, false, ctx.param("original") == Some("1")).await?;
    let totals = counts(&reads, "pairs").await?;
    reads.answer(&json!({"pairs": items, "next": next, "counts": totals}))
}

/// GET /api/side-fill/pair?id= → the pair (as in pairs) with {neighbours: {previous, next}}
pub async fn pair(ctx: &Ctx) -> Result<Response> {
    let reads = Reads::new(ctx);
    let Some(id) = ctx.param("id").filter(|i| !i.is_empty()) else { return http::error(400, "Give the pair id.") };
    let Some(row) = reads.first::<PairRow>(&format!("SELECT {PAIR_COLUMNS} FROM fill_pairs f WHERE f.reference_id = ?"), args![id]).await? else {
        return http::error(404, "Unknown fill side pair.");
    };
    #[derive(Deserialize)]
    struct Id { reference_id: String }
    let previous = reads.first::<Id>("SELECT reference_id FROM fill_pairs WHERE sort_key < ? ORDER BY sort_key DESC LIMIT 1", args![row.sort_key.clone()]).await?;
    let next = reads.first::<Id>("SELECT reference_id FROM fill_pairs WHERE sort_key > ? ORDER BY sort_key LIMIT 1", args![row.sort_key.clone()]).await?;
    let mut item = details(&reads, std::slice::from_ref(&row), true, true).await?.remove(0);
    item["neighbours"] = json!({"previous": previous.map(|p| p.reference_id), "next": next.map(|p| p.reference_id)});
    reads.answer(&item)
}

#[derive(Deserialize)]
struct PartRow { key: String, role: String, sort_key: String, status: String, note: Option<String>, text: Option<String>, pair_count: f64,
                 source_sha: Option<String>, source_review: Option<String> }

/// GET /api/side-fill/parts?role=main|sub&status=&after=&limit=&q= → {parts: [{…, variants}], next, counts}
pub async fn parts(ctx: &Ctx) -> Result<Response> {
    let reads = Reads::new(ctx);
    let role = if ctx.param("role") == Some("sub") { "sub" } else { "main" };
    let Some(limit) = limit_param(ctx, 48) else { return http::error(400, &format!("limit must be 1 to {MAX_LIMIT}.")) };
    let status = ctx.param("status").filter(|s| !s.is_empty() && *s != "all");
    if status.is_some_and(|s| !PART_STATUSES.contains(&s)) {
        return http::error(400, "Unknown part status.");
    }
    let mut filters = vec!["p.role = ?"];
    let mut values: Vec<Arg> = vec![role.into()];
    if let Some(s) = status { filters.push("p.status = ?"); values.push(s.into()); }
    if let Some((from, to)) = prefix_range(ctx.param("q")) { filters.push("p.sort_key >= ? AND p.sort_key < ?"); values.push(from.into()); values.push(to.into()); }
    if let Some(after) = ctx.param("after").filter(|a| !a.is_empty()) { filters.push("p.sort_key > ?"); values.push(after.into()); }
    values.push((limit + 1).into());
    // The part's own icon (its outline): current drawing and review, one lookup each by key.
    let mut rows: Vec<PartRow> = reads.all(&format!("SELECT p.key, p.role, p.sort_key, p.status, p.note, p.text, p.pair_count, \
            i.svg_sha256 AS source_sha, (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS source_review \
        FROM fill_parts p LEFT JOIN icons i ON i.key = p.key WHERE {} ORDER BY p.sort_key LIMIT ?",
        filters.join(" AND ")), values).await?;
    let next = if rows.len() as i64 > limit { rows.truncate(limit as usize); rows.last().map(|r| r.sort_key.clone()) } else { None };
    let keys: Vec<&str> = rows.iter().map(|r| r.key.as_str()).collect();
    let variants = variants_of(&reads, &keys).await?;
    let items: Vec<Value> = rows.iter().map(|r| json!({"key": r.key, "role": r.role, "status": r.status, "note": r.note, "text": r.text,
        "pair_count": r.pair_count as i64, "sort_key": r.sort_key, "source_sha256": r.source_sha,
        "source_review": r.source_review.clone().unwrap_or_else(|| "ready".into()),
        "variants": variants.get(&r.key).cloned().unwrap_or_default()})).collect();
    let totals = counts(&reads, role).await?;
    reads.answer(&json!({"parts": items, "next": next, "counts": totals}))
}

/// The pair (`id`) moved to the state `next` with its totals, from the state it has when the batch runs (sql::state_moves).
fn state_moves(ctx: &Ctx, id: &str, next: &str, now: &str) -> Result<Vec<worker::D1PreparedStatement>> {
    sql::state_moves(next).iter().map(|q| db::stmt(&ctx.db, q, args![id, now])).collect()
}

/// The pair version a request names, when it names one (a number; anything else is refused by the caller).
fn named_version(data: &Value) -> std::result::Result<Option<i64>, ()> {
    match data.get("version") { None | Some(Value::Null) => Ok(None), Some(v) => v.as_i64().map(Some).ok_or(()) }
}

/// Run a write batch: its results, or the 409 for a batch refused by a guard (the pair, its pick or a part drawing
/// changed) or by an output key another build just took. Nothing of a refused batch is written.
async fn write(ctx: &Ctx, statements: Vec<worker::D1PreparedStatement>) -> Result<std::result::Result<Vec<worker::D1Result>, Response>> {
    match db::batch(&ctx.db, statements).await {
        Ok(results) => Ok(Ok(results)),
        Err(error) if sql::is_guard_error(&error.to_string()) =>
            Ok(Err(http::error(409, "This pair changed since it was loaded (in another tab, or by someone else). Reload it and try again.")?)),
        Err(error) if error.to_string().contains("UNIQUE constraint failed: icons.key") =>
            Ok(Err(http::error(409, "Another build took this output's key at the same moment. Build again.")?)),
        Err(error) => Err(error),
    }
}

/// The version sql::EDITED committed in this batch (its RETURNING row), not one read later: another tab may have
/// saved since, and its version is not this write's.
fn committed_version(results: &[worker::D1Result], at: usize) -> Result<i64> {
    #[derive(Deserialize)]
    struct V { version: f64 }
    Ok(results.get(at).map(|r| r.results::<V>()).transpose()?.and_then(|rows| rows.into_iter().next()).map_or(0, |v| v.version as i64))
}

/// POST /api/side-fill/pick {reference_id, rank?, main, sub, layout?: {main, sub}}: the fill variant icons a pick
/// uses, checked against the pair's parts (each must be a fill variant of that part's source).
pub async fn pick(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" { return http::error(401, "Log in to pick fill variants."); }
    let reads = Reads::new(ctx);
    let Some(id) = data["reference_id"].as_str() else { return http::error(400, "Give the pair's reference_id.") };
    let Ok(version) = named_version(data) else { return http::error(400, "version must be the pair's version number.") };
    let (append, insert) = (data["append"] == json!(true), data["insert"] == json!(true));
    if append && insert { return http::error(400, "A pick is appended or inserted, not both."); }
    let Some(row) = reads.first::<PairRow>(&format!("SELECT {PAIR_COLUMNS} FROM fill_pairs f WHERE f.reference_id = ?"), args![id]).await? else {
        return http::error(404, "Unknown fill side pair.");
    };
    if version.is_some_and(|v| v != row.version as i64) {
        return http::error(409, "This pair changed since it was loaded (in another tab, or by someone else). Reload it and try again.");
    }
    #[derive(Deserialize)]
    struct Ranks { top: Option<f64>, here: Option<f64> }
    let asked = data["rank"].as_i64().unwrap_or(1);
    let ranks = reads.first::<Ranks>("SELECT max(rank) AS top, sum(rank = ?) AS here FROM reference_part_fills WHERE reference_id = ?",
        args![asked, id]).await?;
    let top = ranks.as_ref().and_then(|r| r.top).unwrap_or(0.0) as i64;
    let exists = ranks.as_ref().and_then(|r| r.here).unwrap_or(0.0) > 0.0;
    // Appending and inserting add a pick (at most 9); replacing changes one that is there.
    let rank = if append { top + 1 } else { asked };
    if (append || insert) && top >= MAX_RANK {
        return http::error(409, "A pair keeps at most 9 picks: remove one, or replace a pick instead.");
    }
    if !(1..=MAX_RANK).contains(&rank) || (insert && rank > top + 1) { return http::error(400, "rank must be 1 to 9, and a new pick goes at most one after the last."); }
    if !append && !insert && !exists {
        return http::error(409, "There is no pick at that rank to replace (it may have been removed): reload the pair, or add this as a new pick.");
    }
    #[derive(Deserialize)]
    struct Of { key: String, style: String, style_of: Option<String> }
    let mut chosen = vec![];
    for (role, source) in [("main", &row.main_source), ("sub", &row.sub_source)] {
        let Some(key) = data[role].as_str() else { return http::error(400, &format!("Give the {role} fill variant icon.")) };
        let found = reads.first::<Of>("SELECT key, style, style_of FROM icons WHERE key = ?", args![key]).await?;
        match found {
            // A fill variant of the pair's part, or the part's own solo / sub icon (its outline).
            Some(of) if (of.style == PART_STYLE && of.style_of.is_some() && &of.style_of == source)
                        || source.as_deref() == Some(of.key.as_str()) => chosen.push((role, of.key)),
            _ => return http::error(400, &format!("{key} is neither a fill variant of this pair's {role} nor the {role} itself.")),
        }
    }
    for role in ["main", "sub"] {
        if !layout_ok(&data["layout"][role]) {
            return http::error(400, &format!("The {role} layout must be a list of {{x, y, w, h}} boxes on the 64 grid."));
        }
    }
    let Some(options) = options_of(&data["options"]) else {
        return http::error(400, "options are {omit: [main element numbers], overlap: 'join' | 'clear', sub_scaled: true | false}.");
    };
    let now = iso_utc(chrono::Utc::now());
    let mut statements = vec![];
    if let Some(v) = version { statements.push(db::stmt(&ctx.db, sql::GUARD, args![id, v])?); }
    if insert {
        // Through negative ranks, so the primary key never collides mid-update.
        statements.push(db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = -(rank + 1) WHERE reference_id = ? AND rank >= ?", args![id, rank])?);
        statements.push(db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = -rank WHERE reference_id = ? AND rank < 0", args![id])?);
    }
    for (role, key) in &chosen {
        let layout = data["layout"][*role].clone();
        let layout_arg: Arg = if layout.is_null() { Arg::Null } else { layout.to_string().into() };
        let options_arg: Arg = match (&options, *role) { (Some(o), "main") => o.to_string().into(), _ => Arg::Null };
        // A changed pick needs building again: built_sha is cleared, the combined icon's key stays with the pick.
        statements.push(db::stmt(&ctx.db, "INSERT INTO reference_part_fills(reference_id, role, rank, icon, layout, options, updated_at, updated_by) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(reference_id, role, rank) DO UPDATE SET icon = excluded.icon, \
            layout = COALESCE(excluded.layout, reference_part_fills.layout), options = excluded.options, built_sha = NULL, \
            updated_at = excluded.updated_at, updated_by = excluded.updated_by",
            args![id, *role, rank, key.as_str(), layout_arg, options_arg, now.clone(), user])?);
    }
    statements.extend(state_moves(ctx, id, "'picked'", &now)?);
    let edited = statements.len();
    statements.push(db::stmt(&ctx.db, sql::EDITED, args![id, now.clone()])?);
    statements.push(db::activity(&ctx.db, user, "fill_pick", Some(id), db::details(vec![("rank", json!(rank)),
        ("main", json!(chosen[0].1)), ("sub", json!(chosen[1].1))]))?);
    let results = match write(ctx, statements).await? { Ok(results) => results, Err(refused) => return Ok(refused) };
    let version = committed_version(&results, edited)?;
    reads.answer(&json!({"reference_id": id, "rank": rank, "main": chosen[0].1, "sub": chosen[1].1, "updated_at": now, "version": version}))
}

/// POST /api/side-fill/unpick {reference_id, rank}: drop a pick; the later ranks move up one.
pub async fn unpick(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" { return http::error(401, "Log in to change fill picks."); }
    let reads = Reads::new(ctx);
    let Some(id) = data["reference_id"].as_str() else { return http::error(400, "Give the pair's reference_id.") };
    let Some(rank) = data["rank"].as_i64().filter(|r| (1..=MAX_RANK).contains(r)) else { return http::error(400, "rank must be 1 to 9.") };
    let Ok(version) = named_version(data) else { return http::error(400, "version must be the pair's version number.") };
    let Some(row) = reads.first::<PairRow>(&format!("SELECT {PAIR_COLUMNS} FROM fill_pairs f WHERE f.reference_id = ?"), args![id]).await? else {
        return http::error(404, "Unknown fill side pair.");
    };
    if version.is_some_and(|v| v != row.version as i64) {
        return http::error(409, "This pair changed since it was loaded (in another tab, or by someone else). Reload it and try again.");
    }
    #[derive(Deserialize)]
    struct Top { top: Option<f64> }
    let top = reads.first::<Top>("SELECT max(rank) AS top FROM reference_part_fills WHERE reference_id = ?", args![id]).await?
        .and_then(|t| t.top).unwrap_or(0.0) as i64;
    // The dropped pick's combined icon goes too unless someone reviewed it (then it stays in Icon review as it is).
    #[derive(Deserialize)]
    struct Orphan { combined: String, reviewed: f64 }
    let orphan = reads.first::<Orphan>("SELECT p.combined, EXISTS (SELECT 1 FROM reviews v WHERE v.icon = p.combined) AS reviewed \
        FROM reference_part_fills p WHERE p.reference_id = ? AND p.role = 'main' AND p.rank = ? AND p.combined IS NOT NULL",
        args![id, rank]).await?.filter(|o| o.reviewed == 0.0);
    let now = iso_utc(chrono::Utc::now());
    let left = if top >= rank { top - 1 } else { top };
    let state = if left > 0 { "picked" } else { "unpicked" };
    let mut statements = version.map(|v| db::stmt(&ctx.db, sql::GUARD, args![id, v])).transpose()?.into_iter().collect::<Vec<_>>();
    statements.extend([
        db::stmt(&ctx.db, "DELETE FROM reference_part_fills WHERE reference_id = ? AND rank = ?", args![id, rank])?,
        // Later ranks move up; done through a negative rank so the primary key never collides mid-update.
        db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = -(rank - 1) WHERE reference_id = ? AND rank > ?", args![id, rank])?,
        db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = -rank WHERE reference_id = ? AND rank < 0", args![id])?,
    ]);
    statements.extend(state_moves(ctx, id, sql::STATE_AFTER_UNPICK, &now)?);
    let edited = statements.len();
    statements.push(db::stmt(&ctx.db, sql::EDITED, args![id, now.clone()])?);
    if let Some(o) = &orphan {
        statements.extend(super::icon_list::remove(&ctx.db, &o.combined)?);
        statements.push(db::stmt(&ctx.db, "DELETE FROM icon_references WHERE icon = ?", args![o.combined.clone()])?);
        statements.push(db::stmt(&ctx.db, "DELETE FROM icons WHERE key = ? AND family = ? AND style = ?", args![o.combined.clone(), COMBINED_FAMILY, COMBINED_STYLE])?);
    }
    statements.push(db::activity(&ctx.db, user, "fill_unpick", Some(id), db::details(vec![("rank", json!(rank)),
        ("removed_icon", json!(orphan.as_ref().map(|o| o.combined.clone())))]))?);
    let results = match write(ctx, statements).await? { Ok(results) => results, Err(refused) => return Ok(refused) };
    let version = committed_version(&results, edited)?;
    reads.answer(&json!({"reference_id": id, "rank": rank, "picks_left": left, "state": state, "version": version}))
}

/// Layout boxes as reference_part_fills stores them: null, or a list of {x, y, w, h} (and `paths`) on the 64 grid.
fn layout_ok(layout: &Value) -> bool {
    let number = |v: &Value| v.as_f64().is_some_and(|n| n.is_finite() && (-64.0..=128.0).contains(&n));
    layout.is_null() || layout.as_array().is_some_and(|boxes| boxes.len() <= 64 && boxes.iter().all(|b| {
        ["x", "y", "w", "h"].iter().all(|k| number(&b[*k]))
            && (b["paths"].is_null() || b["paths"].as_array().is_some_and(|p| p.len() <= 200 && p.iter().all(|i| i.as_u64().is_some_and(|n| n < 1000))))
    }))
}

/// A pick's options, cleaned: Some(None) when there are none, None when they are not understood.
fn options_of(options: &Value) -> Option<Option<Value>> {
    if options.is_null() { return Some(None); }
    let object = options.as_object()?;
    if object.keys().any(|k| !["omit", "overlap", "sub_scaled"].contains(&k.as_str())) { return None; }
    let mut out = serde_json::Map::new();
    if let Some(omit) = object.get("omit").filter(|o| !o.is_null()) {
        let numbers: Vec<u64> = omit.as_array()?.iter().map(|n| n.as_u64().filter(|n| *n < 1000)).collect::<Option<_>>()?;
        if numbers.len() > 200 { return None; }
        if !numbers.is_empty() { out.insert("omit".into(), json!(numbers)); }
    }
    match object.get("overlap").and_then(Value::as_str) {
        None | Some("clear") => {}
        Some("join") => { out.insert("overlap".into(), json!("join")); }
        Some(_) => return None,
    }
    match object.get("sub_scaled") {
        None | Some(Value::Null) | Some(Value::Bool(false)) => {}
        Some(Value::Bool(true)) => { out.insert("sub_scaled".into(), json!(true)); }
        Some(_) => return None,
    }
    Some((!out.is_empty()).then(|| Value::Object(out)))
}

/// POST /api/side-fill/build {reference_id, rank, version, svg, main: {icon, svg_sha256}, sub: {icon, svg_sha256}}: a pick's
/// combined drawing, made in the browser from the pick's icons, saved as the pick's icon (a
/// side_combination64 icon of style fill), as combinations::build saves a side pair: the parts must still be the pick's and their
/// current drawings, the SVG passes the sanitizer, and a part not approved in Icon review marks it build_failed.
/// A new drawing has no review yet: Ready in Icon review. Reads the pair, its pick rows and the two parts (~10 rows).
/// `version` is the pair version the drawing was combined from: when a pick, move or unpick changed the pair since,
/// the build is refused and nothing is written (sql::GUARD first in the batch), so a stale tab cannot overwrite
/// newer work. A pick without an output yet gets the first `--fill[-n]` key no icon has, a kept reviewed output of
/// a removed pick included; it is inserted, not upserted, so two builds can never share it.
/// The push token builds as `side-fill import` (cloud/migrate/build_fill_pairs.mjs builds every imported pick once).
pub async fn build(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    let user = if user == "system" && super::internal::authorized(ctx) { "side-fill import" } else { user };
    if user == "system" { return http::error(401, "Log in to save fill side pairs."); }
    let reads = Reads::new(ctx);
    let Some(id) = data["reference_id"].as_str() else { return http::error(400, "Give the pair's reference_id.") };
    let Some(rank) = data["rank"].as_i64().filter(|r| (1..=MAX_RANK).contains(r)) else { return http::error(400, "rank must be 1 to 9.") };
    let Some(version) = data["version"].as_i64() else {
        return http::error(400, "Give the pair version the drawing was combined from (reload the pair).");
    };
    let Some(row) = reads.first::<PairRow>(&format!("SELECT {PAIR_COLUMNS} FROM fill_pairs f WHERE f.reference_id = ?"), args![id]).await? else {
        return http::error(404, "Unknown fill side pair.");
    };
    if version != row.version as i64 {
        return http::error(409, "This pair changed since it was loaded (in another tab, or by someone else). Reload it and build again.");
    }
    let picks: Vec<PickRow> = reads.all(&format!("SELECT {PICK_COLUMNS} FROM {PICK_FROM} WHERE p.reference_id = ?"), args![id]).await?;
    let mine = |role: &str| picks.iter().find(|p| p.rank as i64 == rank && p.role == role);
    let (Some(main), Some(sub)) = (mine("main"), mine("sub")) else { return http::error(409, "That pick is gone. Reload the pair.") };
    #[derive(Deserialize)]
    struct Drawing { key: String, svg_sha256: String, review: Option<String> }
    let keys: Vec<&str> = [&main.icon, &sub.icon].iter().filter_map(|k| k.as_deref()).collect();
    let drawings: Vec<Drawing> = reads.all("SELECT i.key, i.svg_sha256, \
            (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review \
        FROM icons i WHERE i.key IN (SELECT value FROM json_each(?))", args![json!(keys).to_string()]).await?;
    let mut errors = vec![];
    for (role, pick) in [("main", main), ("sub", sub)] {
        let sent = &data[role];
        if sent["icon"].as_str() != pick.icon.as_deref() {
            return http::error(409, &format!("The {role} of this pick changed since it was loaded. Reload the pair."));
        }
        let Some(drawing) = drawings.iter().find(|d| Some(d.key.as_str()) == pick.icon.as_deref()) else {
            return http::error(409, &format!("The {role} icon no longer exists. Pick another variant."));
        };
        if sent["svg_sha256"].as_str() != Some(drawing.svg_sha256.as_str()) {
            return http::error(409, &format!("The {role} {} was redrawn since it was loaded. Reload and build again.", drawing.key));
        }
        if drawing.review.as_deref() != Some("approve") {
            let name = drawing.key.split_once('/').map_or(drawing.key.as_str(), |(_, n)| n);
            errors.push(format!("{} {name} is not approved in Icon review", if role == "main" { "Main" } else { "Sub" }));
        }
    }
    let svg = data["svg"].as_str().unwrap_or("").to_string();
    if let Err(error) = pictographic_core::svg::safe_svg(&svg, 64) { return http::error(400, &error); }
    let sha = hex::encode(Sha256::digest(svg.as_bytes()));
    let fresh = main.combined.is_none();
    let key = match &main.combined {
        Some(own) => own.clone(),
        None => {
            #[derive(Deserialize)]
            struct Key { key: String }
            let mut taken: Vec<String> = picks.iter().filter(|p| p.rank as i64 != rank).filter_map(|p| p.combined.clone()).collect();
            taken.extend(reads.all::<Key>(sql::OUTPUT_KEYS, args![format!("{COMBINED_FAMILY}/{id}--{COMBINED_STYLE}")]).await?
                .into_iter().map(|k| k.key));
            free_combined_key(id, &taken)
        }
    };
    let icon_id = key.split_once('/').map_or(key.as_str(), |(_, n)| n).to_string();
    let now = iso_utc(chrono::Utc::now());
    let preview = format!("/api/icon-artwork/svg?icon={}&v={}", http::percent_encode(&key), &sha[..12]);
    let parts = json!({"main": main.icon, "sub": sub.icon});
    let style_of = format!("{COMBINED_FAMILY}/{id}");
    let (keyshape, keyshape_bounds) = keyshape_of(&[main.layout.as_deref(), sub.layout.as_deref()]);
    let record = json!({"parts": parts, "errors": errors, "reference_id": id, "rank": rank, "built_by": user, "built_at": now,
                        "icon_style": COMBINED_STYLE, "style_of": style_of, "keyshape": keyshape, "keyshape_bounds": keyshape_bounds});
    let listed = json!({"add": true, "key": key, "icon_id": icon_id, "name": row.concept, "family": COMBINED_FAMILY,
        "icon_style": COMBINED_STYLE, "style_of": style_of, "keyshape": keyshape, "keyshape_bounds": keyshape_bounds,
        "profile": "SIDE_COMBINATION64", "category": "Side", "canvas_size": 64, "svg_sha256": sha, "preview_url": preview,
        "build_failed": !errors.is_empty(), "validation": {"status": if errors.is_empty() { "valid" } else { "invalid" },
            "automatic_status": if errors.is_empty() { "pass" } else { "fail" }, "errors": errors},
        "original_sources": [], "combination_reference_id": id, "main_key": main.icon, "sub_key": sub.icon, "created_at": now,
        "created_at_source": "side-fill-pair", "uploaded_icon": false});
    let db = &ctx.db;
    let mut statements = vec![
        // The pair at the version, the pick still of these icons, each still the drawing combined: or nothing lands.
        db::stmt(db, sql::BUILD_GUARD, args![id, version, rank, main.icon.clone(), data["main"]["svg_sha256"].as_str().unwrap_or(""),
                                            sub.icon.clone(), data["sub"]["svg_sha256"].as_str().unwrap_or("")])?,
        // origin combination-build, as a side pair build: a catalog push leaves the icon and its list columns alone.
        db::stmt(db, "INSERT OR IGNORE INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES (?, ?, ?, 'combination-build', ?)",
                 args![sha.clone(), key.clone(), svg, now.clone()])?,
    ];
    statements.extend(super::icon_list::uncount(db, &key)?);
    // Only ever a fill icon's row: the guard keeps a write off the pair's normal side combination icon. A new key is
    // inserted plainly: if another build took it meanwhile, the batch fails instead of writing over that output.
    let upsert = if fresh { "" } else { " ON CONFLICT(key) DO UPDATE SET svg_sha256 = excluded.svg_sha256, \
        preview_url = excluded.preview_url, build_failed = excluded.build_failed, record = excluded.record \
        WHERE icons.family = excluded.family AND icons.style = excluded.style" };
    statements.push(db::stmt(db, &format!("INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, \
        build_failed, uploaded, record, pushed_at, style, style_of) VALUES (?, ?, (SELECT concept FROM \"references\" WHERE reference_id = ?), ?, 'Side', \
        'SIDE_COMBINATION64', 64, ?, ?, ?, 0, ?, ?, ?, ?){upsert}"),
        args![key.clone(), icon_id.clone(), id, COMBINED_FAMILY, sha.clone(), preview.clone(), !errors.is_empty(), record.to_string(), now.clone(),
              COMBINED_STYLE, style_of.clone()])?);
    statements.push(super::icon_list::index_statement(db, &key, &listed, Some("style = 'fill'"))?);
    statements.push(db::stmt(db, "UPDATE icons SET sort_name = COALESCE(NULLIF(name, ''), icon_id), \
        search = lower(COALESCE(name, '') || ' ' || icon_id || '   ' || COALESCE(category, '')) WHERE key = ? AND style = ?",
        args![key.clone(), COMBINED_STYLE])?);
    statements.extend(super::icon_list::recount(db, &key, true)?);
    statements.push(db::stmt(db, "INSERT OR IGNORE INTO icon_references(icon, reference_id) VALUES (?, ?)", args![key.clone(), id])?);
    for (role, part) in [("main", main), ("sub", sub)] {
        statements.push(db::stmt(db, "UPDATE reference_part_fills SET built_sha = ?, combined = CASE WHEN role = 'main' THEN ? ELSE combined END \
            WHERE reference_id = ? AND role = ? AND rank = ?",
            args![part.icon_sha.clone(), key.clone(), id, role, rank])?);
    }
    statements.push(db::activity(db, user, "fill_build", Some(&key), db::details(vec![("svg_sha256", json!(sha)), ("rank", json!(rank)),
        ("errors", json!(errors))]))?);
    if let Err(refused) = write(ctx, statements).await? { return Ok(refused); }
    reads.answer(&json!({"reference_id": id, "rank": rank, "key": key, "svg_sha256": sha, "build_failed": !errors.is_empty(),
                         "errors": errors, "preview_url": preview, "version": version}))
}

/// POST /api/side-fill/move {reference_id, rank, to}: a pick to another rank, keeping its icons, boxes and combined
/// icon; the picks between move one rank the other way. Rank 1 is the pair's output.
pub async fn move_pick(ctx: &Ctx, data: &Value, user: &str) -> Result<Response> {
    if user == "system" { return http::error(401, "Log in to change fill picks."); }
    let reads = Reads::new(ctx);
    let Some(id) = data["reference_id"].as_str() else { return http::error(400, "Give the pair's reference_id.") };
    let (Some(from), Some(to)) = (data["rank"].as_i64().filter(|r| (1..=MAX_RANK).contains(r)), data["to"].as_i64().filter(|r| (1..=MAX_RANK).contains(r))) else {
        return http::error(400, "rank and to must be 1 to 9.");
    };
    let Ok(version) = named_version(data) else { return http::error(400, "version must be the pair's version number.") };
    #[derive(Deserialize)]
    struct Top { top: Option<f64>, here: f64 }
    let found = reads.first::<Top>("SELECT max(rank) AS top, sum(rank = ?) AS here FROM reference_part_fills WHERE reference_id = ?", args![from, id]).await?;
    let Some(found) = found.filter(|f| f.here > 0.0) else { return http::error(404, "That pick is gone. Reload the pair.") };
    let to = to.min(found.top.unwrap_or(1.0) as i64);
    if to == from { return reads.answer(&json!({"reference_id": id, "rank": from, "to": to})); }
    let (low, high, step) = if to < from { (to, from - 1, 1) } else { (from + 1, to, -1) };
    let now = iso_utc(chrono::Utc::now());
    let mut statements = version.map(|v| db::stmt(&ctx.db, sql::GUARD, args![id, v])).transpose()?.into_iter().collect::<Vec<_>>();
    statements.extend([
        db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = CASE WHEN rank = ? THEN -? ELSE -(rank + ?) END \
            WHERE reference_id = ? AND (rank = ? OR rank BETWEEN ? AND ?)", args![from, to, step, id, from, low, high])?,
        db::stmt(&ctx.db, "UPDATE reference_part_fills SET rank = -rank WHERE reference_id = ? AND rank < 0", args![id])?,
    ]);
    let edited = statements.len();
    statements.push(db::stmt(&ctx.db, sql::EDITED, args![id, now])?);
    statements.push(db::activity(&ctx.db, user, "fill_move", Some(id), db::details(vec![("rank", json!(from)), ("to", json!(to))]))?);
    let results = match write(ctx, statements).await? { Ok(results) => results, Err(refused) => return Ok(refused) };
    let version = committed_version(&results, edited)?;
    reads.answer(&json!({"reference_id": id, "rank": from, "to": to, "version": version}))
}

/// The parts of a fill side pair's combined icon (`key`) that are not approved on their current drawing, as
/// "the main x and the sub y", or None: Icon review approves the combined icon only once both are (as for side pairs).
pub async fn unapproved_parts(db: &worker::D1Database, key: &str) -> Result<Option<String>> {
    #[derive(Deserialize)]
    struct Waiting { role: String, icon: Option<String> }
    let rows: Vec<Waiting> = db::all(db, "SELECT p.role, p.icon FROM reference_part_fills m \
        JOIN reference_part_fills p ON p.reference_id = m.reference_id AND p.rank = m.rank LEFT JOIN icons i ON i.key = p.icon \
        WHERE m.combined = ? AND m.role = 'main' \
          AND COALESCE((SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256), '') != 'approve' ORDER BY p.role",
        args![key]).await?;
    Ok((!rows.is_empty()).then(|| rows.iter().map(|w| format!("the {} {}", w.role,
        w.icon.as_deref().map_or("(none picked)", |k| k.split_once('/').map_or(k, |(_, n)| n)))).collect::<Vec<_>>().join(" and ")))
}

/// The keyshape a pick fills, as the fill side pair pages measure it (side-fill-overlay.js keyshape): the parts' boxes
/// (placed centerlines) plus the 4px stroke, the nearest of a 56 square, 60×44 or 44×60 when within 1px, else the
/// measured box as FREE. No profile defines Side combination 64 keyshapes, so Icon review reads them from the record.
fn keyshape_of(layouts: &[Option<&str>]) -> (String, Vec<f64>) {
    const KEYSHAPES: [(&str, [f64; 4]); 3] = [("SQUARE", [4.0, 4.0, 60.0, 60.0]), ("HRECT", [2.0, 10.0, 62.0, 54.0]), ("VRECT", [10.0, 2.0, 54.0, 62.0])];
    let mut b = [f64::INFINITY, f64::INFINITY, f64::NEG_INFINITY, f64::NEG_INFINITY];
    for layout in layouts.iter().flatten() {
        for g in serde_json::from_str::<Vec<Value>>(layout).unwrap_or_default() {
            let (x, y, w, h) = (g["x"].as_f64().unwrap_or(0.0), g["y"].as_f64().unwrap_or(0.0), g["w"].as_f64().unwrap_or(0.0), g["h"].as_f64().unwrap_or(0.0));
            b = [b[0].min(x - 2.0), b[1].min(y - 2.0), b[2].max(x + w + 2.0), b[3].max(y + h + 2.0)];
        }
    }
    if !b.iter().all(|v| v.is_finite()) { return ("FREE".into(), vec![0.0, 0.0, 64.0, 64.0]); }
    let (name, target, off) = KEYSHAPES.iter().map(|(n, k)| (*n, *k, k.iter().zip(b).map(|(a, v)| (a - v).abs()).fold(0.0, f64::max)))
        .min_by(|a, c| a.2.total_cmp(&c.2)).unwrap();
    if off <= 1.0 { (name.into(), target.to_vec()) } else { ("FREE".into(), b.to_vec()) }
}
