//! The Worker's icon list SQL (icon_query) against the answers gallery.html gave over the same made-up catalog
//! (fixtures/icon-query-expected.json, from make_icon_query_expected.mjs), on the D1 schema built from the migrations.

use pictographic_core::catalog::{Catalog, Icon};
use pictographic_core::icon_index::index;
use pictographic_core::icon_query::{self, Params};
use pictographic_core::reviews::{current_decisions, ActiveSplit, ReviewRow};
use rusqlite::{params_from_iter, Connection};
use serde_json::{json, Value};
use std::collections::{BTreeMap, HashMap};
use std::path::Path;

fn read(name: &str) -> Value {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures").join(name);
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}

fn sql_value(value: &Value) -> rusqlite::types::Value {
    match value {
        Value::Null => rusqlite::types::Value::Null,
        Value::Bool(b) => rusqlite::types::Value::Integer(*b as i64),
        Value::Number(n) => n.as_i64().map(rusqlite::types::Value::Integer).unwrap_or_else(|| rusqlite::types::Value::Real(n.as_f64().unwrap())),
        Value::String(s) => rusqlite::types::Value::Text(s.clone()),
        other => rusqlite::types::Value::Text(other.to_string()),
    }
}

/// The schema every migration builds, filled with the fixture as the Worker stores it.
fn database(fixture: &Value) -> Connection {
    let db = Connection::open_in_memory().unwrap();
    let dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(&dir).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    for file in files {
        db.execute_batch(&std::fs::read_to_string(&file).unwrap()).unwrap_or_else(|e| panic!("{}: {e}", file.display()));
    }
    let facets = &fixture["facets"];
    for record in fixture["records"].as_array().unwrap() {
        let key = record["key"].as_str().unwrap();
        let i = index(record, facets.get(key));
        db.execute("INSERT INTO icons(key, icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, build_failed,
                    uploaded, record, pushed_at, card, search, sort_name, keyshape, author, side_role, stroke_count, segment_count,
                    created_ms, modified_ms, version_group, version, variant, has_original, artwork_source, symmetry, symmetry_sha)
                    VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, 'p', ?13, ?14, ?15, ?16, ?17, ?18, ?19, ?20, ?21, ?22, ?23, ?24,
                    ?25, ?26, ?27, ?28, ?29)",
            rusqlite::params![key, record["icon_id"].as_str(), record["name"].as_str(), record["family"].as_str(), record["category"].as_str(),
                record["profile"].as_str(), 48, fixture["current_sha"][key].as_str().unwrap(), record["preview_url"].as_str(),
                record["build_failed"].as_bool().unwrap_or(false), record["uploaded_icon"].as_bool().unwrap_or(false), record.to_string(),
                i.card, i.search, i.sort_name, i.keyshape, i.author, i.side_role, i.stroke_count, i.segment_count, i.created_ms,
                i.modified_ms, i.version_group, i.version, i.variant, i.has_original, i.artwork_source, i.symmetry, i.symmetry_sha]).unwrap();
    }
    for r in fixture["reviews"].as_array().unwrap() {
        db.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, COALESCE(?8, ''))",
            rusqlite::params![r["icon"].as_str(), r["svg_sha256"].as_str(), r["status"].as_str(), r["updated_at"].as_str(),
                r["updated_by"].as_str(), r["worker"].as_str(), r["claimed_at"].as_str(), r["note"].as_str()]).unwrap();
    }
    for s in fixture["splits"].as_array().unwrap() {
        db.execute("INSERT INTO split_requests(icon, svg_sha256, combination_type, reason, reference_path, active, created_at, created_by)
                    VALUES (?1, ?2, 'side', 'r', 'p', ?3, ?4, ?5)",
            rusqlite::params![s["icon"].as_str(), s["svg_sha256"].as_str(), s["active"].as_i64(), s["created_at"].as_str(), s["created_by"].as_str()]).unwrap();
    }
    for f in fixture["feedback"].as_array().unwrap() {
        db.execute("INSERT INTO feedback(id, icon, feedback, svg_sha256, created_at, author, reason) VALUES (?1, ?2, 'x', ?3, 't', ?4, ?5)",
            rusqlite::params![f["id"].as_i64(), f["icon"].as_str(), f["svg_sha256"].as_str(), f["author"].as_str(), f["reason"].as_str()]).unwrap();
    }
    for a in fixture["artwork"].as_array().unwrap() {
        db.execute("INSERT INTO store_documents(store, key, document, updated_at, updated_by) VALUES ('icon-artwork', ?1, ?2, 't', 'u')",
            rusqlite::params![a["key"].as_str(), a["document"].to_string()]).unwrap();
    }
    for sha in fixture["graphs"].as_array().unwrap() {
        db.execute("INSERT INTO icon_graphs(svg_sha256, icon, graph) VALUES (?1, 'x', '{}')", rusqlite::params![sha.as_str()]).unwrap();
    }
    refresh(&db);
    db
}

