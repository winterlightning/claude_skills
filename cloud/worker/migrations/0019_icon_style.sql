-- Style beside family: every icon so far is "normal"; corner_processing adds a "round" and a "sharp" record of an
-- icon (key `<icon>--round` / `--sharp`, style_of = the normal icon's key), each reviewed on its own. The list shows
-- one style at a time (GET /api/icons style=, normal by default), so the tab and category counts carry it too.
ALTER TABLE icons ADD COLUMN style TEXT NOT NULL DEFAULT 'normal';
ALTER TABLE icons ADD COLUMN style_of TEXT;
CREATE INDEX icons_style_family ON icons(style, family);

DROP TABLE icon_counts;
-- style has a default so a Worker built before this migration still counts its writes (as normal) until redeployed.
CREATE TABLE icon_counts (family TEXT NOT NULL, side_role TEXT NOT NULL, style TEXT NOT NULL DEFAULT 'normal', state TEXT NOT NULL,
  category TEXT NOT NULL, built_failed INTEGER NOT NULL, n INTEGER NOT NULL,
  PRIMARY KEY(family, side_role, style, state, category, built_failed));
INSERT INTO icon_counts SELECT COALESCE(family, ''), COALESCE(side_role, ''), style, COALESCE(state, ''), COALESCE(category, ''),
  build_failed, COUNT(*) FROM icons GROUP BY 1, 2, 3, 4, 5, 6;
