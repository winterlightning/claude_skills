-- Where a 64x64 container places its 32x32 symbol, adjusted on the Progression › Container pairs
-- page (routes/container_centers.rs). sub = '' applies to every symbol in that container; a sub
-- icon id applies to that pair only and wins. Defaults come from gallery/container-centers.json.
CREATE TABLE container_centers (
    main TEXT NOT NULL, sub TEXT NOT NULL DEFAULT '',
    x REAL NOT NULL, y REAL NOT NULL,
    updated_at TEXT NOT NULL, updated_by TEXT NOT NULL,
    PRIMARY KEY(main, sub));
