//! Icon review's list as SQL over D1 (GET /api/icons): the filters, review states, counts and pages gallery.html
//! used to work out in the browser over the whole catalog. Each rule names the page function it mirrors.
//!
//! Review state (`iconState`): an active split or any rejected revision rejects; otherwise the current revision's
//! review row (re-generated is ready, disapproved and claimed are "pending"), and a failing build waiting for a
//! decision is "failed". A side / container combination whose build failed shows as failed unless rejected or
//! disapproved (the page compared /api/reviews statuses, where a disapproval is "pending" and a claim "claimed").

use serde_json::{json, Value};
use std::collections::HashMap;

pub type Args = Vec<Value>;

pub const STATES: [&str; 5] = ["ready", "failed", "pending", "approve", "rejected"];
const SORTS: [&str; 9] = ["name", "newest", "oldest", "modified-newest", "modified-oldest", "strokes-asc", "strokes-desc",
                          "segments-asc", "segments-desc"];
pub const PAGE_SIZES: [i64; 4] = [24, 48, 96, 192];

/// The page's filters, by the names its URL uses.
#[derive(Clone, Debug, Default, PartialEq)]
pub struct Params {
    pub family: String,
    pub category: Option<String>,
    /// "uncategorized": no category, or one of the `_uncategorized_N` placeholders (the approved collection's group).
    pub category_group: String,
    pub q: String,
    /// Words that must all appear (the approved collection's and symbol pickers' search), unlike `q`'s phrase.
    pub terms: Vec<String>,
    /// Exact profile (Design Document examples).
    pub profile: String,
    pub status: String,
    pub reviewer: String,
    pub icon_feedback_by: String,
    pub symmetry: String,
    pub strokes: String,
    pub keyshape: String,
    pub author: String,
    pub revision: String,
    pub reference: String,
    pub artwork: String,
    pub reason: String,
    pub pending_feedback: String,
    pub sort: String,
    /// "All versions": icons grouped by version, paged by group.
    pub versions: bool,
    pub offset: i64,
    pub limit: i64,
}

fn one_of(value: Option<&str>, allowed: &[&str]) -> String {
    value.filter(|v| allowed.contains(v)).unwrap_or("").to_string()
}

impl Params {
    /// From the query string; unknown values are ignored like the page's selects ignore them.
    pub fn from_query(get: impl Fn(&str) -> Option<String>) -> Params {
        let text = |name: &str| get(name).map(|v| v.trim().to_string()).unwrap_or_default();
        let opt = |name: &str| get(name);
        let mut params = Params {
            family: text("family"),
            category: opt("category").filter(|c| !c.is_empty()),
            category_group: one_of(opt("category_group").as_deref(), &["uncategorized"]),
            q: text("q").to_lowercase(),
            terms: text("terms").to_lowercase().split_whitespace().map(str::to_string).collect(),
            profile: text("profile"),
            status: one_of(opt("status").as_deref(), &STATES),
            reviewer: text("reviewer"),
            icon_feedback_by: text("icon_feedback_by"),
            symmetry: one_of(opt("symmetry").as_deref(), &["symmetric", "vertical", "horizontal", "both", "asymmetric", "unknown"]),
            strokes: one_of(opt("strokes").as_deref(), &["1-3", "4-6", "7-10", "11+", "unknown"]),
            keyshape: text("keyshape"),
            author: text("author"),
            revision: one_of(opt("revision").as_deref(), &["original", "variant"]),
            reference: one_of(opt("reference").as_deref(), &["with", "without"]),
            artwork: one_of(opt("artwork").as_deref(), &["original", "modified", "edited", "uploaded", "work_fix"]),
            reason: one_of(opt("reason").as_deref(), &["bad-stroke", "manual-fix-request", "meaning", "other", "missing", "cannot-fix"]),
            pending_feedback: one_of(opt("pending_feedback").as_deref(), &["with", "without"]),
            sort: one_of(opt("sort").as_deref(), &SORTS),
            versions: opt("view").as_deref() == Some("versions"),
            offset: opt("offset").and_then(|v| v.parse().ok()).filter(|v: &i64| *v >= 0).unwrap_or(0),
            limit: opt("limit").and_then(|v| v.parse().ok()).filter(|v| PAGE_SIZES.contains(v)).unwrap_or(48),
        };
        if params.sort.is_empty() {
            params.sort = "name".into();
        }
        // restoreURL: a disapproval reason shows the Disapproved tab.
        if !params.reason.is_empty() {
            params.status = "pending".into();
        }
        if params.status != "pending" {
            params.pending_feedback.clear();
        }
        params
    }

