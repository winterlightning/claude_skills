-- Serve the gallery's image URLs from the database instead of copied files.
--
-- Solo, sub, container, symbol and text are only a profile/family on an icon row; the old
-- folder URLs (/solo48/<icon_id>.svg, /failed/sub32/<icon_id>.svg) are looked up by
-- (profile, icon_id, build_failed) and answered with the icon's current drawing.

CREATE INDEX icons_profile_id ON icons(profile, icon_id, build_failed);

-- Drawings the review pages still show that are not catalog icons (left over from failed builds).
CREATE TABLE extra_drawings (
    profile TEXT NOT NULL, icon_id TEXT NOT NULL, failed INTEGER NOT NULL,
    svg_sha256 TEXT NOT NULL,
    PRIMARY KEY(profile, icon_id, failed));

-- Reference files by content hash: the review pages name reference copies by sha256.
ALTER TABLE "references" ADD COLUMN sha256 TEXT;
CREATE INDEX references_sha ON "references"(sha256);
