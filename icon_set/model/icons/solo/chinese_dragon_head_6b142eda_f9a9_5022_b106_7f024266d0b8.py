"""A frontal Chinese dragon mask with paired horns, brows, muzzle and trailing whiskers; dense mane detail omitted."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b142eda-f9a9-5022-b106-7f024266d0b8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/chinese dragon_6b142eda-f9a9-5022-b106-7f024266d0b8.svg'


class ChineseDragonHead(Solo48):
    icon_id = 'chinese-dragon-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('dragon', 'chinese', 'mythology', 'lunar new year', 'beast', 'mask', 'asian', 'legend')

    def build(self) -> None:
        # SQUARE: visible extremes (0, 0, 48, 48); centerlines inset 2.
        # Curved horns and cheek lobes retain the mask's organic silhouette.
        self.add_arc("horn-left-lower", (14,16), (8,8), radius_x=6, radius_y=8)
        self.add_arc("horn-left-tip", (8,8), (10,2), radius_x=10)
        self.add_contour("horn-left", "horn-left-lower", "horn-left-tip")
        self.add_arc("horn-right-lower", (34,16), (40,8), radius_x=6, radius_y=8, sweep=False)
        self.add_arc("horn-right-tip", (40,8), (38,2), radius_x=10, sweep=False)
        self.add_contour("horn-right", "horn-right-lower", "horn-right-tip")
        self.add_arc("brow", (14,16), (34,16), radius_x=18, radius_y=4)
        self.add_line("cheek-right-1", (34,16), (42,20))
        self.add_line("cheek-right-2", (42,20), (36,28))
        self.add_line("cheek-right-3", (36,28), (34,38))
        self.add_line("jaw-right", (34,38), (24,46))
        self.add_line("jaw-left", (24,46), (14,38))
        self.add_line("cheek-left-1", (14,38), (12,28))
        self.add_line("cheek-left-2", (12,28), (6,20))
        self.add_line("cheek-left-3", (6,20), (14,16))
        self.add_contour("face", "brow", "cheek-right-1", "cheek-right-2", "cheek-right-3", "jaw-right", "jaw-left", "cheek-left-1", "cheek-left-2", "cheek-left-3", closed=True)
        self.add_line("antler-left", (8,8), (2,6))
        self.add_line("antler-right", (40,8), (46,6))
        self.relate("connect", "horn-left", "antler-left")
        self.relate("connect", "horn-right", "antler-right")
        self.add_line("eye-left", (18,24), (20,26))
        self.add_line("eye-right", (30,24), (28,26))
        self.add_arc("muzzle-left", (14,38), (24,38), radius_x=5, radius_y=4)
        self.add_arc("muzzle-right", (24,38), (34,38), radius_x=5, radius_y=4)
        self.add_contour("muzzle", "muzzle-left", "muzzle-right")
        self.add_arc("whisker-left", (14,38), (2,32), radius_x=12, radius_y=6)
        self.add_arc("whisker-right", (34,38), (46,32), radius_x=12, radius_y=6, sweep=False)
        for part in ("horn-left", "horn-right", "muzzle", "whisker-left", "whisker-right"):
            self.relate("connect", "face", part)
        self.relate("connect", "muzzle", "whisker-left")
        self.relate("connect", "muzzle", "whisker-right")