    /// `facetFields` plus the reviewer filters: any of them turns off version grouping.
    fn narrowed(&self) -> bool {
        [&self.symmetry, &self.strokes, &self.reason, &self.keyshape, &self.revision, &self.reference, &self.artwork,
         &self.author, &self.reviewer, &self.icon_feedback_by].iter().any(|v| !v.is_empty())
    }

    /// `filteredIcons`: whether "All versions" shows whole version groups.
    pub fn grouped(&self) -> bool {
        self.versions && !self.narrowed() && self.status != "rejected" && !(self.status == "pending" && !self.pending_feedback.is_empty())
    }
}

/// Every icon matching `pre` (conditions on `icons i`), with its review state, decision actor, shown artwork and
/// current measurements, as the CTE `u` (materialized once per statement). Joins, not correlated subqueries: each
/// lookup runs once per icon.
fn icons_cte(pre: &str) -> String {
    // `+x.status`: look rejected revisions up by icon (the primary key), not by the status index.
    format!("WITH s AS MATERIALIZED (
  SELECT i.key, i.icon_id, i.family, i.category, i.svg_sha256, i.build_failed, i.uploaded, i.sort_name, i.keyshape,
         i.author, i.side_role, i.stroke_count,
         i.segment_count, i.created_ms, i.modified_ms, i.version_group, i.version, i.variant, i.has_original,
         i.artwork_source, i.symmetry, i.symmetry_sha,
         r.status AS row_status, r.updated_by AS row_by, r.updated_at AS row_at, r.worker, r.claimed_at, r.note,
         sp.icon IS NOT NULL AS split, sp.created_by AS split_by,
         -- The latest rejection of any revision ('' when no one is recorded): one lookup for the flag and the actor.
         (SELECT COALESCE(x.updated_by, '') FROM reviews x WHERE x.icon = i.key AND +x.status = 'rejected' ORDER BY x.updated_at DESC LIMIT 1) AS rejected_by,
         CASE WHEN json_extract(d.document, '$.source_svg_sha256') IS NOT NULL
               AND (json_extract(d.document, '$.source_svg_sha256') = i.svg_sha256 OR g.svg_sha256 IS NULL)
              THEN COALESCE(json_extract(d.document, '$.source_mode'), 'use_org') END AS picked
  FROM icons i
  LEFT JOIN reviews r ON r.icon = i.key AND r.svg_sha256 = i.svg_sha256
  LEFT JOIN split_requests sp ON sp.icon = i.key AND sp.svg_sha256 = i.svg_sha256 AND sp.active = 1
  LEFT JOIN store_documents d ON d.store = 'icon-artwork' AND d.key = i.key AND i.uploaded = 0
  LEFT JOIN icon_graphs g ON g.svg_sha256 = i.svg_sha256{pre}),
t AS (
  SELECT s.*, CASE WHEN split OR rejected_by IS NOT NULL THEN 'rejected' ELSE COALESCE(row_status, 'ready') END AS decision,
         CASE WHEN split THEN split_by WHEN rejected_by IS NOT NULL THEN NULLIF(rejected_by, '') ELSE row_by END AS actor,
         COALESCE(picked, artwork_source, 'use_org') AS mode
  FROM s),
u AS MATERIALIZED (
  SELECT t.*,
         CASE WHEN decision = 'rejected' THEN 'rejected'
              WHEN family IN ('side_combination64', 'container_combination64') AND build_failed AND decision != 'pending' THEN 'failed'
              WHEN decision IN ('pending', 'claimed') THEN 'pending'
              WHEN decision IN ('ready', 're-generated') AND build_failed THEN 'failed'
              WHEN decision = 're-generated' THEN 'ready'
              ELSE decision END AS state,
         CASE WHEN mode = 'use_edited' THEN 'edited'
              WHEN mode = 'use_upload' OR (uploaded AND mode = 'use_org') THEN 'uploaded'
              WHEN mode = 'work_fix' THEN 'work_fix' ELSE 'original' END AS artwork,
         CASE WHEN mode = 'use_org' THEN stroke_count END AS strokes,
         CASE WHEN mode = 'use_org' THEN segment_count END AS segments,
         CASE WHEN symmetry_sha = svg_sha256 THEN symmetry END AS axes
  FROM t)")
}

