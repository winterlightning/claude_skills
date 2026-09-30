"""horse-pulling-small-carriage (redraw of the new-pipeline traced SVG).

Plan: a side-profile horse walking left, joined by one straight shaft to a
small open carriage riding on a single wheel, on HRECT_M (centerline box
(4,10)-(44,38), ink (2,8)-(46,40)).
- Horse: one open outline contour from the front hoof (7,38) up the chest
  and neck front to the throat notch (8,17), a short jaw to the muzzle (the
  left extreme x=4), the face up to the pointed ear (the top extreme y=10),
  one arched crest cubic that lands level on the back (y=17), a
  quarter-circle rump (r=4) into the vertical thigh and a hind leg to its
  hoof (24,38). A straight belly at y=30 joins the front knee and the hock
  at shared nodes (back to belly is 13 on centerlines).
- Shaft: horizontal at y=21 from the rump node (25,21) to the carriage's
  left wall, exactly 8 long, so the horse stays 8 from the carriage and the
  shaft stays 8 from the wheel.
- Carriage: a 10-wide bowl (walls x=33 and x=43, flat rim y=18) whose walls
  round into the wheel at its 3-4-5 points (34,30) and (42,30), and a back
  post leaning out from the right rim corner to (44,12), the right extreme.
- Wheel: r=5 about (38,33), bottom on y=38, split at the two wall nodes.
Dropped: the far-side (inner) front and hind legs and the ear notch. Four
legs need 8 between hooves and would push the horse into the carriage; two
splayed legs read as a walking horse at 48 px.

Metric issues:
- clearance e0/e2, e1/e4, e1/e5, e2/e5 (errors): fixed. The inner-leg/belly
  stroke (e5) that crossed the outer legs is replaced by one belly line
  sharing nodes with the legs; the shaft (e2) and carriage (e4) meet the
  horse, bowl and wheel only at declared shared nodes, and every other pair
  keeps 8 on centerlines (re-running svg_metrics on the redraw: 0 issues).
- hole [12.5,23.7] 2.0 wide (error): fixed; the horse body is 13 tall and
  the neck 8+ wide, so no pinched pocket remains (body hole 9.4 inscribed).
- hole [37.9,29.6] 3.0 wide (error): fixed; the bowl pocket is 10x10 on
  centerlines (6.0 inscribed) and the wheel is r=5 (5.9 inscribed).
- keyshape-short-axis (warn, y fill 65%): fixed; the ear sits on y=10 and
  the hooves and wheel on y=38, filling HRECT_M exactly on both axes.
- stroke-width (info, trace 2.62): redrawn at stroke 4.
No useful Lucide match: Lucide has no horse or carriage; the wheel follows
Lucide's plain round-wheel construction (no spokes).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "589093c2-50d1-4d6e-b46e-2aef2795cea3"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1529-horse-pulling-small-carriage/"
    "horse-pulling-small-carriage_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Shared nodes.
KNEE = (11, 30)       # front leg top, belly start
HOCK = (25, 30)       # hind leg joint, belly end
RUMP = (25, 21)       # rump end, hind leg top, shaft start
BACK_Y = 17
WALL_L = 33           # carriage left wall x; shaft ends on it
WALL_R = 43
RIM_Y = 18
WHEEL_C = (38, 33)
WHEEL_R = 5
WHEEL_L = (34, 30)    # WHEEL_C + (-4, -3)
WHEEL_R_PT = (42, 30)  # WHEEL_C + (4, -3)


class HorsePullingSmallCarriageRedraw(Solo48):
    icon_id = "horse-pulling-small-carriage-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("horse-carriage", "horse-cart", "buggy")
    keywords = ("horse", "carriage", "cart", "buggy", "wagon", "pulling",
                "transport", "coach", "animal", "wheel")

    def build(self) -> None:
        # Horse outline: front hoof -> chest -> head -> crest -> rump -> hind hoof.
        self.add_line("horse-foreleg", (7, 38), KNEE)
        self.add_bezier("horse-chest", KNEE, ((10, 25), (8, 20), (8, 17)))
        self.add_line("horse-jaw", (8, 17), (4, 18))
        self.add_line("horse-face", (4, 18), (9, 10))
        self.add_bezier("horse-crest", (9, 10),
                        ((15, 10), (15, BACK_Y), (19, BACK_Y)))
        self.add_line("horse-back", (19, BACK_Y), (21, BACK_Y))
        self.add_arc("horse-rump", (21, BACK_Y), RUMP, radius_x=4)
        self.add_line("horse-thigh", RUMP, HOCK)
        self.add_line("horse-hindleg", HOCK, (24, 38))
        self.add_contour("horse", "horse-foreleg", "horse-chest", "horse-jaw",
                         "horse-face", "horse-crest", "horse-back", "horse-rump",
                         "horse-thigh", "horse-hindleg")
        self.add_line("horse-belly", KNEE, HOCK)

        # Shaft from rump to carriage wall.
        wall = (WALL_L, RUMP[1])
        self.add_line("shaft", RUMP, wall)

        # Carriage bowl: straight walls that round into the wheel, flat rim,
        # and a back post leaning out from the right rim corner.
        self.add_bezier("carriage-wall-left-foot", WHEEL_L,
                        ((33.2, 28.4), (WALL_L, 26.6), (WALL_L, 25)))
        self.add_line("carriage-wall-left", (WALL_L, 25), wall)
        self.add_line("carriage-wall-left-top", wall, (WALL_L, RIM_Y))
        self.add_line("carriage-rim", (WALL_L, RIM_Y), (WALL_R, RIM_Y))
        self.add_line("carriage-wall-right", (WALL_R, RIM_Y), (WALL_R, 25))
        self.add_bezier("carriage-wall-right-foot", (WALL_R, 25),
                        ((WALL_R, 26.6), (42.8, 28.4), WHEEL_R_PT))
        self.add_contour("carriage-bowl", "carriage-wall-left-foot",
                         "carriage-wall-left", "carriage-wall-left-top",
                         "carriage-rim", "carriage-wall-right",
                         "carriage-wall-right-foot")
        self.add_line("carriage-post", (WALL_R, RIM_Y), (44, 12))

        # Wheel split at the two wall nodes.
        self.add_arc("wheel-top", WHEEL_L, WHEEL_R_PT, radius_x=WHEEL_R)
        self.add_arc("wheel-bottom", WHEEL_R_PT, WHEEL_L, radius_x=WHEEL_R,
                     large_arc=True)
        self.add_contour("wheel", "wheel-top", "wheel-bottom", closed=True)

        self.relate("connect", "horse", "horse-belly")
        self.relate("connect", "horse", "shaft")
        self.relate("connect", "shaft", "carriage-bowl")
        self.relate("connect", "carriage-bowl", "carriage-post")
        self.relate("connect", "carriage-bowl", "wheel")
