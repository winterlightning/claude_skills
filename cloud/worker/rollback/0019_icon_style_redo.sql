-- After 0019_icon_style_down.sql: icon_counts with style in its key again, as migration 0019 makes it (its
-- ALTER TABLE statements are not repeated: the columns stayed). Run right before deploying the new Worker again.
--
--   npx wrangler d1 execute pictographic-review-next --remote --file cloud/worker/rollback/0019_icon_style_redo.sql
DROP TABLE icon_counts;
CREATE TABLE icon_counts (family TEXT NOT NULL, side_role TEXT NOT NULL, style TEXT NOT NULL DEFAULT 'normal', state TEXT NOT NULL,
  category TEXT NOT NULL, built_failed INTEGER NOT NULL, n INTEGER NOT NULL,
  PRIMARY KEY(family, side_role, style, state, category, built_failed));
INSERT INTO icon_counts SELECT COALESCE(family, ''), COALESCE(side_role, ''), style, COALESCE(state, ''), COALESCE(category, ''),
  build_failed, COUNT(*) FROM icons GROUP BY 1, 2, 3, 4, 5, 6;
