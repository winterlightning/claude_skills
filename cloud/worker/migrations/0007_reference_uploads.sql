-- Manual uploads made for a combination component that has no generated drawing yet (Progression ›
-- Container pairs): the reference (pair main_id / sub_id) → the uploaded icon that stands in for it.
-- Written by POST /api/icons/upload with `reference`; listed by GET /api/reference-uploads.
CREATE TABLE reference_uploads (
    reference TEXT PRIMARY KEY, role TEXT NOT NULL CHECK(role IN ('container', 'symbol')),
    icon_key TEXT NOT NULL, updated_at TEXT NOT NULL, updated_by TEXT NOT NULL);
