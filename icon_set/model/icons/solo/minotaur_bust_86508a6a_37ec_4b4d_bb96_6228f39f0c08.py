"""A bull-headed minotaur with raised horns, pointed ears, long muzzle, and human shoulders. Eyes omitted to leave the face open.

Construction: Lucide user-round: broad, smooth shoulders under a distinct head.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86508a6a-37ec-4b4d-bb96-6228f39f0c08'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/minotaur_86508a6a-37ec-4b4d-bb96-6228f39f0c08.svg'


class MinotaurBust(Solo48):
    icon_id = 'minotaur-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('minotaur', 'bull', 'mythology', 'greek', 'horns', 'beast', 'labyrinth', 'legend')

    def build(self) -> None:
        self.add_line("brow", (14,14), (34,14))
        self.add_line("cheek-right", (34,14), (32,28))
        self.add_arc("jaw-right", (32,28), (26,34), radius_x=6)
        self.add_line("chin", (26,34), (22,34))
        self.add_arc("jaw-left", (22,34), (16,28), radius_x=6)
        self.add_line("cheek-left", (16,28), (14,14))
        self.add_contour("head", "brow", "cheek-right", "jaw-right", "chin", "jaw-left", "cheek-left", closed=True)
        self.add_arc("horn-left", (14,14), (6,2), radius_x=8, radius_y=12)
        self.add_arc("horn-right", (34,14), (42,2), radius_x=8, radius_y=12, sweep=False)
        self.add_polyline("ear-left", (14,14), (5,20))
        self.add_polyline("ear-right", (34,14), (43,20))
        self.add_arc("shoulder-left", (2,46), (12,39), radius_x=10, radius_y=7)
        self.add_line("neck-left", (12,39), (22,34))
        self.add_contour("bust-left", "shoulder-left", "neck-left")
        self.add_line("neck-right", (26,34), (36,39))
        self.add_arc("shoulder-right", (36,39), (46,46), radius_x=10, radius_y=7)
        self.add_contour("bust-right", "neck-right", "shoulder-right")
        self.add_line("muzzle", (22,26), (26,26))
        for part in ("horn-left", "horn-right", "ear-left", "ear-right", "bust-left", "bust-right"):
            self.relate("connect", "head", part)
        self.relate("connect", "horn-left", "ear-left")
        self.relate("connect", "horn-right", "ear-right")
