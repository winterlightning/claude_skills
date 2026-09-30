"""json-logo-redraw (redraw of the new-pipeline traced SVG).

Plan: the JSON mark as a pair of curly braces on SQUARE (centerline box
(6,6)-(42,42)), the right brace mirrored from the left about x=24.
- each brace is one open contour: a short tail at the top (y=6), an r4
  corner into a vertical wall (x=12), two r6 quarter arcs meeting at the
  point (x=6, y=24), a second wall and an r4 corner out to the bottom tail
  (y=42). The point is the deliberate brace cusp, as in Lucide braces.
- the tails end at x=18 / x=30, leaving a 12-unit centerline gap (8 ink)
  between the braces, wider than the 8 minimum.
Construction reference: icon_set/references/lucide/original/braces.svg
(tail, rounded corner, straight wall, two quarter arcs into the point),
rebuilt at this grid's stroke 4 with larger radii.
Traced shape: 20260930-1541-json-logo/json-logo_raw.svg (not its coordinates).

Metric issues:
- keyshape-short-axis (warn): fixed. The trace filled only 87% of the SQUARE
  height; the braces now run the full y=6..42 and the points sit on x=6 / x=42,
  so all four extremes touch the box.
- stroke-width (info): fixed by construction. The model is stroked at 4 and
  the only gap (brace to brace) is 12 on centerlines, so it survives stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd2eaa4c-1430-46f4-adcf-5755852eaadf"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1541-json-logo/json-logo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, BOTTOM, MID = 6, 42, 24
TIP_X = 6          # brace point on the box edge
WALL_X = 12        # vertical wall
TAIL_X = 18        # tail end, 12 from the mirrored tail
CORNER_R = 4
POINT_R = 6        # WALL_X - TIP_X


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class JsonLogoRedraw(Solo48):
    icon_id = "json-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("json", "curly braces")
    keywords = ("json", "braces", "curly", "data", "format", "code", "developer", "logo")

    def build(self) -> None:
        pts = [
            (TAIL_X, TOP),
            (WALL_X + CORNER_R, TOP),
            (WALL_X, TOP + CORNER_R),
            (WALL_X, MID - POINT_R),
            (TIP_X, MID),
            (WALL_X, MID + POINT_R),
            (WALL_X, BOTTOM - CORNER_R),
            (WALL_X + CORNER_R, BOTTOM),
            (TAIL_X, BOTTOM),
        ]
        # (kind, radius, sweep) for each span of the left brace, top to bottom.
        spans = [
            ("line", None, None),
            ("arc", CORNER_R, False),
            ("line", None, None),
            ("arc", POINT_R, True),
            ("arc", POINT_R, True),
            ("line", None, None),
            ("arc", CORNER_R, False),
            ("line", None, None),
        ]
        for side, flip in (("l", lambda p: p), ("r", mirror)):
            names = []
            for i, (kind, r, sweep) in enumerate(spans):
                name = f"{side}{i}"
                a, b = flip(pts[i]), flip(pts[i + 1])
                if kind == "line":
                    self.add_line(name, a, b)
                else:
                    # Mirroring reverses the turn direction.
                    self.add_arc(name, a, b, radius_x=r, sweep=sweep if side == "l" else not sweep)
                names.append(name)
            self.add_contour(f"brace-{side}", *names)
