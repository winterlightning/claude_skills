-- icon_search's key column is UNINDEXED (an FTS5 table indexes only its text), so the triggers' DELETE ... WHERE key = ?
-- read every row of the search index: about 35,000 rows for each icon deleted or each search text changed.
-- icon_search_keys maps a key to its search row, so the triggers delete that one row by rowid instead.
-- Filling it reads the search index once.
CREATE TABLE icon_search_keys (key TEXT PRIMARY KEY, search_rowid INTEGER NOT NULL);
INSERT OR REPLACE INTO icon_search_keys(key, search_rowid) SELECT key, rowid FROM icon_search;

DROP TRIGGER icon_search_insert;
DROP TRIGGER icon_search_delete;
DROP TRIGGER icon_search_update;
CREATE TRIGGER icon_search_insert AFTER INSERT ON icons BEGIN
  INSERT INTO icon_search(search, key) VALUES (NEW.search, NEW.key);
  INSERT OR REPLACE INTO icon_search_keys(key, search_rowid) VALUES (NEW.key, last_insert_rowid());
END;
CREATE TRIGGER icon_search_delete AFTER DELETE ON icons BEGIN
  DELETE FROM icon_search WHERE rowid = (SELECT search_rowid FROM icon_search_keys WHERE key = OLD.key);
  DELETE FROM icon_search_keys WHERE key = OLD.key;
END;
CREATE TRIGGER icon_search_update AFTER UPDATE OF search ON icons BEGIN
  DELETE FROM icon_search WHERE rowid = (SELECT search_rowid FROM icon_search_keys WHERE key = OLD.key);
  INSERT INTO icon_search(search, key) VALUES (NEW.search, NEW.key);
  INSERT OR REPLACE INTO icon_search_keys(key, search_rowid) VALUES (NEW.key, last_insert_rowid());
END;
