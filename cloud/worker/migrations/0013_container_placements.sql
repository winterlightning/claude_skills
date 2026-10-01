-- Where a container places its symbol when a pair has no box of its own (routes/combinations.rs placements):
-- symbol = '' applies to every symbol in that container, a symbol icon id to that pair only (it wins). The
-- centre is in half units on the 64 grid; width / height are the symbol's painted size (NULL keeps the symbol's
-- natural size). The same rows as container_centers (0006, 0008, dropped by 0010), carried over by
-- backfill_combinations.py. Defaults still come from gallery/container-centers.json.
CREATE TABLE container_placements (
    container TEXT NOT NULL, symbol TEXT NOT NULL DEFAULT '',
    x REAL NOT NULL, y REAL NOT NULL, width REAL, height REAL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL,
    PRIMARY KEY(container, symbol));
