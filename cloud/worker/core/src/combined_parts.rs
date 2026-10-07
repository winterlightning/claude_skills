//! Whether a combined icon's build failed, again from its parts' current reviews.
//!
//! `POST /api/combinations/build` stores a combined icon (side 64, side 72, container 64) as a failed build, with
//! one error per part, when a drawing it was built from is not approved in Icon review; Icon review then lists it
//! as "failed", not "To review". The parts' reviews change after that: approving the main or sub must take the pair
//! out of "failed", and disapproving one must put it back. These statements say it again from the reviews of the
//! drawings each pair was built from (the part's `built_sha`; its current drawing when none is recorded), whoever
//! built it. A pair whose part was redrawn and only the new drawing approved stays failed until it is rebuilt.
//!
//! Each statement binds one JSON array of combined icon keys (`?1`). App routes run `CHANGED` for the pairs that
//! use a part whose review was written, then, for each changed icon, its uncount, `UPDATE` and recount.

/// The not-approved parts of the combined icons in `?1`, as `errs(key, errors)`: errors is a JSON array of
/// "Main x is not approved in Icon review", the text the build writes, sorted by role.
macro_rules! part_errors {
    () => {
        "WITH parts AS (\
           SELECT i.key, p.role, p.icon FROM icons i JOIN reference_parts p ON p.reference_id = i.icon_id \
            WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.family IN ('side_combination64', 'container_combination64') \
              AND p.icon IS NOT NULL AND COALESCE((SELECT v.status FROM reviews v WHERE v.icon = p.icon AND v.svg_sha256 = \
                  COALESCE(p.built_sha, (SELECT x.svg_sha256 FROM icons x WHERE x.key = p.icon))), '') != 'approve' \
           UNION ALL \
           SELECT i.key, p.role, p.icon FROM icons i JOIN reference_part_sizes p ON p.reference_id = i.icon_id AND p.size = 72 \
            WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.family = 'combination-72' \
              AND p.icon IS NOT NULL AND COALESCE((SELECT v.status FROM reviews v WHERE v.icon = p.icon AND v.svg_sha256 = \
                  COALESCE(p.built_sha, (SELECT x.svg_sha256 FROM icons x WHERE x.key = p.icon))), '') != 'approve'), \
         errs AS (SELECT key, json_group_array(upper(substr(role, 1, 1)) || substr(role, 2) || ' ' || \
                         substr(icon, instr(icon, '/') + 1) || ' is not approved in Icon review') AS errors \
                  FROM (SELECT key, role, icon FROM parts ORDER BY key, role) GROUP BY key) "
    };
}

/// The combined icons (keys) built from a part (`?1`, its icon key) in any size: the ones to check again after
/// that part's review changed.
pub const USING_PART: &str = "SELECT i.key FROM icons i WHERE i.uploaded = 0 AND (\
    (i.family IN ('side_combination64', 'container_combination64') AND i.icon_id IN (SELECT reference_id FROM reference_parts WHERE icon = ?1)) \
    OR (i.family = 'combination-72' AND i.icon_id IN (SELECT reference_id FROM reference_part_sizes WHERE icon = ?1 AND size = 72)))";

/// The icons in `?1` whose failed flag or errors are no longer what their parts' reviews say.
pub const CHANGED: &str = concat!(part_errors!(),
    "SELECT i.key FROM icons i LEFT JOIN errs e ON e.key = i.key \
     WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.uploaded = 0 \
       AND (i.build_failed != (e.key IS NOT NULL) OR COALESCE(json_extract(i.record, '$.errors'), '[]') != COALESCE(e.errors, '[]'))");

/// Store them: the failed flag, the record's errors (and, where the record carries them, its build_failed and
/// validation status) and the list card's copy of each.
pub const UPDATE: [&str; 2] = [
    concat!(part_errors!(),
        "UPDATE icons SET build_failed = EXISTS (SELECT 1 FROM errs e WHERE e.key = icons.key), \
           record = json_set(COALESCE(record, '{}'), '$.errors', json(COALESCE((SELECT e.errors FROM errs e WHERE e.key = icons.key), '[]'))) \
         WHERE key IN (SELECT value FROM json_each(?1)) AND uploaded = 0"),
    "UPDATE icons SET \
       record = CASE WHEN json_type(record, '$.validation') = 'object' THEN json_set(record, \
           '$.validation.status', CASE WHEN build_failed THEN 'invalid' ELSE 'valid' END, \
           '$.validation.automatic_status', CASE WHEN build_failed THEN 'fail' ELSE 'pass' END, \
           '$.validation.errors', json(json_extract(record, '$.errors'))) ELSE record END, \
       card = CASE WHEN card IS NULL THEN NULL ELSE json_set(card, \
           '$.build_failed', json(CASE WHEN build_failed THEN 'true' ELSE 'false' END), \
           '$.validation', json(CASE WHEN json_type(card, '$.validation') = 'object' THEN json_set(json_extract(card, '$.validation'), \
               '$.status', CASE WHEN build_failed THEN 'invalid' ELSE 'valid' END, \
               '$.automatic_status', CASE WHEN build_failed THEN 'fail' ELSE 'pass' END) \
             ELSE json_object('status', CASE WHEN build_failed THEN 'invalid' ELSE 'valid' END, \
                              'automatic_status', CASE WHEN build_failed THEN 'fail' ELSE 'pass' END) END), \
           '$.errors', json(json_extract(record, '$.errors'))) END \
     WHERE key IN (SELECT value FROM json_each(?1)) AND uploaded = 0",
];

