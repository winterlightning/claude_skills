//! Review decisions: which status each catalog icon currently holds and who set it.
//! Ported from deploy.py `review_detail` and reviewer_stats.py `current_decisions` / `current_reviews`.

use crate::catalog::Catalog;
use serde::{Deserialize, Serialize};
use serde_json::{json, Map, Value};

/// One row of the `reviews` table.
#[derive(Clone, Debug, Default, Deserialize, Serialize, PartialEq)]
pub struct ReviewRow {
    pub icon: String,
    pub svg_sha256: String,
    pub status: String,
    #[serde(default)]
    pub updated_at: Option<String>,
    #[serde(default)]
    pub updated_by: Option<String>,
    #[serde(default)]
    pub worker: Option<String>,
    #[serde(default)]
    pub claimed_at: Option<String>,
    #[serde(default)]
    pub note: Option<String>,
}

/// An active row of `split_requests` (a rejected combination).
#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct ActiveSplit {
    pub icon: String,
    pub svg_sha256: String,
    #[serde(default)]
    pub created_by: Option<String>,
    #[serde(default)]
    pub created_at: Option<String>,
}

/// (status, actor, decided_at) — the tuple deploy.py passes around as `decision`.
#[derive(Clone, Debug, PartialEq)]
pub struct Decision {
    pub status: String,
    pub actor: Option<String>,
    pub stamp: Option<String>,
}

impl Decision {
    pub fn ready() -> Self {
        Decision { status: "ready".into(), actor: None, stamp: None }
    }

    /// `{'status', 'updated_by', 'updated_at'}` as review_detail returns it.
    pub fn detail(&self) -> Value {
        json!({"status": self.status, "updated_by": self.actor, "updated_at": self.stamp})
    }
}

fn normalized(status: &str) -> String {
    if status == "re-generated" { "ready".into() } else { status.into() }
}

/// The API and gallery say `disapprove` where the database keeps the legacy `pending`.
pub fn public_status(status: &str) -> String {
    match status {
        "pending" => "disapprove".into(),
        "re-generated" => "ready".into(),
        other => other.into(),
    }
}

/// Current decision per catalog icon. `rows` must be ordered by `updated_at` (later wins).
pub fn current_decisions(rows: &[ReviewRow], splits: &[ActiveSplit], catalog: &Catalog) -> Vec<(String, Decision)> {
    let mut decisions: indexmap_like::OrderedMap<Decision> = indexmap_like::OrderedMap::default();
    for icon in catalog.iter() {
        decisions.insert(icon.key.clone(), Decision::ready());
    }
    for row in rows {
        if let Some(icon) = catalog.get(&row.icon) {
            if icon.svg_sha256 == row.svg_sha256 {
                decisions.insert(row.icon.clone(), Decision {
                    status: normalized(&row.status), actor: row.updated_by.clone(), stamp: row.updated_at.clone(),
                });
            }
        }
    }
    for row in rows {
        if catalog.contains(&row.icon) && row.status == "rejected" {
            decisions.insert(row.icon.clone(), Decision {
                status: "rejected".into(), actor: row.updated_by.clone(), stamp: row.updated_at.clone(),
            });
        }
    }
    for split in splits {
        if let Some(icon) = catalog.get(&split.icon) {
            if icon.svg_sha256 == split.svg_sha256 {
                decisions.insert(split.icon.clone(), Decision {
                    status: "rejected".into(), actor: split.created_by.clone(), stamp: split.created_at.clone(),
                });
            }
        }
    }
    decisions.into_vec()
}

/// Statuses plus who approved, disapproved and rejected (the `/api/reviews` payload parts).
pub struct CurrentReviews {
    pub statuses: Map<String, Value>,
    pub approved_by: Map<String, Value>,
    pub disapproved_by: Map<String, Value>,
    pub rejected_by: Map<String, Value>,
}

pub fn current_reviews(decisions: &[(String, Decision)]) -> CurrentReviews {
    let by = |wanted: &[&str]| {
        let mut map = Map::new();
        for (key, decision) in decisions {
            if wanted.contains(&decision.status.as_str()) {
                if let Some(actor) = decision.actor.as_ref().filter(|actor| !actor.is_empty()) {
                    map.insert(key.clone(), Value::String(actor.clone()));
                }
            }
        }
        map
    };
    CurrentReviews {
        statuses: decisions.iter().map(|(key, d)| (key.clone(), Value::String(d.status.clone()))).collect(),
        approved_by: by(&["approve"]),
        disapproved_by: by(&["pending", "disapprove", "claimed"]),
        rejected_by: by(&["rejected"]),
    }
}

