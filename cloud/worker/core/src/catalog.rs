//! The gallery catalog as the routes see it: built icons, then uploads, then (optionally) failed builds,
//! in that order, exactly like deploy.py's `catalog(include_failed=...)`.

use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::collections::HashMap;

#[derive(Clone, Debug, Default, Deserialize, Serialize, PartialEq)]
pub struct Icon {
    pub key: String,
    #[serde(default)]
    pub icon_id: Option<String>,
    #[serde(default)]
    pub name: Option<String>,
    #[serde(default)]
    pub family: Option<String>,
    #[serde(default)]
    pub category: Option<String>,
    #[serde(default)]
    pub svg_sha256: String,
    /// `{path, family, class_name}` of the authored module, or null.
    #[serde(default)]
    pub python_source: Value,
    #[serde(default)]
    pub preview_url: Option<String>,
    #[serde(default)]
    pub original_sources: Value,
    #[serde(default)]
    pub canvas_size: Option<i64>,
    #[serde(default)]
    pub build_failed: bool,
    #[serde(default)]
    pub uploaded: bool,
}

#[derive(Clone, Debug, Default)]
pub struct Catalog {
    order: Vec<String>,
    icons: HashMap<String, Icon>,
}

impl Catalog {
    /// Build from rows already ordered built → uploaded → failed; later duplicates are ignored.
    pub fn new(rows: Vec<Icon>, include_failed: bool) -> Self {
        let mut catalog = Catalog::default();
        for icon in rows {
            if icon.build_failed && !include_failed {
                continue;
            }
            if catalog.icons.contains_key(&icon.key) {
                continue;
            }
            catalog.order.push(icon.key.clone());
            catalog.icons.insert(icon.key.clone(), icon);
        }
        catalog
    }

    pub fn get(&self, key: &str) -> Option<&Icon> {
        self.icons.get(key)
    }

    pub fn contains(&self, key: &str) -> bool {
        self.icons.contains_key(key)
    }

    pub fn len(&self) -> usize {
        self.order.len()
    }

    pub fn is_empty(&self) -> bool {
        self.order.is_empty()
    }

    /// Icons in catalog order.
    pub fn iter(&self) -> impl Iterator<Item = &Icon> {
        self.order.iter().map(|key| &self.icons[key])
    }

    pub fn filtered(&self, keep: impl Fn(&Icon) -> bool) -> Catalog {
        let mut catalog = Catalog::default();
        for icon in self.iter().filter(|icon| keep(icon)) {
            catalog.order.push(icon.key.clone());
            catalog.icons.insert(icon.key.clone(), icon.clone());
        }
        catalog
    }
}
