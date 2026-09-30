-- The symbol's box on a saved container center (routes/container_centers.rs), resized in the
-- Container pairs popup; width and height are independent. NULL keeps the standard 32 on that axis.
ALTER TABLE container_centers ADD COLUMN width REAL;
ALTER TABLE container_centers ADD COLUMN height REAL;
