"""file-shield (redraw of the new-pipeline traced SVG).

Plan: a tall document with a cut top-right corner on VRECT_L (centerline box
(8,4)-(40,44)), holding a Lucide `shield` centred on the document axis x=24.
- page: one closed contour, r4 rounded corners on the three square corners and a
  45-degree cut corner from (30,4) to (40,14). Extremes sit on the box exactly:
  left x=8, right x=40, top y=4, bottom y=44.
- shield: one closed contour mirrored about x=24. Straight sides on x=17 / x=31
  (9 inside the page walls), flat Lucide shoulders rising to a peak at (24,17)
  and two cubic flanks meeting at the tip (24,35), 9 above the page bottom. The
  right shoulder stays 11.3 from the cut corner. The gaps are 9, not 8, because
  the engine returns an exact-8 page/shield gap as `review`.
- keyshape: VRECT_M (the metrics' suggestion, score 1.21 vs 1.17) was drawn
  first and validated, but its 28-wide page leaves a 10-wide shield with a
  6-unit interior that pinches at 48 px. VRECT_L fits the trace's width better
  (fill x 0.92 vs y 0.96 short on VRECT_M) and gives a 14-wide shield with a
  10-unit interior, so it was kept.
Reference: Lucide `file` (page outline + cut corner) and `shield` (shoulder
curves, straight sides, curved flanks to a pointed tip).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap was budgeted at stroke 4.
- keyshape-short-axis (VRECT_M fills 96% of y): on VRECT_L the page reaches
  every extreme exactly (x 8/40, y 4/44), with no stretching.
- clearance e0-e2 (shield tip 3.19 above the page bottom): the shield now ends
  9 above the bottom and 9 inside both walls.
- hole at the fold (2.0 wide): the folded-corner triangle cannot hold a 6-unit
  inscribed hole (a right triangle needs legs of 17, over half of the 32-wide
  page), so the fold crease is dropped and the corner is drawn as a clean cut;
  no enclosed sliver remains.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4b6ec7ff-fa5a-4489-9bab-e1e940ac236f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1224-file-shield/file-shield_raw.svg"
AUTHOR = "claude-opus-5-5"

L, T, R, B = 8, 4, 40, 44    # VRECT_L centerline box
CORNER = 4                   # page corner radius
CUT = 10                     # cut-corner leg
AX = 24                      # shared axis
HALF = 7                     # shield half width (9 inside each wall)
PEAK, SHOULDER, SIDE_END, TIP = 17, 20, 26, 35


class FileShieldRedraw(Solo48):
    icon_id = "file-shield-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "security"
    aliases = ("secure file", "protected document")
    keywords = ("file", "document", "shield", "security", "protection", "safe")

    def build(self) -> None:
        self.page()
        self.shield()

    def page(self) -> None:
        k = CORNER
        self.add_line("page-top", (L + k, T), (R - CUT, T))
        self.add_line("page-cut", (R - CUT, T), (R, T + CUT))
        self.add_line("page-right", (R, T + CUT), (R, B - k))
        self.add_arc("page-br", (R, B - k), (R - k, B), radius_x=k, sweep=True)
        self.add_line("page-bottom", (R - k, B), (L + k, B))
        self.add_arc("page-bl", (L + k, B), (L, B - k), radius_x=k, sweep=True)
        self.add_line("page-left", (L, B - k), (L, T + k))
        self.add_arc("page-tl", (L, T + k), (L + k, T), radius_x=k, sweep=True)
        self.add_contour("page", "page-top", "page-cut", "page-right", "page-br",
                         "page-bottom", "page-bl", "page-left", "page-tl", closed=True)

    def shield(self) -> None:
        # Right half runs peak -> shoulder -> side -> tip; the left half is its
        # mirror, authored in travel order tip -> side -> shoulder -> peak.
        xr, xl = AX + HALF, AX - HALF
        self.add_bezier("shield-top-r", (AX, PEAK), ((AX + 2, PEAK + 1), (xr - 3, SHOULDER), (xr, SHOULDER)))
        self.add_line("shield-side-r", (xr, SHOULDER), (xr, SIDE_END))
        self.add_bezier("shield-flank-r", (xr, SIDE_END), ((xr, SIDE_END + 5), (AX + 4, TIP - 2), (AX, TIP)))
        self.add_bezier("shield-flank-l", (AX, TIP), ((AX - 4, TIP - 2), (xl, SIDE_END + 5), (xl, SIDE_END)))
        self.add_line("shield-side-l", (xl, SIDE_END), (xl, SHOULDER))
        self.add_bezier("shield-top-l", (xl, SHOULDER), ((xl + 3, SHOULDER), (AX - 2, PEAK + 1), (AX, PEAK)))
        self.add_contour("shield", "shield-top-r", "shield-side-r", "shield-flank-r",
                         "shield-flank-l", "shield-side-l", "shield-top-l", closed=True)
