//! Run the real Worker's list SQL on a migrated local D1 copy.
use pictographic_core::icon_query::{self, Params};
use rusqlite::{params_from_iter, Connection, OpenFlags};
use serde_json::Value;

fn value(v: &Value) -> rusqlite::types::Value {
    match v {
        Value::String(s) => s.clone().into(),
        Value::Number(n) => n.as_i64().unwrap().into(),
        Value::Null => rusqlite::types::Value::Null,
        _ => panic!("unexpected list parameter"),
    }
}

#[test]
#[ignore = "requires REJECTED_REHEARSAL_DB: the explicit local 379-record rehearsal database"]
fn migrated_routes_are_visible_through_worker_list_queries() {
    let path = std::env::var("REJECTED_REHEARSAL_DB").expect("set REJECTED_REHEARSAL_DB to the local applied copy");
    let db = Connection::open_with_flags(path, OpenFlags::SQLITE_OPEN_READ_ONLY).unwrap();
    for (family, where_sql) in [("font-48", "family='font-48'"), ("side_sub", "side_role='sub'")] {
        let p = Params::from_query(|key| match key {
            "family" => Some(family.into()), "status" => Some("rejected".into()),
            "limit" => Some("192".into()), _ => None,
        });
        let (sql, args) = icon_query::list(&p);
        let mut stmt = db.prepare(&sql).unwrap();
        let rows = stmt.query_map(params_from_iter(args.iter().map(value)), |row| {
            Ok((row.get::<_, String>(0)?, row.get::<_, String>(2)?))
        }).unwrap();
        let mut total = None;
        let mut seen = 0;
        for row in rows {
            let (part, raw) = row.unwrap();
            let data: Value = serde_json::from_str(&raw).unwrap();
            if part == "total" { total = data["total"].as_i64(); }
            if part == "item" {
                seen += 1;
                let card: Value = serde_json::from_str(data["card"].as_str().unwrap()).unwrap();
                if family == "font-48" {
                    assert_eq!(data["family"], "font-48");
                    assert_eq!(card["family"], "font-48");
                    assert_eq!(data["canvas_size"], 48);
                } else {
                    assert_eq!(card["side_role"], "sub");
                }
                assert_eq!(data["state"], "rejected");
            }
        }
        let expected: i64 = db.query_row(&format!("SELECT count(*) FROM icons WHERE {where_sql} AND state='rejected' AND style='normal'"), [], |r| r.get(0)).unwrap();
        assert_eq!(total, Some(expected));
        assert!(seen > 0);
        if family == "font-48" { assert_eq!(expected, 78); }
    }
}
