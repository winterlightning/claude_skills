//! Rejected-combination split briefs — ported from brief_queue.py `validate_split`.

use serde_json::{json, Value};

pub struct Split {
    pub kind: String,
    pub parts: Vec<Value>,
    pub reason: String,
}

pub fn validate_split(data: &Value) -> Result<Split, String> {
    let kind = data.get("combination_type").and_then(Value::as_str).filter(|k| *k == "container" || *k == "side")
        .ok_or("Choose container combination or side combination.")?;
    let parts = data.get("components").and_then(Value::as_array).filter(|p| p.len() == 2)
        .ok_or("Describe exactly two component icons.")?;
    let mut cleaned = Vec::new();
    for part in parts {
        if !part.is_object() {
            return Err("Invalid component brief.".into());
        }
        for (key, limit) in [("name", 160usize), ("description", 10000)] {
            let ok = part.get(key).and_then(Value::as_str).is_some_and(|v| {
                let length = v.trim().chars().count();
                length > 0 && length <= limit
            });
            if !ok {
                return Err(format!("Each component needs a {key} (maximum {limit} characters)."));
            }
        }
        let family = part.get("family").and_then(Value::as_str).unwrap_or("");
        if !["solo", "sub", "container"].contains(&family) {
            return Err("Each component needs a valid family.".into());
        }
        cleaned.push(json!({"name": part["name"].as_str().unwrap().trim(), "family": family,
                            "description": part["description"].as_str().unwrap().trim()}));
    }
    if cleaned[0]["name"].as_str().unwrap().to_lowercase() == cleaned[1]["name"].as_str().unwrap().to_lowercase() {
        return Err("Give the two components distinct names.".into());
    }
    let first_ok = if kind == "container" { cleaned[0]["family"] == "container" } else { cleaned[0]["family"] == "solo" || cleaned[0]["family"] == "container" };
    if !first_ok || cleaned[1]["family"] != "sub" {
        return Err("Use container + sub for a container combination; solo/container + sub for a side combination.".into());
    }
    let reason = match data.get("reason") {
        None | Some(Value::Null) => String::new(),
        Some(Value::String(text)) if text.chars().count() <= 10000 => text.trim().to_string(),
        _ => return Err("Invalid rejection reason.".into()),
    };
    Ok(Split { kind: kind.into(), parts: cleaned, reason })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn split_rules() {
        let ok = json!({"combination_type": "side", "reason": " dup ", "components": [
            {"name": "Monitor", "family": "solo", "description": "d"},
            {"name": "Cloud", "family": "sub", "description": "d"}]});
        let split = validate_split(&ok).unwrap();
        assert_eq!((split.kind.as_str(), split.reason.as_str()), ("side", "dup"));
        let mut same = ok.clone();
        same["components"][1]["name"] = json!("monitor");
        assert_eq!(validate_split(&same).err().unwrap(), "Give the two components distinct names.");
        let mut container = ok.clone();
        container["combination_type"] = json!("container");
        assert!(validate_split(&container).is_err());
    }
}
