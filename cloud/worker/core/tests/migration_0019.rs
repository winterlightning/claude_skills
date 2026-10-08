//! Migration 0019 and its rollback (cloud/worker/rollback): a Worker built before 0019 cannot count its writes on
//! the migrated schema; after the down script it can, the counts match the icons, and the redo script brings the
//! new Worker's statements back (PR #4 review).

use pictographic_core::icon_query;
use rusqlite::Connection;
use std::path::Path;

/// A Worker built before 0019 (origin/cloudflare-db icon_query RECOUNT_ICON[0]).
const OLD_RECOUNT: &str = "INSERT INTO icon_counts(family, side_role, state, category, built_failed, n) \
    SELECT COALESCE(family, ''), COALESCE(side_role, ''), COALESCE(state, ''), COALESCE(category, ''), build_failed, 1 \
    FROM icons WHERE key = ?1 ON CONFLICT(family, side_role, state, category, built_failed) DO UPDATE SET n = n + 1";

fn worker_dir() -> std::path::PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("..")
}

fn migrated(upto: &str) -> Connection {
    let db = Connection::open_in_memory().unwrap();
    let mut files: Vec<_> = std::fs::read_dir(worker_dir().join("migrations")).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    for file in files.iter().filter(|f| f.file_name().unwrap().to_str().unwrap() <= upto) {
        db.execute_batch(&std::fs::read_to_string(file).unwrap()).unwrap_or_else(|e| panic!("{}: {e}", file.display()));
    }
    db
}

fn script(db: &Connection, name: &str) {
    db.execute_batch(&std::fs::read_to_string(worker_dir().join("rollback").join(name)).unwrap()).unwrap();
}

fn add_icon(db: &Connection, key: &str, style: &str) {
    db.execute("INSERT INTO icons(key, icon_id, name, family, category, svg_sha256, preview_url, build_failed, uploaded, record, pushed_at, style) \
                VALUES (?1, ?1, ?1, 'solo', 'c', 's', 'p', 0, 1, '{}', 'p', ?2)", rusqlite::params![key, style]).unwrap();
}

fn total(db: &Connection) -> i64 {
    db.query_row("SELECT COALESCE(SUM(n), 0) FROM icon_counts", [], |r| r.get(0)).unwrap()
}

#[test]
fn old_worker_counts_fail_after_0019_and_work_after_the_down_script() {
    let before = migrated("0018_refresh_stats.sql");
    add_icon_pre_0019(&before, "solo/a");
    before.execute(OLD_RECOUNT, ["solo/a"]).expect("the old statement works before 0019");

    let db = migrated("0019_icon_style.sql");
    add_icon(&db, "solo/a", "normal");
    add_icon(&db, "solo/a--round", "round");
    let error = db.execute(OLD_RECOUNT, ["solo/a"]).expect_err("0019 breaks the old Worker's count upsert");
    assert!(error.to_string().contains("ON CONFLICT"), "{error}");

    script(&db, "0019_icon_style_down.sql");
    assert_eq!(total(&db), 2, "the down script counts every icon again");
    db.execute(OLD_RECOUNT, ["solo/a"]).expect("the old Worker counts again after the down script");
    assert_eq!(total(&db), 3);

    script(&db, "0019_icon_style_redo.sql");
    assert_eq!(total(&db), 2, "the redo script recounts from the icons");
    for sql in icon_query::UNCOUNT_ICON.iter().chain(&icon_query::RECOUNT_ICON) {
        db.execute(sql, ["solo/a--round"]).expect("the new Worker counts again after the redo script");
    }
    assert_eq!(total(&db), 2);
    let round: i64 = db.query_row("SELECT n FROM icon_counts WHERE style = 'round'", [], |r| r.get(0)).unwrap();
    assert_eq!(round, 1);
}

fn add_icon_pre_0019(db: &Connection, key: &str) {
    db.execute("INSERT INTO icons(key, icon_id, name, family, category, svg_sha256, preview_url, build_failed, uploaded, record, pushed_at) \
                VALUES (?1, ?1, ?1, 'solo', 'c', 's', 'p', 0, 1, '{}', 'p')", [key]).unwrap();
}
