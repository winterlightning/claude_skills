-- The fix-queue reads (GET /api/work, /queue, /disapproved, /review) start from the stored review state instead of
-- loading every icon, review and activity row.
--
-- Icons whose current drawing carries a worker (claimed, done, cannot-fix) are found through this partial index; it
-- holds only the few hundred rows with a worker.
CREATE INDEX reviews_worker ON reviews(worker) WHERE worker IS NOT NULL;

-- How many times each icon was disapproved, kept by every write (core icon_query DISAPPROVALS_KEY), so the queue's
-- max_disapprovals and the review page's 1 / 2 / 3+ counts need no activity log. Filled here for the icons the queue
-- shows (disapproved, claimed, or worked on); the rest get theirs when a write makes them disapproved.
ALTER TABLE icons ADD COLUMN disapprovals INTEGER NOT NULL DEFAULT 0;
UPDATE icons SET disapprovals = (WITH e AS (SELECT id, created_at, CASE WHEN json_valid(details) THEN json_extract(details, '$.status') END AS status, action FROM activity_log WHERE icon = icons.key AND action IN ('work_done', 'upload', 'review', 'feedback')),
  k AS (SELECT CASE WHEN action IN ('work_done', 'upload') OR (action = 'review' AND status IN ('ready', 're-generated', 'approve')) THEN 'fix' WHEN action IN ('review', 'feedback') AND status IN ('pending', 'disapprove') THEN 'bad' END AS kind, created_at, id FROM e),
  w AS (SELECT kind, LAG(kind) OVER (ORDER BY created_at, id) AS prev FROM k WHERE kind IS NOT NULL)
  SELECT MAX((SELECT COUNT(*) FROM w WHERE kind = 'bad' AND (prev IS NULL OR prev = 'fix')), (SELECT COUNT(*) FROM (SELECT svg_sha256 FROM reviews WHERE icon = icons.key AND status IN ('pending', 'claimed')
  UNION SELECT svg_sha256 FROM feedback WHERE icon = icons.key
  UNION SELECT json_extract(details, '$.svg_sha256') FROM activity_log WHERE icon = icons.key AND action IN ('review', 'feedback') AND json_valid(details) AND json_extract(details, '$.status') IN ('pending', 'disapprove') AND COALESCE(json_extract(details, '$.svg_sha256'), '') != ''
  UNION SELECT icons.svg_sha256 WHERE icons.decision IN ('pending', 'claimed'))),
  CASE WHEN icons.decision IN ('pending', 'claimed') AND (EXISTS (SELECT 1 FROM work_results WHERE icon = icons.key AND stage = 'after') OR EXISTS (SELECT 1 FROM activity_log WHERE icon = icons.key AND action = 'work_done')) THEN 2 ELSE 0 END))
  WHERE (state = 'pending' OR key IN (SELECT icon FROM reviews WHERE worker IS NOT NULL));