/// `approvedCategory(...) === 'Uncategorized'`: no category, or `uncategorized` / `_uncategorized` / `…_<digits>`.
const UNCATEGORIZED: &str = "(COALESCE(u.category, '') = '' OR lower(trim(u.category)) IN ('uncategorized', '_uncategorized') \
    OR lower(trim(u.category)) GLOB 'uncategorized_[0-9]*' OR lower(trim(u.category)) GLOB '_uncategorized_[0-9]*')";

/// The latest disapproval reason on the current revision (`loadPendingFeedback`'s `pendingReasons`).
const REASON: &str = "COALESCE((SELECT CASE WHEN f.reason = 'bad-draw' THEN 'bad-stroke' ELSE COALESCE(NULLIF(f.reason, ''), 'other') END
  FROM feedback f WHERE f.icon = u.key AND f.svg_sha256 = u.svg_sha256 ORDER BY f.id DESC LIMIT 1), 'missing')";

/// Which filters a clause list includes.
#[derive(Clone, Copy)]
struct Parts { category: bool, section: bool }

/// Family and search, which every count shares: applied to `icons` before the review states are worked out.
fn pre(p: &Params, args: &mut Args) -> String {
    let mut w: Vec<String> = Vec::new();
    // matchesFamily
    match p.family.as_str() {
        "" => {}
        "side_main" | "side_sub" => { w.push("i.side_role = ?".into()); args.push(json!(&p.family[5..])); }
        family => { w.push("i.family = ?".into()); args.push(json!(family)); }
    }
    // matchesSearch
    if !p.q.is_empty() {
        w.push("instr(i.search, ?) > 0".into());
        args.push(json!(p.q));
    }
    for term in &p.terms {
        w.push("instr(i.search, ?) > 0".into());
        args.push(json!(term));
    }
    if !p.profile.is_empty() {
        w.push("i.profile = ?".into());
        args.push(json!(p.profile));
    }
    where_sql(&w)
}

fn clauses(p: &Params, parts: Parts, args: &mut Args) -> Vec<String> {
    let mut w = Vec::new();
    if parts.category {
        if let Some(category) = &p.category {
            w.push("u.category = ?".into());
            args.push(json!(category));
        }
        if p.category_group == "uncategorized" {
            w.push(format!("{UNCATEGORIZED}"));
        }
    }
    // matchesFacets
    match p.symmetry.as_str() {
        "" => {}
        "unknown" => w.push("u.axes IS NULL".into()),
        "symmetric" => w.push("u.axes IS NOT NULL AND u.axes != ''".into()),
        "asymmetric" => w.push("u.axes = ''".into()),
        "both" => w.push("u.axes = 'vertical,horizontal'".into()),
        axis => { w.push("instr(',' || u.axes || ',', ?) > 0".into()); args.push(json!(format!(",{axis},"))); }
    }
    match p.strokes.as_str() {
        "" => {}
        "unknown" => w.push("u.strokes IS NULL".into()),
        "11+" => w.push("u.strokes >= 11".into()),
        range => {
            let (low, high) = range.split_once('-').unwrap_or(("0", "0"));
            w.push("u.strokes BETWEEN ? AND ?".into());
            args.push(json!(low.parse::<i64>().unwrap_or(0)));
            args.push(json!(high.parse::<i64>().unwrap_or(0)));
        }
    }
    if !p.keyshape.is_empty() {
        w.push("u.keyshape = ?".into());
        args.push(json!(p.keyshape));
    }
    if !p.author.is_empty() {
        w.push("COALESCE(u.author, 'unknown') = ?".into());
        args.push(json!(p.author));
    }
    if !p.revision.is_empty() {
        w.push(format!("u.variant = {}", (p.revision == "variant") as i32));
    }
    if !p.reference.is_empty() {
        w.push(format!("u.has_original = {}", (p.reference == "with") as i32));
    }
    match p.artwork.as_str() {
        "" => {}
        "modified" => w.push("u.artwork != 'original'".into()),
        kind => { w.push("u.artwork = ?".into()); args.push(json!(kind)); }
    }
    match p.reason.as_str() {
        "" => {}
        "cannot-fix" => w.push("u.state = 'pending' AND u.row_status = 'pending' AND COALESCE(u.worker, '') != ''".into()),
        reason => { w.push(format!("u.state = 'pending' AND {REASON} = ?")); args.push(json!(reason)); }
    }
    // matchesApprover, matchesFeedbackAuthor
    if !p.reviewer.is_empty() {
        w.push("u.state IN ('approve', 'pending', 'rejected') AND u.actor = ?".into());
        args.push(json!(p.reviewer));
    }
    if !p.icon_feedback_by.is_empty() {
        w.push("EXISTS (SELECT 1 FROM feedback f WHERE f.icon = u.key AND f.author = ?)".into());
        args.push(json!(p.icon_feedback_by));
    }
    if parts.section {
        // inSection
        if !p.status.is_empty() {
            w.push("u.state = ?".into());
            args.push(json!(p.status));
        } else if p.reviewer.is_empty() {
            w.push("u.state != 'rejected'".into());
        }
        // matchesPendingFeedback
        match p.pending_feedback.as_str() {
            "with" => w.push("u.state = 'pending' AND EXISTS (SELECT 1 FROM feedback f WHERE f.icon = u.key)".into()),
            "without" => w.push("u.state = 'pending' AND NOT EXISTS (SELECT 1 FROM feedback f WHERE f.icon = u.key)".into()),
            _ => {}
        }
    }
    w
}

