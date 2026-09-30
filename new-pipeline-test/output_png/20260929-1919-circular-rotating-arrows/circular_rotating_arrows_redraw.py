"""circular rotating arrows (redraw of the new-pipeline traced SVG).

Plan: two clockwise arrows on one circle, CIRCLE keyshape (centerline radius
20 about (24,24)), built once and rotated 180 degrees about the centre.
- shaft: arc of radius R=15 about (24,24) from START (upper left, 37 degrees
  above the axis on the 9-12-15 lattice point) clockwise over the top to TIP
  on the right-hand horizontal extreme, so the arrow points straight down.
- head: open V at TIP, two equal arms mirrored about the arc's vertical
  back tangent (opening 77 degrees); the outer arm end is the CIRCLE
  extreme at centerline radius 19.6, poking outside the shaft circle as in
  the generated image.
- the second arrow is the point reflection through (24,24) of the first.
The trace's arc is about r=16 and its heads reach r=20; R=15 keeps the arc
centre and every endpoint on the integer grid while leaving room for the
heads inside the CIRCLE envelope.

Metric issues: the only item was info `stroke-width` (trace stroke 2.44,
target 4). Fixed by construction: at stroke 4 every gap between distinct
parts is at least 8 on centerlines (tip to the other shaft's start 9.5),
where the trace's closest pair was 8.76. validate_icon(): valid, no
warnings.
Lucide construction used: `refresh-cw` (two concentric arcs with open
corner heads at the arc ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e63cb3c3-10bb-4fb1-a675-1e6b119047a5"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1919-circular-rotating-arrows/circular-rotating-arrows_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24
R = 15
START = (C - 12, C - 9)        # upper arc starts 37 degrees above the axis
TIP = (C + R, C)               # arrowhead tip on the horizontal extreme
ARM_X, ARM_Y = 4, 5            # head arms (+-ARM_X, -ARM_Y), mirrored about the tangent
HEAD_OUT = (TIP[0] + ARM_X, TIP[1] - ARM_Y)   # radius 19.6: reaches the envelope
HEAD_IN = (TIP[0] - ARM_X, TIP[1] - ARM_Y)


def rot(p):
    """Point reflection through the centre (180-degree rotation)."""
    return (2 * C - p[0], 2 * C - p[1])


class CircularRotatingArrowsRedraw(Solo48):
    icon_id = "circular-rotating-arrows-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/navigation"
    aliases = ("rotation arrows", "spin arrows", "refresh arrows")
    keywords = ("rotate", "rotation", "arrows", "circular", "cycle", "refresh", "sync", "spin")

    def _arrow(self, name, start, tip, head_out, head_in) -> None:
        self.add_arc(f"{name}-shaft", start, tip, radius_x=R)
        self.add_line(f"{name}-head-out", head_out, tip)
        self.add_line(f"{name}-head-in", tip, head_in)
        self.add_contour(f"{name}-head", f"{name}-head-out", f"{name}-head-in")
        self.relate("connect", f"{name}-shaft", f"{name}-head")

    def build(self) -> None:
        self._arrow("upper", START, TIP, HEAD_OUT, HEAD_IN)
        self._arrow("lower", rot(START), rot(TIP), rot(HEAD_OUT), rot(HEAD_IN))
