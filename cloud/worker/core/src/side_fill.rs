//! SQL of the fill side pairs writes (migration 0023) that must hold under concurrent edits, shared by the Worker
//! routes (routes/side_fill.rs, routes/styled.rs) and tested here on the migrated schema.

/// Fails its batch when the pair (`?1`) is no longer at version `?2`: it inserts NULL into fill_guard's NOT NULL
/// column, and D1 rolls the whole batch back. Put it first in a batch that must not land on a changed pair.
pub const GUARD: &str = "INSERT INTO fill_guard(ok) SELECT NULL \
    WHERE NOT EXISTS (SELECT 1 FROM fill_pairs WHERE reference_id = ?1 AND version = ?2)";

/// Whether a batch failed on GUARD (the pair changed since the request was made).
pub fn is_guard_error(message: &str) -> bool {
    message.contains("fill_guard")
}

/// A person changed the pair's picks (`?1`, at time `?2`): a new version, and the import leaves its picks alone.
pub const EDITED: &str = "UPDATE fill_pairs SET version = version + 1, edited_at = ?2, updated_at = ?2 WHERE reference_id = ?1";

/// Why a pair whose main and sub both have no fill is not combined (side_fill d1_import writes the same text).
pub const NO_FILL_NOTE: &str = "Neither the main nor the sub has a fill: this pair has no fill version.";

/// The output keys in use for a pair (`?1` = `side_combination64/<id>--fill`): every icon with that key or a
/// numbered one (`--fill-2` …), kept reviewed outputs of removed picks included. A key range on the primary key.
pub const OUTPUT_KEYS: &str = "SELECT key FROM icons WHERE key >= ?1 AND key < ?1 || '.'";

/// The first fill of a part (`?1`, its solo / sub key; `?2` the time): the part becomes Filled and the pairs that
/// waited for a fill on either part (state uncombined, NO_FILL_NOTE `?3`) can be picked, the totals moving with
/// them. In this order, each reading what the one before left. Nothing changes for a part already filled. Each
/// statement takes the first `n` of (?1, ?2, ?3).
pub const FIRST_FILL: [(&str, usize); 7] = [
    ("UPDATE fill_counts SET n = n - 1 WHERE (scope, status) IN \
        (SELECT role, status FROM fill_parts WHERE key = ?1 AND status IN ('no-fill', 'outline'))", 1),
    ("INSERT INTO fill_counts(scope, status, n) SELECT role, 'ready', 1 FROM fill_parts WHERE key = ?1 AND status IN ('no-fill', 'outline') \
        ON CONFLICT(scope, status) DO UPDATE SET n = n + 1", 1),
    ("UPDATE fill_parts SET status = 'ready', note = 'Has a fill: combined in its pairs.', updated_at = ?2 \
        WHERE key = ?1 AND status IN ('no-fill', 'outline')", 2),
    ("INSERT OR IGNORE INTO fill_counts(scope, status, n) SELECT 'pairs', 'unpicked', 0 \
        WHERE EXISTS (SELECT 1 FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) AND ?2 IS NOT NULL", 3),
    ("UPDATE fill_counts SET n = n + (SELECT COUNT(*) FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) \
        WHERE scope = 'pairs' AND status = 'unpicked' AND ?2 IS NOT NULL", 3),
    ("UPDATE fill_counts SET n = n - (SELECT COUNT(*) FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) \
        WHERE scope = 'pairs' AND status = 'uncombined' AND ?2 IS NOT NULL", 3),
    ("UPDATE fill_pairs SET state = 'unpicked', note = NULL, updated_at = ?2 \
        WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)", 3),
];

#[cfg(test)]
mod tests {
    use super::*;
    use rusqlite::{params, Connection};

