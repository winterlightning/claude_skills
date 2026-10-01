//! Print the icon list statement for query-string pairs, with its arguments inlined (for timing in sqlite3).
use pictographic_core::icon_query::{list, Params};
fn main() {
    let pairs: Vec<(String, String)> = std::env::args().skip(1).filter_map(|a| a.split_once('=').map(|(k, v)| (k.into(), v.into()))).collect();
    let p = Params::from_query(|name| pairs.iter().find(|(k, _)| k == name).map(|(_, v)| v.clone()));
    let (sql, args) = list(&p);
    let mut out = String::new();
    let mut args = args.into_iter();
    for c in sql.chars() {
        if c == '?' {
            let v = args.next().unwrap();
            out += &match v { serde_json::Value::String(s) => format!("'{}'", s.replace('\'', "''")), other => other.to_string() };
        } else { out.push(c); }
    }
    println!("{out};");
}