/// What POST /api/icons/refresh {full: true} does, over every icon: the stored state, the search rows and the counts
/// (nothing keeps them current between refreshes since migration 0018).
fn refresh(db: &Connection) {
    db.execute(icon_query::REFRESH_RANGE, rusqlite::params![0i64, i64::MAX]).unwrap();
    let keys: Vec<String> = db.prepare("SELECT key FROM icons").unwrap().query_map([], |r| r.get(0)).unwrap().map(Result::unwrap).collect();
    for chunk in keys.chunks(100) {
        let list = json!(chunk).to_string();
        let before: i64 = db.query_row(icon_query::SEARCH_MAX, [], |r| r.get(0)).unwrap();
        let [delete_rows, delete_keys, insert_rows, remember] = icon_query::SEARCH_REFRESH;
        for sql in [delete_rows, delete_keys, insert_rows] {
            db.execute(sql, rusqlite::params![list]).unwrap();
        }
        db.execute(remember, rusqlite::params![before]).unwrap();
    }
    let groups: Vec<icon_query::Group> = db.prepare(icon_query::GROUPS).unwrap().query_map([], |r| Ok(icon_query::Group {
        family: r.get(0)?, side_role: r.get(1)?, state: r.get(2)?, category: r.get(3)?, build_failed: r.get::<_, i64>(4)? as f64,
        author: r.get(5)?, keyshape: r.get(6)?, n: r.get::<_, i64>(7)? as f64 })).unwrap().map(Result::unwrap).collect();
    let (counts, facets) = icon_query::count_rows(&groups);
    for sql in icon_query::COUNTS_CLEAR {
        db.execute(sql, []).unwrap();
    }
    for (family, side_role, state, category, failed, n) in counts {
        db.execute(&format!("{}(?1, ?2, ?3, ?4, ?5, ?6)", icon_query::COUNTS_INSERT), rusqlite::params![family, side_role, state, category, failed, n]).unwrap();
    }
    for (kind, value, n) in facets {
        db.execute(&format!("{}(?1, ?2, ?3)", icon_query::FACETS_INSERT), rusqlite::params![kind, value, n]).unwrap();
    }
}

fn rows(db: &Connection, (sql, args): (String, Vec<Value>)) -> Vec<HashMap<String, Value>> {
    let mut statement = db.prepare(&sql).unwrap_or_else(|e| panic!("{e}\n{sql}"));
    let names: Vec<String> = statement.column_names().iter().map(|s| s.to_string()).collect();
    let found = statement.query_map(params_from_iter(args.iter().map(sql_value)), |row| {
        Ok(names.iter().enumerate().map(|(i, name)| {
            let value = match row.get_ref(i).unwrap() {
                rusqlite::types::ValueRef::Null => Value::Null,
                rusqlite::types::ValueRef::Integer(n) => json!(n),
                rusqlite::types::ValueRef::Real(f) => json!(f),
                rusqlite::types::ValueRef::Text(t) => json!(String::from_utf8_lossy(t)),
                rusqlite::types::ValueRef::Blob(_) => Value::Null,
            };
            (name.clone(), value)
        }).collect())
    }).unwrap();
    found.map(Result::unwrap).collect()
}

