-- Side pairs made on the cloud from a primitive classified as a combination (routes/side_pairs.rs):
-- `side-pairs`, key <primitive uuid>, the pair row (main = a solo icon, sub = a sub icon, position).
-- SQLite cannot change a CHECK in place, so the table is rebuilt.
CREATE TABLE store_documents_new (
    store TEXT NOT NULL CHECK(store IN ('icon-artwork', 'stroke-edits', 'side-layouts', 'side-renders', 'side-pairs')),
    key TEXT NOT NULL, document TEXT NOT NULL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL,
    PRIMARY KEY(store, key));
INSERT INTO store_documents_new(store, key, document, updated_at, updated_by)
    SELECT store, key, document, updated_at, updated_by FROM store_documents;
DROP TABLE store_documents;
ALTER TABLE store_documents_new RENAME TO store_documents;
