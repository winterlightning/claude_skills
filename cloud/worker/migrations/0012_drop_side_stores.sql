-- Side pairs live in the combination tables (reference_parts: icon, layout, built_sha, form; 0009, 0011) and are
-- built in the browser (combine-side.js). The stores the old side routes kept are copied there by
-- backfill_combinations.py, which reads a snapshot taken before this runs.
DELETE FROM store_documents WHERE store IN ('side-layouts', 'side-renders', 'side-pairs');
