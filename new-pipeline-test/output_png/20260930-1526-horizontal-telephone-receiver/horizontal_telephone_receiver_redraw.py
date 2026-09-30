"""horizontal-telephone-receiver (redraw of the new-pipeline traced SVG).

Subject: a classic handset lying on its back, a shallow arched handle joining
two matching earpiece cups that turn down at the left and right ends, drawn as
one continuous hollow outline.

Plan (symbols before coordinates), mirrored about x = 24:
- keyshape HRECT_M as suggested; centerline box (4,10)-(44,38).
- outer arch: one half-ellipse about (24, ARCH_Y), rx 20, ry ARCH_Y - TOP,
  split at the apex (24,10); it meets the vertical outer walls tangentially.
- earpiece cup: outer wall x = 4 down to r4 corner, short flat base on
  y = 38, r CUP_R inner cup rounding up into the neck at x = NECK_X.
- recess: r4 rounding from the neck into a flat handle underside at y = UNDER_Y.
  Every straight/curve join is tangent, so the outline reads as one smooth tube.

Metric issues fixed:
- keyshape-short-axis (warn): the trace filled only 48% of the HRECT_M height.
  The handset is re-proportioned (deeper arch, taller earpieces) so its
  extremes sit exactly on x 4/44 and y 10/38.
- stroke-width (info): the trace stroke was 2.67 after fitting; every wall pair
  is now spaced for stroke 4 (handle 12, earpiece 12 between centerlines,
  well above the 8 minimum) and the single hole is far above 6 inscribed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "791f3e5f-2569-40aa-92db-6d888122af9d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1526-horizontal-telephone-receiver/horizontal-telephone-receiver_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, LEFT, RIGHT, TOP, BASE = 24, 4, 44, 10, 38
ARCH_Y = 24          # outer walls turn into the half-ellipse here
CORNER_R = 4         # outer bottom corners and recess corners
CUP_R = 6            # inner cup rounding of each earpiece
NECK_X = 16          # left neck; right neck mirrors to 32
UNDER_Y = 22         # handle underside


class HorizontalTelephoneReceiverRedraw(Solo48):
    icon_id = "horizontal-telephone-receiver-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "phones"
    aliases = ("handset", "phone receiver", "telephone handset")
    keywords = ("telephone", "receiver", "handset", "horizontal", "call", "phone", "communication")

    def build(self) -> None:
        def mx(x):
            return 2 * CX - x

        rx, ry = CX - LEFT, ARCH_Y - TOP
        cup_x = NECK_X - CUP_R  # where the flat base meets the cup
        names = []

        def line(n, a, b):
            self.add_line(n, a, b)
            names.append(n)

        def arc(n, a, b, r, sweep, ry_=None):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry_ if ry_ is not None else r, sweep=sweep)
            names.append(n)

        # Clockwise from the apex.
        arc("arch-right", (CX, TOP), (RIGHT, ARCH_Y), rx, True, ry)
        line("wall-right", (RIGHT, ARCH_Y), (RIGHT, BASE - CORNER_R))
        arc("corner-right", (RIGHT, BASE - CORNER_R), (RIGHT - CORNER_R, BASE), CORNER_R, True)
        line("base-right", (RIGHT - CORNER_R, BASE), (mx(cup_x), BASE))
        arc("cup-right", (mx(cup_x), BASE), (mx(NECK_X), BASE - CUP_R), CUP_R, True)
        line("neck-right", (mx(NECK_X), BASE - CUP_R), (mx(NECK_X), UNDER_Y + CORNER_R))
        arc("recess-right", (mx(NECK_X), UNDER_Y + CORNER_R), (mx(NECK_X + CORNER_R), UNDER_Y), CORNER_R, False)
        line("underside", (mx(NECK_X + CORNER_R), UNDER_Y), (NECK_X + CORNER_R, UNDER_Y))
        arc("recess-left", (NECK_X + CORNER_R, UNDER_Y), (NECK_X, UNDER_Y + CORNER_R), CORNER_R, False)
        line("neck-left", (NECK_X, UNDER_Y + CORNER_R), (NECK_X, BASE - CUP_R))
        arc("cup-left", (NECK_X, BASE - CUP_R), (cup_x, BASE), CUP_R, True)
        line("base-left", (cup_x, BASE), (LEFT + CORNER_R, BASE))
        arc("corner-left", (LEFT + CORNER_R, BASE), (LEFT, BASE - CORNER_R), CORNER_R, True)
        line("wall-left", (LEFT, BASE - CORNER_R), (LEFT, ARCH_Y))
        arc("arch-left", (LEFT, ARCH_Y), (CX, TOP), rx, True, ry)
        self.add_contour("receiver", *names, closed=True)