/// The list statement's parts: (total row, page keys in order, tab counts, category counts).
fn list(db: &Connection, p: &Params) -> (Value, Vec<Value>, BTreeMap<String, i64>, BTreeMap<String, i64>) {
    let mut total = json!({});
    let mut items: Vec<(i64, Value)> = Vec::new();
    let (mut states, mut categories) = (BTreeMap::new(), BTreeMap::new());
    for row in rows(db, icon_query::list(p)) {
        let data: Value = serde_json::from_str(row["data"].as_str().unwrap()).unwrap();
        match row["part"].as_str().unwrap() {
            "total" => total = data,
            "state" => { states.insert(data["state"].as_str().unwrap().to_string(), data["n"].as_i64().unwrap()); }
            "category" => { categories.insert(data["category"].as_str().unwrap().to_string(), data["n"].as_i64().unwrap()); }
            "family" => {}
            _ => items.push((row["seq"].as_i64().unwrap(), data["key"].clone())),
        }
    }
    items.sort_by_key(|(seq, _)| *seq);
    (total, items.into_iter().map(|(_, key)| key).collect(), states, categories)
}

fn params(case: &Value) -> Params {
    Params::from_query(|name| case.get(name).map(|v| v.as_str().map(str::to_string).unwrap_or_else(|| v.to_string())))
}

#[test]
fn decisions_match_the_statuses_the_page_loaded() {
    let fixture = read("icon-query.json");
    let expected = read("icon-query-expected.json");
    let icons: Vec<Icon> = fixture["records"].as_array().unwrap().iter().map(|r| Icon {
        key: r["key"].as_str().unwrap().into(), svg_sha256: fixture["current_sha"][r["key"].as_str().unwrap()].as_str().unwrap().into(),
        ..Icon::default() }).collect();
    let mut reviews: Vec<ReviewRow> = serde_json::from_value(fixture["reviews"].clone()).unwrap();
    reviews.sort_by(|a, b| a.updated_at.cmp(&b.updated_at));
    let splits: Vec<ActiveSplit> = serde_json::from_value(fixture["splits"].clone()).unwrap();
    let decisions = current_decisions(&reviews, &splits, &Catalog::new(icons, true));
    let statuses: BTreeMap<String, String> = decisions.into_iter().map(|(k, d)| (k, d.status)).collect();
    let wanted: BTreeMap<String, String> = serde_json::from_value(expected["statuses"].clone()).unwrap();
    assert_eq!(statuses, wanted);
}

#[test]
fn lists_what_the_page_listed() {
    let fixture = read("icon-query.json");
    let expected = read("icon-query-expected.json");
    let db = database(&fixture);
    let mut failures = Vec::new();
    for (case, want) in fixture["cases"].as_array().unwrap().iter().zip(expected["results"].as_array().unwrap()) {
        let mut p = params(case);
        let mut parts = list(&db, &p);
        let total = parts.0["total"].as_i64().unwrap();
        // The page shows its last page when asked past the end.
        if p.offset >= total && total > 0 {
            p.offset = (total - 1) / p.limit * p.limit;
            parts = list(&db, &p);
        }
        let (count, keys, states, categories) = parts;
        let got = json!({"keys": keys, "total": total, "versions": count["versions"], "offset": p.offset, "states": states, "categories": categories});
        let want_sorted = json!({"keys": want["keys"], "total": want["total"], "versions": want["versions"], "offset": want["offset"],
            "states": serde_json::from_value::<BTreeMap<String, i64>>(want["states"].clone()).unwrap(),
            "categories": serde_json::from_value::<BTreeMap<String, i64>>(want["categories"].clone()).unwrap()});
        if got != want_sorted {
            failures.push(format!("{case}\n  got  {got}\n  want {want_sorted}"));
        }
    }
    assert!(failures.is_empty(), "{} of {} cases differ:\n{}", failures.len(), expected["results"].as_array().unwrap().len(), failures.join("\n"));
}

#[test]
fn search_words_profile_and_uncategorized() {
    let fixture = read("icon-query.json");
    let db = database(&fixture);
    let records = fixture["records"].as_array().unwrap();
    let p = |pairs: &[(&str, &str)]| params(&json!(pairs.iter().map(|(k, v)| (k.to_string(), json!(v))).collect::<serde_json::Map<_, _>>()));
    let all = |p: &Params| { let mut p = p.clone(); p.limit = 192; list(&db, &p).1 };
    let words = all(&p(&[("terms", "Cup  00")]));
    assert!(!words.is_empty() && words.iter().all(|k| { let r = records.iter().find(|r| r["key"] == *k).unwrap();
        let text = index(r, None).search; text.contains("cup") && text.contains("00") }));
    let profile = all(&p(&[("profile", "SUB")]));
    assert!(!profile.is_empty() && profile.iter().all(|k| k.as_str().unwrap().starts_with("sub/")));
    let none = all(&p(&[("category_group", "uncategorized")]));
    assert!(!none.is_empty() && none.iter().all(|k| records.iter().find(|r| r["key"] == *k).unwrap()["category"].as_str().unwrap_or("").is_empty()));
    // Family counts add up to the total.
    let rows = rows(&db, icon_query::list(&p(&[])));
    let (mut sum, mut total) = (0, 0);
    for row in rows {
        let data: Value = serde_json::from_str(row["data"].as_str().unwrap()).unwrap();
        match row["part"].as_str().unwrap() { "family" => sum += data["n"].as_i64().unwrap(), "total" => total = data["total"].as_i64().unwrap(), _ => {} }
    }
    assert_eq!(sum, total);
}

