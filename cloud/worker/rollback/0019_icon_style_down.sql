-- Rollback of migration 0019 for a Worker built before it (the icon-artwork / style release of 2026-10-07).
--
-- 0019 gave icon_counts a `style` column inside its primary key. A Worker built before 0019 counts every write with
-- `ON CONFLICT(family, side_role, state, category, built_failed)`, which no longer names a unique key: SQLite refuses
-- the statement, and with it the whole batch of the review, upload or pick it belongs to. So before rolling the
-- Worker back past 0019, put icon_counts back to the old key (counts are derived data: rebuilt from icons here), and
-- deploy the old Worker right after (the new Worker's count writes fail in between; keep that window to seconds):
--
--   npx wrangler d1 execute pictographic-review-next --remote --file cloud/worker/rollback/0019_icon_style_down.sql
--   (then deploy the old Worker build)
--
-- The style / style_of columns stay (they have defaults; the old Worker never names them), and so do the round and
-- sharp records with their reviews: the old Worker lists them among the normal icons until the new one is back.
-- To go forward again: run 0019_icon_style_redo.sql, then deploy the new Worker (d1_migrations already lists 0019).
DROP TABLE icon_counts;
CREATE TABLE icon_counts (family TEXT NOT NULL, side_role TEXT NOT NULL, state TEXT NOT NULL, category TEXT NOT NULL,
  built_failed INTEGER NOT NULL, n INTEGER NOT NULL, PRIMARY KEY(family, side_role, state, category, built_failed));
INSERT INTO icon_counts SELECT COALESCE(family, ''), COALESCE(side_role, ''), COALESCE(state, ''), COALESCE(category, ''),
  build_failed, COUNT(*) FROM icons GROUP BY 1, 2, 3, 4, 5;