/// deploy.py `review_detail`: an active split wins, then any rejected revision, then this revision's row.
pub fn review_detail(split: Option<(Option<String>, Option<String>)>,
                     rejected: Option<(Option<String>, Option<String>)>,
                     row: Option<(String, Option<String>, Option<String>)>) -> Decision {
    if let Some((by, at)) = split {
        return Decision { status: "rejected".into(), actor: by, stamp: at };
    }
    if let Some((by, at)) = rejected {
        return Decision { status: "rejected".into(), actor: by, stamp: at };
    }
    match row {
        Some((status, by, at)) => Decision { status: normalized(&status), actor: by, stamp: at },
        None => Decision::ready(),
    }
}

/// A tiny insertion-ordered map, so decisions iterate in catalog order like Python dicts.
mod indexmap_like {
    use std::collections::HashMap;

    pub struct OrderedMap<V> {
        index: HashMap<String, usize>,
        items: Vec<(String, V)>,
    }

    impl<V> Default for OrderedMap<V> {
        fn default() -> Self {
            OrderedMap { index: HashMap::new(), items: Vec::new() }
        }
    }

    impl<V> OrderedMap<V> {
        pub fn insert(&mut self, key: String, value: V) {
            if let Some(&position) = self.index.get(&key) {
                self.items[position].1 = value;
            } else {
                self.index.insert(key.clone(), self.items.len());
                self.items.push((key, value));
            }
        }

        pub fn into_vec(self) -> Vec<(String, V)> {
            self.items
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::catalog::Icon;

    fn icon(key: &str, sha: &str) -> Icon {
        Icon { key: key.into(), svg_sha256: sha.into(), family: Some("solo".into()), ..Default::default() }
    }

    fn row(key: &str, sha: &str, status: &str, by: &str, at: &str) -> ReviewRow {
        ReviewRow { icon: key.into(), svg_sha256: sha.into(), status: status.into(),
                    updated_by: Some(by.into()), updated_at: Some(at.into()), ..Default::default() }
    }

    #[test]
    fn decisions_follow_deploy_precedence() {
        let catalog = Catalog::new(vec![icon("solo/a", "1"), icon("solo/b", "2"), icon("solo/c", "3")], false);
        let rows = vec![
            row("solo/a", "old", "approve", "ray", "2026-01-01"),   // other revision: ignored
            row("solo/b", "2", "pending", "hina", "2026-01-02"),
            row("solo/c", "old", "rejected", "an", "2026-01-03"),   // rejected on any revision wins
            row("solo/c", "3", "approve", "ray", "2026-01-04"),
        ];
        let decisions = current_decisions(&rows, &[], &catalog);
        let keys: Vec<_> = decisions.iter().map(|(k, _)| k.as_str()).collect();
        assert_eq!(keys, ["solo/a", "solo/b", "solo/c"]);
        assert_eq!(decisions[0].1, Decision::ready());
        assert_eq!(decisions[1].1.status, "pending");
        assert_eq!(decisions[2].1.status, "rejected");
        assert_eq!(decisions[2].1.actor.as_deref(), Some("an"));
        let reviews = current_reviews(&decisions);
        assert_eq!(reviews.disapproved_by["solo/b"], "hina");
        assert!(reviews.approved_by.is_empty());
    }

    #[test]
    fn split_rejects_only_its_revision() {
        let catalog = Catalog::new(vec![icon("solo/a", "1")], false);
        let splits = vec![ActiveSplit { icon: "solo/a".into(), svg_sha256: "0".into(), ..Default::default() }];
        assert_eq!(current_decisions(&[], &splits, &catalog)[0].1.status, "ready");
    }

    #[test]
    fn public_status_names() {
        assert_eq!(public_status("pending"), "disapprove");
        assert_eq!(public_status("re-generated"), "ready");
        assert_eq!(public_status("claimed"), "claimed");
    }
}
