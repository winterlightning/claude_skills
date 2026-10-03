-- No more triggers. The stored review state (icons.decision … picked), the tab and filter counts (icon_counts,
-- icon_facet_counts) and the search index (icon_search) are refreshed on demand by POST /api/icons/refresh, the
-- gallery's "Refresh stats" button. The triggers of 0015 / 0017 recomputed every state column on every row written,
-- several times per request and blind to batches; a bulk job paid for each row. Now a write costs its own rows, and
-- the refresh recomputes only the icons the activity log names since the last press (`list_refresh` remembers it),
-- then rebuilds the counts from one pass over icons.
DROP TRIGGER IF EXISTS icon_state_review_insert;
DROP TRIGGER IF EXISTS icon_state_review_update;
DROP TRIGGER IF EXISTS icon_state_review_delete;
DROP TRIGGER IF EXISTS icon_state_split_insert;
DROP TRIGGER IF EXISTS icon_state_split_update;
DROP TRIGGER IF EXISTS icon_state_split_delete;
DROP TRIGGER IF EXISTS icon_state_feedback_insert;
DROP TRIGGER IF EXISTS icon_state_feedback_update;
DROP TRIGGER IF EXISTS icon_state_feedback_delete;
DROP TRIGGER IF EXISTS icon_state_pick_insert;
DROP TRIGGER IF EXISTS icon_state_pick_update;
DROP TRIGGER IF EXISTS icon_state_pick_delete;
DROP TRIGGER IF EXISTS icon_state_graph_insert;
DROP TRIGGER IF EXISTS icon_state_icon_insert;
DROP TRIGGER IF EXISTS icon_state_icon_update;
DROP TRIGGER IF EXISTS icon_counts_insert;
DROP TRIGGER IF EXISTS icon_counts_delete;
DROP TRIGGER IF EXISTS icon_counts_update;
DROP TRIGGER IF EXISTS icon_facets_insert;
DROP TRIGGER IF EXISTS icon_facets_delete;
DROP TRIGGER IF EXISTS icon_facets_update;
DROP TRIGGER IF EXISTS icon_search_insert;
DROP TRIGGER IF EXISTS icon_search_delete;
DROP TRIGGER IF EXISTS icon_search_update;

-- The refresh re-inserts search rows and remembers them by rowid: MAX(search_rowid) must not scan.
CREATE INDEX icon_search_keys_rowid ON icon_search_keys(search_rowid);

-- The one row of refresh bookkeeping: the last activity_log id a refresh has processed.
CREATE TABLE list_refresh (id INTEGER PRIMARY KEY CHECK(id = 1), last_activity_id INTEGER NOT NULL DEFAULT 0,
    refreshed_at TEXT, refreshed_by TEXT, refreshed_icons INTEGER NOT NULL DEFAULT 0);
INSERT INTO list_refresh(id, last_activity_id) VALUES (1, COALESCE((SELECT MAX(id) FROM activity_log), 0));
