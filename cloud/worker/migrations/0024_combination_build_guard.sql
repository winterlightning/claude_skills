-- Abort an entire D1 build batch if a container or its selected artwork changed.
-- Successful guards insert no rows; a conflict violates NOT NULL and rolls back.
CREATE TABLE combination_build_guard (ok INTEGER NOT NULL);
