"""counterclockwise-refresh-arrow (redraw of the new-pipeline traced SVG).

Plan: CIRCLE keyshape (centerline radius 20 about (24,24)), as the metrics
suggest. One ring arc plus one open V head, touching at the head tip.
- ring: a radius-17 arc about (26,25), an 8-15-17 triangle, so both ends sit
  on integer points mirrored about y=25: tail (11,33) lower left, tip (11,17)
  upper left. It is the large arc running down, round the bottom, the right
  and the top (counterclockwise on screen); the gap stays at the lower left.
  The ring centre sits 2 right / 1 down from the canvas centre so the head,
  which sticks out past the ring at the upper left, still fits the radius.
- head: a polyline (17,15)-(11,17)-(9,11). Its wings run (3,-1) and (-1,-3)
  from the tip: perpendicular to each other and within 4 deg of +/-45 about
  the ring's tangent (-8,15) there, so the V points down-left along the arc.
  It shares the tip with the ring (declared connect).
Extremes: ring right (43,25) at 19.03 from the centre, wing end (9,11) at
19.85; everything is inside the radius-20 centerline circle.

Metric issues:
- stroke-width (trace 2.4 vs 4): fixed -- redrawn at stroke 4. The only
  distinct-part spacing is the ring gap: tail (11,33) to tip (11,17) is 16
  on centerlines and the upper wing ends 22 from the tail. No holes.
Lucide rotate-ccw informed the open ring with a V head at the upper-left
end; the arc-end head, not Lucide's straight lead-in, follows the generated
image. The drawing is directional and deliberately not mirrored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "77f5a2c6-8120-4350-aa53-7bb00704de7d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1052-counterclockwise-refresh-arrow/counterclockwise-refresh-arrow_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, R = 26, 25, 17       # ring centre and radius (8-15-17 triangle)
DX, DY = 15, 8               # both ring ends sit at (CX - DX, CY -/+ DY)
WING = ((3, -1), (-1, -3))   # head wings, +/-45 deg about the tangent
WING_K = 2                   # wing length multiplier (2 * sqrt(10) = 6.3)


class CounterclockwiseRefreshArrowRedraw(Solo48):
    icon_id = "counterclockwise-refresh-arrow-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ("counterclockwise refresh arrow", "rotate counterclockwise", "rotate left", "undo")
    keywords = ("refresh", "reload", "rotate", "counterclockwise", "anticlockwise", "arrow", "undo", "reset")

    def build(self) -> None:
        tail = (CX - DX, CY + DY)
        tip = (CX - DX, CY - DY)
        self.add_arc("ring", tail, tip, radius_x=R, large_arc=True, sweep=False)
        a = (tip[0] + WING_K * WING[0][0], tip[1] + WING_K * WING[0][1])
        b = (tip[0] + WING_K * WING[1][0], tip[1] + WING_K * WING[1][1])
        self.add_polyline("head", a, tip, b)
        self.relate("connect", "ring", "head")
