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

/// `approvedCategory(...) === 'Uncategorized'` on a category column: none, or `uncategorized` / `_uncategorized` / `…_<digits>`.
fn uncategorized(column: &str) -> String {
    format!("(COALESCE({column}, '') = '' OR lower(trim({column})) IN ('uncategorized', '_uncategorized') \
             OR lower(trim({column})) GLOB 'uncategorized_[0-9]*' OR lower(trim({column})) GLOB '_uncategorized_[0-9]*')")
}

/// Which filters a clause list includes.
#[derive(Clone, Copy)]
struct Parts { category: bool, section: bool }

/// A search phrase: through the trigram index (icon_search) when it has three characters or more, so only matching
/// icons are read; shorter ones are looked for in each icon's text.
fn search(column_key: &str, column_text: &str, phrase: &str, w: &mut Vec<String>, args: &mut Args) {
    if phrase.chars().count() >= 3 {
        w.push(format!("{column_key} IN (SELECT key FROM icon_search WHERE icon_search MATCH ?)"));
        args.push(json!(format!("\"{}\"", phrase.replace('"', "\"\""))));
    } else {
        w.push(format!("instr({column_text}, ?) > 0"));
        args.push(json!(phrase));
    }
}

/// The page's filters on the icons table (alias `u`), every one on a stored column (migration 0015).
fn clauses(p: &Params, parts: Parts, args: &mut Args) -> Vec<String> {
    let mut w = Vec::new();
    // matchesFamily
    match p.family.as_str() {
        "" => {}
        "side_main" | "side_sub" => { w.push("u.side_role = ?".into()); args.push(json!(&p.family[5..])); }
        family => { w.push("u.family = ?".into()); args.push(json!(family)); }
    }
    // matchesSearch: the phrase, and (terms) every word
    if !p.q.is_empty() {
        search("u.key", "u.search", &p.q, &mut w, args);
    }
    for term in &p.terms {
        search("u.key", "u.search", term, &mut w, args);
    }
    if !p.profile.is_empty() {
        w.push("u.profile = ?".into());
        args.push(json!(p.profile));
    }
    if parts.category {
        if let Some(category) = &p.category {
            w.push("u.category = ?".into());
            args.push(json!(category));
        }
        if p.category_group == "uncategorized" {
            w.push(uncategorized("u.category"));
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
        "cannot-fix" => w.push("u.state = 'pending' AND u.cannot_fix".into()),
        reason => { w.push("u.state = 'pending' AND u.reason = ?".into()); args.push(json!(reason)); }
    }
    // matchesApprover, matchesFeedbackAuthor
    if !p.reviewer.is_empty() {
        w.push("u.actor = ? AND u.state IN ('approve', 'pending', 'rejected')".into());
        args.push(json!(p.reviewer));
    }
    if !p.icon_feedback_by.is_empty() {
        w.push("u.key IN (SELECT icon FROM feedback WHERE author = ?)".into());
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
            "with" => w.push("u.state = 'pending' AND u.has_feedback".into()),
            "without" => w.push("u.state = 'pending' AND NOT u.has_feedback".into()),
            _ => {}
        }
    }
    w
}

fn where_sql(w: &[String]) -> String {
    if w.is_empty() { String::new() } else { format!(" WHERE {}", w.join(" AND ")) }
}

