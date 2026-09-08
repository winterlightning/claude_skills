"""A jewellery display bust with a square neck, sloped shoulders and a draped necklace."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1867e209-557c-5fbe-b481-8b8be3ca4b39'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/necklace stand_1867e209-557c-5fbe-b481-8b8be3ca4b39.svg'
AUTHOR = 'astra-chatgpt'


class NecklaceDisplayBust(Solo48):
    icon_id = 'necklace-display-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'display', 'bust', 'stand', 'mannequin', 'jewellery', 'jewelry', 'shop', 'retail')

    def build(self) -> None:
        # SQUARE: authored directly to its SOLO48 centerline extremes.
        self.add_line('neck-top', (17, 2), (31, 2))
        self.add_line('neck-r', (31, 2), (31, 8))
        self.add_arc('shoulder-r', (31, 8), (39, 16), radius_x=8, radius_y=8, sweep=False)
        self.add_line('shoulder-r-out', (39, 16), (42, 16))
        self.add_arc('corner-r', (42, 16), (46, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_line('side-r', (46, 20), (46, 29))
        self.add_line('taper-r', (46, 29), (34, 41))
        self.add_line('foot-r', (34, 41), (34, 46))
        self.add_line('base', (34, 46), (14, 46))
        self.add_line('foot-l', (14, 46), (14, 41))
        self.add_line('taper-l', (14, 41), (2, 29))
        self.add_line('side-l', (2, 29), (2, 20))
        self.add_arc('corner-l', (2, 20), (6, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line('shoulder-l-out', (6, 16), (9, 16))
        self.add_arc('shoulder-l', (9, 16), (17, 8), radius_x=8, radius_y=8, sweep=False)
        self.add_line('neck-l', (17, 8), (17, 2))
        self.add_contour('bust', 'neck-top', 'neck-r', 'shoulder-r', 'shoulder-r-out', 'corner-r', 'side-r', 'taper-r', 'foot-r', 'base', 'foot-l', 'taper-l', 'side-l', 'corner-l', 'shoulder-l-out', 'shoulder-l', 'neck-l', closed=True)
        self.add_arc('necklace', (9, 16), (39, 16), radius_x=15, radius_y=16, sweep=False)
        self.relate("connect", 'necklace', 'bust')
