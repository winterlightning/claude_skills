"""bird-egg-nest (redraw of the new-pipeline traced SVG).

Plan: two upright eggs resting above a shallow U-shaped nest, with two twig
strokes running under the nest's lower edge. HRECT_L, centerline box
(4,8)-(44,40): egg tops on y=8, nest rim ends on x=4 / x=44, twig bottoms on
y=40. The whole icon is mirrored about x=24.
- eggs: one egg definition repeated at x=14 and x=34 (10 wide, 14 tall):
  lower half a circle r5, upper half two elliptical quarters rx5 ry9, all
  meeting with vertical tangents at the equator y=17. Width 10 leaves a
  6-unit inscribed hole; the equators are 10 apart (8 needed on curves).
- nest: one contour, arc r20 about (16,11) from the rim end (4,27) to the
  bottom (16,31), a flat floor to (32,31), and the mirrored arc about
  (32,11) up to (44,27). Tangent-continuous at both floor ends. The arc
  centre sits 6.3 from each egg centre, so the nest stays 8.7 clear of the
  egg's lower half.
- twigs: two short cubics following the nest's arc 9 lower (a radius-29
  offset), ending flat on y=40 and 10 apart at the centre.

Metric issues (bird-egg-nest_metrics.json):
- clearance e0/e1 (eggs 2.94 apart): fixed, egg equators 10 apart.
- clearance e0/e2, e1/e2 (eggs crossing the nest): fixed, nest >= 8.7 from eggs.
- clearance e0/e3, e1/e4 (eggs near twigs): fixed, twigs sit under the nest.
- clearance e2/e3, e2/e4 (twigs on the nest): fixed, twigs offset >= 8.4.
- hole at (23.8, 29.6), 4.32 wide: fixed, eggs and nest no longer cross, so
  the sliver between them is gone; each egg keeps a 6-unit hole.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (HRECT_M fills 85% of y): switched to HRECT_L. At
  stroke 4 the stacked egg / nest / twig bands need 32 units of height
  (14 egg + 9 to the nest floor + 9 to the twigs), which HRECT_M's 28 cannot
  hold; HRECT_L's box is filled exactly on all four sides.
No useful Lucide match (Lucide `egg` only informs the round-bottom,
narrower-top egg outline).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "24877473-aa74-4eb9-a2ef-3b61dec1c3f5"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1711-bird-egg-nest/"
    "bird-egg-nest_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
EGG_DX = 10              # egg centre offset from the axis
EGG_EQ = 17              # egg equator (widest line)
EGG_R = 5                # half width and lower radius
EGG_TOP = 8              # upper radius_y = EGG_EQ - EGG_TOP
NEST_CX = 8              # nest arc centre offset from the axis
NEST_CY = 11
NEST_R = 20
NEST_RIM = (4, 27)       # left rim end on the arc (12, 16, 20 triple)
FLOOR_Y = NEST_CY + NEST_R
TWIG_START = (6, 38)
TWIG_END = (19, 40)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class BirdEggNestRedraw(Solo48):
    icon_id = "bird-egg-nest-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ("bird nest", "nest with eggs", "eggs in nest")
    keywords = ("bird", "egg", "eggs", "nest", "nature", "spring", "hatch", "birdwatching")

    def egg(self, name: str, cx: int) -> None:
        left, right = (cx - EGG_R, EGG_EQ), (cx + EGG_R, EGG_EQ)
        top = (cx, EGG_TOP)
        ry = EGG_EQ - EGG_TOP
        self.add_arc(f"{name}-bottom", left, right, radius_x=EGG_R, sweep=False)
        self.add_arc(f"{name}-upper-right", right, top, radius_x=EGG_R, radius_y=ry, sweep=False)
        self.add_arc(f"{name}-upper-left", top, left, radius_x=EGG_R, radius_y=ry, sweep=False)
        self.add_contour(name, f"{name}-bottom", f"{name}-upper-right", f"{name}-upper-left", closed=True)

    def build(self) -> None:
        self.egg("egg-left", AXIS - EGG_DX)
        self.egg("egg-right", AXIS + EGG_DX)

        floor_l, floor_r = (AXIS - NEST_CX, FLOOR_Y), (AXIS + NEST_CX, FLOOR_Y)
        self.add_arc("nest-left", NEST_RIM, floor_l, radius_x=NEST_R, sweep=False)
        self.add_line("nest-floor", floor_l, floor_r)
        self.add_arc("nest-right", floor_r, mirror(NEST_RIM), radius_x=NEST_R, sweep=False)
        self.add_contour("nest", "nest-left", "nest-floor", "nest-right")

        # Twig: rises gently from the flat end, following the nest arc offset.
        sx, sy = TWIG_START
        ex, ey = TWIG_END
        self.add_bezier("twig-left", TWIG_START, ((sx + 3.5, sy + 1.4), (ex - 5, ey), TWIG_END))
        self.add_bezier(
            "twig-right", mirror(TWIG_END),
            (mirror((ex - 5, ey)), mirror((sx + 3.5, sy + 1.4)), mirror(TWIG_START)),
        )
