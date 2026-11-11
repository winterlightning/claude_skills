//! SQL of the fill side pairs writes (migrations 0023, 0026) that must hold under concurrent edits, shared by the Worker
//! routes (routes/side_fill.rs, routes/styled.rs) and tested here on the migrated schema.
//!
//! A pair is a reference at a size: 64 (solo / sub parts, side_combination64 outputs) or 72 (main-54 / sub-36 parts,
//! combination-72 outputs). Every statement that names a pair takes its size; the 72 totals are fill_counts scopes
//! with a `:72` suffix (pairs:72, main:72, sub:72), the 64 ones keep their names.

/// The fill_counts scope of a base scope (pairs, main, sub) at a size.
pub fn scope(base: &str, size: i64) -> String {
    if size == 72 { format!("{base}:72") } else { base.to_string() }
}

/// The sizes a fill side pair comes in.
pub fn size_ok(size: i64) -> bool {
    size == 64 || size == 72
}

/// Fails its batch when the pair (`?1` at size `?3`) is no longer at version `?2`: it inserts NULL into fill_guard's
/// NOT NULL column, and D1 rolls the whole batch back. Put it first in a batch that must not land on a changed pair.
pub const GUARD: &str = "INSERT INTO fill_guard(ok) SELECT NULL \
    WHERE NOT EXISTS (SELECT 1 FROM fill_pairs WHERE reference_id = ?1 AND size = ?3 AND version = ?2)";

/// Whether a batch failed on GUARD (the pair changed since the request was made).
pub fn is_guard_error(message: &str) -> bool {
    message.contains("fill_guard")
}

/// A person changed the pair's picks (`?1` at size `?3`, at time `?2`): a new version, and the import leaves its picks
/// alone. It returns the version this very write committed (never read again later: another tab may have saved since).
pub const EDITED: &str = "UPDATE fill_pairs SET version = version + 1, edited_at = ?2, updated_at = ?2 WHERE reference_id = ?1 AND size = ?3 RETURNING version";

/// A build lands only on what it was made from (`?1` pair, `?2` version, `?3` rank, `?4` / `?5` the main icon and its
/// drawing, `?6` / `?7` the sub's, `?8` the size): the pair at that version, the pick still of those icons, each still
/// that drawing. Checked inside the batch, so a pick, move, unpick or redraw that lands first makes it fail whole.
pub const BUILD_GUARD: &str = "INSERT INTO fill_guard(ok) SELECT NULL WHERE \
    NOT EXISTS (SELECT 1 FROM fill_pairs WHERE reference_id = ?1 AND size = ?8 AND version = ?2) \
    OR NOT EXISTS (SELECT 1 FROM reference_part_fills WHERE reference_id = ?1 AND size = ?8 AND rank = ?3 AND role = 'main' AND icon = ?4) \
    OR NOT EXISTS (SELECT 1 FROM reference_part_fills WHERE reference_id = ?1 AND size = ?8 AND rank = ?3 AND role = 'sub' AND icon = ?6) \
    OR NOT EXISTS (SELECT 1 FROM icons WHERE key = ?4 AND svg_sha256 = ?5) \
    OR NOT EXISTS (SELECT 1 FROM icons WHERE key = ?6 AND svg_sha256 = ?7)";

/// The fill_counts scope of the pairs at the size `?3`.
const PAIRS_SCOPE: &str = "(CASE WHEN ?3 = 72 THEN 'pairs:72' ELSE 'pairs' END)";

/// A pair (`?1` at size `?3`, at time `?2`) moved to the state `next` (an SQL expression: `'picked'`, or one reading
/// the picks the batch left) with its totals, both from the state it has when these statements run, not one read
/// before: a write that changed it meanwhile (a first fill, another pick) cannot leave the totals off.
pub fn state_moves(next: &str) -> [String; 3] {
    [format!("UPDATE fill_counts SET n = n - 1 WHERE scope = {PAIRS_SCOPE} \
              AND status = (SELECT state FROM fill_pairs WHERE reference_id = ?1 AND size = ?3) AND status != {next} AND ?2 IS NOT NULL"),
     format!("INSERT INTO fill_counts(scope, status, n) SELECT {PAIRS_SCOPE}, {next}, 1 FROM fill_pairs WHERE reference_id = ?1 AND size = ?3 \
              AND state != {next} AND ?2 IS NOT NULL ON CONFLICT(scope, status) DO UPDATE SET n = n + 1"),
     format!("UPDATE fill_pairs SET state = {next}, note = CASE WHEN {next} = 'picked' THEN NULL ELSE note END, updated_at = ?2 \
              WHERE reference_id = ?1 AND size = ?3")]
}