fn where_sql(w: &[String]) -> String {
    if w.is_empty() { String::new() } else { format!(" WHERE {}", w.join(" AND ")) }
}

/// `sortIcons` (the name tie-break approximates localeCompare without case).
fn order(sort: &str) -> String {
    let name = "u.sort_name COLLATE NOCASE, u.key COLLATE NOCASE";
    let by = |column: &str, desc: bool| format!("({column} IS NULL), {column} {}, {name}", if desc { "DESC" } else { "ASC" });
    match sort {
        "newest" => by("u.created_ms", true),
        "oldest" => by("u.created_ms", false),
        "modified-newest" => by("u.modified_ms", true),
        "modified-oldest" => by("u.modified_ms", false),
        "strokes-asc" => by("u.strokes", false),
        "strokes-desc" => by("u.strokes", true),
        "segments-asc" => by("u.segments", false),
        "segments-desc" => by("u.segments", true),
        _ => name.into(),
    }
}

/// What a list row carries (the card is built from them, see `item`).
const FIELDS: [&str; 23] = ["key", "icon_id", "family", "category", "svg_sha256", "build_failed", "uploaded", "state", "decision",
    "actor", "artwork", "mode", "strokes", "segments", "axes", "version_group", "version", "row_status", "row_at", "worker",
    "claimed_at", "note", "picked"];
/// Read from `icons` only for the rows a page shows (the CTE leaves them out to stay small).
const SHOWN: [&str; 5] = ["card", "name", "profile", "canvas_size", "preview_url"];

/// A list row as JSON; `alias` is the CTE row, `c` the icon row joined in for SHOWN.
fn row_json(alias: &str) -> String {
    let fields = FIELDS.iter().map(|f| format!("'{f}', {alias}.{f}")).chain(SHOWN.iter().map(|f| format!("'{f}', c.{f}")))
        // `regeneratedVariants(icon).length`: later versions made from this one.
        .chain(std::iter::once("'revisions', (SELECT COUNT(*) FROM icons v WHERE v.family = c.family AND v.variant_of = c.icon_id)".to_string()));
    format!("json_object({})", fields.collect::<Vec<_>>().join(", "))
}

