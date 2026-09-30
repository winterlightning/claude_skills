"""curved string of beads (redraw of the new-pipeline traced SVG).

Plan: three equal hollow beads hung on a U-shaped string, HRECT_M (centerline
box (4,10)-(44,38)), mirrored about x=24.
- beads: circles of radius BEAD_R, each a closed contour of two half arcs split
  at the point where a string attaches. The end beads sit in the top corners
  (left apex on x=4, top apex on y=10; mirrored on x=44); the middle bead's
  bottom apex is the y=38 extreme.
- string: one elliptical quarter arc per side, leaving an end bead's bottom apex
  straight down and arriving level at the middle bead's side apex, so the two
  runs read as one sagging U. Each run shares its endpoints with both beads.
Metric issues fixed:
- hole x3 (3.8 inscribed, need 6): beads redrawn at r=6, hole 8 inscribed.
- keyshape-short-axis (y filled 50% of HRECT_M): the string drops further so
  the beads span y 10..38 exactly; the x extremes stay on 4 and 44.
- loose-join x2 (string 0.36 short of the middle bead): every string end is a
  shared bead-arc endpoint, declared with relate("connect").
- stroke-width (2.68 in the trace): drawn at the profile stroke 4; bead gap
  kept at 9.3 centerline (>= 9 because both parts are curved).
No useful Lucide match (no bead/necklace icon); construction follows Lucide's
circle-and-arc style.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ed4699f6-a912-4876-9b67-eba4703923e0"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1114-curved-string-of-beads/curved-string-of-beads_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BEAD_R = 6
END_C = (10, 16)               # left end bead: x 4..16, y 10..22
MID_C = (AXIS, 32)             # middle bead: x 18..30, y 26..38
# String sag: ellipse centred at (MID_C.x - BEAD_R, END_C.y + BEAD_R).
STRING_RX = MID_C[0] - BEAD_R - END_C[0]        # 8
STRING_RY = MID_C[1] - END_C[1] - BEAD_R        # 10


def mx(p):
    return (2 * AXIS - p[0], p[1])


class CurvedStringOfBeadsRedraw(Solo48):
    icon_id = "curved-string-of-beads-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/jewelry"
    aliases = ("bead string", "string of beads", "beaded necklace")
    keywords = ("beads", "bead", "string", "necklace", "bracelet", "jewelry", "rosary", "craft")

    def _bead(self, name, centre, split_a, split_b):
        self.add_arc(f"{name}-1", split_a, split_b, radius_x=BEAD_R)
        self.add_arc(f"{name}-2", split_b, split_a, radius_x=BEAD_R)
        self.add_contour(name, f"{name}-1", f"{name}-2", closed=True)

    def build(self) -> None:
        cx, cy = END_C
        end_l_top, end_l_bottom = (cx, cy - BEAD_R), (cx, cy + BEAD_R)
        mid_l = (MID_C[0] - BEAD_R, MID_C[1])
        mid_r = mx(mid_l)

        self._bead("bead-left", END_C, end_l_top, end_l_bottom)
        self._bead("bead-right", mx(END_C), mx(end_l_bottom), mx(end_l_top))
        self._bead("bead-middle", MID_C, mid_l, mid_r)

        self.add_arc("string-left", end_l_bottom, mid_l,
                     radius_x=STRING_RX, radius_y=STRING_RY, sweep=False)
        self.add_arc("string-right", mx(end_l_bottom), mid_r,
                     radius_x=STRING_RX, radius_y=STRING_RY, sweep=True)
        for side in ("left", "right"):
            self.relate("connect", f"string-{side}", f"bead-{side}")
            self.relate("connect", f"string-{side}", "bead-middle")
