//! Uploaded icons (notably solo-64) must keep their picked artwork in the thumbnail list.
use pictographic_core::icon_query;
use rusqlite::{params, Connection};
use serde_json::{json, Value};
use std::path::Path;

fn before_migration() -> Connection {
    let db = Connection::open_in_memory().unwrap();
    let dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(dir).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    for file in files.iter().filter(|f| f.file_name().unwrap().to_str().unwrap() < "0025") {
        db.execute_batch(&std::fs::read_to_string(file).unwrap()).unwrap();
    }
    db
}

fn seed(db: &Connection, key: &str, mode: &str, current: &str, graph: bool) {
    db.execute("INSERT INTO icons(key, icon_id, family, name, canvas_size, svg_sha256, uploaded, record, pushed_at,
        preview_url, stroke_count, segment_count) VALUES (?1, ?1, ?3, ?1, 64, ?2, 1, '{}', 't', 'old.svg', 4, 8)",
        params![key, current, key.split('/').next().unwrap()]).unwrap();
    let choice = json!({"source_svg_sha256": "original", "selected_svg_sha256": "selected", "source_mode": mode});
    db.execute("INSERT INTO store_documents(store, key, document, updated_at, updated_by)
        VALUES ('icon-artwork', ?1, ?2, 't', 'reviewer')", params![key, choice.to_string()]).unwrap();
    if graph {
        db.execute("INSERT OR IGNORE INTO icon_graphs(svg_sha256, icon, graph) VALUES (?1, ?2, '{}')", params![current, key]).unwrap();
    }
    db.execute(icon_query::REFRESH_KEY, [key]).unwrap();
}

fn state(db: &Connection, key: &str) -> (String, String, Option<String>, Option<i64>) {
    db.query_row("SELECT mode, artwork, picked, strokes FROM icons WHERE key = ?", [key],
        |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?))).unwrap()
}

fn migrate(db: &Connection) {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations/0025_uploaded_artwork_choices.sql");
    db.execute_batch(&std::fs::read_to_string(path).unwrap()).unwrap();
}

#[test]
fn existing_uploaded_edits_are_backfilled_and_listed() {
    let db = before_migration();
    for (key, mode, graph) in [("solo-64/browser", "use_edited", false), ("solo-64/manual", "use_upload", true)] {
        seed(&db, key, mode, "selected", graph);
        assert_eq!(state(&db, key).0, "use_org", "reproduce the old uploaded-icon exclusion");
    }
    let choices: String = db.query_row("SELECT group_concat(document) FROM store_documents", [], |r| r.get(0)).unwrap();
    migrate(&db);
    assert_eq!(state(&db, "solo-64/browser"), ("use_edited".into(), "edited".into(), Some("use_edited".into()), None));
    assert_eq!(state(&db, "solo-64/manual"), ("use_upload".into(), "uploaded".into(), Some("use_upload".into()), None));
    assert_eq!(choices, db.query_row::<String, _, _>("SELECT group_concat(document) FROM store_documents", [], |r| r.get(0)).unwrap());

    // The real gallery query must include the edit and carry the current pick/hash for its thumbnail URL.
    let p = icon_query::Params::from_query(|name| match name {
        "family" => Some("solo-64".into()), "artwork" => Some("edited".into()), _ => None,
    });
    let (sql, args) = icon_query::list(&p);
    let args: Vec<rusqlite::types::Value> = args.iter().map(|v| match v {
        Value::String(s) => s.clone().into(), Value::Number(n) => n.as_i64().unwrap().into(), _ => panic!("unexpected bind"),
    }).collect();
    let mut stmt = db.prepare(&sql).unwrap();
    let items: Vec<Value> = stmt.query_map(rusqlite::params_from_iter(args), |r| {
        Ok((r.get::<_, String>(0)?, r.get::<_, String>(2)?))
    }).unwrap().map(Result::unwrap).filter(|(part, _)| part == "item")
        .map(|(_, data)| serde_json::from_str(&data).unwrap()).collect();
    assert_eq!(items.len(), 1);
    assert_eq!(items[0]["key"], "solo-64/browser");
    assert_eq!(items[0]["picked"], "use_edited");
    assert_eq!(items[0]["svg_sha256"], "selected");
}

#[test]
fn future_picks_survive_graph_loading_but_stale_choices_do_not_apply() {
    let db = before_migration();
    migrate(&db);
    seed(&db, "solo-64/new", "use_edited", "selected", true);
    assert_eq!(state(&db, "solo-64/new").2.as_deref(), Some("use_edited"));
    seed(&db, "solo-64/stale", "use_edited", "replacement", false);
    assert_eq!(state(&db, "solo-64/stale"), ("use_org".into(), "uploaded".into(), None, Some(4)));
    seed(&db, "solo-64/original", "use_org", "original", true);
    assert_eq!(state(&db, "solo-64/original"), ("use_org".into(), "uploaded".into(), Some("use_org".into()), Some(4)));
}

#[test]
fn every_family_and_style_keeps_its_pick_without_changing_review_counts() {
    let db = before_migration();
    let families = ["solo", "solo-64", "icon-72", "container", "container-72", "main-54", "sub", "sub-36",
        "symbol", "symbol-36", "container_combination64", "container-combination-72", "side_combination64", "combination-72", "text"];
    let mut cases = Vec::new();
    for family in families {
        for style in ["normal", "round", "sharp", "fill"] {
            for mode in ["use_upload", "use_edited"] {
                let key = format!("{family}/{style}-{mode}");
                seed(&db, &key, mode, "selected", true);
                db.execute("UPDATE icons SET style = ?, state = 'approve', decision = 'approve', actor = 'reviewer' WHERE key = ?",
                    params![style, key]).unwrap();
                for sql in icon_query::RECOUNT_ICON {
                    db.execute(sql, [&key]).unwrap();
                }
                cases.push((key, mode));
            }
        }
    }
    let count_before: i64 = db.query_row("SELECT SUM(n) FROM icon_counts", [], |r| r.get(0)).unwrap();
    migrate(&db);
    for (key, mode) in &cases {
        assert_eq!(state(&db, key).2.as_deref(), Some(*mode), "{key}");
        let review: (String, String, String) = db.query_row("SELECT state, decision, actor FROM icons WHERE key = ?", [key],
            |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap();
        assert_eq!(review, ("approve".into(), "approve".into(), "reviewer".into()));
    }
    assert_eq!(count_before, cases.len() as i64);
    assert_eq!(count_before, db.query_row::<i64, _, _>("SELECT SUM(n) FROM icon_counts", [], |r| r.get(0)).unwrap());
}