/// `sortIcons`, in forms the list indexes serve (missing values last; the name tie-break approximates localeCompare
/// without case).
fn order(sort: &str) -> String {
    let name = "u.sort_name COLLATE NOCASE, u.key COLLATE NOCASE";
    let by = |column: &str, desc: bool| if desc {
        format!("COALESCE({column}, -9223372036854775807) DESC, {name}")
    } else {
        format!("COALESCE({column}, 9223372036854775807), {name}")
    };
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

/// What a list row carries (the card is built from them, see `item`); `r` is the current revision's review row.
const FIELDS: [&str; 22] = ["key", "icon_id", "family", "category", "svg_sha256", "build_failed", "uploaded", "state", "decision",
    "actor", "artwork", "mode", "strokes", "segments", "axes", "version_group", "version", "picked", "card", "name", "profile",
    "canvas_size"];

fn row_json(alias: &str) -> String {
    let fields = FIELDS.iter().map(|f| format!("'{f}', {alias}.{f}"))
        .chain(["'preview_url', {a}.preview_url", "'row_status', r.status", "'row_at', r.updated_at", "'worker', r.worker",
                "'claimed_at', r.claimed_at", "'note', r.note"].iter().map(|f| f.replace("{a}", alias)))
        // `regeneratedVariants(icon).length`: later versions made from this one.
        .chain(std::iter::once(format!("'revisions', (SELECT COUNT(*) FROM icons v WHERE v.family = {alias}.family AND v.variant_of = {alias}.icon_id)")));
    format!("json_object({})", fields.collect::<Vec<_>>().join(", "))
}

/// The review row of a shown icon's current drawing (its work claim).
fn review_join(alias: &str) -> String {
    format!(" LEFT JOIN reviews r ON r.icon = {alias}.key AND r.svg_sha256 = {alias}.svg_sha256")
}

/// Whether the counts can come from icon_counts: only family, state and category narrow the list.
fn counted(p: &Params) -> bool {
    p.q.is_empty() && p.terms.is_empty() && p.profile.is_empty() && !p.narrowed() && p.pending_feedback.is_empty()
}

/// icon_counts conditions for the family and (optionally) the section and category.
fn count_clauses(p: &Params, section: bool, category: bool, args: &mut Args) -> String {
    let mut w: Vec<String> = Vec::new();
    match p.family.as_str() {
        "" => {}
        "side_main" | "side_sub" => { w.push("c.side_role = ?".into()); args.push(json!(&p.family[5..])); }
        family => { w.push("c.family = ?".into()); args.push(json!(family)); }
    }
    if category {
        if let Some(value) = &p.category {
            w.push("c.category = ?".into());
            args.push(json!(value));
        }
        if p.category_group == "uncategorized" {
            w.push(uncategorized("c.category"));
        }
    }
    if section {
        if !p.status.is_empty() {
            w.push("c.state = ?".into());
            args.push(json!(p.status));
        } else {
            w.push("c.state != 'rejected'".into());
        }
    }
    w.push("c.n > 0".into());
    where_sql(&w)
}

/// The page of icons, how many it pages over, the tab counts, category counts and family counts in one statement
/// → rows `{part, seq, data}`: part "total" `{total, versions}`, "state" / "category" / "family" `{…, n}`, "item" (a
/// list row, `seq` its place on the page).
///
/// A page reads its own rows through the list indexes. With only family, state and category chosen, the counts come
/// from icon_counts; other filters count the icons that match them. Units are icons, or with "All versions" version
/// groups (`versionGroups`), whose paging reads the matching icons; without narrowing filters a group brings all its
/// active versions (`filteredIcons`). Tabs count matching icons in any section; categories ignore the category filter.
pub fn list(p: &Params) -> (String, Args) {
    let mut args = Vec::new();
    let mut parts: Vec<String> = Vec::new();
    let w = clauses(p, Parts { category: true, section: true }, &mut args);
    let page = if p.versions {
        let from = if p.grouped() {
            format!("WITH hit AS (SELECT DISTINCT u.version_group FROM icons u{}), \
                     member AS (SELECT u.* FROM icons u WHERE u.version_group IN (SELECT version_group FROM hit) AND u.state != 'rejected')",
                    where_sql(&w))
        } else {
            format!("WITH member AS (SELECT u.* FROM icons u{})", where_sql(&w))
        };
        args.push(json!(p.limit));
        args.push(json!(p.offset));
        let sql = format!("{from}, ranked AS (SELECT u.*, ROW_NUMBER() OVER (ORDER BY {}) AS rank FROM member u), \
            grp AS (SELECT version_group, MIN(rank) AS first FROM ranked GROUP BY version_group ORDER BY first LIMIT ? OFFSET ?), \
            counted AS (SELECT COUNT(DISTINCT version_group) AS total, COUNT(*) AS versions FROM member) \
            SELECT 'total' AS part, 0 AS seq, json_object('total', total, 'versions', versions) AS data FROM counted \
            UNION ALL SELECT 'item', ROW_NUMBER() OVER (ORDER BY g.first, u.version, u.icon_id), {} FROM ranked u \
            JOIN grp g ON g.version_group = u.version_group{}", order(&p.sort), row_json("u"), review_join("u"));
        parts.push(sql);
        String::new()
    } else {
        let o = order(&p.sort);
        args.push(json!(p.limit));
        args.push(json!(p.offset));
        // The page's rows first (through the list indexes), then their review rows and cards.
        format!("SELECT 'item' AS part, ROW_NUMBER() OVER (ORDER BY {}) AS seq, {} AS data FROM \
                 (SELECT u.* FROM icons u{} ORDER BY {o} LIMIT ? OFFSET ?) page{}", o.replace("u.", "page."), row_json("page"),
                where_sql(&w), review_join("page"))
    };
    if !page.is_empty() {
        parts.push(page);
    }
    if counted(p) {
        // From icon_counts: a few rows per family.
        if !p.versions {
            let w = count_clauses(p, true, true, &mut args);
            parts.push(format!("SELECT 'total', 0, json_object('total', COALESCE(SUM(c.n), 0), 'versions', COALESCE(SUM(c.n), 0)) FROM icon_counts c{w}"));
        }
        let w = count_clauses(p, false, true, &mut args);
        parts.push(format!("SELECT 'state', 0, json_object('state', state, 'n', n) FROM (SELECT c.state, SUM(c.n) AS n FROM icon_counts c{w} GROUP BY 1)"));
        let w = count_clauses(p, true, false, &mut args);
        parts.push(format!("SELECT 'category', 0, json_object('category', category, 'n', n) FROM (SELECT c.category, SUM(c.n) AS n FROM icon_counts c{w} GROUP BY 1)"));
        let w = count_clauses(p, true, true, &mut args);
        parts.push(format!("SELECT 'family', 0, json_object('family', family, 'n', n) FROM (SELECT c.family, SUM(c.n) AS n FROM icon_counts c{w} GROUP BY 1)"));
    } else {
        // Other filters: the matching icons are counted.
        if !p.versions {
            let w = clauses(p, Parts { category: true, section: true }, &mut args);
            parts.push(format!("SELECT 'total', 0, json_object('total', COUNT(*), 'versions', COUNT(*)) FROM icons u{}", where_sql(&w)));
        }
        let w = clauses(p, Parts { category: true, section: false }, &mut args);
        parts.push(format!("SELECT 'state', 0, json_object('state', state, 'n', n) FROM (SELECT u.state, COUNT(*) AS n FROM icons u{} GROUP BY 1)", where_sql(&w)));
        let w = clauses(p, Parts { category: false, section: true }, &mut args);
        parts.push(format!("SELECT 'category', 0, json_object('category', category, 'n', n) FROM (SELECT COALESCE(u.category, '') AS category, COUNT(*) AS n FROM icons u{} GROUP BY 1)", where_sql(&w)));
        let w = clauses(p, Parts { category: true, section: true }, &mut args);
        parts.push(format!("SELECT 'family', 0, json_object('family', family, 'n', n) FROM (SELECT u.family, COUNT(*) AS n FROM icons u{} GROUP BY 1)", where_sql(&w)));
    }
    // A WITH clause belongs to the whole compound statement: the versions part goes first.
    (parts.join(" UNION ALL "), args)
}

/// Every version of one version group (`inspectVariants`), as list rows `{data}`.
pub fn by_group(group: &str) -> (String, Args) {
    (format!("SELECT {} AS data FROM icons u{} WHERE u.version_group = ?", row_json("u"), review_join("u")), vec![json!(group)])
}

/// Particular icons by key, as list rows `{data}` (the feedback list, opened icons and their versions).
pub fn by_keys(keys: &[String]) -> (String, Args) {
    (format!("SELECT {} AS data FROM icons u{} WHERE u.key IN (SELECT value FROM json_each(?))", row_json("u"), review_join("u")),
     vec![json!(json!(keys).to_string())])
}

/// Recompute the stored review state (view icon_state) of icons with rowid in [from, to): the full pass of
/// POST /api/icons/refresh and /api/icons/reindex. Nothing keeps the state current between refreshes (0018).
pub const REFRESH_RANGE: &str = "UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, \
    cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, \
    v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE rowid >= ? AND rowid < ?";

/// The same for the icons named in a JSON array of keys (one bound value).
pub const REFRESH_KEYS: &str = concat!(
    "UPDATE icons SET (decision, actor, state, mode, artwork, strokes, segments, axes, reason, has_feedback, ",
    "cannot_fix, picked) = (SELECT v.decision, v.actor, v.state, v.mode, v.artwork, v.strokes, v.segments, v.axes, v.reason, ",
    "v.has_feedback, v.cannot_fix, v.picked FROM icon_state v WHERE v.key = icons.key) WHERE key IN (SELECT value FROM json_each(?))");

/// The search rows of the icons in a JSON array of keys again. An FTS table cannot look up its key column, so the
/// old rows go by the rowid icon_search_keys remembers; the icons that still exist are inserted afresh and remembered.
/// The first three statements bind the array; the last binds `SEARCH_MAX` read before them.
pub const SEARCH_REFRESH: [&str; 4] = [
    "DELETE FROM icon_search WHERE rowid IN (SELECT search_rowid FROM icon_search_keys WHERE key IN (SELECT value FROM json_each(?)))",
    "DELETE FROM icon_search_keys WHERE key IN (SELECT value FROM json_each(?))",
    "INSERT INTO icon_search(search, key) SELECT search, key FROM icons WHERE key IN (SELECT value FROM json_each(?))",
    "INSERT INTO icon_search_keys(key, search_rowid) SELECT key, rowid FROM icon_search WHERE rowid > ?",
];
pub const SEARCH_MAX: &str = "SELECT COALESCE(MAX(search_rowid), 0) AS n FROM icon_search_keys";

/// One pass over icons for the counts: a row per distinct combination of what icon_counts and icon_facet_counts group by.
pub const GROUPS: &str = "SELECT family, side_role, state, category, build_failed, author, keyshape, COUNT(*) AS n \
    FROM icons GROUP BY 1, 2, 3, 4, 5, 6, 7";
pub const COUNTS_CLEAR: [&str; 2] = ["DELETE FROM icon_counts", "DELETE FROM icon_facet_counts"];
pub const COUNTS_INSERT: &str = "INSERT INTO icon_counts(family, side_role, state, category, built_failed, n) VALUES ";
pub const FACETS_INSERT: &str = "INSERT INTO icon_facet_counts(kind, value, n) VALUES ";

/// A `GROUPS` row (D1 returns integers as numbers).
#[derive(Clone, Debug, Default, serde::Deserialize)]
pub struct Group {
    pub family: Option<String>,
    pub side_role: Option<String>,
    pub state: Option<String>,
    pub category: Option<String>,
    pub build_failed: f64,
    pub author: Option<String>,
    pub keyshape: Option<String>,
    pub n: f64,
}

/// icon_counts rows `(family, side_role, state, category, built_failed, n)` and icon_facet_counts rows
/// `(kind, value, n)` from the groups: the same rules as migration 0015's first fill (authors and families of
/// every icon; keyshapes, categories and the built total of icons whose build did not fail).
pub fn count_rows(groups: &[Group]) -> (Vec<(String, String, String, String, i64, i64)>, Vec<(&'static str, String, i64)>) {
    let mut counts: HashMap<(String, String, String, String, i64), i64> = HashMap::new();
    let mut facets: HashMap<(&'static str, String), i64> = HashMap::new();
    let text = |v: &Option<String>| v.clone().unwrap_or_default();
    for g in groups {
        let (n, failed) = (g.n as i64, g.build_failed != 0.0);
        *counts.entry((text(&g.family), text(&g.side_role), text(&g.state), text(&g.category), failed as i64)).or_default() += n;
        *facets.entry(("author", g.author.clone().unwrap_or_else(|| "unknown".into()))).or_default() += n;
        *facets.entry(("family", text(&g.family))).or_default() += n;
        if !failed {
            if let Some(keyshape) = &g.keyshape {
                *facets.entry(("keyshape", keyshape.clone())).or_default() += n;
            }
            if !text(&g.category).is_empty() {
                *facets.entry(("category", text(&g.category))).or_default() += n;
            }
            *facets.entry(("total", "built".into())).or_default() += n;
        }
    }
    let mut counts: Vec<_> = counts.into_iter().map(|((f, s, st, c, b), n)| (f, s, st, c, b, n)).collect();
    let mut facets: Vec<_> = facets.into_iter().map(|((k, v), n)| (k, v, n)).collect();
    counts.sort();
    facets.sort();
    (counts, facets)
}

/// The list's filter choices, rebuilt by the refresh → rows `{kind, value, n}`.
pub const FACETS: &str = "SELECT kind, value, n FROM icon_facet_counts WHERE n > 0";

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
        for (sql, args) in [list(&p), list(&params(&[("view", "versions")])), list(&params(&[])), list(&params(&[("q", "ab")])),
                            list(&params(&[("view", "versions"), ("q", "cup")])), by_keys(&["a".into()]), by_group("solo/a")] {
            assert_eq!(sql.matches('?').count(), args.len(), "{sql}");
        }
    }
}
