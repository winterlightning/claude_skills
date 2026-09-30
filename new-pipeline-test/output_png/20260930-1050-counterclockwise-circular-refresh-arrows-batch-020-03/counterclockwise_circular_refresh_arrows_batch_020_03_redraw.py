"""counterclockwise circular refresh arrows (redraw of the new-pipeline traced SVG).

Plan: two counterclockwise arrows on one circle, CIRCLE keyshape (centerline
radius 20 about (24,24)), built once and rotated 180 degrees about the centre.
- shaft: arc of radius R=15 about (24,24) from START (upper right, 37 degrees
  above the axis on the 12-9-15 lattice point) counterclockwise over the top
  to TIP on the left-hand horizontal extreme, so the arrow points straight
  down (the generated image points down-left, a few degrees off vertical).
- head: open V at TIP, two equal arms mirrored about the arc's vertical
  tangent (opening 77 degrees); the outer arm end is the CIRCLE extreme at
  centerline radius 19.6, poking outside the shaft circle as in the image.
- the lower arrow is the point reflection through (24,24) of the upper one,
  so it runs from the lower left under the bottom and points straight up.
The trace's arcs are about r=15.8 x 15.1 with the centre near (23.8,22.9);
R=15 about (24,24) makes the loop truly circular with its centre and every
endpoint on the integer grid, and leaves room for the heads in the envelope.

Metric issues: the only item was info `stroke-width` (trace stroke 2.49
after fitting, target 4). Fixed by construction: at stroke 4 every gap
between distinct parts is at least 8 on centerlines (each tip to the other
shaft's start is 9.5), where the trace's closest pair was 8.34. The trace's
slightly ragged lower shaft (a four-cubic path with a kink before the head)
is replaced by one clean arc. validate_icon(): valid, no warnings.
Lucide construction used: `refresh-ccw` (two concentric arcs with open
corner heads at the arc ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0a11ecc5-12d2-479f-ad50-bf72f2730e09"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1050-counterclockwise-circular-refresh-arrows-batch-020-03/counterclockwise-circular-refresh-arrows-batch-020-03_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24
R = 15
START = (C + 12, C - 9)        # upper arc starts 37 degrees above the axis
TIP = (C - R, C)               # arrowhead tip on the horizontal extreme
ARM_X, ARM_Y = 4, 5            # head arms (+-ARM_X, -ARM_Y), mirrored about the tangent
HEAD_OUT = (TIP[0] - ARM_X, TIP[1] - ARM_Y)   # radius 19.6: reaches the envelope
HEAD_IN = (TIP[0] + ARM_X, TIP[1] - ARM_Y)


def rot(p):
    """Point reflection through the centre (180-degree rotation)."""
    return (2 * C - p[0], 2 * C - p[1])


class CounterclockwiseCircularRefreshArrowsBatch02003Redraw(Solo48):
    icon_id = "counterclockwise-circular-refresh-arrows-batch-020-03-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/navigation"
    aliases = ("refresh arrows", "reload arrows", "counterclockwise arrows")
    keywords = ("refresh", "reload", "sync", "rotate", "counterclockwise", "anticlockwise",
                "arrows", "circular", "cycle", "undo")

    def _arrow(self, name, start, tip, head_out, head_in) -> None:
        self.add_arc(f"{name}-shaft", start, tip, radius_x=R, sweep=False)
        self.add_line(f"{name}-head-out", head_out, tip)
        self.add_line(f"{name}-head-in", tip, head_in)
        self.add_contour(f"{name}-head", f"{name}-head-out", f"{name}-head-in")
        self.relate("connect", f"{name}-shaft", f"{name}-head")

    def build(self) -> None:
        self._arrow("upper", START, TIP, HEAD_OUT, HEAD_IN)
        self._arrow("lower", rot(START), rot(TIP), rot(HEAD_OUT), rot(HEAD_IN))
