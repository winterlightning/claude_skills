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

// A native form carries the catalog key (model_key and/or text/<icon>) and the exact
// SVG it embeds. Never guess by name, reference, or a hash shared by several icons.
// Conflicting identities fail closed; malformed JSON behaves like a missing pick.
macro_rules! parts64 {
    () => {
        "WITH forms64 AS (SELECT p.*, CASE WHEN json_valid(p.form) THEN p.form ELSE '{}' END AS text_form \
                         FROM reference_parts p), \
         identities64 AS (SELECT f.*, \
           CASE WHEN json_type(text_form, '$.model_key') = 'text' THEN NULLIF(json_extract(text_form, '$.model_key'), '') END AS model_key, \
           CASE WHEN json_extract(text_form, '$.family') = 'text' AND json_type(text_form, '$.icon') = 'text' \
                     AND length(json_extract(text_form, '$.icon')) > 0 \
                THEN 'text/' || json_extract(text_form, '$.icon') END AS text_key \
           FROM forms64 f), \
         parts64 AS (SELECT f.*, CASE WHEN icon IS NOT NULL THEN icon \
           WHEN role = 'sub' AND json_extract(text_form, '$.native_text') = 1 \
             AND COALESCE(json_extract(text_form, '$.family'), 'text') = 'text' \
             AND (json_extract(text_form, '$.model_key') IS NULL OR model_key IS NOT NULL) \
             AND (json_extract(text_form, '$.icon') IS NULL OR text_key IS NOT NULL) \
             AND (model_key IS NULL OR text_key IS NULL OR model_key = text_key) \
             AND COALESCE(model_key, text_key) GLOB 'text/?*' \
           THEN COALESCE(model_key, text_key) END AS resolved_icon, \
           CASE WHEN json_type(text_form, '$.sha256') = 'text' THEN NULLIF(json_extract(text_form, '$.sha256'), '') END AS form_sha \
           FROM identities64 f) "
    };
}

// Native text is rendered from the stored form, not automatically replaced by a
// newly picked text drawing. Both the form and any recorded build must still match.
macro_rules! invalid_native64 {
    () => {
        "(p.icon IS NULL AND (p.resolved_icon IS NULL OR x.family IS NOT 'text' OR p.form_sha IS NULL \
           OR p.form_sha IS NOT x.svg_sha256 OR (p.built_sha IS NOT NULL AND p.built_sha IS NOT p.form_sha)))"
    };
}

/// Resolve native text for a build from the server's forms, never from client identity claims.
pub const NATIVE_TEXT_PARTS: &str = concat!(parts64!(),
    "SELECT p.reference_id, p.role, x.key AS icon, p.form_sha AS svg_sha256, \
       CASE WHEN json_type(p.text_form, '$.document') = 'text' THEN json_extract(p.text_form, '$.document') END AS document, x.svg_sha256 AS current_sha, \
       (SELECT status FROM reviews v WHERE v.icon = x.key AND v.svg_sha256 = p.form_sha) AS review \
     FROM parts64 p LEFT JOIN icons x ON x.key = p.resolved_icon AND x.family = 'text' \
     WHERE p.icon IS NULL AND p.reference_id IN (SELECT value FROM json_each(?1))");

