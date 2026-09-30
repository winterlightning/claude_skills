"""boat-propeller (redraw of the new-pipeline traced SVG).

Plan: a three-blade boat propeller on CIRCLE (centerline radius 20 about
(24,24)), seen head-on and swept clockwise.
- blade: one open stroke of three tangent-continuous cubics, authored once
  for the upright blade (relative to the centre) and repeated at 120 and 240
  degrees. The leading edge leaves the root, sweeps out to a tight tip on the
  upper left, the back edge arcs over the top (apex on radius 20 at about
  15 degrees) and sweeps back in to the trailing root. Knots are rounded to
  the integer grid after rotation (neighbouring controls shifted with them
  to keep the tangents), so the three copies differ by < 0.5.
- hub: a single dot at the centre; every blade root stays 8.6+ from it.
Traced shape: 20260929-1817-boat-propeller/boat-propeller_raw.svg (read for
the subject only; nothing copied from its coordinates).
Lucide: lucide/fan informed the construction (three swept blades repeated
about the centre with a dot hub); the blades here are open, hollow paddles
as in the generated image.

Metric issues:
- clearance e0/e1, e1/e2, e1/e3 (blades 1.8 from the hub ring): fixed, the
  hub is a dot and every blade stays 8.6+ from it on centerlines.
- clearance e0/e2, e0/e3, e2/e3 (neighbouring blades 4.5-5.4 apart): fixed,
  the blades are rebuilt with narrower roots so neighbours stay 9.8+ apart.
- hole at the hub (3.88 inscribed, need 6): fixed by drawing the hub as a
  dot. A ring with a 6-wide hole needs r5, which pushes the blade roots to
  radius 13 and leaves the blades only 7 deep on centerlines, too thin for
  a hollow paddle.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4b9f4301-4746-5105-a80a-44e05e91227c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1817-boat-propeller/"
    "boat-propeller_raw.svg"
)
AUTHOR = "claude-opus-5-5"

C = 24           # propeller centre (hub dot)
BLADES = 3       # repeated every 120 degrees, clockwise

# Upright blade relative to the centre (y down): start knot, then
# (control1, control2, knot) per cubic.
ROOT_LEAD = (-1, -9)
BLADE = (
    ((-2, -12), (-4.2, -14.3), (-6, -16)),       # leading edge sweeps out to the tip
    ((-8.2, -18), (-2, -20.6), (5, -19.2)),      # rounded tip over the top
    ((12.5, -17.6), (15, -9), (7, -6)),          # back edge sweeps in to the root
)


def _turn(p, k):
    a = math.radians(360 / BLADES * k)
    x, y = p
    return (C + x * math.cos(a) - y * math.sin(a), C + x * math.sin(a) + y * math.cos(a))


def _blade(k):
    """Blade k on the grid: knots rounded, each knot's neighbouring controls
    moved by the same offset so the tangents stay continuous."""
    knots = [ROOT_LEAD] + [seg[2] for seg in BLADE]
    exact = [_turn(p, k) for p in knots]
    grid = [(round(x), round(y)) for x, y in exact]
    shift = [(g[0] - e[0], g[1] - e[1]) for g, e in zip(grid, exact)]

    def moved(c, i):
        x, y = _turn(c, k)
        return (round(x + shift[i][0], 2), round(y + shift[i][1], 2))

    segs = [(moved(c1, i), moved(c2, i + 1), grid[i + 1])
            for i, (c1, c2, _) in enumerate(BLADE)]
    return grid[0], segs


class BoatPropellerRedraw(Solo48):
    icon_id = "boat-propeller-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation/marine"
    aliases = ("propeller", "ship-propeller", "screw-propeller")
    keywords = ("propeller", "boat", "ship", "marine", "screw", "blade", "engine", "fan")

    def build(self) -> None:
        for k in range(BLADES):
            start, segs = _blade(k)
            self.add_bezier(f"blade-{k + 1}", start, *segs)
        self.add_dot("hub", (C, C))