    fn db() -> Connection {
        let db = Connection::open_in_memory().unwrap();
        let dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
        let mut files: Vec<_> = std::fs::read_dir(&dir).unwrap().map(|e| e.unwrap().path()).collect();
        files.sort();
        for f in &files { db.execute_batch(&std::fs::read_to_string(f).unwrap()).unwrap(); }
        db.execute_batch("INSERT INTO \"references\"(reference_id, kind, concept, source) VALUES ('p1', 'combination', 'P', 't'), ('p2', 'combination', 'Q', 't');
            INSERT INTO fill_pairs(reference_id, sort_key, state, main_source, sub_source, updated_at) VALUES ('p1', 'p p1', 'picked', 'solo/a', 'sub/b', 'x');").unwrap();
        db
    }

    #[test]
    fn a_batch_on_a_changed_pair_lands_nothing() {
        let mut db = db();
        let tx = db.transaction().unwrap();
        tx.execute(GUARD, params!["p1", 0]).unwrap();          // current version: nothing inserted, nothing fails
        tx.execute("UPDATE fill_pairs SET note = 'built' WHERE reference_id = 'p1'", []).unwrap();
        tx.commit().unwrap();
        db.execute(EDITED, params!["p1", "now"]).unwrap();     // another tab changed the picks
        let tx = db.transaction().unwrap();
        let error = tx.execute(GUARD, params!["p1", 0]).unwrap_err().to_string();
        assert!(is_guard_error(&error), "{error}");
        drop(tx);                                              // rolled back
        let (note, version, edited): (String, i64, String) = db.query_row("SELECT note, version, edited_at FROM fill_pairs WHERE reference_id = 'p1'",
            [], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap();
        assert_eq!((note.as_str(), version, edited.as_str()), ("built", 1, "now"));
        assert_eq!(db.query_row("SELECT COUNT(*) FROM fill_guard", [], |r| r.get::<_, i64>(0)).unwrap(), 0);
    }

    #[test]
    fn output_keys_include_kept_outputs_and_no_other_pair() {
        let db = db();
        for key in ["side_combination64/p1--fill", "side_combination64/p1--fill-3", "side_combination64/p1", "side_combination64/p10--fill"] {
            db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, record, pushed_at) VALUES (?1, ?1, 'side_combination64', 's', '{}', 'x')", [key]).unwrap();
        }
        let keys: Vec<String> = db.prepare(OUTPUT_KEYS).unwrap().query_map(["side_combination64/p1--fill"], |r| r.get(0)).unwrap()
            .map(Result::unwrap).collect();
        assert_eq!(keys, ["side_combination64/p1--fill", "side_combination64/p1--fill-3"]);
    }

    #[test]
    fn the_first_fill_of_a_part_unlocks_its_pairs_once() {
        let db = db();
        db.execute_batch(&format!("INSERT INTO fill_pairs(reference_id, sort_key, state, main_source, sub_source, note, updated_at)
                VALUES ('p2', 'q p2', 'uncombined', 'solo/c', 'sub/d', '{NO_FILL_NOTE}', 'x');
            INSERT INTO fill_parts(key, role, sort_key, status, updated_at) VALUES ('solo/c', 'main', 'c', 'outline', 'x');
            INSERT INTO fill_counts VALUES ('pairs', 'uncombined', 1), ('pairs', 'picked', 1), ('main', 'outline', 1), ('main', 'ready', 5);")).unwrap();
        for _ in 0..2 {           // a second fill of the same part changes nothing
            for (sql, n) in FIRST_FILL {
                let all: [&dyn rusqlite::ToSql; 3] = [&"solo/c", &"now", &NO_FILL_NOTE];
                db.execute(sql, &all[..n]).unwrap();
            }
        }
        let counts: Vec<(String, String, i64)> = db.prepare("SELECT scope, status, n FROM fill_counts ORDER BY 1, 2").unwrap()
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap().map(Result::unwrap).collect();
        assert_eq!(counts, [("main".into(), "outline".into(), 0), ("main".into(), "ready".into(), 6),
            ("pairs".into(), "picked".into(), 1), ("pairs".into(), "uncombined".into(), 0), ("pairs".into(), "unpicked".into(), 1)]);
        let (state, note): (String, Option<String>) = db.query_row("SELECT state, note FROM fill_pairs WHERE reference_id = 'p2'", [],
            |r| Ok((r.get(0)?, r.get(1)?))).unwrap();
        assert_eq!((state.as_str(), note), ("unpicked", None));
        assert_eq!(db.query_row("SELECT status FROM fill_parts WHERE key = 'solo/c'", [], |r| r.get::<_, String>(0)).unwrap(), "ready");
    }
}
