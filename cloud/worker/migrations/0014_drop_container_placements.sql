-- Container placements live in each pair's symbol layout (reference_parts.layout, set by container-pairs.html through
-- POST /api/combinations/parts), so the Worker has no placement routes. 0013 created this table in production only.
DROP TABLE IF EXISTS container_placements;