/// The not-approved parts of the combined icons in `?1`, as `errs(key, errors)`: errors is a JSON array of
/// "Main x is not approved in Icon review", the text the build writes, sorted by role.
macro_rules! part_errors {
    () => {
        concat!(parts64!(), ", parts AS (\
           SELECT i.key, p.role, p.resolved_icon AS icon FROM icons i JOIN parts64 p ON p.reference_id = i.icon_id \
             LEFT JOIN icons x ON x.key = p.resolved_icon \
            WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.family IN ('side_combination64', 'container_combination64') \
              AND (", invalid_native64!(), " OR x.key IS NULL OR COALESCE((SELECT v.status FROM reviews v \
                WHERE v.icon = p.resolved_icon AND v.svg_sha256 = COALESCE(p.built_sha, \
                    CASE WHEN p.icon IS NULL THEN p.form_sha END, x.svg_sha256)), '') != 'approve') \
           UNION ALL \
           SELECT i.key, p.role, p.icon FROM icons i JOIN reference_part_sizes p ON p.reference_id = COALESCE(json_extract(i.record, '$.reference_id'), i.icon_id) AND p.size = 72 \
            WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.family IN ('combination-72', 'container-combination-72') \
              AND COALESCE(i.style, '') != 'fill' \
              AND p.icon IS NOT NULL AND COALESCE((SELECT v.status FROM reviews v WHERE v.icon = p.icon AND v.svg_sha256 = \
                  COALESCE(p.built_sha, (SELECT x.svg_sha256 FROM icons x WHERE x.key = p.icon))), '') != 'approve' \
           UNION ALL \
           SELECT i.key, p.role, p.icon FROM icons i JOIN reference_part_fills m ON m.combined = i.key AND m.role = 'main' \
             JOIN reference_part_fills p ON p.reference_id = m.reference_id AND p.size = m.size AND p.rank = m.rank \
            WHERE i.key IN (SELECT value FROM json_each(?1)) AND i.family IN ('side_combination64', 'combination-72') AND i.style = 'fill' \
              AND p.icon IS NOT NULL AND COALESCE((SELECT v.status FROM reviews v WHERE v.icon = p.icon AND v.svg_sha256 = \
                  COALESCE(p.built_sha, (SELECT x.svg_sha256 FROM icons x WHERE x.key = p.icon))), '') != 'approve'), \
         errs AS (SELECT key, json_group_array(upper(substr(role, 1, 1)) || substr(role, 2) || ' ' || \
                         COALESCE(substr(icon, instr(icon, '/') + 1), '(none picked)') || ' is not approved in Icon review') AS errors \
                  FROM (SELECT key, role, icon FROM parts ORDER BY key, role) GROUP BY key) ")
    };
}

/// Parts blocking side-64 approval: current approval plus matching build/form hashes.
pub const UNAPPROVED_64: &str = concat!(parts64!(),
    "SELECT p.role, p.resolved_icon AS icon FROM parts64 p LEFT JOIN icons x ON x.key = p.resolved_icon \
     WHERE p.reference_id = ?1 AND (", invalid_native64!(), " \
       OR (p.built_sha IS NOT NULL AND p.built_sha IS NOT x.svg_sha256) \
       OR COALESCE((SELECT status FROM reviews v WHERE v.icon = x.key AND v.svg_sha256 = x.svg_sha256), '') != 'approve') \
     ORDER BY p.role");

/// The combined icons (keys) built from a part (`?1`, its icon key) in any size: the ones to check again after
/// that part's review changed. It runs on every review, so the 64 branches look icons up by key, from the part
/// tables (a combined 64 icon's key is `<family>/<reference_id>`, a fill output's is its pick's `combined`), never
/// by walking a family: Side combination 64 holds the fill outputs too.
pub const USING_PART: &str = concat!(parts64!(), "SELECT i.key FROM icons i WHERE (i.uploaded = 0 OR (i.family = 'container-combination-72' AND json_extract(i.record, '$.built_at') IS NOT NULL)) AND (\
    i.key IN (SELECT f.family || '/' || p.reference_id FROM parts64 p, \
        (SELECT 'side_combination64' AS family UNION ALL SELECT 'container_combination64') f WHERE p.resolved_icon = ?1) \
    OR (i.family IN ('combination-72', 'container-combination-72') AND COALESCE(i.style, '') != 'fill' AND COALESCE(json_extract(i.record, '$.reference_id'), i.icon_id) IN (SELECT reference_id FROM reference_part_sizes WHERE icon = ?1 AND size = 72)) \
    OR i.key IN (SELECT m.combined FROM reference_part_fills m WHERE m.role = 'main' AND m.combined IS NOT NULL \
        AND EXISTS (SELECT 1 FROM reference_part_fills x WHERE x.icon = ?1 AND x.reference_id = m.reference_id AND x.size = m.size)))");

/// The icons in `?1` whose failed flag or errors are no longer what their parts' reviews say.
pub const CHANGED: &str = concat!(part_errors!(),
    "SELECT i.key FROM icons i LEFT JOIN errs e ON e.key = i.key \
     WHERE i.key IN (SELECT value FROM json_each(?1)) AND (i.uploaded = 0 OR (i.family = 'container-combination-72' AND json_extract(i.record, '$.built_at') IS NOT NULL)) \
       AND (i.build_failed != (e.key IS NOT NULL) OR COALESCE(json_extract(i.record, '$.errors'), '[]') != COALESCE(e.errors, '[]'))");