/// The point of the stored columns: a page reads its own rows. The same requests on catalogs of 7,200 and 21,600 icons
/// (copies of the fixture) must not scan the icons table, and their work must not grow with the catalog; only a
/// narrowing filter (here author) counts the icons that match it.
#[test]
fn a_page_reads_its_own_rows() {
    let fixture = read("icon-query.json");
    let p = |pairs: &[(&str, &str)]| params(&json!(pairs.iter().map(|(k, v)| (k.to_string(), json!(v))).collect::<serde_json::Map<_, _>>()));
    let cases = [
        ("default solo page", p(&[("family", "solo")]), true),
        ("all families, Disapproved tab", p(&[("family", ""), ("status", "pending")]), true),
        ("a category", p(&[("family", "solo"), ("category", "food")]), true),
        ("page 3", p(&[("family", "solo"), ("offset", "96")]), true),
        ("newest first", p(&[("family", "solo"), ("sort", "newest")]), true),
        ("search", p(&[("family", ""), ("q", "cloud 0")]), false),
        ("author filter (counts the matches)", p(&[("family", "solo"), ("author", "gpt-x")]), false),
    ];
    let mut steps = Vec::new();
    for copies in [100, 300] {
        let db = database(&fixture);
        db.execute_batch(&format!("CREATE TEMP TABLE n(i); WITH RECURSIVE c(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM c WHERE i < {}) \
                                   INSERT INTO n SELECT i FROM c;", copies - 1)).unwrap();
        let columns = "icon_id, name, family, category, profile, canvas_size, svg_sha256, preview_url, build_failed, uploaded, record, pushed_at, \
            card, search, sort_name, keyshape, author, side_role, stroke_count, segment_count, created_ms, modified_ms, version_group, version, \
            variant, has_original, artwork_source, symmetry, symmetry_sha";
        db.execute_batch(&format!("INSERT INTO icons(key, {columns}) SELECT i.key || '-c' || n.i, {} FROM icons i, n",
            columns.split(", ").map(|c| format!("i.{c}")).collect::<Vec<_>>().join(", "))).unwrap();
        refresh(&db);
        let mut row = Vec::new();
        for (label, case, flat) in &cases {
            let (sql, args) = icon_query::list(case);
            let plan: Vec<String> = db.prepare(&format!("EXPLAIN QUERY PLAN {sql}")).unwrap()
                .query_map(params_from_iter(args.iter().map(sql_value)), |r| r.get::<_, String>(3)).unwrap().map(Result::unwrap).collect();
            let scans: Vec<&String> = plan.iter().filter(|line| line.starts_with("SCAN u") || line.starts_with("SCAN icons")).collect();
            if *flat {
                assert!(scans.is_empty(), "{label} scans the icons table: {plan:#?}");
            }
            let mut statement = db.prepare(&sql).unwrap();
            let out = statement.query_map(params_from_iter(args.iter().map(sql_value)), |_| Ok(())).unwrap().count();
            let work = statement.get_status(rusqlite::StatementStatus::VmStep);
            println!("{} icons · {label}: {out} rows out, {work} VM steps", 72 * copies);
            row.push(work);
        }
        steps.push(row);
    }
    for (i, (label, _, flat)) in cases.iter().enumerate() {
        let (small, large) = (steps[0][i] as f64, steps[1][i] as f64);
        if *flat {
            assert!(large <= small * 1.25, "{label}: {small} VM steps at 7,200 icons, {large} at 21,600");
        }
    }
}
