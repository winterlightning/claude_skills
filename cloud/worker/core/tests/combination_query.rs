use pictographic_core::{combination_identity, combination_query};
use rusqlite::{params, Connection, StatementStatus};

fn database() -> Connection {
    let db = Connection::open_in_memory().unwrap();
    let dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(dir).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    for file in files {
        db.execute_batch(&std::fs::read_to_string(file).unwrap()).unwrap();
    }
    db
}

fn icon(db: &Connection, key: &str, sha: &str) {
    db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, preview_url, uploaded, record, pushed_at)
        VALUES (?1, ?1, ?2, ?3, 'preview', 1, '{}', 'today')", params![key, key.split('/').next(), sha]).unwrap();
}

fn pair(db: &Connection, id: &str, kind: &str) {
    db.execute("INSERT INTO \"references\"(reference_id, kind, concept, source) VALUES (?1, 'combination', ?1, 'test')", [id]).unwrap();
    let roles = if kind == "container" { ["container", "symbol"] } else { ["main", "sub"] };
    for role in roles {
        db.execute("INSERT INTO reference_parts(reference_id, role, part_reference_id) VALUES (?, ?, 'source')", params![id, role]).unwrap();
    }
}

fn link(db: &Connection, id: &str, key: &str) {
    db.execute("INSERT INTO icon_references(icon, reference_id) VALUES (?, ?)", params![key, id]).unwrap();
}

type Row = (String, String, String, i64, String);

fn combinations(db: &Connection, size: i64) -> Vec<Row> {
    db.prepare(&format!("{} SELECT reference_id, kind, state, missing, {} FROM combos c ORDER BY reference_id",
        combination_query::cte(size), combination_query::icon_key(size)))
        .unwrap().query_map([], |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?, r.get(4)?)))
        .unwrap().map(Result::unwrap).collect()
}

#[test]
fn identities_states_and_reviews_stay_size_specific() {
    let db = database();
    for (id, kind) in [("upload", "container"), ("duplicate", "container"), ("canonical", "container"),
        ("stale", "container"), ("side", "side"), ("unbuilt", "container"), ("partial", "side")] {
        pair(&db, id, kind);
    }
    for key in ["container-combination-72/original-upload", "container-combination-72/z-duplicate",
        "container-combination-72/a-duplicate", "container-combination-72/canonical",
        "container-combination-72/stale", "combination-72/side", "side_combination64/side"] {
        icon(&db, key, "current");
    }
    link(&db, "upload", "container-combination-72/original-upload");
    link(&db, "duplicate", "container-combination-72/z-duplicate");
    link(&db, "duplicate", "container-combination-72/a-duplicate");
    link(&db, "stale", "container-combination-72/stale");
    // A container-family link on a side reference must not change its identity or state.
    link(&db, "side", "container-combination-72/original-upload");
    // Nor should a link to another family make an unbuilt container look built.
    link(&db, "unbuilt", "combination-72/side");
    icon(&db, "container-72/part", "new");
    db.execute("INSERT INTO reference_part_sizes(reference_id, role, size, icon, built_sha)
        VALUES ('stale', 'container', 72, 'container-72/part', 'old')", []).unwrap();
    // A missing current icon does not count as a redraw, matching the previous rule.
    db.execute("INSERT INTO reference_part_sizes(reference_id, role, size, icon, built_sha)
        VALUES ('partial', 'main', 72, 'main-54/missing', 'old')", []).unwrap();
    db.execute("UPDATE reference_parts SET icon = 'side_combination64/side', built_sha = 'current' WHERE reference_id = 'side'", []).unwrap();
    db.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by)
        VALUES ('container-combination-72/original-upload', 'current', 'approve', 'today', 'human')", []).unwrap();
    let expected = [
        ("canonical", "container", "unbuilt", 1, "container-combination-72/canonical"),
        ("duplicate", "container", "built", 1, "container-combination-72/a-duplicate"),
        ("partial", "side", "built", 1, "combination-72/partial"),
        ("side", "side", "unbuilt", 1, "combination-72/side"),
        ("stale", "container", "stale", 1, "container-combination-72/stale"),
        ("unbuilt", "container", "unbuilt", 1, "container-combination-72/unbuilt"),
        ("upload", "container", "built", 1, "container-combination-72/original-upload"),
    ].map(|(id, kind, state, missing, key)| (id.into(), kind.into(), state.into(), missing, key.into()));
    assert_eq!(combinations(&db, 72), expected);
    for (id, kind, state, missing, key) in combinations(&db, 64) {
        assert_eq!(key, format!("{kind}_combination64/{id}"));
        assert_eq!(state, if id == "side" { "built" } else { "unbuilt" });
        assert_eq!(missing, if id == "side" { 0 } else { 1 });
    }
    let page = combination_query::page(72, "WHERE c.reference_id = ?");
    let got: (String, String, String) = db.query_row(&page, params!["upload", 2, 0], |r| Ok((r.get(4)?, r.get(5)?, r.get(6)?))).unwrap();
    assert_eq!(got, ("container-combination-72/original-upload".into(), "current".into(), "approve".into()));
    // Saving still sees every duplicate, including a canonical key without a link.
    let keys: Vec<String> = db.prepare(combination_identity::EXISTING_CONTAINER72).unwrap()
        .query_map(params!["duplicate", "container-combination-72/canonical"], |r| r.get(0)).unwrap().map(Result::unwrap).collect();
    assert_eq!(keys, ["container-combination-72/a-duplicate", "container-combination-72/canonical", "container-combination-72/z-duplicate"]);
}

// The deployed query before this fix: retain it here as a cost and behavior baseline.
fn legacy_cte() -> &'static str {
    "WITH parts AS (
        SELECT p.reference_id, p.role, s.icon, s.built_sha, i.svg_sha256 AS current_sha
        FROM reference_parts p LEFT JOIN reference_part_sizes s ON s.reference_id = p.reference_id AND s.role = p.role AND s.size = 72
        LEFT JOIN icons i ON i.key = s.icon),
    combos AS (
        SELECT r.reference_id, r.concept,
            CASE WHEN max(pt.role IN ('container', 'symbol')) THEN 'container' ELSE 'side' END AS kind,
            CASE WHEN count(pt.built_sha) = 0 THEN
                CASE WHEN max(pt.role IN ('container', 'symbol')) AND EXISTS (
                    SELECT 1 FROM icons i JOIN icon_references ir ON ir.icon = i.key
                    WHERE ir.reference_id = r.reference_id AND i.family = 'container-combination-72') THEN 'built' ELSE 'unbuilt' END
                WHEN max(pt.built_sha IS NOT NULL AND pt.current_sha IS NOT NULL AND pt.built_sha != pt.current_sha) THEN 'stale'
                ELSE 'built' END AS state,
            max(pt.icon IS NULL) AS missing
        FROM \"references\" r JOIN parts pt ON pt.reference_id = r.reference_id
        WHERE r.kind = 'combination' GROUP BY r.reference_id)"
}

