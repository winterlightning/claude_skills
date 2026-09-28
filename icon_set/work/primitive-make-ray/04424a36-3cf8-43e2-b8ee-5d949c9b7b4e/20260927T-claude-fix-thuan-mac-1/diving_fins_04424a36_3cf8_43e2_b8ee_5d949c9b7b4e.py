"""Diving fins: a pair of swim fins laid side by side, heel to toe -- each a long
paddle that widens from a rounded foot pocket to a broad, square-cornered blade.

Revision (disapproved, reason not recorded): the rejected drawing made each fin a
straight box split by a crossbar, with a trapezoid cap, so they read as two
pencils or markers; the original's fins taper smoothly from a rounded heel to a
wide blade and lie head-to-toe. The tapered, rounded paddle silhouette and the
head-to-toe arrangement are restored.

Symbol plan: point symmetry about (24,24): the right fin is the left fin turned
half a turn. Left fin: rounded heel at the top, a radius-5 arc about (13,11)
(top 6); walls taper out from (8,11)/(18,11) to (6,38)/(20,38); radius-4 blade
corners to the blade edge y=42. Right fin: the same shape turned 180 degrees
about (24,24) (heel at the bottom, blade at the top). The fins' facing walls stay
10 apart.
Omissions: the foot-pocket slot and the blade rib (a line inside a 10-14 wide fin
cannot keep 8 from both walls).
Lucide construction: rounded-rectangle corners; no fin glyph in Lucide.
Keyshape SQUARE: centerline (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "04424a36-3cf8-43e2-b8ee-5d949c9b7b4e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diving-fins/20260926T182653Z-thuan-mac-1/reference/diving fins_04424a36-3cf8-43e2-b8ee-5d949c9b7b4e.svg"
AUTHOR = "claude-opus-5-5"


def turn(p):
    return (48 - p[0], 48 - p[1])


class DivingFins(Solo48):
    icon_id = "diving-fins"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/diving"
    aliases = ("swim-fins", "flippers")
    keywords = ("diving", "fins", "flippers", "swim", "snorkel", "scuba", "water", "sport")

    def fin(self, name, pt):
        self.add_arc(f"{name}-heel", pt((8, 11)), pt((18, 11)), radius_x=5)
        self.add_line(f"{name}-right", pt((18, 11)), pt((20, 38)))
        self.add_arc(f"{name}-corner-r", pt((20, 38)), pt((16, 42)), radius_x=4)
        self.add_line(f"{name}-blade", pt((16, 42)), pt((10, 42)))
        self.add_arc(f"{name}-corner-l", pt((10, 42)), pt((6, 38)), radius_x=4)
        self.add_line(f"{name}-left", pt((6, 38)), pt((8, 11)))
        self.add_contour(name, f"{name}-heel", f"{name}-right", f"{name}-corner-r", f"{name}-blade",
                         f"{name}-corner-l", f"{name}-left", closed=True)

    def build(self) -> None:
        self.fin("fin-left", lambda p: p)
        self.fin("fin-right", turn)
