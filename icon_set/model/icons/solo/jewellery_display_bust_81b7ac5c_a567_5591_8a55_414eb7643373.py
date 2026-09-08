"""An empty jewellery display bust with squared neck, sloping sides and flat base; omit seams.

Lucide construction: shirt: mirrored silhouette and rounded shoulder transitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81b7ac5c-a567-5591-8a55-414eb7643373'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/necklace stand_81b7ac5c-a567-5591-8a55-414eb7643373.svg'
AUTHOR = 'astra-chatgpt'


class JewelleryDisplayBust(Solo48):
    icon_id = 'jewellery-display-bust'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('display', 'bust', 'stand', 'mannequin', 'jewellery', 'jewelry', 'shop', 'retail', 'necklace')

    def build(self) -> None:
        # Exact keyshape envelope: (3, 0, 45, 48).
        self.add_line('neck-top', (17, 2), (31, 2))
        self.add_line('neck-r', (31, 2), (31, 6))
        self.add_arc('shoulder-r', (31, 6), (39, 14), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('corner-r', (39, 14), (43, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_line('side-r', (43, 18), (43, 24))
        self.add_arc('turn-r', (43, 24), (40, 30), radius_x=8, radius_y=8, sweep=True)
        self.add_line('taper-r', (40, 30), (32, 39))
        self.add_arc('foot-r', (32, 39), (29, 46), radius_x=10, radius_y=10, sweep=False)
        self.add_line('base', (29, 46), (19, 46))
        self.add_arc('foot-l', (19, 46), (16, 39), radius_x=10, radius_y=10, sweep=False)
        self.add_line('taper-l', (16, 39), (8, 30))
        self.add_arc('turn-l', (8, 30), (5, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_line('side-l', (5, 24), (5, 18))
        self.add_arc('corner-l', (5, 18), (9, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('shoulder-l', (9, 14), (17, 6), radius_x=8, radius_y=8, sweep=False)
        self.add_line('neck-l', (17, 6), (17, 2))
        self.add_contour('bust', 'neck-top', 'neck-r', 'shoulder-r', 'corner-r', 'side-r', 'turn-r', 'taper-r', 'foot-r', 'base', 'foot-l', 'taper-l', 'turn-l', 'side-l', 'corner-l', 'shoulder-l', 'neck-l', closed=True)
        self.add_line('base-left', (10, 46), (19, 46))
        self.add_line('base-right', (29, 46), (38, 46))
        self.relate("connect", 'base-left', 'bust')
        self.relate("connect", 'base-right', 'bust')
