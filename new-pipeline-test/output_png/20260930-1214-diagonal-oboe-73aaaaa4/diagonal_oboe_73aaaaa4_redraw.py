"""diagonal-oboe (redraw of the new-pipeline traced SVG, source 73aaaaa4).

Plan: oboe on SQUARE (centerline box (6,6)-(42,42)) laid on the 45-degree
diagonal, bell lower-left and reed upper-right, mirrored about the axis
x + y = 48 (mirror (x, y) -> (48 - y, 48 - x)).
- body: two parallel walls x+y=42 and x+y=54 (8.49 apart on centerlines),
  closed at the top by a perpendicular cap split at its midpoint (36,12).
- bell: one cubic per side from the wall end, tangent to the wall, flaring
  out to a straight rim (6,32)-(16,42), 1.7x the body width; the flare ends
  are the left/bottom extremes, so the keyshape fit is exact.
- reed: one stroke from the cap midpoint (36,12) to (42,6), the top/right
  extremes, declared as a connection to the body.
- keys: two detached bars parallel to the body on x+y=30 and x+y=66, each
  8.49 from its wall, staggered like the reference (upper-left one higher).
Metric issues fixed: stroke-width (redrawn at stroke 4 with every gap
budgeted for it); keyshape-short-axis (extremes sit exactly on 6 and 42);
all four clearance errors (e2/e3 body walls 2.65 -> 8.49; keys vs walls
4.04/4.16 -> 8.49; keys e4/e5 5.61 -> 14+); loose-join e0/e3 (bell sides
and rim share exact endpoints in one closed contour); the narrow-join and
loose-join warnings of e4/e5 (keys are free parts clear of the walls, not
fused wedges); hole at the bell (the traced bell collar hole is gone, the
bell interior is one open 8.49+ wide region).
No Lucide oboe exists; construction follows Lucide's diagonal wind
instruments / tools (straight 45-degree walls, round caps).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "73aaaaa4-5952-463a-a503-f7716b6e5ad7"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1214-diagonal-oboe-73aaaaa4/"
    "diagonal-oboe-73aaaaa4_raw.svg"
)
AUTHOR = "claude-opus-5-5"


def mirror(p):
    """Reflect across the oboe axis x + y = 48."""
    return (48 - p[1], 48 - p[0])


WALL_TOP = (33, 9)        # upper-left wall top (x+y=42)
WALL_LOW = (16, 26)       # upper-left wall bottom, start of the flare
CAP_MID = (36, 12)        # cap midpoint on the axis; reed root
REED_TIP = (42, 6)
RIM = (6, 32)             # bell rim end on the upper-left side
FLARE_K = 4               # wall-direction handle at the flare start
RIM_K = (4, 0)            # rim-end handle (arrives heading west)
KEY_A = ((19, 11), (23, 7))    # x+y=30, beside the upper body
KEY_B = ((34, 32), (38, 28))   # x+y=66, lower on the far wall


class DiagonalOboeRedraw(Solo48):
    icon_id = "diagonal-oboe-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ("oboe", "woodwind", "double reed")
    keywords = ("oboe", "woodwind", "reed", "instrument", "music", "orchestra")

    def build(self) -> None:
        c1 = (WALL_LOW[0] - FLARE_K, WALL_LOW[1] + FLARE_K)
        c2 = (RIM[0] + RIM_K[0], RIM[1] + RIM_K[1])
        self.add_line("wall_a", WALL_TOP, WALL_LOW)
        self.add_bezier("flare_a", WALL_LOW, (c1, c2, RIM))
        self.add_line("rim", RIM, mirror(RIM))
        self.add_bezier(
            "flare_b", mirror(RIM), (mirror(c2), mirror(c1), mirror(WALL_LOW))
        )
        self.add_line("wall_b", mirror(WALL_LOW), mirror(WALL_TOP))
        self.add_line("cap_b", mirror(WALL_TOP), CAP_MID)
        self.add_line("cap_a", CAP_MID, WALL_TOP)
        self.add_contour(
            "body", "wall_a", "flare_a", "rim", "flare_b", "wall_b", "cap_b", "cap_a",
            closed=True,
        )

        self.add_line("reed", CAP_MID, REED_TIP)
        self.relate("connect", "reed", "body")

        self.add_line("key_a", *KEY_A)
        self.add_line("key_b", *KEY_B)
