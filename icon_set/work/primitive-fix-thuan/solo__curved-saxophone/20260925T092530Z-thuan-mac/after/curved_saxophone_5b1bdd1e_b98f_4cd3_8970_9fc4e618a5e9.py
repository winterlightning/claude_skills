"""Saxophone: a mouthpiece neck hooking over the top of the body tube, the
tube running down into a U-bend and rising again as a bell that flares out to
the right, with key tabs on the inner wall.

Symbol plan: one closed outline - neck line, radius-6 neck bend, inner wall,
radius-4 inner U, bell wall, flare diagonals, radius-14 outer U, outer wall
(which meets the neck line at a split node). Two key tabs leave split nodes
on the inner wall and stop 8 from the outer wall. Parallel walls sit exactly
8 apart. Deliberately asymmetric like the instrument.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: no saxophone; the J-tube with a bell flare follows
Lucide's trumpet/horn bell construction (straight flare diagonals off a
tube wall).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__curved-saxophone/20260925T092530Z-thuan-mac/reference/instrument saxophone_5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9.svg"
AUTHOR = "claude-opus-5-5"


class CurvedSaxophone(Solo48):
    icon_id = "curved-saxophone"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ("saxophone", "sax")
    keywords = ("saxophone", "sax", "instrument", "music", "jazz")

    def build(self) -> None:
        outer, inner, bell, bell_right = 10, 22, 30, 38
        bend_y = 28          # centre height of both U-bends
        keys = (20, 28)
        self.add_line("sax-1", (6, 6), (outer, 6))                          # mouthpiece
        self.add_line("sax-2", (outer, 6), (16, 6))
        self.add_arc("sax-3", (16, 6), (inner, 12), radius_x=6)             # neck bend
        self.add_line("sax-4", (inner, 12), (inner, keys[0]))
        self.add_line("sax-5", (inner, keys[0]), (inner, keys[1]))
        self.add_arc("sax-6", (inner, bend_y), (bell, bend_y), radius_x=4, sweep=False)
        self.add_line("sax-7", (bell, bend_y), (bell, 12))                  # bell wall
        self.add_line("sax-8", (bell, 12), (42, 24))                        # flare
        self.add_line("sax-9", (42, 24), (bell_right, bend_y))
        self.add_arc("sax-10", (bell_right, bend_y), (outer, bend_y), radius_x=14)
        self.add_line("sax-11", (outer, bend_y), (outer, 6))
        self.add_contour("sax", *[f"sax-{i}" for i in range(2, 12)], closed=True)
        self.add_contour("mouthpiece", "sax-1")
        self.relate("connect", "mouthpiece", "sax")
        for index, y in enumerate(keys, 1):
            self.add_line(f"key-{index}", (inner, y), (inner - 4, y))
            self.relate("connect", "sax", f"key-{index}")
