# Monitor with Application Squares

Result: cannot-fix; full validation: fail.

VRECT_L maximizes the available height for two vertically stacked tiles and the stand.

Construction reference: Lucide monitor: framed screen, centered stand and repeated squares.

Reduction and omissions: No tile omitted or rearranged. The final failed candidate uses readable 6-unit squares; the larger 8-unit counter attempt is saved and fails against the screen floor.

Visual review at native 48px and enlarged size, light and dark: Both square tiles are readable, but their inner openings and top/bottom margins fail. Not approved.

MIC: square-0 and square-1 internal edges and screen margins. Two 8-unit square centerline heights, an 8-unit gap and 8-unit top/bottom margins require 40 units for the screen alone; an 8-unit stand needs more than any SOLO48 rectangle height.

Exact automated findings are in release-validation.json; overlays are in qa/. Model-only findings are in validation.txt.
