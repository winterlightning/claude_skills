"""bow tie suit (redraw of the new-pipeline traced SVG).

Plan: front view of a dinner jacket with a bow tie on VRECT_L (centerline box
(8,4)-(40,44)), mirrored about x=24.
- bow tie: two small wedges meeting at the knot (24,7); each wedge is a closed
  triangle too small to leave a hole at stroke 4, so the tie reads solid. Its
  top corners are the y=4 extreme.
- jacket: one closed silhouette - collar point, rounded shoulder, straight
  side (x=8 / x=40 extremes), rounded hem corner, hem (y=44 extreme), up the
  other side, then back through the lapel V that meets at the button (24,34).
  The collar points sit 8.25 from the tie's lower corners, so the tie sits in
  the open neck.
- front: one closure line from the button to the hem centre, sharing both
  endpoints with the silhouette.
Metric issues fixed:
- all 31 clearance errors: the shirt-front lines (e8/e9), the inner sleeve
  lines (e7/e10), the collar notches and the splayed hem cutaway were dropped;
  the tie is >= 8 from the jacket on centerlines, and touching parts share an
  endpoint declared with relate("connect").
- hole at (24,14.6) 3.69 wide: the hollow bow-tie loops are now solid wedges
  (no hole); the two jacket halves keep large openings.
- loose joins at the button and hem: lapels, front line and hem meet exactly
  at shared integer nodes.
- narrow joins (17.9-33.5 deg wedges): the lapel V now opens at 47 deg and the
  front line leaves it at 156 deg; the tie wedges fill solid by design.
- keyshape short axis (81% y fill): the tie reaches y=4 and the hem y=44.
- stroke count 11 -> 4 parts (bow-l, bow-r, jacket, front).
- stroke width: drawn at stroke 4 with gaps sized for it.
Not kept: sleeves. A sleeve seam needs 8 from the side and 8 from the lapel,
which the 32-wide box cannot give beside the V. Lucide `shirt` informed the
shoulder outline only; Lucide has no jacket or bow tie.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2487ed91-55b8-44a8-a6e9-f9630de162fe"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1724-bow-tie-suit/bow-tie-suit_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
KNOT = (AXIS, 7)
TIE_TOP_L, TIE_BOT_L = (19, 4), (19, 10)
COLLAR_L = (17, 18)            # 8.25 from the tie's lower corner (19,10)
BUTTON = (AXIS, 34)
HEM_MID = (AXIS, 44)
SIDE_X = 8
SHOULDER_L = (SIDE_X, 25)
CORNER_R = 2
HEM_CORNER_L = (SIDE_X + CORNER_R, 44)
SIDE_BOTTOM_L = (SIDE_X, 44 - CORNER_R)
# Left shoulder from the collar point down to the side: (control1, control2, knot).
SHOULDER_L_CURVE = ((12, 18), (SIDE_X, 19), SHOULDER_L)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class BowTieSuitRedraw(Solo48):
    icon_id = "bow-tie-suit-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing/formal"
    aliases = ("tuxedo", "dinner jacket", "suit and bow tie")
    keywords = ("suit", "tuxedo", "bow tie", "jacket", "formal", "blazer", "wedding", "clothing")

    def build(self) -> None:
        self.add_polyline("bow-l", KNOT, TIE_TOP_L, TIE_BOT_L, closed=True)
        self.add_polyline("bow-r", KNOT, mx(TIE_BOT_L), mx(TIE_TOP_L), closed=True)
        self.relate("connect", "bow-l", "bow-r")

        # Jacket silhouette, one closed run: left collar point, down the left
        # side, across the hem (split at the front line), up the right side,
        # then back through the lapel V and the button.
        c1, c2, _ = SHOULDER_L_CURVE
        self.add_bezier("shoulder-l", COLLAR_L, SHOULDER_L_CURVE)
        self.add_line("side-l", SHOULDER_L, SIDE_BOTTOM_L)
        self.add_arc("corner-l", SIDE_BOTTOM_L, HEM_CORNER_L, radius_x=CORNER_R, sweep=False)
        self.add_line("hem-l", HEM_CORNER_L, HEM_MID)
        self.add_line("hem-r", HEM_MID, mx(HEM_CORNER_L))
        self.add_arc("corner-r", mx(HEM_CORNER_L), mx(SIDE_BOTTOM_L), radius_x=CORNER_R, sweep=False)
        self.add_line("side-r", mx(SIDE_BOTTOM_L), mx(SHOULDER_L))
        self.add_bezier("shoulder-r", mx(SHOULDER_L), (mx(c2), mx(c1), mx(COLLAR_L)))
        self.add_line("lapel-r", mx(COLLAR_L), BUTTON)
        self.add_line("lapel-l", BUTTON, COLLAR_L)
        self.add_contour("jacket", "shoulder-l", "side-l", "corner-l", "hem-l", "hem-r",
                         "corner-r", "side-r", "shoulder-r", "lapel-r", "lapel-l",
                         closed=True)

        # Front closure below the button.
        self.add_line("front", BUTTON, HEM_MID)
        self.relate("connect", "front", "jacket")
