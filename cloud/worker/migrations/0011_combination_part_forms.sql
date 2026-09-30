-- What the side engine combines for a part while its drawing is the published one: the pair item of
-- experiment-combination.json (document, bounds, canvas, sizing mode, SUB32 ink, native text), so a side pair
-- is built in the browser (combine-side.js) without reading the published file. NULL for a part picked on the
-- cloud: the browser measures its drawing (side_recombine.pair_with_documents).
ALTER TABLE reference_parts ADD COLUMN form TEXT;
