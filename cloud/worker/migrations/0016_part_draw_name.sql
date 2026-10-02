-- The name of the icon still to draw for a combination part: the side pair picker's "None of these: it needs
-- drawing" (side-pair-maker.js). Shown under the part until an icon is picked for it; picking one clears it.
ALTER TABLE reference_parts ADD COLUMN draw_name TEXT;
