//! `urllib.parse.parse_qs` semantics: repeated keys collect values, blank values are dropped.

use std::collections::BTreeMap;

pub type Query = BTreeMap<String, Vec<String>>;

fn decode(part: &str) -> String {
    let bytes = part.replace('+', " ").into_bytes();
    let mut out = Vec::with_capacity(bytes.len());
    let mut index = 0;
    while index < bytes.len() {
        if bytes[index] == b'%' && index + 2 < bytes.len() {
            let hex = std::str::from_utf8(&bytes[index + 1..index + 3]).ok();
            if let Some(value) = hex.and_then(|h| u8::from_str_radix(h, 16).ok()) {
                out.push(value);
                index += 3;
                continue;
            }
        }
        out.push(bytes[index]);
        index += 1;
    }
    String::from_utf8_lossy(&out).into_owned()
}

pub fn parse_qs(query: &str) -> Query {
    let mut result = Query::new();
    for pair in query.split('&') {
        let Some((key, value)) = pair.split_once('=') else { continue };
        let value = decode(value);
        if value.is_empty() {
            continue;
        }
        result.entry(decode(key)).or_default().push(value);
    }
    result
}

/// `query.get(name, [default])[0]`.
pub fn first<'a>(query: &'a Query, name: &str) -> Option<&'a str> {
    query.get(name).and_then(|values| values.first()).map(String::as_str)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn like_parse_qs() {
        let q = parse_qs("icon=solo%2Fheart-a&family=&state=working&state=done&q=a+b&bare");
        assert_eq!(first(&q, "icon"), Some("solo/heart-a"));
        assert_eq!(first(&q, "family"), None);
        assert_eq!(q["state"], vec!["working", "done"]);
        assert_eq!(first(&q, "q"), Some("a b"));
        assert!(!q.contains_key("bare"));
    }
}
