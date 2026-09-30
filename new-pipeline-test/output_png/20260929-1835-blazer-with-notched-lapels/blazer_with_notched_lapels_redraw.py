"""blazer-with-notched-lapels (redraw of the new-pipeline trace).

PLAN
- Keyshape SQUARE, centerline box (6,6)-(42,42), not the suggested VRECT_L: the
  trace is square (aspect 0.99, SQUARE fill 0.99 x 1.00 with no stretch), and the
  jacket needs the extra width for sleeve + body + lapels at 8-unit clearance.
- Mirrored about x = 24. One closed jacket contour: back neck (20..28, y 6),
  cubic shoulders rolling into vertical sleeves at x = 6, cuffs at y = 38 ending
  on the body side x = 14, a 4-unit step down to the hem at y = 42 (sleeves read
  as separate from the body), hem meeting the centre front at (24,42).
- Sleeve seams: x = 14 from the cuff up to y = 32, connected to the cuff corner.
- Notched lapels: one polyline per side from the neck corner, collar tip (17,16),
  notch (20,19), lapel peak (17,22), meeting the other lapel at the V (24,31);
  the centre front line runs from the V to the hem.
- Dropped: the inner V (shirt-opening) lines of the trace and the sleeve/body
  wedge; neither survives 8-unit clearance at 48.

METRIC ISSUES
- stroke-width (info): redrawn at stroke 4; every gap re-planned on centerlines.
- stroke-count 8 > 6: now 6 strokes (jacket, 2 lapels, front, 2 seams).
- keyshape-short-axis (VRECT_L y fill 81%): SQUARE, all four extremes exactly on
  the box (sleeves x 6 / 42, neck y 6, hem y 42).
- clearance e0/e3/e4/e7 (collar, inner V lines): inner V lines removed; lapels
  kept 8 apart at the notches (x 20 / 28).
- clearance e1/e2 vs e5 (sleeve inner edge vs body side, 1.8): sleeve inner edge
  and body side merged into one line (x 14), the seam starts at the cuff corner.
- clearance e3/e6, e6/e7, e1/e3, e2/e4 (lapel vs sleeve/armhole): seam top at
  y 32 is 8+ from the lapel edge; collar tip 8+ from the shoulder curve.
- narrow-join wedges at the armpits and inner V: gone with the removed lines.
- loose-join: every contact shares an exact endpoint and is declared connect.
- holes 1.2 / 2.4 / 5.1 wide: remaining openings are 8.4 (V) and 8.4 (panels).
Re-running svg_metrics.py on the redraw reports no issues.
Not fixable: the neck corner where shoulder, back neck and collar meet stays an
acute (~35 deg) garment corner; it is a shared endpoint, not a clearance fault.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "adeca2a9-4991-40c1-9620-baf03987dc2a"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1835-blazer-with-notched-lapels/"
    "blazer-with-notched-lapels_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
TOP, BOTTOM = 6, 42          # SQUARE centerline box (6,6)-(42,42)
NECK_HALF = 4                # neck corners at x = 19 / 29
SLEEVE_X = 6                 # outer sleeve edge (keyshape side)
SHOULDER_Y = 18              # shoulder curve turns vertical here
CUFF_Y = 38                  # sleeve ends above the hem
SIDE_X = 14                  # body side / sleeve seam
SEAM_TOP = 32                # sleeve seam stops clear of the lapel
# left lapel, mirrored: collar tip, notch, lapel peak, V bottom
COLLAR_TIP = (17, 16)
NOTCH = (20, 19)
PEAK = (17, 22)
V_Y = 31


def _m(p):
    return (2 * AX - p[0], p[1])


class BlazerWithNotchedLapelsRedraw(Solo48):
    icon_id = "blazer-with-notched-lapels-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothes"
    aliases = ("suit-jacket", "sport-coat", "jacket")
    keywords = ("blazer", "jacket", "suit", "lapel", "formal", "clothes")

    def build(self) -> None:
        neck_l, neck_r = (AX - NECK_HALF, TOP), (AX + NECK_HALF, TOP)
        sh_l, sh_r = (SLEEVE_X, SHOULDER_Y), _m((SLEEVE_X, SHOULDER_Y))
        cuff_ol, cuff_il = (SLEEVE_X, CUFF_Y), (SIDE_X, CUFF_Y)
        hem_l, hem_c = (SIDE_X, BOTTOM), (AX, BOTTOM)

        self.add_line("neck", neck_r, neck_l)
        self.add_bezier("shoulder-left", neck_l, ((12, 7), (SLEEVE_X, 9), sh_l))
        self.add_line("sleeve-left", sh_l, cuff_ol)
        self.add_line("cuff-left", cuff_ol, cuff_il)
        self.add_line("side-left", cuff_il, hem_l)
        self.add_line("hem-left", hem_l, hem_c)
        self.add_line("hem-right", hem_c, _m(hem_l))
        self.add_line("side-right", _m(hem_l), _m(cuff_il))
        self.add_line("cuff-right", _m(cuff_il), _m(cuff_ol))
        self.add_line("sleeve-right", _m(cuff_ol), sh_r)
        self.add_bezier("shoulder-right", sh_r, ((42, 9), (36, 7), neck_r))
        self.add_contour(
            "jacket", "neck", "shoulder-left", "sleeve-left", "cuff-left", "side-left",
            "hem-left", "hem-right", "side-right", "cuff-right", "sleeve-right",
            "shoulder-right", closed=True,
        )

        v = (AX, V_Y)
        self.add_polyline("lapel-left", neck_l, COLLAR_TIP, NOTCH, PEAK, v)
        self.add_polyline("lapel-right", neck_r, _m(COLLAR_TIP), _m(NOTCH), _m(PEAK), v)
        self.add_line("front", v, hem_c)
        self.relate("connect", "jacket", "lapel-left")
        self.relate("connect", "jacket", "lapel-right")
        self.relate("connect", "lapel-left", "lapel-right")
        self.relate("connect", "front", "lapel-left")
        self.relate("connect", "front", "lapel-right")
        self.relate("connect", "front", "jacket")

        for side, top, cuff in (("left", (SIDE_X, SEAM_TOP), cuff_il),
                                ("right", _m((SIDE_X, SEAM_TOP)), _m(cuff_il))):
            self.add_line(f"seam-{side}", cuff, top)
            self.relate("connect", "jacket", f"seam-{side}")