/// The state a pair (`?1` at size `?3`) is in once a batch removed one of its picks: picked while any is left.
pub const STATE_AFTER_UNPICK: &str = "(CASE WHEN EXISTS (SELECT 1 FROM reference_part_fills WHERE reference_id = ?1 AND size = ?3) \
    THEN 'picked' ELSE 'unpicked' END)";

/// Why a pair whose main and sub both have no fill is not combined (side_fill d1_import writes the same text).
pub const NO_FILL_NOTE: &str = "Neither the main nor the sub has a fill: this pair has no fill version.";

/// The output keys in use for a pair (`?1` = `side_combination64/<id>--fill` or `combination-72/<id>--fill`): every
/// icon with that key or a numbered one (`--fill-2` …), kept reviewed outputs of removed picks included. A key range
/// on the primary key.
pub const OUTPUT_KEYS: &str = "SELECT key FROM icons WHERE key >= ?1 AND key < ?1 || '.'";

/// The first fill of a part (`?1`, its solo / sub / main-54 / sub-36 key; `?2` the time): the part becomes Filled and
/// the pairs that waited for a fill on either part (state uncombined, NO_FILL_NOTE `?3`) can be picked, the totals of
/// the part's size moving with them. In this order, each reading what the one before left. Nothing changes for a part
/// already filled. Each statement takes the first `n` of (?1, ?2, ?3).
pub const FIRST_FILL: [(&str, usize); 7] = [
    ("UPDATE fill_counts SET n = n - 1 WHERE (scope, status) IN \
        (SELECT role || CASE WHEN ?1 LIKE 'main-54/%' OR ?1 LIKE 'sub-36/%' THEN ':72' ELSE '' END, status FROM fill_parts \
         WHERE key = ?1 AND status IN ('no-fill', 'outline'))", 1),
    ("INSERT INTO fill_counts(scope, status, n) SELECT role || CASE WHEN ?1 LIKE 'main-54/%' OR ?1 LIKE 'sub-36/%' THEN ':72' ELSE '' END, \
        'ready', 1 FROM fill_parts WHERE key = ?1 AND status IN ('no-fill', 'outline') \
        ON CONFLICT(scope, status) DO UPDATE SET n = n + 1", 1),
    ("UPDATE fill_parts SET status = 'ready', note = 'Has a fill: combined in its pairs.', updated_at = ?2 \
        WHERE key = ?1 AND status IN ('no-fill', 'outline')", 2),
    ("INSERT OR IGNORE INTO fill_counts(scope, status, n) SELECT 'pairs' || CASE WHEN ?1 LIKE 'main-54/%' OR ?1 LIKE 'sub-36/%' THEN ':72' ELSE '' END, \
        'unpicked', 0 WHERE EXISTS (SELECT 1 FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) \
        AND ?2 IS NOT NULL", 3),
    ("UPDATE fill_counts SET n = n + (SELECT COUNT(*) FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) \
        WHERE scope = 'pairs' || CASE WHEN ?1 LIKE 'main-54/%' OR ?1 LIKE 'sub-36/%' THEN ':72' ELSE '' END AND status = 'unpicked' AND ?2 IS NOT NULL", 3),
    ("UPDATE fill_counts SET n = n - (SELECT COUNT(*) FROM fill_pairs WHERE state = 'uncombined' AND note = ?3 AND (main_source = ?1 OR sub_source = ?1)) \
        WHERE scope = 'pairs' || CASE WHEN ?1 LIKE 'main-54/%' OR ?1 LIKE 'sub-36/%' THEN ':72' ELSE '' END AND status = 'uncombined' AND ?2 IS NOT NULL", 3),
    // A new version too: a pick of one of these pairs made from what it was before is refused.
    ("UPDATE fill_pairs SET state = 'unpicked', note = NULL, version = version + 1, updated_at = ?2 \
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
        tx.execute(GUARD, params!["p1", 0, 64]).unwrap();          // current version: nothing inserted, nothing fails
        tx.execute("UPDATE fill_pairs SET note = 'built' WHERE reference_id = 'p1'", []).unwrap();
        tx.commit().unwrap();
        db.query_row(EDITED, params!["p1", "now", 64], |r| r.get::<_, i64>(0)).unwrap();     // another tab changed the picks
        let tx = db.transaction().unwrap();
        let error = tx.execute(GUARD, params!["p1", 0, 64]).unwrap_err().to_string();
        assert!(is_guard_error(&error), "{error}");
        drop(tx);                                              // rolled back
        let (note, version, edited): (String, i64, String) = db.query_row("SELECT note, version, edited_at FROM fill_pairs WHERE reference_id = 'p1'",
            [], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap();
        assert_eq!((note.as_str(), version, edited.as_str()), ("built", 1, "now"));
        assert_eq!(db.query_row("SELECT COUNT(*) FROM fill_guard", [], |r| r.get::<_, i64>(0)).unwrap(), 0);
    }

    #[test]
    fn each_save_returns_the_version_it_committed() {
        let db = db();
        // Tab A saves, then tab B: A is told the version A made (1), never B's (2).
        let a: i64 = db.query_row(EDITED, params!["p1", "a", 64], |r| r.get(0)).unwrap();
        let b: i64 = db.query_row(EDITED, params!["p1", "b", 64], |r| r.get(0)).unwrap();
        assert_eq!((a, b), (1, 2));
        // A builds with its version: refused, B's layout stays.
        let mut db = db;
        let tx = db.transaction().unwrap();
        assert!(is_guard_error(&tx.execute(GUARD, params!["p1", a, 64]).unwrap_err().to_string()));
    }

    #[test]
    fn a_build_lands_only_on_the_drawings_it_was_made_from() {
        let db = db();
        db.execute_batch("INSERT INTO icons(key, icon_id, family, svg_sha256, record, pushed_at) VALUES ('solo/a--fill', 'a', 'solo', 'm1', '{}', 'x'), ('sub/b--fill', 'b', 'sub', 's1', '{}', 'x');
            INSERT INTO reference_part_fills(reference_id, role, rank, icon, updated_at) VALUES ('p1', 'main', 1, 'solo/a--fill', 'x'), ('p1', 'sub', 1, 'sub/b--fill', 'x');").unwrap();
        let build = |main_sha: &str, sub_icon: &str| db.execute(BUILD_GUARD, params!["p1", 0, 1, "solo/a--fill", main_sha, sub_icon, "s1", 64]);
        build("m1", "sub/b--fill").unwrap();                                  // what it was made from: lands
        db.execute("UPDATE icons SET svg_sha256 = 'm2' WHERE key = 'solo/a--fill'", []).unwrap();
        assert!(is_guard_error(&build("m1", "sub/b--fill").unwrap_err().to_string()), "the main was redrawn meanwhile");
        assert!(is_guard_error(&build("m2", "sub/other").unwrap_err().to_string()), "the pick's sub changed meanwhile");
        build("m2", "sub/b--fill").unwrap();
    }

    #[test]
    fn totals_move_from_the_state_a_pair_has_when_the_batch_runs() {
        let db = db();
        db.execute_batch(&format!("INSERT INTO fill_pairs(reference_id, sort_key, state, main_source, sub_source, note, updated_at)
                VALUES ('p2', 'q p2', 'uncombined', 'solo/c', 'sub/d', '{NO_FILL_NOTE}', 'x');
            INSERT INTO fill_counts VALUES ('pairs', 'uncombined', 1), ('pairs', 'picked', 1), ('pairs', 'unpicked', 0);")).unwrap();
        // A pick of p2 was read while it waited for a fill; a first fill makes it unpicked before the pick lands.
        for (sql, n) in FIRST_FILL {
            let all: [&dyn rusqlite::ToSql; 3] = [&"solo/c", &"now", &NO_FILL_NOTE];
            db.execute(sql, &all[..n]).unwrap();
        }
        assert_eq!(db.query_row("SELECT version FROM fill_pairs WHERE reference_id = 'p2'", [], |r| r.get::<_, i64>(0)).unwrap(), 1);
        for sql in state_moves("'picked'") { db.execute(&sql, params!["p2", "now", 64]).unwrap(); }
        let counts: Vec<(String, i64)> = db.prepare("SELECT status, n FROM fill_counts WHERE scope = 'pairs' ORDER BY 1").unwrap()
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?))).unwrap().map(Result::unwrap).collect();
        assert_eq!(counts, [("picked".into(), 2), ("uncombined".into(), 0), ("unpicked".into(), 0)]);
        // Picking an already picked pair moves nothing.
        for sql in state_moves("'picked'") { db.execute(&sql, params!["p2", "now", 64]).unwrap(); }
        assert_eq!(db.query_row("SELECT n FROM fill_counts WHERE scope = 'pairs' AND status = 'picked'", [], |r| r.get::<_, i64>(0)).unwrap(), 2);
        // Removing the last pick: unpicked, read from the picks the batch left.
        for sql in state_moves(STATE_AFTER_UNPICK) { db.execute(&sql, params!["p2", "now", 64]).unwrap(); }
        assert_eq!(db.query_row("SELECT state FROM fill_pairs WHERE reference_id = 'p2'", [], |r| r.get::<_, String>(0)).unwrap(), "unpicked");
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

    #[test]
    fn a_72_pair_is_its_own_row_beside_the_64_one() {
        let db = db();
        // The same reference at 72: its own version, state, picks and totals; the 64 pair is never touched.
        db.execute_batch("INSERT INTO fill_pairs(reference_id, size, sort_key, state, main_source, sub_source, updated_at)
                VALUES ('p1', 72, 'p p1', 'unpicked', 'main-54/a', 'sub-36/b', 'x');
            INSERT INTO fill_counts VALUES ('pairs', 'picked', 1), ('pairs:72', 'unpicked', 1);
            INSERT INTO reference_part_fills(reference_id, size, role, rank, icon, updated_at) VALUES ('p1', 72, 'main', 1, 'main-54/a--fill', 'x'),
              ('p1', 72, 'sub', 1, 'sub-36/b', 'x');").unwrap();
        let v72: i64 = db.query_row(EDITED, params!["p1", "now", 72], |r| r.get(0)).unwrap();
        assert_eq!(v72, 1);
        for sql in state_moves("'picked'") { db.execute(&sql, params!["p1", "now", 72]).unwrap(); }
        let rows: Vec<(i64, String, i64)> = db.prepare("SELECT size, state, version FROM fill_pairs WHERE reference_id = 'p1' ORDER BY size").unwrap()
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap().map(Result::unwrap).collect();
        assert_eq!(rows, [(64, "picked".into(), 0), (72, "picked".into(), 1)]);
        let counts: Vec<(String, String, i64)> = db.prepare("SELECT scope, status, n FROM fill_counts ORDER BY 1, 2").unwrap()
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap().map(Result::unwrap).collect();
        assert_eq!(counts, [("pairs".into(), "picked".into(), 1), ("pairs:72".into(), "picked".into(), 1), ("pairs:72".into(), "unpicked".into(), 0)]);
        // A 72 build guard reads only the 72 pick.
        db.execute_batch("INSERT INTO icons(key, icon_id, family, svg_sha256, record, pushed_at) VALUES ('main-54/a--fill', 'a', 'main-54', 'm1', '{}', 'x'),
            ('sub-36/b', 'b', 'sub-36', 's1', '{}', 'x');").unwrap();
        db.execute(BUILD_GUARD, params!["p1", 1, 1, "main-54/a--fill", "m1", "sub-36/b", "s1", 72]).unwrap();
        assert!(is_guard_error(&db.execute(BUILD_GUARD, params!["p1", 1, 1, "main-54/a--fill", "m1", "sub-36/b", "s1", 64]).unwrap_err().to_string()));
        assert_eq!(scope("main", 72), "main:72");
        assert_eq!(scope("pairs", 64), "pairs");
    }

    #[test]
    fn the_first_fill_of_a_72_part_moves_the_72_totals() {
        let db = db();
        db.execute_batch(&format!("INSERT INTO fill_pairs(reference_id, size, sort_key, state, main_source, sub_source, note, updated_at)
                VALUES ('p2', 72, 'q p2', 'uncombined', 'main-54/c', 'sub-36/d', '{NO_FILL_NOTE}', 'x');
            INSERT INTO fill_parts(key, role, size, sort_key, status, updated_at) VALUES ('main-54/c', 'main', 72, 'c', 'outline', 'x');
            INSERT INTO fill_counts VALUES ('pairs', 'uncombined', 4), ('pairs:72', 'uncombined', 1), ('main:72', 'outline', 1), ('main', 'outline', 7);")).unwrap();
        for (sql, n) in FIRST_FILL {
            let all: [&dyn rusqlite::ToSql; 3] = [&"main-54/c", &"now", &NO_FILL_NOTE];
            db.execute(sql, &all[..n]).unwrap();
        }
        let counts: Vec<(String, String, i64)> = db.prepare("SELECT scope, status, n FROM fill_counts ORDER BY 1, 2").unwrap()
            .query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?))).unwrap().map(Result::unwrap).collect();
        assert_eq!(counts, [("main".into(), "outline".into(), 7), ("main:72".into(), "outline".into(), 0), ("main:72".into(), "ready".into(), 1),
            ("pairs".into(), "uncombined".into(), 4), ("pairs:72".into(), "uncombined".into(), 0), ("pairs:72".into(), "unpicked".into(), 1)]);
    }
}
