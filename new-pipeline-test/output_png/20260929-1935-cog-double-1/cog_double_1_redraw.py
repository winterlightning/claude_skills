"""cog-double-1 (redraw of the new-pipeline traced SVG).

Subject: two six-tooth cogs on the falling diagonal, upper left and lower right.

Plan
- SQUARE keyshape (metrics suggestion, fill 1.0 x 1.0): centerline box (6,6)-(42,42).
- One tooth definition repeated: six flat-topped teeth, tips at r11 (+-9 deg),
  valley corners at r7.5 (+-23 deg), each point rounded to the integer grid.
  Tapering keeps the two flanks of a tooth more than 30 deg apart, so the
  internal-spacing gate passes without making the teeth thin.
- Front cog: centre (17,17), teeth at 45 + 60k. Its tips reach x=6 and y=6.
- Back cog: centre (31,31), the same tooth turned 30 deg (teeth at 15 + 60k), so
  its notch sits opposite the front cog's diagonal tooth like meshing gears.
  Only the four teeth outside the front cog's 8-unit clearance zone are drawn
  (315, 15, 75, 135 deg); the run ends at the tooth roots, so it reads as
  a cog passing behind the front one. Its tips reach x=42 and y=42.
- The whole drawing is mirrored across the x = y diagonal.

Metric issues
- clearance e0/e1 and e2/e3 (cog outline vs its axle ring, 3.5 apart): fixed by
  dropping the separate axle rings. A ring needs r>=3.5 plus 8 to the valley,
  i.e. valleys at r>=11.5, and there is no room for that. The open centre of
  each cog now stands for the axle hole (inscribed well over 6).
- clearance e0/e2 (the two cogs 3.06 apart): fixed. The nearest distance
  between the cogs is now >= 8 on centerlines.
- hole x14 (1.4-3.2 wide slivers): fixed. The only enclosed hole is the front
  cog's centre.
- stroke-width (info): drawn at stroke 4.
- Not kept from the brief: "clear white gap between their facing teeth" with two
  complete, equal cogs. Two separate cogs that keep 8 units apart on the
  diagonal can only have tips at about r9. Every lattice version of that
  validated, but at 48 px the notches close under the 4-unit stroke and both
  cogs read as flowers. So the lower cog is shown partly hidden behind the upper one.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "82c1163c-aaf6-4c80-9120-18bf38090361"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1935-cog-double-1/cog-double-1_raw.svg"
AUTHOR = "claude-opus-5-5"

TIP_R, TIP_HALF = 11, 9          # tooth tip radius and half-angle (deg)
ROOT_R, ROOT_HALF = 7.5, 23      # valley corner radius and half-angle (deg)
FRONT_C, BACK_C = 17, 31         # centres on the x = y diagonal
FRONT_TEETH = (45, 105, 165, 225, 285, 345)
BACK_TEETH = (315, 15, 75, 135)  # the back cog's teeth that clear the front cog


def _tooth(c: int, angle: float) -> list[tuple[int, int]]:
    pts = []
    for off, r in ((-ROOT_HALF, ROOT_R), (-TIP_HALF, TIP_R), (TIP_HALF, TIP_R), (ROOT_HALF, ROOT_R)):
        t = math.radians(angle + off)
        pts.append((c + round(r * math.cos(t)), c + round(r * math.sin(t))))
    return pts


def _teeth(c: int, angles) -> list[tuple[int, int]]:
    pts: list[tuple[int, int]] = []
    for a in angles:
        for p in _tooth(c, a):
            if not pts or pts[-1] != p:
                pts.append(p)
    return pts


class CogDouble1Redraw(Solo48):
    icon_id = "cog-double-1-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("cogs", "gears", "double cog")
    keywords = ("cog", "gear", "settings", "mechanism", "machine", "preferences")

    def build(self) -> None:
        self.add_polyline("cog-front", *_teeth(FRONT_C, FRONT_TEETH), closed=True)
        self.add_polyline("cog-back", *_teeth(BACK_C, BACK_TEETH))
