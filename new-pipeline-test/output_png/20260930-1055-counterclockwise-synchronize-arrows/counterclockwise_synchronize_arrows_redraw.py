"""counterclockwise synchronize arrows (redraw of the new-pipeline traced SVG).

Plan: two counterclockwise arrows on one circle, CIRCLE keyshape (centerline
radius 20 about (24,24)), built once and rotated 180 degrees about the centre.
- shaft: arc of radius R=15 about (24,24) from START (right side, 37 degrees
  below the axis on the 12-9-15 lattice point) counterclockwise up the right
  side and over the top to TIP on the top vertical extreme, so the arrow
  points straight left along the arc's horizontal tangent.
- head: open V at TIP with two equal arms (5,+-4) mirrored about that
  tangent (77-degree opening; the image's 90 degrees with 4,4 arms reached
  only radius 19.4, short of the CIRCLE envelope's 19.5); the outer arm end
  is the CIRCLE extreme at centerline radius 19.6, poking outside the shaft
  circle as in the image.
- the lower arrow is the point reflection through (24,24) of the upper one,
  so it runs from the upper left down the left side, under the bottom, and
  points straight right.
The trace's arcs are ellipses of about r=15.5 x 14.6 with the centre near
(23.9,23.5) and the tip joined by a short straight run; R=15 about (24,24)
makes the loop truly circular with its centre and every endpoint on the
integer grid, drops the straight run, and leaves room for the heads.

Metric issues: the only item was info `stroke-width` (trace stroke 2.64
after fitting, target 4). Fixed by construction: drawn at stroke 4 with every
gap between distinct parts at least 8 on centerlines (each tail to the other
arrow's tip is 13.4). validate_icon(): valid, no warnings.
Lucide construction used: `refresh-ccw` (two arcs on one circle with open
corner heads at the arc ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bafc5d96-6820-5892-a08b-927ab58a96ff"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1055-counterclockwise-synchronize-arrows/counterclockwise-synchronize-arrows_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24
R = 15
START = (C + 12, C + 9)        # upper arrow's tail, 37 degrees below the axis
TIP = (C, C - R)               # arrowhead tip on the top extreme
ARM_X, ARM_Y = 5, 4            # head arms (+ARM_X, +-ARM_Y), mirrored about the tangent
HEAD_OUT = (TIP[0] + ARM_X, TIP[1] - ARM_Y)   # radius 19.6: reaches the envelope
HEAD_IN = (TIP[0] + ARM_X, TIP[1] + ARM_Y)


def rot(p):
    """Point reflection through the centre (180-degree rotation)."""
    return (2 * C - p[0], 2 * C - p[1])


class CounterclockwiseSynchronizeArrowsRedraw(Solo48):
    icon_id = "counterclockwise-synchronize-arrows-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/navigation"
    aliases = ("sync arrows", "synchronize", "refresh arrows", "counterclockwise arrows")
    keywords = ("sync", "synchronize", "refresh", "reload", "rotate", "counterclockwise",
                "anticlockwise", "arrows", "circular", "cycle")

    def _arrow(self, name, start, tip, head_out, head_in) -> None:
        self.add_arc(f"{name}-shaft", start, tip, radius_x=R, sweep=False)
        self.add_line(f"{name}-head-out", head_out, tip)
        self.add_line(f"{name}-head-in", tip, head_in)
        self.add_contour(f"{name}-head", f"{name}-head-out", f"{name}-head-in")
        self.relate("connect", f"{name}-shaft", f"{name}-head")

    def build(self) -> None:
        self._arrow("upper", START, TIP, HEAD_OUT, HEAD_IN)
        self._arrow("lower", rot(START), rot(TIP), rot(HEAD_OUT), rot(HEAD_IN))
