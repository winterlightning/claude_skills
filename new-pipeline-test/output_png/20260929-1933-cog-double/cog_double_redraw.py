"""cog-double (redraw of the new-pipeline traced SVG).

Plan: two equal six-tooth cogs on SQUARE (centerline box (6,6)-(42,42)) on
the falling diagonal, both with a tooth pointing straight up as in the
generated image. The upper-left cog stands in front and is drawn whole; the
lower-right cog sits behind it, and its outline runs from one knot of the
front outline round to another (declared connect), so the front cog's
lower-right tooth hides the back cog's upper-left tooth tip.
- one tooth definition per cog (a quarter from the top tip to the right
  valley), mirrored on both axes into a closed 18-point outline: flat tips
  4 wide on radius ~11, tapered flanks, V valleys on radius 8.
- front cog centre (17,17): top tip on y 6 and left tips on x 6 (extremes).
- back cog centre (31,31): bottom tip on y 42 and right tips on x 42.
- each hub is a dot on the cog centre, 8 from the nearest valley.
The back cog's side teeth sit one unit wider/lower than the front's (grid
rounding of a 60 degree tooth), which is what lets both junctions land on
grid knots: (27,24) and (21,25), both vertices of the front outline.
Lucide construction: `cog` (hub + evenly spaced teeth around one centre);
its ring-with-stubs build cannot hold 8-unit gaps at this size, so the teeth
are one tapered outline instead, as in the generated image.

Metric issues (cog-double_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (SQUARE fills 86% of y): the cogs now reach all four
  sides of the SQUARE box exactly (top/left front, bottom/right back).
- clearance e0/e1 and e2/e3 (hub circles 2.7-2.8 from the cog outlines):
  the hollow hub ring is replaced by a hub dot 8 from the nearest valley. A
  hollow hub needs a 6-wide hole plus 8 of clearance, i.e. a root radius of
  11 and a tip radius of ~15 -- two such cogs cannot share a 36 box.
- clearance e0/e2 (the two cogs 2.97 apart): two separate six-tooth cogs
  cannot keep 8 between them in a 36 box (tip radius would be <= 8.9, too
  small for six readable teeth at stroke 4). The cogs now overlap, the back
  one occluded, and every non-connected pair keeps 8 on centerlines.
- hole x14 (tooth pinches 0.6-0.8 wide, hubs 3.5 wide): the pinches came
  from a thin trace stroke hugging each tooth; the redrawn outline is a
  single stroke per cog, so each cog interior is one open region around its
  hub dot, far wider than 6.
Not reproduced: the white gap between the cogs and the hollow hub rings
(both impossible at stroke 4 on 48, as above).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b484255b-2a40-40d1-9943-7e27cfb9f399"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1933-cog-double/cog-double_raw.svg"
AUTHOR = "claude-opus-5-5"

# Quarter outline relative to the cog centre: top tip corner, valley, the
# upper-right tooth's two tip corners, right valley. Mirrored on x and y.
FRONT_QUARTER = ((2, -11), (4, -8), (10, -7), (11, -4), (8, 0))
BACK_QUARTER = ((2, -11), (4, -7), (9, -8), (11, -4), (8, 0))
FRONT_C = (17, 17)
BACK_C = (31, 31)
# The back outline leaves the front cog at its upper-left valley and returns
# on its upper-left tooth tip, both on front knots.
BACK_FROM = (-4, -7)          # back valley under front vertex (27,24)
BACK_TO_TIP = (-10, -6)       # point on back tip edge at front vertex (21,25)


def cog_ring(quarter, centre):
    """Closed tooth outline, clockwise from the top tip's right corner."""
    half = list(quarter) + [(x, -y) for x, y in reversed(quarter) if y != 0]
    ring = half + [(-x, y) for x, y in reversed(half)]
    cx, cy = centre
    return [(cx + x, cy + y) for x, y in ring]


class CogDoubleRedraw(Solo48):
    icon_id = "cog-double-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("cogs", "gears", "double cog", "two gears")
    keywords = ("cog", "gear", "settings", "machinery", "mechanism", "engineering", "preferences")

    def build(self) -> None:
        self.add_polyline("front", *cog_ring(FRONT_QUARTER, FRONT_C), closed=True)
        self.add_dot("front-hub", FRONT_C)

        ring = cog_ring(BACK_QUARTER, BACK_C)
        bx, by = BACK_C
        start = ring.index((bx + BACK_FROM[0], by + BACK_FROM[1]))
        # clockwise all the way round, stopping short of the hidden tip corner
        visible = ring[start:] + ring[:start - 1] + [(bx + BACK_TO_TIP[0], by + BACK_TO_TIP[1])]
        self.add_polyline("back", *visible)
        self.relate("connect", "back", "front")
        self.add_dot("back-hub", BACK_C)
