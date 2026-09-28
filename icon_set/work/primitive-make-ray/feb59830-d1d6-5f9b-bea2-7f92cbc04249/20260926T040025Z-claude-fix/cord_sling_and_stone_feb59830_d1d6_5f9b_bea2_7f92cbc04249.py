"""An antique cord sling with its stone: a grip, two cords meeting at a teardrop pouch,
a loose tail, and the stone lying beside it.

Symbol plan: the grip is a short straight stroke at the top-left. One cord drops from the
grip's foot in a smooth curve to the junction J, where it turns up the long diagonal to
the pouch point P; the loose tail continues that diagonal beyond J to the lower-left. The
second cord leaves the grip's top, runs right and bends down into P. The pouch is a
teardrop from P: its upper edge climbs to the crest (y=6) and rounds over the far end
(x=42), its lower edge returns nearly level into P. The stone is an r4 circle bottom-right.
Lucide construction: no sling glyph; cubic cords and a teardrop loop as in 'lasso', and
a plain circle for the stone.
Keyshape SQUARE: centerline x 6..42 (grip, pouch end), y 6..42 (grip top and pouch crest, stone).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "feb59830-d1d6-5f9b-bea2-7f92cbc04249"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cord-sling-and-stone/20260926T035939Z-thuan-mac/reference/antique sling_feb59830-d1d6-5f9b-bea2-7f92cbc04249.svg"
AUTHOR = "claude-opus-5-5"


class CordSlingAndStone(Solo48):
    icon_id = "cord-sling-and-stone"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weapons/antique"
    aliases = ("antique-sling", "sling", "slingshot-cord")
    keywords = ("sling", "stone", "cord", "antique", "weapon", "david", "throw", "shepherd", "ancient")

    def build(self) -> None:
        G0, G1, J, P = (6, 6), (6, 13), (13, 32), (22, 20)
        self.add_line("grip", G0, G1)
        self.add_bezier("cord-drop", G1, ((6, 22), (9, 28), J))
        self.add_line("cord-rise", J, P)
        self.add_line("tail", J, (7, 40))
        self.add_bezier("cord-top", G0, ((13, 6), (19, 13), P))
        self.add_bezier("pouch", P, ((24, 15), (28, 6), (34, 6)),
                        ((39, 6), (42, 9), (42, 12)),
                        ((42, 17), (38, 20), (32, 21)),
                        ((28, 21.5), (24.5, 21), P))
        for a, b in (("grip", "cord-drop"), ("grip", "cord-top"), ("cord-drop", "cord-rise"),
                     ("cord-drop", "tail"), ("cord-rise", "tail"), ("cord-rise", "pouch"),
                     ("cord-top", "pouch"), ("cord-rise", "cord-top")):
            self.relate("connect", a, b)
        self.add_arc("stone-top", (32, 38), (40, 38), radius_x=4, sweep=True)
        self.add_arc("stone-bottom", (40, 38), (32, 38), radius_x=4, sweep=True)
        self.add_contour("stone", "stone-top", "stone-bottom", closed=True)
