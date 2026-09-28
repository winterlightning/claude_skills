"""Japanese gyoza dumpling with a fan of pleats.

Symbol plan: five r5 pleat lobes fanned around a front dome, all lobe
nodes on r5 lattice offsets so adjacent lobes share integer notches:
centres (9,26) (15,18) (24,15) (33,18) (39,26), notches (12,30) (12,22)
(20,18) (28,18) (36,22) (36,30). The silhouette is the lobe chain plus
an r13 belly (bottom y=38); the front dome's top edge runs through the
notches (r18 arcs) so each pleat reads as its own crimped fold.
Mirror-symmetric about x=24.
Revision: the rejected drawing was a flat oval with a dome and three
spokes (read as a bun); the reference is a crescent with rounded pleats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "21395538-12e9-5de3-acef-658966ba5bd2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__japanese-gyoza-dumpling/20260927T153253Z-thuan-mac-1/reference/gyoza grill deep fried dumpling_21395538-12e9-5de3-acef-658966ba5bd2.svg"
AUTHOR = "claude-opus-5-5"

NOTCHES = ((12, 30), (12, 22), (20, 18), (28, 18), (36, 22), (36, 30))


class JapaneseGyozaDumpling(Solo48):
    icon_id = "japanese-gyoza-dumpling"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("gyoza", "potsticker", "dumpling")
    keywords = ("gyoza", "dumpling", "potsticker", "japanese", "fried", "food")

    def build(self) -> None:
        lobes = []
        for i in range(5):
            self.add_arc(f"pleat-{i}", NOTCHES[i], NOTCHES[i + 1], radius_x=5,
                         sweep=True, large_arc=True)
            lobes.append(f"pleat-{i}")
        self.add_arc("belly", NOTCHES[5], NOTCHES[0], radius_x=13, sweep=True)
        self.add_contour("outline", *lobes, "belly", closed=True)

        self.add_line("dome-left", NOTCHES[0], NOTCHES[1])
        for i in (1, 2, 3):
            self.add_arc(f"dome-{i}", NOTCHES[i], NOTCHES[i + 1], radius_x=18, sweep=True)
        self.add_line("dome-right", NOTCHES[4], NOTCHES[5])
        self.add_contour("dome", "dome-left", "dome-1", "dome-2", "dome-3", "dome-right")
        self.relate("connect", "outline", "dome")
