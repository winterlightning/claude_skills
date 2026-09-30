"""dune-buggy (redraw of the new-pipeline traced SVG).

Plan: an open dune buggy facing right on HRECT_L (centerline box
(4,8)-(44,40)). Three parts, as in the generated image:
- two detached hollow wheels, r=6, centred (10,34) and (38,34); mirrored about
  x=24. Rear wheel is the left extreme (x=4), front wheel the right extreme
  (x=44), both wheel bottoms the bottom extreme (y=40).
- the roll cage and low chassis as one closed outline: a trapezoid cage
  (rear pillar (8,19)-(14,8), roof (14,8)-(26,8) = top extreme, front pillar
  (26,8)-(32,19)) standing on a chassis that runs at y=19 over each wheel and
  dips to a floor at y=24 between them. The dip is mirrored about x=24 like the
  wheels, so both wheel gaps match.
- a short raised nose bar leaving the front chassis corner (32,19) up to
  (36,16) and running flat to (42,16), sharing that corner (declared connect).
Every body point stays at least 14 from a wheel centre (>= 8 from the r6 tyre
on centerlines): chassis y=19 over the wheels (gap 9), dip corners (21,24) /
(27,24) at 14.87 (gap 8.87), the dip diagonals at 14.85 (gap 8.85).
Reference: Lucide car (hollow circle wheels detached from the body, straight
body runs); the image's thin curved rear kink is simplified to a straight
pillar.

Metric issues:
- clearance e0/e1 (body-front wheel 2.19) and e0/e2 (body-rear wheel 2.29):
  the chassis now rides above the wheels and dips only between them; both
  gaps are >= 8.85 on centerlines.
- hole at (7.8,28.8) (3.74) and (39.8,28.8) (4.12): wheels are r6 circles,
  an 8-unit inscribed opening at stroke 4.
- keyshape-short-axis (HRECT_M, y 65%): HRECT_M's 28-unit height cannot hold
  a 12-unit wheel, an 8-unit gap and a cage with an open interior, so the
  redraw uses HRECT_L (32 high) and reaches every extreme exactly: x 4/44 on
  the wheels, y 8 on the roof, y 40 on the wheel bottoms.
- stroke-width (trace 2.62): redrawn at stroke 4 with the 8-unit gaps above.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bb0b20be-48e9-58c8-a781-dea110e7df94"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1217-dune-buggy/dune-buggy_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                  # wheels and chassis dip mirror about x=24
WHEEL_R, WHEEL_Y = 6, 34   # bottom of the wheels is y=40
WHEEL_DX = 14              # wheel centres at x=10 and x=38
DECK_Y = 19                # chassis over the wheels (15 above the wheel centre)
FLOOR_Y = 24               # chassis floor between the wheels
FLOOR_HALF = 3             # floor runs x=21..27
DECK_INNER = 8             # deck meets the dip at x=16 / x=32
ROOF_Y = 8
ROOF = (14, 26)            # roof ends
CAGE_REAR_X = 8            # rear pillar foot
NOSE = ((36, 16), (42, 16))


class DuneBuggyRedraw(Solo48):
    icon_id = "dune-buggy-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("buggy", "beach buggy", "sand rail")
    keywords = ("dune buggy", "off-road", "offroad", "roll cage", "vehicle", "desert", "adventure", "atv")

    def build(self) -> None:
        r, y = WHEEL_R, WHEEL_Y
        for side, x in (("rear", AXIS - WHEEL_DX), ("front", AXIS + WHEEL_DX)):
            self.add_arc(f"{side}-upper", (x - r, y), (x + r, y), radius_x=r)
            self.add_arc(f"{side}-lower", (x + r, y), (x - r, y), radius_x=r)
            self.add_contour(f"{side}-wheel", f"{side}-upper", f"{side}-lower", closed=True)

        front_deck = (AXIS + DECK_INNER, DECK_Y)
        self.add_polyline(
            "body",
            (CAGE_REAR_X, DECK_Y),
            (ROOF[0], ROOF_Y),
            (ROOF[1], ROOF_Y),
            front_deck,
            (AXIS + FLOOR_HALF, FLOOR_Y),
            (AXIS - FLOOR_HALF, FLOOR_Y),
            (AXIS - DECK_INNER, DECK_Y),
            closed=True,
        )
        self.add_polyline("nose", front_deck, *NOSE)
        self.relate("connect", "body", "nose")
