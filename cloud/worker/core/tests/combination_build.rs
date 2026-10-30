use pictographic_core::{combination_build as sql, icon_query};
use rusqlite::{params, Connection};
use serde_json::{json, Value};
const KEY: &str = "container_combination64/test";
fn database() -> Connection {
    let db = Connection::open_in_memory().unwrap();
    let dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(dir)
        .unwrap()
        .map(|e| e.unwrap().path())
        .collect();
    files.sort();
    for file in files {
        db.execute_batch(&std::fs::read_to_string(file).unwrap())
            .unwrap();
    }
    for (key, sha) in [
        (KEY, "old"),
        ("symbol/test", "part"),
        ("solo/unrelated", "unchanged"),
    ] {
        db.execute("INSERT INTO icons(key,icon_id,family,svg_sha256,preview_url,record,pushed_at) VALUES (?1,?1,?2,?3,'p','{}','t')",params![key,key.split('/').next(),sha]).unwrap();
        db.execute(
            "INSERT INTO revisions VALUES (?1,?2,'<svg/>','artwork','t')",
            params![sha, key],
        )
        .unwrap();
    }
    let doc=json!({"source_mode":"use_upload","source_svg_sha256":"baseline","selected_svg_sha256":"old","revision":2,"uploaded":{"svg_sha256":"old"},"edited":{"revision":7}}).to_string();
    db.execute(
        "INSERT INTO store_documents VALUES ('icon-artwork',?1,?2,'t','reviewer')",
        params![KEY, doc],
    )
    .unwrap();
    db
}
fn choice(db: &Connection) -> String {
    db.query_row(
        "SELECT document FROM store_documents WHERE key=?",
        [KEY],
        |r| r.get(0),
    )
    .unwrap()
}
fn build(db: &mut Connection, expected: &str, doc: &str, next: &str) -> rusqlite::Result<()> {
    let tx = db.transaction()?;
    tx.execute(
        sql::GUARD,
        params![
            KEY,
            expected,
            doc,
            r#"{"symbol/test":{"svg_sha256":"part"}}"#
        ],
    )?;
    for s in icon_query::UNCOUNT_ICON {
        tx.execute(s, [KEY])?;
    }
    tx.execute(
        "INSERT OR IGNORE INTO revisions VALUES (?1,?2,'<svg/>','combination-build','now')",
        params![next, KEY],
    )?;
    tx.execute(sql::SELECT_BUILD, params![KEY, next, "now", "tester"])?;
    tx.execute(
        "UPDATE icons SET svg_sha256=?1, artwork_source='use_org' WHERE key=?2",
        params![next, KEY],
    )?;
    tx.execute(icon_query::REFRESH_KEY, [KEY])?;
    for s in icon_query::RECOUNT_ICON {
        tx.execute(s, [KEY])?;
    }
    tx.commit()
}
#[test]
fn rebuild_selects_new_artwork_keeps_history_and_repeats() {
    let mut db = database();
    let old = choice(&db);
    build(&mut db, "old", &old, "new").unwrap();
    let c: Value = serde_json::from_str(&choice(&db)).unwrap();
    assert_eq!(c["source_mode"], "use_org");
    assert_eq!(c["source_svg_sha256"], "new");
    assert_eq!(c["revision"], 3);
    assert_eq!(c["uploaded"]["svg_sha256"], "old");
    assert_eq!(c["edited"]["revision"], 7);
    let shown: (String, String, String) = db
        .query_row(
            "SELECT svg_sha256,mode,picked FROM icons WHERE key=?",
            [KEY],
            |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?)),
        )
        .unwrap();
    assert_eq!(shown, ("new".into(), "use_org".into(), "use_org".into()));
    let fresh = choice(&db);
    build(&mut db, "new", &fresh, "new").unwrap();
    assert_eq!(
        serde_json::from_str::<Value>(&choice(&db)).unwrap()["revision"],
        4
    );
    assert_eq!(
        db.query_row("SELECT count(*) FROM revisions WHERE icon=?", [KEY], |r| {
            r.get::<_, i64>(0)
        })
        .unwrap(),
        2
    );
    assert_eq!(
        db.query_row(
            "SELECT svg_sha256 FROM icons WHERE key='solo/unrelated'",
            [],
            |r| r.get::<_, String>(0)
        )
        .unwrap(),
        "unchanged"
    );
}
#[test]
fn stale_hash_selection_and_part_changes_abort() {
    for conflict in ["hash", "choice", "part"] {
        let mut db = database();
        let old = choice(&db);
        match conflict {
            "hash"=>db.execute("UPDATE icons SET svg_sha256='concurrent' WHERE key=?",[KEY]).unwrap(),
            "choice"=>db.execute("UPDATE store_documents SET document=json_set(document,'$.revision',3) WHERE key=?",[KEY]).unwrap(),
            _=>db.execute("UPDATE icons SET svg_sha256='redrawn' WHERE key='symbol/test'",[]).unwrap(),
        };
        let before = choice(&db);
        let err = build(&mut db, "old", &old, "new").unwrap_err();
        assert!(sql::is_conflict(&err.to_string()), "{err}");
        assert_eq!(choice(&db), before);
        assert_eq!(
            db.query_row(
                "SELECT count(*) FROM revisions WHERE svg_sha256='new'",
                [],
                |r| r.get::<_, i64>(0)
            )
            .unwrap(),
            0
        );
    }
}
#[test]
fn conflicting_creation_rolls_back_earlier_batch_writes() {
    let mut db = database();
    let tx = db.transaction().unwrap();
    tx.execute(
        "UPDATE icons SET name='changed' WHERE key='solo/unrelated'",
        [],
    )
    .unwrap();
    let err = tx
        .execute(
            sql::GUARD,
            params![KEY, Option::<String>::None, Option::<String>::None, "{}"],
        )
        .unwrap_err();
    assert!(sql::is_conflict(&err.to_string()));
    drop(tx);
    assert_eq!(
        db.query_row(
            "SELECT name FROM icons WHERE key='solo/unrelated'",
            [],
            |r| r.get::<_, Option<String>>(0)
        )
        .unwrap(),
        None
    );
}

#[test]
fn uploaded_72_keeps_candidate_history_and_selects_rebuild() {
    let mut db = database();
    db.execute(
        "UPDATE icons SET family='container-combination-72', uploaded=1 WHERE key=?",
        [KEY],
    )
    .unwrap();
    let old = choice(&db);
    build(&mut db, "old", &old, "new72").unwrap();
    let c: Value = serde_json::from_str(&choice(&db)).unwrap();
    assert_eq!(c["uploaded"]["svg_sha256"], "old");
    assert_eq!(c["source_mode"], "use_org");
    assert_eq!(
        db.query_row("SELECT uploaded FROM icons WHERE key=?", [KEY], |r| r
            .get::<_, i64>(0))
            .unwrap(),
        1
    );
}

#[test]
fn no_selection_does_not_create_artwork_choice() {
    let mut db = database();
    db.execute("DELETE FROM store_documents WHERE key=?", [KEY])
        .unwrap();
    let tx = db.transaction().unwrap();
    tx.execute(
        sql::GUARD,
        params![KEY, "old", Option::<String>::None, "{}"],
    )
    .unwrap();
    assert_eq!(
        tx.execute(sql::SELECT_BUILD, params![KEY, "new", "now", "tester"])
            .unwrap(),
        0
    );
    tx.commit().unwrap();
}
