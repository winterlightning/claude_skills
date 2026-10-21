-- The keyshape of each icon's displayed drawing, measured where the drawing is drawn (the gallery's icon-guides.js, or a
-- batch with the same rule): a Browser Edit, a picked upload or a drawing that fits no contract keyshape exactly differs
-- from the generated record's keyshape. POST /api/icons/keyshape writes it and copies it onto the list row (card
-- keyshape / keyshape_bounds and the keyshape column), and every rebuild of a list row applies it again. A row is
-- dropped when the displayed drawing changes (a new pick, or a catalog push of another drawing), until it is measured
-- again.
CREATE TABLE IF NOT EXISTS icon_keyshapes (
  key TEXT PRIMARY KEY,
  svg_sha256 TEXT NOT NULL,
  keyshape TEXT NOT NULL,
  keyshape_bounds TEXT NOT NULL,
  measured_at TEXT NOT NULL,
  measured_by TEXT
);
