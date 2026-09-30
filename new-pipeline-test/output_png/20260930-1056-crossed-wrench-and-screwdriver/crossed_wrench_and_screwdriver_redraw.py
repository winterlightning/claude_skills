"""crossed-wrench-and-screwdriver (redraw of the new-pipeline traced SVG).

Plan: an open-end wrench crossed with a flathead screwdriver in an X on
SQUARE, the keyshape the metrics suggested (centerline box (6,6)-(42,42)).
- wrench head: a radius-5 C ring centred at HEAD (16,11), its jaw opening up
  and to the left along the handle axis between the ring's top (16,6) and
  left (11,11) points. The ring is split at the 3-4-5 lattice point
  NECK = HEAD+(4,3), where the handle leaves it; both arcs share that point
  with the handle.
- wrench handle: one 45-degree centerline on y = x - 6 from NECK to (42,36),
  the right extreme (the trace's double outline reduced to one stroke).
- screwdriver: axis x + y = 48. The handle is a closed 45-degree rectangle
  whose sides sit (4,4) either side of the axis (11.3 apart on centerlines,
  a 7.3 inner hole); its far corners are the left (6,34) and bottom (14,42)
  extremes. The shaft leaves the middle of the handle's top edge (19,29) and
  runs to the tip (42,6), the top/right corner.
- the two axes meet at the lattice point CROSS (27,21); both tools are split
  there and the four halves share it and are related with `connect`.
Dropped: the image's over/under break in the screwdriver shaft. Leaving 8 on
centerlines either side of the wrench left a floating shaft stub that no
longer read as part of the screwdriver (tried first; valid but unreadable);
a plain X keeps the screwdriver whole. Also dropped: the flared blade outline
(it would close a hole under 6 at the tip) and the jaw's inner notch.
Handle length is capped at 12.7 by the 9 needed between the ring and the
handle's top corner (15,25); it stays a little stubby for that reason.
Lucide `wrench` gave the open-jaw head on a diagonal; `swords` the crossed-X
construction. No local Lucide screwdriver; handle + shaft follow the image.

Metric issues (crossed-wrench-and-screwdriver_metrics.json):
- stroke-width (info, trace 2.77 fitted): redrawn at stroke 4 with every gap
  budgeted for 4.
- clearance e0/e1 (error, 1.96) and e0/e2 (error, 2.45): the trace outlined
  the wrench handle as two edges that ran into the screwdriver pieces at the
  crossing. Each tool is now one centerline and they meet at a declared
  shared point; unrelated parts keep >= 9 (ring to handle corner 9.0, ring to
  shaft 9.8, wrench handle to screwdriver-handle corners 11.3).
- hole at (15.8,15.6) (error, 3.54 wide): the closed wrench-head outline is
  replaced by an open C ring, so the head encloses no hole.
- hole at (36.6,11.8) (error, 1.26 wide): the outlined blade is dropped; the
  shaft is a single stroke ending in a round cap.
- hole at (10.6,36.7) (error, 3.96 wide): the screwdriver handle is 11.3 wide
  on centerlines, an inner hole of 7.3.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8b935d53-8cae-4d27-b6e5-0fed82d9789e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1056-crossed-wrench-and-screwdriver/crossed-wrench-and-screwdriver_raw.svg"
AUTHOR = "claude-opus-5-5"

R = 5                          # wrench ring radius
HEAD = (16, 11)                # ring centre: top (16,6) on the box edge
NECK = (20, 14)                # HEAD + (4,3), 3-4-5 lattice point
WRENCH_END = (42, 36)          # wrench axis y = x - 6: right extreme
CROSS = (27, 21)               # y = x - 6 meets x + y = 48 on the lattice
HALF = (4, 4)                  # screwdriver handle half-width across the axis
GRIP_TOP = (19, 29)            # screwdriver axis x + y = 48
GRIP_END = (10, 38)
TIP = (42, 6)                  # top/right corner of the box


def _add(a, b, k=1):
    return (a[0] + k * b[0], a[1] + k * b[1])


class CrossedWrenchAndScrewdriverRedraw(Solo48):
    icon_id = "crossed-wrench-and-screwdriver-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("wrench and screwdriver", "tools", "repair tools")
    keywords = ("wrench", "screwdriver", "tools", "repair", "settings",
                "maintenance", "service", "fix", "mechanic", "crossed")

    def build(self) -> None:
        cx, cy = HEAD
        top = (cx, cy - R)
        left = (cx - R, cy)
        # C ring clockwise from the top jaw tip round to the left jaw tip,
        # split at the neck so the handle shares a drawn endpoint.
        self.add_arc("wrench-head-a", top, NECK, radius_x=R, sweep=True)
        self.add_arc("wrench-head-b", NECK, left, radius_x=R, sweep=True)
        self.add_contour("wrench-head", "wrench-head-a", "wrench-head-b")
        # Both tools are split where they cross so the halves share CROSS.
        self.add_line("wrench-handle-upper", NECK, CROSS)
        self.add_line("wrench-handle-lower", CROSS, WRENCH_END)
        self.relate("connect", "wrench-head-a", "wrench-head-b",
                    "wrench-handle-upper")

        # Screwdriver handle: rectangle along x + y = 48, its top edge split
        # at GRIP_TOP where the shaft leaves it.
        self.add_polyline(
            "screwdriver-handle",
            GRIP_TOP, _add(GRIP_TOP, HALF), _add(GRIP_END, HALF),
            _add(GRIP_END, HALF, -1), _add(GRIP_TOP, HALF, -1),
            closed=True,
        )
        self.add_line("screwdriver-shaft-lower", GRIP_TOP, CROSS)
        self.add_line("screwdriver-shaft-upper", CROSS, TIP)
        self.relate("connect", "screwdriver-shaft-lower", "screwdriver-handle-1",
                    "screwdriver-handle-5")
        self.relate("connect", "wrench-handle-upper", "wrench-handle-lower",
                    "screwdriver-shaft-lower", "screwdriver-shaft-upper")
