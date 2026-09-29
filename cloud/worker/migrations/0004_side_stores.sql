-- Side pairs combined on the cloud (routes/side.rs): `side-layouts` (recombined or hand-adjusted pairs,
-- key <pair id>) and `side-renders` (automatic renders of pairs without a published preview,
-- key <pair id>|<main>|<sub>). SQLite cannot change a CHECK in place, so the table is rebuilt.
CREATE TABLE store_documents_new (
    store TEXT NOT NULL CHECK(store IN ('icon-artwork', 'stroke-edits', 'side-layouts', 'side-renders')),
    key TEXT NOT NULL, document TEXT NOT NULL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL,
    PRIMARY KEY(store, key));
INSERT INTO store_documents_new(store, key, document, updated_at, updated_by)
    SELECT store, key, document, updated_at, updated_by FROM store_documents;
DROP TABLE store_documents;
ALTER TABLE store_documents_new RENAME TO store_documents;