/// The page of icons, how many it pages over, the tab counts and the category counts in one statement, so the
/// icons are read once → rows `{part, seq, data}`: part "total" `{total, versions}`, "state" `{state, n}`,
/// "category" `{category, n}`, "item" (a list row, `seq` its place on the page).
///
/// Units are icons, or with "All versions" version groups (`versionGroups`: every version of each group on the page,
/// groups in the order their first version sorts); without narrowing filters a group brings all its active versions
/// (`filteredIcons`). Tabs count matching icons in any section; categories ignore the category filter (`categoryCounts`).
pub fn list(p: &Params) -> (String, Args) {
    let mut args = Vec::new();
    let pre = pre(p, &mut args);
    let mut sql = icons_cte(&pre);
    let w = clauses(p, Parts { category: true, section: true }, &mut args);
    if p.grouped() {
        sql += &format!(", hit AS (SELECT DISTINCT u.version_group FROM u{}),
  member AS (SELECT u.* FROM u WHERE u.version_group IN (SELECT version_group FROM hit) AND u.state != 'rejected')", where_sql(&w));
    } else {
        sql += &format!(", member AS (SELECT u.* FROM u{})", where_sql(&w));
    }
    let page = if p.versions {
        sql += &format!(", ranked AS (SELECT u.*, ROW_NUMBER() OVER (ORDER BY {}) AS rank FROM member u),
  grp AS (SELECT version_group, MIN(rank) AS first FROM ranked GROUP BY version_group ORDER BY first LIMIT ? OFFSET ?)", order(&p.sort));
        args.push(json!(p.limit));
        args.push(json!(p.offset));
        format!("SELECT {} AS data, ROW_NUMBER() OVER (ORDER BY g.first, u.version, u.icon_id) AS seq \
                 FROM ranked u JOIN grp g ON g.version_group = u.version_group JOIN icons c ON c.key = u.key", row_json("u"))
    } else {
        let o = order(&p.sort);
        // The page's keys first, then their cards.
        format!("SELECT {} AS data, p.seq FROM (SELECT u.*, ROW_NUMBER() OVER (ORDER BY {o}) AS seq FROM member u ORDER BY {o} LIMIT ? OFFSET ?) p \
                 JOIN icons c ON c.key = p.key", row_json("p"))
    };
    let units = if p.versions { "COUNT(DISTINCT version_group)" } else { "COUNT(*)" };
    sql += &format!(" SELECT 'total' AS part, 0 AS seq, json_object('total', {units}, 'versions', COUNT(*)) AS data FROM member");
    let w = clauses(p, Parts { category: true, section: false }, &mut args);
    sql += &format!(" UNION ALL SELECT 'state', 0, json_object('state', state, 'n', n) FROM (SELECT u.state, COUNT(*) AS n FROM u{} GROUP BY u.state)",
                    where_sql(&w));
    let w = clauses(p, Parts { category: false, section: true }, &mut args);
    sql += &format!(" UNION ALL SELECT 'category', 0, json_object('category', category, 'n', n) FROM \
                    (SELECT COALESCE(u.category, '') AS category, COUNT(*) AS n FROM u{} GROUP BY 1)", where_sql(&w));
    // The section's matching icons by family (the approved collection's family counts).
    let w = clauses(p, Parts { category: true, section: true }, &mut args);
    sql += &format!(" UNION ALL SELECT 'family', 0, json_object('family', family, 'n', n) FROM \
                    (SELECT u.family, COUNT(*) AS n FROM u{} GROUP BY 1)", where_sql(&w));
    sql += &format!(" UNION ALL SELECT 'item', seq, data FROM ({page})");
    if !p.versions {
        // The page's LIMIT / OFFSET are its last placeholders.
        args.push(json!(p.limit));
        args.push(json!(p.offset));
    }
    (sql, args)
}

/// Every version of one version group (`inspectVariants`), as list rows `{data}`.
pub fn by_group(group: &str) -> (String, Args) {
    (format!("{} SELECT {} AS data FROM u JOIN icons c ON c.key = u.key", icons_cte(" WHERE i.version_group = ?"), row_json("u")),
     vec![json!(group)])
}

/// Particular icons by key, as list rows `{data}` (the feedback list, opened icons and their versions).
pub fn by_keys(keys: &[String]) -> (String, Args) {
    (format!("{} SELECT {} AS data FROM u JOIN icons c ON c.key = u.key", icons_cte(" WHERE i.key IN (SELECT value FROM json_each(?))"), row_json("u")),
     vec![json!(json!(keys).to_string())])
}

/// The list's filter choices: authors over every icon, keyshapes and categories over built and uploaded icons
/// (`icons` without failed builds, as the page filled its selects) → rows `{kind, value, n}`.
pub const FACETS: &str = "SELECT 'author' AS kind, COALESCE(author, 'unknown') AS value, COUNT(*) AS n FROM icons GROUP BY 2
  UNION ALL SELECT 'keyshape', keyshape, COUNT(*) FROM icons WHERE keyshape IS NOT NULL AND build_failed = 0 GROUP BY 2
  UNION ALL SELECT 'category', category, COUNT(*) FROM icons WHERE COALESCE(category, '') != '' AND build_failed = 0 GROUP BY 2
  UNION ALL SELECT 'family', family, COUNT(*) FROM icons GROUP BY 2
  UNION ALL SELECT 'total', 'built', COUNT(*) FROM icons WHERE build_failed = 0";

/// A list row as the page gets it: the card with the current drawing, review and work state merged in.
pub fn item(row: &HashMap<String, Value>, work: Value) -> Value {
    let mut card = row.get("card").and_then(Value::as_str).and_then(|c| serde_json::from_str::<Value>(c).ok())
        .filter(Value::is_object).unwrap_or_else(|| json!({}));
    // A row stored without a card (built in the browser) still shows: its columns are the card.
    for field in ["key", "icon_id", "name", "family", "category", "profile", "canvas_size", "preview_url"] {
        if card.get(field).is_none_or(Value::is_null) {
            if let Some(value) = row.get(field).filter(|v| !v.is_null()) {
                card[field] = value.clone();
            }
        }
    }
    let flag = |name: &str| row.get(name).and_then(Value::as_f64).is_some_and(|v| v != 0.0);
    card["svg_sha256"] = row.get("svg_sha256").cloned().unwrap_or(Value::Null);
    card["build_failed"] = json!(flag("build_failed"));
    if flag("uploaded") {
        card["uploaded_icon"] = json!(true);
    }
    let mode = row.get("mode").and_then(Value::as_str).unwrap_or("use_org");
    if mode != "use_org" || card.get("artwork_source").is_some() {
        card["artwork_source"] = json!(mode);
    }
    let number = |name: &str| row.get(name).and_then(Value::as_f64).map(|v| v as i64);
    card["stroke_count"] = json!(number("strokes"));
    card["segment_count"] = json!(number("segments"));
    card["symmetry_axes"] = match row.get("axes").and_then(Value::as_str) {
        Some(axes) => json!(axes.split(',').filter(|a| !a.is_empty()).collect::<Vec<_>>()),
        None => Value::Null,
    };
    card["review"] = json!({"state": row.get("state"), "status": row.get("decision"), "by": row.get("actor")});
    card["revisions"] = json!(number("revisions").unwrap_or(0));
    card["work"] = work;
    card
}

#[cfg(test)]
mod tests {
    use super::*;

    fn params(pairs: &[(&str, &str)]) -> Params {
        let map: HashMap<String, String> = pairs.iter().map(|(k, v)| (k.to_string(), v.to_string())).collect();
        Params::from_query(|name| map.get(name).cloned())
    }

    #[test]
    fn parses_like_restore_url() {
        let p = params(&[("reason", "meaning"), ("sort", "bogus"), ("limit", "50"), ("q", "  Cup "), ("pending_feedback", "with")]);
        assert_eq!((p.status.as_str(), p.sort.as_str(), p.limit, p.q.as_str()), ("pending", "name", 48, "cup"));
        assert_eq!(p.pending_feedback, "with");
        assert_eq!(params(&[("pending_feedback", "with")]).pending_feedback, "");
        assert!(params(&[("view", "versions")]).grouped());
        assert!(!params(&[("view", "versions"), ("author", "x")]).grouped());
    }

    #[test]
    fn placeholders_match_arguments() {
        let p = params(&[("family", "side_main"), ("q", "a"), ("category", "c"), ("symmetry", "vertical"), ("strokes", "4-6"),
                         ("keyshape", "K"), ("author", "m"), ("artwork", "edited"), ("reason", "meaning"), ("reviewer", "ray"),
                         ("icon_feedback_by", "hina"), ("pending_feedback", "without"), ("view", "versions")]);
        for (sql, args) in [list(&p), list(&params(&[("view", "versions")])), list(&params(&[])), by_keys(&["a".into()]), by_group("solo/a")] {
            assert_eq!(sql.matches('?').count(), args.len(), "{sql}");
        }
    }
}
