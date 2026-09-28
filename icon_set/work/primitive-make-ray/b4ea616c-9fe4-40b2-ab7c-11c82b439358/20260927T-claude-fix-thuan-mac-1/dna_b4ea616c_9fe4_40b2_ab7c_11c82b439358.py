"""DNA: one twist of the double helix -- two strands crossing in the middle,
joined by a base-pair rung near each end, with the strand ends running on past
the rungs.

Revision (disapproved, reason not recorded): the rejected drawing closed the top
and bottom with the strands' ends meeting the rungs at the corners and pinching
the strands to a point in the middle, so it read as an hourglass. In the
original the two strands cross over each other and run on beyond the rungs.
The crossing and the free strand ends are restored.

Symbol plan: point symmetry about (24,24) and mirror symmetry about x=24. Strand
A: (8,4) straight down to (8,8), one S-cubic (8,8)-(40,40) with vertical end
tangents (split at its exact midpoint (24,24), the crossing), then (40,40) down
to (40,44). Strand B is A mirrored about x=24. Rungs (8,8)-(40,8) and
(8,40)-(40,40) join the strands where their straight ends begin.
Omissions: the middle rungs (a third rung would cut the crossing into triangles
below the hole minimum).
Lucide construction: 'dna' (crossing strands with rungs).
Keyshape VRECT_L: centerline (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b4ea616c-9fe4-40b2-ab7c-11c82b439358"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dna/20260926T182653Z-thuan-mac-1/reference/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.svg"
AUTHOR = "claude-opus-5-5"

# Full S-cubic (8,8) (8,17) (40,31) (40,40), split at t=0.5 by de Casteljau.
FIRST_HALF = ((8, 12.5), (16, 17.25), (24, 24))
SECOND_HALF = ((32, 30.75), (40, 35.5), (40, 40))


def mirror(p):
    return (48 - p[0], p[1])


class Dna(Solo48):
    icon_id = "dna"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ("double-helix", "genetics")
    keywords = ("dna", "helix", "gene", "genetics", "biology", "science", "strand")

    def strand(self, name, m):
        self.add_line(f"{name}-top", m((8, 4)), m((8, 8)))
        self.add_bezier(f"{name}-upper", m((8, 8)), tuple(m(p) for p in FIRST_HALF))
        self.add_bezier(f"{name}-lower", m((24, 24)), tuple(m(p) for p in SECOND_HALF))
        self.add_line(f"{name}-bottom", m((40, 40)), m((40, 44)))
        self.add_contour(name, f"{name}-top", f"{name}-upper", f"{name}-lower", f"{name}-bottom")

    def build(self) -> None:
        self.strand("strand-a", lambda p: p)
        self.strand("strand-b", mirror)
        self.relate("connect", "strand-a", "strand-b")
        self.add_line("rung-top", (8, 8), (40, 8))
        self.add_line("rung-bottom", (8, 40), (40, 40))
        for rung in ("rung-top", "rung-bottom"):
            self.relate("connect", rung, "strand-a")
            self.relate("connect", rung, "strand-b")
