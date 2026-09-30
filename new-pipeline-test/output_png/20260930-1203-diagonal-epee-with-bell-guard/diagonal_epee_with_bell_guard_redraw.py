"""diagonal-epee-with-bell-guard (redraw of the new-pipeline traced SVG).

Plan: a fencing epee laid on the 45-degree anti-diagonal x + y = 48, tip at
the upper right, on SQUARE (centerline box (6,6)-(42,42)). Three parts
sharing one axis:
- guard: a closed semicircular bell about C=(15,33). Its flat side is the
  diameter (7,25)-(23,41), perpendicular to the blade and split at C where
  the grip meets it. The convex side faces the tip and is two quarter-circle
  cubics (radius 8*sqrt(2), controls from the circle constant) meeting at
  the apex (23,25), the point on the axis where the blade starts.
- blade: one straight line from the apex (23,25) to the tip (42,6),
  radial to the bell so it leaves the dome square-on.
- grip: one straight line from C (15,33) out behind the guard to the
  pommel end (6,42).
Extremes: grip end sets left x=6 and bottom y=42, blade tip sets right
x=42 and top y=6; the bell stays inside (x 7..26.3, y 21.7..41).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8.
- keyshape-short-axis (warn, y filled 86%): fixed. The whole weapon lies
  on the true 45-degree diagonal of the box, so x and y both span 6..42.
- clearance e1/e2 (error, blade and grip 5.63 apart): fixed. The blade now
  starts on the dome apex and the grip on the diameter centre, so the two
  loose ends are a full radius (11.3) apart and each is joined to the guard
  (declared connect) instead of floating near the other.
- hole at [14.0, 33.3] (error, 1.56 wide): fixed. The trace crossed the
  grip through the bell and pinched a sliver; the bell is now a clean
  radius-11.3 half disc whose interior is about 7.3 inscribed, and the grip
  stays outside it.
Lucide construction: `swords` / `sword` informed the single-line 45-degree
blade with round caps; Lucide has no epee, the bell guard is a plain
half-circle on the blade axis.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8a647e0e-f452-4aea-8ac1-7d82ccfdd824"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1203-diagonal-epee-with-bell-guard/"
    "diagonal-epee-with-bell-guard_raw.svg"
)
AUTHOR = "claude-opus-5-5"

CX, CY = 15, 33            # bell centre, on the axis x + y = 48
H = 8                      # half-diameter offset along (1,1) and (1,-1)
R = H * math.sqrt(2)       # bell radius
GUARD_A = (CX - H, CY - H)   # (7,25)  diameter end, upper left
GUARD_B = (CX + H, CY + H)   # (23,41) diameter end, lower right
APEX = (CX + H, CY - H)      # (23,25) dome apex, blade root
TIP = (42, 6)
POMMEL = (6, 42)
K = 4 / 3 * math.tan(math.pi / 8)   # quarter-circle cubic constant


def _quarter(start, end):
    """Cubic control points for a 90-degree arc about (CX, CY)."""
    sx, sy = start[0] - CX, start[1] - CY
    ex, ey = end[0] - CX, end[1] - CY
    # tangents: start rotated towards end, end rotated back towards start
    c1 = (start[0] + K * ex, start[1] + K * ey)
    c2 = (end[0] + K * sx, end[1] + K * sy)
    return c1, c2, end


class DiagonalEpeeWithBellGuardRedraw(Solo48):
    icon_id = "diagonal-epee-with-bell-guard-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sport"
    aliases = ("epee", "fencing sword", "foil", "fencing")
    keywords = ("epee", "fencing", "sword", "bell guard", "blade", "sport",
                "duel", "weapon", "olympics")

    def build(self) -> None:
        # bell guard: diameter split at the grip, then the dome over the apex
        self.add_line("guard-flat-upper", GUARD_A, (CX, CY))
        self.add_line("guard-flat-lower", (CX, CY), GUARD_B)
        self.add_bezier("guard-dome-lower", GUARD_B, _quarter(GUARD_B, APEX))
        self.add_bezier("guard-dome-upper", APEX, _quarter(APEX, GUARD_A))
        self.add_contour("guard", "guard-flat-upper", "guard-flat-lower",
                         "guard-dome-lower", "guard-dome-upper", closed=True)

        self.add_line("blade", APEX, TIP)
        self.relate("connect", "blade", "guard")

        self.add_line("grip", (CX, CY), POMMEL)
        self.relate("connect", "grip", "guard")