#[cfg(test)]
mod tests {
    use super::*;
    use rusqlite::{params, Connection};

    fn db() -> Connection {
        let db = Connection::open_in_memory().unwrap();
        db.execute_batch("CREATE TABLE icons (key TEXT PRIMARY KEY, icon_id TEXT, family TEXT, svg_sha256 TEXT, uploaded INTEGER DEFAULT 0, \
                            build_failed INTEGER DEFAULT 0, record TEXT, card TEXT);
                          CREATE TABLE reviews (icon TEXT, svg_sha256 TEXT, status TEXT, PRIMARY KEY (icon, svg_sha256));
                          CREATE TABLE reference_parts (reference_id TEXT, role TEXT, icon TEXT, built_sha TEXT);
                          CREATE TABLE reference_part_sizes (reference_id TEXT, role TEXT, size INTEGER, icon TEXT, built_sha TEXT);").unwrap();
        for (key, sha) in [("solo/bag", "m1"), ("sub/check", "s2")] {
            db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, record) VALUES (?, ?, ?, ?, '{}')",
                       params![key, key, key.split('/').next().unwrap(), sha]).unwrap();
        }
        // Built from main m1 and sub s1; the sub has since been redrawn (s2).
        db.execute_batch("INSERT INTO reference_parts VALUES ('p1', 'main', 'solo/bag', 'm1'), ('p1', 'sub', 'sub/check', 's1');
            INSERT INTO icons(key, icon_id, family, svg_sha256, build_failed, record, card) VALUES ('side_combination64/p1', 'p1',
              'side_combination64', 'c1', 1, '{\"parts\":{\"main\":\"solo/bag\",\"sub\":\"sub/check\"},\"errors\":[\"Main bag is not approved in Icon review\"]}',
              '{\"key\":\"side_combination64/p1\",\"build_failed\":true,\"validation\":{\"status\":\"invalid\",\"automatic_status\":\"fail\"}}');").unwrap();
        db
    }

    fn changed(db: &Connection) -> Vec<String> {
        let mut statement = db.prepare(CHANGED).unwrap();
        let keys = statement.query_map(params![r#"["side_combination64/p1"]"#], |r| r.get(0)).unwrap();
        keys.map(Result::unwrap).collect()
    }

    fn update(db: &Connection) -> (bool, String, String) {
        for sql in UPDATE {
            db.execute(sql, params![r#"["side_combination64/p1"]"#]).unwrap();
        }
        db.query_row("SELECT build_failed, json_extract(record, '$.errors'), card FROM icons WHERE key = 'side_combination64/p1'", [],
                     |r| Ok((r.get::<_, i64>(0)? != 0, r.get(1)?, r.get(2)?))).unwrap()
    }

    #[test]
    fn approving_the_parts_ends_the_failed_build() {
        let db = db();
        db.execute_batch("INSERT INTO reviews VALUES ('solo/bag', 'm1', 'pending'), ('sub/check', 's1', 'approve');").unwrap();
        assert!(changed(&db).is_empty(), "still failing for the same reason");
        db.execute("UPDATE reviews SET status = 'approve' WHERE icon = 'solo/bag'", []).unwrap();
        assert_eq!(changed(&db), vec!["side_combination64/p1"]);
        let (failed, errors, card) = update(&db);
        assert!(!failed);
        assert_eq!(errors, "[]");
        let card: serde_json::Value = serde_json::from_str(&card).unwrap();
        assert_eq!(card["build_failed"], false);
        assert_eq!(card["validation"]["status"], "valid");
        assert!(changed(&db).is_empty());
        assert_eq!(db.query_row(USING_PART, params!["sub/check"], |r| r.get::<_, String>(0)).unwrap(), "side_combination64/p1");
    }

    #[test]
    fn the_built_drawing_counts_not_a_later_one() {
        let db = db();
        // Only the sub's new drawing (s2) is approved; the pair was built from s1.
        db.execute_batch("INSERT INTO reviews VALUES ('solo/bag', 'm1', 'approve'), ('sub/check', 's2', 'approve'), ('sub/check', 's1', 'pending');").unwrap();
        let (failed, errors, _) = update(&db);
        assert!(failed);
        assert_eq!(errors, r#"["Sub check is not approved in Icon review"]"#);
    }
}
