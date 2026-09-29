-- The editable geometry of every generated drawing (the catalog record's graph fields, as
-- icon_artwork.baseline() gives them), keyed by that drawing's sha. The graphics container edits,
-- validates and renders from it; the Worker never interprets it. Never updated after insert.
CREATE TABLE icon_graphs (
    svg_sha256 TEXT PRIMARY KEY,
    icon TEXT NOT NULL,
    graph TEXT NOT NULL);
CREATE INDEX icon_graphs_icon ON icon_graphs(icon);
