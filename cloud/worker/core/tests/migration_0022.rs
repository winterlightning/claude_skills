use rusqlite::{params, Connection};
use pictographic_core::{combination_identity, combination_query, combined_parts};

#[test]
fn native_container_parts_preserve_side_layouts_and_uploaded_identity() {
    let db = Connection::open_in_memory().unwrap();
    let directory = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(&directory).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    for f in files.iter().filter(|f| f.file_name().unwrap().to_str().unwrap() < "0022") {
        db.execute_batch(&std::fs::read_to_string(f).unwrap()).unwrap();
    }
    let rid = "d3c5d63d-804f-4be5-8057-8a88c92a68bc";
    db.execute("INSERT INTO \"references\"(reference_id, kind, concept, source) VALUES (?, 'combination', 'Ticket', 'test')", [rid]).unwrap();
    for role in ["container", "symbol"] {
        db.execute("INSERT INTO reference_parts(reference_id, role, part_reference_id, icon, layout) VALUES (?, ?, 'source', 'old64', '[{\"x\":1}]')", params![rid,role]).unwrap();
    }
    db.execute("INSERT INTO reference_part_sizes(reference_id, role, size, icon, layout) VALUES (?, 'main', 72, 'main-54/saved', '[{\"x\":10}]')", [rid]).unwrap();
    let main = "container-72/admission-ticket-stub-upload-176c499a6e4e0194";
    let sub = "symbol-36/beamed-eighth-musical-notes-upload-25ff7d4f3077bd86";
    let uploaded = "container-combination-72/ticket-upload-existing";
    for key in [main, sub, uploaded] {
        db.execute("INSERT INTO icons(key, icon_id, family, svg_sha256, preview_url, uploaded, record, pushed_at) VALUES (?1, 'original-slug', ?2, 'old', 'preview', 1, '{}', 'today')", params![key,key.split('/').next()]).unwrap();
    }
    db.execute("INSERT INTO icon_references(icon, reference_id) VALUES (?, ?)", params![uploaded,rid]).unwrap();
    db.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by) VALUES (?, 'old', 'approve', 'today', 'human')", [uploaded]).unwrap();
    db.execute_batch(&std::fs::read_to_string(directory.join("0022_container_pairs_72.sql")).unwrap()).unwrap();
    assert_eq!(db.query_row("SELECT icon FROM reference_part_sizes WHERE reference_id = ? AND role = 'container'", [rid], |r| r.get::<_, String>(0)).unwrap(), main);
    assert_eq!(db.query_row("SELECT layout FROM reference_part_sizes WHERE reference_id = ? AND role = 'main'", [rid], |r| r.get::<_, String>(0)).unwrap(), "[{\"x\":10}]");
    assert_eq!(db.query_row("SELECT icon FROM reference_parts WHERE reference_id = ? LIMIT 1", [rid], |r| r.get::<_, String>(0)).unwrap(), "old64");
    assert_eq!(db.query_row("SELECT count(*) FROM reviews", [], |r| r.get::<_, i64>(0)).unwrap(), 1);
    assert_eq!(db.query_row("SELECT status FROM reviews WHERE icon = ?", [uploaded], |r| r.get::<_, String>(0)).unwrap(), "approve");
    db.execute("INSERT INTO uploaded_icons(icon, record, svg) VALUES (?, '{}', '<original/>' )", [uploaded]).unwrap();
    assert_eq!(db.query_row(combination_identity::CURRENT_UPLOADED_SVG, params!["old",uploaded], |r| r.get::<_, String>(0)).unwrap(), "<original/>");
    db.execute("INSERT INTO revisions(svg_sha256, icon, svg, origin, created_at) VALUES ('new', ?, '<layout/>', 'combination-build', 'today')", [uploaded]).unwrap();
    assert_eq!(db.query_row(combination_identity::CURRENT_UPLOADED_SVG, params!["new",uploaded], |r| r.get::<_, String>(0)).unwrap(), "<layout/>");
    assert_eq!(db.query_row("SELECT svg FROM uploaded_icons WHERE icon = ?", [uploaded], |r| r.get::<_, String>(0)).unwrap(), "<original/>");
    let resolved = db.query_row(combination_identity::EXISTING_CONTAINER72, params![rid, format!("container-combination-72/{rid}")], |r| r.get::<_, String>(0)).unwrap();
    assert_eq!(resolved, uploaded);
    let list = format!("{} SELECT icon_key FROM combos WHERE reference_id = ?", combination_query::cte(72));
    assert_eq!(db.query_row(&list, [rid], |r| r.get::<_, String>(0)).unwrap(), uploaded);
    // Only an explicit browser build activates part-review checks on a historical upload.
    let keys = serde_json::json!([uploaded]).to_string();
    assert_eq!(db.prepare(combined_parts::CHANGED).unwrap().query_map([&keys], |_| Ok(())).unwrap().count(), 0);
    db.execute("UPDATE icons SET record = json_object('reference_id', ?, 'built_at', 'today') WHERE key = ?", params![rid,uploaded]).unwrap();
    assert_eq!(db.query_row(combined_parts::USING_PART, [main], |r| r.get::<_, String>(0)).unwrap(), uploaded);
    for sql in combined_parts::UPDATE { db.execute(sql, [&keys]).unwrap(); }
    assert_eq!(db.query_row("SELECT build_failed FROM icons WHERE key = ?", [uploaded], |r| r.get::<_, i64>(0)).unwrap(), 1);
}
