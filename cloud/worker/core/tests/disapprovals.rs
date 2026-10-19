//! The stored disapproval count (icon_query DISAPPROVALS_KEY, kept on every write) against the rule it stores
//! (work::disapproval_counts), over made-up histories, on the D1 schema built from the migrations.

use chrono::{TimeZone, Utc};
use pictographic_core::catalog::{Catalog, Icon};
use pictographic_core::icon_query::{DISAPPROVALS_BACKFILL, DISAPPROVALS_KEY};
use pictographic_core::reviews::{Decision, ReviewRow};
use pictographic_core::work::{disapproval_counts, CountEvent, CountInputs, FeedbackMap, RowMap, WorkData};
use rusqlite::Connection;
use std::collections::HashMap;
use std::path::Path;

fn migrations() -> Vec<std::path::PathBuf> {
    let dir = Path::new(env!("CARGO_MANIFEST_DIR")).join("../migrations");
    let mut files: Vec<_> = std::fs::read_dir(&dir).unwrap().map(|e| e.unwrap().path()).collect();
    files.sort();
    files
}

fn database() -> Connection {
    let db = Connection::open_in_memory().unwrap();
    for file in migrations() {
        db.execute_batch(&std::fs::read_to_string(&file).unwrap()).unwrap_or_else(|e| panic!("{}: {e}", file.display()));
    }
    db
}

/// A tiny deterministic generator, so the histories are the same on every run.
struct Lcg(u64);

impl Lcg {
    fn below(&mut self, n: u64) -> u64 {
        self.0 = self.0.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        (self.0 >> 33) % n
    }
}

const STATUSES: [&str; 6] = ["pending", "claimed", "ready", "approve", "rejected", "re-generated"];
const ACTIONS: [&str; 5] = ["review", "feedback", "work_done", "upload", "login"];
const EVENT_STATUSES: [Option<&str>; 7] = [Some("pending"), Some("disapprove"), Some("ready"), Some("approve"), Some("re-generated"),
                                           Some("rejected"), None];

#[test]
fn stored_count_matches_the_rule() {
    let db = database();
    let mut rng = Lcg(42);
    let mut icons = Vec::new();
    let (mut rows, mut events, mut notes, mut fixes) = (Vec::new(), Vec::new(), Vec::new(), Vec::new());
    for n in 0..400 {
        let key = format!("solo/icon-{n}");
        let shas: Vec<String> = (0..1 + rng.below(3)).map(|i| format!("sha-{n}-{i}")).collect();
        let current = shas[rng.below(shas.len() as u64) as usize].clone();
        let decision = STATUSES[rng.below(STATUSES.len() as u64) as usize];
        db.execute("INSERT INTO icons(key, family, svg_sha256, pushed_at, decision) VALUES (?1, 'solo', ?2, 'p', ?3)",
                   rusqlite::params![key, current, decision]).unwrap();
        icons.push((key.clone(), current.clone(), decision));
        for sha in &shas {
            if rng.below(2) == 0 {
                let status = STATUSES[rng.below(STATUSES.len() as u64) as usize];
                db.execute("INSERT INTO reviews(icon, svg_sha256, status, updated_at) VALUES (?1, ?2, ?3, '2026-10-01')",
                           rusqlite::params![key, sha, status]).unwrap();
                rows.push(ReviewRow { icon: key.clone(), svg_sha256: sha.clone(), status: status.into(), ..Default::default() });
            }
            if rng.below(4) == 0 {
                db.execute("INSERT INTO feedback(icon, feedback, svg_sha256, created_at) VALUES (?1, 'note', ?2, '2026-10-01')",
                           rusqlite::params![key, sha]).unwrap();
                notes.push((key.clone(), sha.clone()));
            }
            if rng.below(6) == 0 {
                db.execute("INSERT INTO work_results(icon, svg_sha256, stage, worker, svg, saved_at) VALUES (?1, ?2, 'after', 'w', '<svg/>', 'x')",
                           rusqlite::params![key, sha]).unwrap();
                fixes.push((key.clone(), sha.clone()));
            }
        }
        // Events, some sharing a time (ties fall back to log order) and some out of log order.
        for _ in 0..rng.below(9) {
            let action = ACTIONS[rng.below(ACTIONS.len() as u64) as usize];
            let status = EVENT_STATUSES[rng.below(EVENT_STATUSES.len() as u64) as usize];
            let sha = if rng.below(5) == 0 { String::new() } else { shas[rng.below(shas.len() as u64) as usize].clone() };
            let at = format!("2026-10-0{}T0{}", 1 + rng.below(3), rng.below(4));
            let details = match status {
                Some(status) => format!(r#"{{"status": "{status}", "svg_sha256": "{sha}"}}"#),
                None => format!(r#"{{"svg_sha256": "{sha}"}}"#),
            };
            db.execute("INSERT INTO activity_log(username, action, icon, details, created_at) VALUES ('u', ?1, ?2, ?3, ?4)",
                       rusqlite::params![action, key, details, at]).unwrap();
            if action != "login" {
                events.push(CountEvent { icon: key.clone(), action: action.into(), status: status.map(Into::into),
                                         svg_sha256: Some(sha), at });
            }
        }
    }
    let catalog = Catalog::new(icons.iter().map(|(key, sha, _)| Icon { key: key.clone(), svg_sha256: sha.clone(), ..Default::default() })
                                    .collect(), true);
    let decisions: Vec<(String, Decision)> = icons.iter().map(|(key, _, status)| (key.clone(), Decision::stored(Some(status), None, None)))
                                                  .collect();
    let row_map: RowMap = rows.iter().map(|row| ((row.icon.clone(), row.svg_sha256.clone()), row.clone())).collect();
    let data = WorkData { catalog: &catalog, decisions: &decisions, rows: &row_map, feedback: &FeedbackMap::new(),
                          types: &HashMap::new(), disapprovals: &HashMap::new(), now: Utc.with_ymd_and_hms(2026, 10, 13, 0, 0, 0).unwrap() };
    let expected = disapproval_counts(&data, &CountInputs { events: &events, feedback: &notes, fixes: &fixes });
    let mut mismatched = Vec::new();
    for (key, _, _) in &icons {
        db.execute(DISAPPROVALS_KEY, [key]).unwrap();
        let stored: u32 = db.query_row("SELECT disapprovals FROM icons WHERE key = ?1", [key], |r| r.get(0)).unwrap();
        if stored != expected[key] {
            mismatched.push((key.clone(), stored, expected[key]));
        }
    }
    assert!(mismatched.is_empty(), "stored vs rule: {mismatched:?}");
    assert!(expected.values().any(|n| *n >= 3), "the histories reach the 3+ bucket");
}

#[test]
fn migration_backfills_with_the_same_rule() {
    let squash = |text: &str| text.split_whitespace().collect::<Vec<_>>().join(" ");
    let migration = migrations().into_iter().find(|f| f.to_string_lossy().contains("0020_")).unwrap();
    let text = squash(&std::fs::read_to_string(migration).unwrap());
    assert!(text.contains(&squash(DISAPPROVALS_BACKFILL)), "migration 0020's backfill differs from DISAPPROVALS_BACKFILL");
}
