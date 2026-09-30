-- A change counter for GET /api/primitives/state (routes/primitives.rs): the primitives page polls every
-- 5 s and gets an empty 304 while this counter and the catalog's R2 etag are unchanged, instead of a scan
-- of both tables. Triggers bump it on every write from any writer (Worker routes, `d1 execute` syncs).
CREATE TABLE primitive_state_version (id INTEGER PRIMARY KEY CHECK(id = 1), version INTEGER NOT NULL);
INSERT INTO primitive_state_version VALUES (1, 0);

CREATE TRIGGER primitive_status_version_insert AFTER INSERT ON primitive_status
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;
CREATE TRIGGER primitive_status_version_update AFTER UPDATE ON primitive_status
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;
CREATE TRIGGER primitive_status_version_delete AFTER DELETE ON primitive_status
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;

CREATE TRIGGER primitive_briefs_version_insert AFTER INSERT ON primitive_briefs
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;
CREATE TRIGGER primitive_briefs_version_update AFTER UPDATE ON primitive_briefs
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;
CREATE TRIGGER primitive_briefs_version_delete AFTER DELETE ON primitive_briefs
BEGIN UPDATE primitive_state_version SET version = version + 1 WHERE id = 1; END;