fn legacy_page(filter: &str) -> String {
    format!("{} SELECT c.reference_id, c.concept, c.kind, c.state, i.key AS icon_key, i.svg_sha256 AS icon_sha,
        (SELECT status FROM reviews v WHERE v.icon = i.key AND v.svg_sha256 = i.svg_sha256) AS review
        FROM combos c LEFT JOIN icons i ON i.key = CASE WHEN c.kind = 'container' THEN COALESCE((
            SELECT x.key FROM icons x JOIN icon_references ir ON ir.icon = x.key
            WHERE ir.reference_id = c.reference_id AND x.family = 'container-combination-72' ORDER BY x.key LIMIT 1),
            'container-combination-72/' || c.reference_id) ELSE 'combination-72/' || c.reference_id END
        {filter} ORDER BY c.reference_id LIMIT ? OFFSET ?", legacy_cte())
}

fn run(db: &Connection, sql: &str, args: &[&dyn rusqlite::ToSql]) -> (Vec<Vec<rusqlite::types::Value>>, i32) {
    let mut stmt = db.prepare(sql).unwrap();
    let columns = stmt.column_count();
    let rows = stmt.query_map(args, |r| (0..columns).map(|i| r.get(i)).collect()).unwrap().map(Result::unwrap).collect();
    (rows, stmt.get_status(StatementStatus::VmStep))
}

#[test]
fn list_and_totals_do_linear_work_instead_of_repeated_family_scans() {
    let mut work = Vec::new();
    for n in [400, 1200] {
        let db = database();
        db.execute_batch("BEGIN").unwrap();
        for i in 0..n {
            let id = format!("pair-{i:05}");
            let key = format!("container-combination-72/upload-{i:05}");
            pair(&db, &id, if i % 4 == 0 { "side" } else { "container" });
            icon(&db, &key, "sha");
            if i % 3 != 0 { link(&db, &id, &key); }
        }
        db.execute_batch("COMMIT").unwrap();
        let mut size_work = Vec::new();
        let cte = combination_query::cte(72);
        let cases = [
            ("page", combination_query::page(72, ""), legacy_page(""), vec![101, 0]),
            ("filtered page", combination_query::page(72, "WHERE c.kind = 'container' AND c.state = 'built'"),
                legacy_page("WHERE c.kind = 'container' AND c.state = 'built'"), vec![51, 100]),
            ("totals", format!("{cte} SELECT kind, state, count(*) FROM combos GROUP BY 1, 2"),
                format!("{} SELECT kind, state, count(*) FROM combos GROUP BY 1, 2", legacy_cte()), vec![]),
            ("filtered total", format!("{cte} SELECT count(*) FROM combos c WHERE c.missing = 1 AND c.concept LIKE 'pair-00%'"),
                format!("{} SELECT count(*) FROM combos c WHERE c.missing = 1 AND c.concept LIKE 'pair-00%'", legacy_cte()), vec![]),
        ];
        for (label, fixed, old, args) in cases {
            let args: Vec<&dyn rusqlite::ToSql> = args.iter().map(|a| a as &dyn rusqlite::ToSql).collect();
            let (rows, steps) = run(&db, &fixed, &args);
            let (before, old_steps) = run(&db, &old, &args);
            assert_eq!(rows, before, "{label}: results at {n} combinations");
            println!("{n} combinations · {label}: {old_steps} → {steps} VM steps");
            assert!(steps * 5 < old_steps, "{label}: {steps} steps vs {old_steps} before");
            size_work.push(steps);
        }
        work.push(size_work);
    }
    for (small, large) in work[0].iter().zip(&work[1]) {
        assert!(*large < small * 4, "tripling the catalog must not cause quadratic work: {small} → {large}");
    }
}

#[test]
fn built_pairs_and_selective_refreshes_keep_their_fast_paths() {
    let db = database();
    db.execute_batch("BEGIN").unwrap();
    for key in ["container-72/part", "symbol-36/part", "main-54/part", "sub-36/part"] {
        icon(&db, key, "current");
        db.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by)
            VALUES (?, 'current', 'approve', 'today', 'human')", [key]).unwrap();
    }
    for i in 0..3000 {
        let id = format!("pair-{i:05}");
        let container = i % 4 != 0;
        pair(&db, &id, if container { "container" } else { "side" });
        let parts = if container { [("container", "container-72/part"), ("symbol", "symbol-36/part")] }
                    else { [("main", "main-54/part"), ("sub", "sub-36/part")] };
        for (role, key) in parts {
            db.execute("INSERT INTO reference_part_sizes(reference_id, role, size, icon, built_sha)
                VALUES (?, ?, 72, ?, 'current')", params![id, role, key]).unwrap();
        }
        let key = format!("{}/{id}", if container { "container-combination-72" } else { "combination-72" });
        icon(&db, &key, "combined");
        link(&db, &id, &key);
    }
    db.execute_batch("COMMIT").unwrap();
    let target = "pair-01501";
    let search = "WHERE (c.concept LIKE ? OR c.reference_id LIKE ?)";
    let by_icon = "WHERE c.reference_id IN (SELECT reference_id FROM icon_references WHERE icon = ?)";
    let cte = combination_query::cte(72);
    use rusqlite::types::Value;
    let cases: Vec<(_, _, _, Vec<Value>)> = vec![
        ("built page", combination_query::page(72, ""), legacy_page(""), vec![101.into(), 0.into()]),
        ("single-pair refresh", combination_query::page(72, search), legacy_page(search),
            vec![format!("%{target}%").into(), format!("{target}%").into(), 2.into(), 0.into()]),
        ("single-icon refresh", combination_query::page(72, by_icon), legacy_page(by_icon),
            vec![format!("container-combination-72/{target}").into(), 2.into(), 0.into()]),
        ("built totals", format!("{cte} SELECT kind, state, count(*) FROM combos GROUP BY 1, 2"),
            format!("{} SELECT kind, state, count(*) FROM combos GROUP BY 1, 2", legacy_cte()), vec![]),
        ("single-pair total", format!("{cte} SELECT count(*) FROM combos c {search}"),
            format!("{} SELECT count(*) FROM combos c {search}", legacy_cte()),
            vec![format!("%{target}%").into(), format!("{target}%").into()]),
        ("empty missing page", combination_query::page(72, "WHERE c.missing = 1"), legacy_page("WHERE c.missing = 1"),
            vec![101.into(), 0.into()]),
    ];
    // Statistics may change join choices; both planner states must retain the fast paths.
    for analyzed in [false, true] {
        if analyzed { db.execute_batch("ANALYZE").unwrap(); }
        for (label, fixed, old, values) in &cases {
            let args: Vec<&dyn rusqlite::ToSql> = values.iter().map(|v| v as &dyn rusqlite::ToSql).collect();
            let (rows, steps) = run(&db, fixed, &args);
            let (before, old_steps) = run(&db, old, &args);
            assert_eq!(rows, before, "{label}: results (analyzed={analyzed})");
            let plan: Vec<String> = db.prepare(&format!("EXPLAIN QUERY PLAN {fixed}")).unwrap()
                .query_map(args.as_slice(), |r| r.get(3)).unwrap().map(Result::unwrap).collect();
            assert!(plan.iter().any(|p| p.contains("SEARCH ir USING INDEX icon_references_reference (reference_id=?)")),
                "{label}: lookups must start from the existing reference index: {plan:#?}");
            assert!(plan.iter().filter(|p| p.starts_with("SEARCH x ")).all(|p| p.contains("(key=?)")),
                "{label}: linked icons must be probed by key, not searched by family: {plan:#?}");
            println!("3,000 built pairs · {label} (analyzed={analyzed}): {old_steps} → {steps} VM steps");
            assert!((steps as f64) <= old_steps as f64 * 1.05,
                "{label}: built/selective work regressed: {old_steps} → {steps} (analyzed={analyzed})");
        }
    }
}