/// Store them: the failed flag, the record's errors (and, where the record carries them, its build_failed and
/// validation status) and the list card's copy of each.
pub const UPDATE: [&str; 2] = [
    concat!(part_errors!(),
        "UPDATE icons SET build_failed = EXISTS (SELECT 1 FROM errs e WHERE e.key = icons.key), \
           record = json_set(COALESCE(record, '{}'), '$.errors', json(COALESCE((SELECT e.errors FROM errs e WHERE e.key = icons.key), '[]'))) \
         WHERE key IN (SELECT value FROM json_each(?1)) AND (uploaded = 0 OR (family = 'container-combination-72' AND json_extract(record, '$.built_at') IS NOT NULL))"),
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
     WHERE key IN (SELECT value FROM json_each(?1)) AND (uploaded = 0 OR (family = 'container-combination-72' AND json_extract(record, '$.built_at') IS NOT NULL))",
];

#[cfg(test)]
mod tests {
    use super::*;
    use rusqlite::{params, Connection};

    fn db() -> Connection {
        let db = Connection::open_in_memory().unwrap();
        db.execute_batch("CREATE TABLE icons (key TEXT PRIMARY KEY, icon_id TEXT, family TEXT, svg_sha256 TEXT, uploaded INTEGER DEFAULT 0, \
                            build_failed INTEGER DEFAULT 0, record TEXT, card TEXT, style TEXT NOT NULL DEFAULT 'normal');
                          CREATE TABLE reviews (icon TEXT, svg_sha256 TEXT, status TEXT, PRIMARY KEY (icon, svg_sha256));
                          CREATE TABLE reference_parts (reference_id TEXT, role TEXT, icon TEXT, built_sha TEXT, form TEXT);
                          CREATE TABLE reference_part_sizes (reference_id TEXT, role TEXT, size INTEGER, icon TEXT, built_sha TEXT);
                          CREATE TABLE reference_part_fills (reference_id TEXT, role TEXT, rank INTEGER, icon TEXT, built_sha TEXT, combined TEXT, size INTEGER NOT NULL DEFAULT 64);").unwrap();
        for (key, sha) in [("solo/bag", "m1"), ("sub/check", "s2")] {
            db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, record) VALUES (?, ?, ?, ?, '{}')",
                       params![key, key, key.split('/').next().unwrap(), sha]).unwrap();
        }
        // Built from main m1 and sub s1; the sub has since been redrawn (s2).
        db.execute_batch("INSERT INTO reference_parts VALUES ('p1', 'main', 'solo/bag', 'm1', NULL), ('p1', 'sub', 'sub/check', 's1', NULL);
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

    #[test]
    fn a_fill_pick_is_rechecked_by_its_rank() {
        let db = db();
        // Pick 2 of fill pair f1 uses the main's region-1 fill (fm1) and the sub; only pick 1 uses its current fill.
        db.execute_batch("INSERT INTO icons(key, icon_id, family, svg_sha256, record) VALUES
              ('solo/bag--fill-region-1', 'bag--fill-region-1', 'solo', 'fm1', '{}'),
              ('side_combination64/f1--fill-2', 'f1--fill-2', 'side_combination64', 'c2', '{\"errors\":[]}');
            UPDATE icons SET style = 'fill' WHERE key IN ('side_combination64/f1--fill-2', 'solo/bag--fill-region-1');
            INSERT INTO reference_part_fills(reference_id, role, rank, icon, built_sha, combined) VALUES ('f1', 'main', 1, 'solo/bag', 'm1', 'side_combination64/f1--fill'),
              ('f1', 'sub', 1, 'sub/check', 's2', NULL), ('f1', 'main', 2, 'solo/bag--fill-region-1', 'fm1', 'side_combination64/f1--fill-2'),
              ('f1', 'sub', 2, 'sub/check', 's2', NULL);
            INSERT INTO reviews VALUES ('sub/check', 's2', 'approve');").unwrap();
        let using: Vec<String> = db.prepare(USING_PART).unwrap().query_map(params!["solo/bag--fill-region-1"], |r| r.get(0)).unwrap()
            .map(Result::unwrap).collect();
        assert_eq!(using, vec!["side_combination64/f1--fill-2"]);
        let key = r#"["side_combination64/f1--fill-2"]"#;
        for sql in UPDATE { db.execute(sql, params![key]).unwrap(); }
        let (failed, errors): (bool, String) = db.query_row("SELECT build_failed, json_extract(record, '$.errors') FROM icons WHERE key = 'side_combination64/f1--fill-2'",
            [], |r| Ok((r.get::<_, i64>(0)? != 0, r.get(1)?))).unwrap();
        assert!(failed);
        assert_eq!(errors, r#"["Main bag--fill-region-1 is not approved in Icon review"]"#);
        db.execute_batch("INSERT INTO reviews VALUES ('solo/bag--fill-region-1', 'fm1', 'approve');").unwrap();
        assert_eq!(db.prepare(CHANGED).unwrap().query_map(params![key], |r| r.get::<_, String>(0)).unwrap().count(), 1);
        for sql in UPDATE { db.execute(sql, params![key]).unwrap(); }
        assert_eq!(db.query_row("SELECT build_failed FROM icons WHERE key = 'side_combination64/f1--fill-2'", [], |r| r.get::<_, i64>(0)).unwrap(), 0);
    }
    #[test]
    fn a_72_fill_output_is_checked_against_its_72_pick_only() {
        let db = db();
        // f3 at 72: pick 1 uses main-54/cup's fill (c1) and the sub-36/dot outline. The same reference's 72 normal
        // pair uses other parts, and its 64 fill pick is another pick: neither is this output's.
        db.execute_batch("INSERT INTO icons(key, icon_id, family, svg_sha256, record) VALUES
              ('main-54/cup--fill', 'cup--fill', 'main-54', 'c1', '{}'), ('sub-36/dot', 'dot', 'sub-36', 'd1', '{}'),
              ('main-54/other', 'other', 'main-54', 'o1', '{}'),
              ('combination-72/f3--fill', 'f3--fill', 'combination-72', 'x1', '{\"errors\":[],\"reference_id\":\"f3\"}');
            UPDATE icons SET style = 'fill' WHERE key IN ('combination-72/f3--fill', 'main-54/cup--fill');
            INSERT INTO reference_part_sizes VALUES ('f3', 'main', 72, 'main-54/other', NULL);
            INSERT INTO reference_part_fills(reference_id, role, rank, icon, built_sha, combined, size) VALUES
              ('f3', 'main', 1, 'main-54/cup--fill', 'c1', 'combination-72/f3--fill', 72), ('f3', 'sub', 1, 'sub-36/dot', 'd1', NULL, 72),
              ('f3', 'main', 1, 'solo/bag', 'm1', 'side_combination64/f3--fill', 64), ('f3', 'sub', 1, 'sub/check', 's2', NULL, 64);
            INSERT INTO reviews VALUES ('sub-36/dot', 'd1', 'approve');").unwrap();
        let using: Vec<String> = db.prepare(USING_PART).unwrap().query_map(params!["main-54/cup--fill"], |r| r.get(0)).unwrap()
            .map(Result::unwrap).collect();
        assert_eq!(using, vec!["combination-72/f3--fill"]);
        let key = r#"["combination-72/f3--fill"]"#;
        for sql in UPDATE { db.execute(sql, params![key]).unwrap(); }
        let errors: String = db.query_row("SELECT json_extract(record, '$.errors') FROM icons WHERE key = 'combination-72/f3--fill'", [], |r| r.get(0)).unwrap();
        assert_eq!(errors, r#"["Main cup--fill is not approved in Icon review"]"#);
        db.execute_batch("INSERT INTO reviews VALUES ('main-54/cup--fill', 'c1', 'approve');").unwrap();
        for sql in UPDATE { db.execute(sql, params![key]).unwrap(); }
        assert_eq!(db.query_row("SELECT build_failed FROM icons WHERE key = 'combination-72/f3--fill'", [], |r| r.get::<_, i64>(0)).unwrap(), 0);
    }
    fn waiting(db: &Connection, reference_id: &str) -> Vec<(String, Option<String>)> {
        db.prepare(UNAPPROVED_64).unwrap().query_map(params![reference_id], |r| Ok((r.get(0)?, r.get(1)?))).unwrap()
            .map(Result::unwrap).collect()
    }

    fn native_db() -> (Connection, String) {
        use sha2::{Digest, Sha256};
        let db = db();
        let document = "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 32 32\"><path d=\"M8 8V24\"/></svg>";
        let sha = hex::encode(Sha256::digest(document.as_bytes()));
        let form = serde_json::json!({"native_text": true, "family": "text", "icon": "nine",
            "model_key": "text/nine", "sha256": sha, "document": document});
        db.execute("UPDATE reference_parts SET icon = NULL, built_sha = ?1, form = ?2 WHERE role = 'sub'",
                   params![sha, form.to_string()]).unwrap();
        db.execute("INSERT INTO icons(key, family, svg_sha256) VALUES ('text/nine', 'text', ?1)", params![sha]).unwrap();
        db.execute("INSERT INTO reviews VALUES ('text/nine', ?1, 'approve')", params![sha]).unwrap();
        db.execute_batch("INSERT INTO reviews VALUES ('solo/bag', 'm1', 'approve');").unwrap();
        (db, sha)
    }

    fn native_part(db: &Connection) -> crate::combination_build::NativeTextPart {
        db.query_row(NATIVE_TEXT_PARTS, params![r#"["p1"]"#], |r| Ok(crate::combination_build::NativeTextPart {
            reference_id: r.get(0)?, role: r.get(1)?, icon: r.get(2)?, svg_sha256: r.get(3)?,
            document: r.get(4)?, current_sha: r.get(5)?, review: r.get(6)?,
        })).unwrap()
    }

    #[test]
    fn approved_matching_native_text_can_build_and_be_approved() {
        for remove in ["$.unused", "$.model_key", "$.icon"] {
            let (db, sha) = native_db();
            db.execute("UPDATE reference_parts SET form = json_remove(form, ?1) WHERE role = 'sub'", [remove]).unwrap();
            assert!(waiting(&db, "p1").is_empty());
            assert_eq!(native_part(&db).validate(Some(&sha)), Ok(None));
            assert!(!update(&db).0);
            assert!(changed(&db).is_empty());
        }
        // Legacy pairs have no built hash for native text: use the form's exact drawing.
        let (db, sha) = native_db();
        db.execute_batch("UPDATE reference_parts SET built_sha = NULL WHERE role = 'sub'").unwrap();
        assert!(waiting(&db, "p1").is_empty());
        assert_eq!(native_part(&db).validate(Some(&sha)), Ok(None));
        assert!(!update(&db).0);
    }

    #[test]
    fn native_text_approval_and_disapproval_propagate_to_the_combination() {
        let (db, sha) = native_db();
        assert_eq!(db.query_row(USING_PART, ["text/nine"], |r| r.get::<_, String>(0)).unwrap(), "side_combination64/p1");
        assert_eq!(db.prepare(USING_PART).unwrap().query_map(["text/unrelated"], |r| r.get::<_, String>(0)).unwrap().count(), 0);
        update(&db);
        for status in ["pending", "approve", "rejected"] {
            db.execute("UPDATE reviews SET status = ?1 WHERE icon = 'text/nine'", [status]).unwrap();
            assert_eq!(changed(&db), vec!["side_combination64/p1"]);
            let approved = status == "approve";
            assert_eq!(waiting(&db, "p1").is_empty(), approved);
            assert_eq!(native_part(&db).validate(Some(&sha)).unwrap().is_none(), approved);
            let (failed, errors, card) = update(&db);
            assert_eq!(failed, !approved);
            assert_eq!(serde_json::from_str::<serde_json::Value>(&card).unwrap()["build_failed"], !approved);
            if !approved { assert_eq!(errors, r#"["Sub nine is not approved in Icon review"]"#); }
            assert!(changed(&db).is_empty());
        }
    }

    #[test]
    fn missing_or_conflicting_native_identities_fail_closed() {
        let cases = [
            "UPDATE reference_parts SET form = '{bad json' WHERE role = 'sub'",
            "UPDATE reference_parts SET form = '{\"native_text\":true}' WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.model_key', 'text/other') WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.model_key', 123) WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.icon', 123) WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.family', 'sub') WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.native_text', 0) WHERE role = 'sub'",
            "UPDATE reference_parts SET role = 'main' WHERE role = 'sub'",
            "DELETE FROM icons WHERE key = 'text/nine'",
            "UPDATE icons SET family = 'sub' WHERE key = 'text/nine'",
        ];
        for sql in cases {
            let (db, sha) = native_db();
            // Another approved icon must not make an ambiguous form acceptable.
            db.execute_batch("INSERT INTO icons(key, family, svg_sha256) SELECT 'text/other', 'text', svg_sha256 FROM icons WHERE key = 'text/nine';
                INSERT INTO reviews SELECT 'text/other', svg_sha256, 'approve' FROM icons WHERE key = 'text/nine';").unwrap();
            db.execute_batch(sql).unwrap();
            assert!(!waiting(&db, "p1").is_empty(), "{sql}");
            assert!(update(&db).0, "{sql}");
            assert!(native_part(&db).validate(Some(&sha)).is_err(), "{sql}");
        }
    }

    #[test]
    fn native_text_needs_approval_of_the_matching_drawing() {
        for sql in [
            "DELETE FROM reviews WHERE icon = 'text/nine'",
            "UPDATE reviews SET svg_sha256 = 'other' WHERE icon = 'text/nine'",
            "UPDATE reference_parts SET built_sha = 'old' WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_set(form, '$.sha256', 'old') WHERE role = 'sub'",
            "UPDATE reference_parts SET built_sha = NULL, form = json_remove(form, '$.sha256') WHERE role = 'sub'",
            "UPDATE icons SET svg_sha256 = 'new' WHERE key = 'text/nine'; INSERT INTO reviews VALUES ('text/nine', 'new', 'approve')",
        ] {
            let (db, _) = native_db();
            db.execute_batch(sql).unwrap();
            assert!(!waiting(&db, "p1").is_empty(), "{sql}");
            assert!(update(&db).0, "{sql}");
        }
    }

    #[test]
    fn native_build_rejects_missing_stale_or_forged_drawing_hashes() {
        let (db, sha) = native_db();
        assert!(native_part(&db).validate(None).is_err());
        assert!(native_part(&db).validate(Some("old")).is_err());
        for sql in [
            "UPDATE reference_parts SET form = json_set(form, '$.document', '<svg/>') WHERE role = 'sub'",
            "UPDATE reference_parts SET form = json_remove(form, '$.document') WHERE role = 'sub'",
            "UPDATE icons SET svg_sha256 = 'new' WHERE key = 'text/nine'",
        ] {
            let (db, _) = native_db();
            db.execute_batch(sql).unwrap();
            assert!(native_part(&db).validate(Some(&sha)).is_err(), "{sql}");
        }
    }

    #[test]
    fn ordinary_parts_still_require_current_approval_and_matching_builds() {
        let db = db();
        db.execute_batch("INSERT INTO reviews VALUES ('solo/bag', 'm1', 'approve'), ('sub/check', 's2', 'approve')").unwrap();
        assert_eq!(waiting(&db, "p1"), vec![("sub".into(), Some("sub/check".into()))]);
        db.execute_batch("UPDATE reference_parts SET built_sha = 's2' WHERE role = 'sub'").unwrap();
        assert!(waiting(&db, "p1").is_empty());
        db.execute_batch("UPDATE reviews SET status = 'pending' WHERE icon = 'solo/bag'").unwrap();
        assert_eq!(waiting(&db, "p1"), vec![("main".into(), Some("solo/bag".into()))]);
    }

    #[test]
    fn a_sub_with_no_icon_that_is_not_text_still_waits() {
        let db = db();
        db.execute_batch("INSERT INTO reference_parts VALUES ('u1', 'main', 'solo/bag', 'm1', NULL), ('u1', 'sub', NULL, NULL, NULL),
              ('u2', 'main', 'solo/bag', 'm1', NULL), ('u2', 'sub', NULL, NULL, '{\"native_text\":false}'),
              ('u3', 'main', 'solo/bag', 'm1', NULL), ('u3', 'sub', NULL, NULL, 'not json');
            INSERT INTO reviews VALUES ('solo/bag', 'm1', 'approve');").unwrap();
        assert_eq!(waiting(&db, "u1"), vec![("sub".to_string(), None)]);
        assert_eq!(waiting(&db, "u2"), vec![("sub".to_string(), None)]);
        assert_eq!(waiting(&db, "u3"), vec![("sub".to_string(), None)], "a malformed form waits, it does not fail the query");
        assert_eq!(waiting(&db, "p1"), vec![("sub".to_string(), Some("sub/check".to_string()))], "a drawn sub on its unapproved drawing waits");
    }
}
