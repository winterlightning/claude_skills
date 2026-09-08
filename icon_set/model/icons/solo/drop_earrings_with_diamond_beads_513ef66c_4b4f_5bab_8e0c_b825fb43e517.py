"""A matched pair of hooked earrings with large diamond drops; fine bead tiers omitted."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '513ef66c-4b4f-5bab-8e0c-b825fb43e517'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/accessories earrings oriental_513ef66c-4b4f-5bab-8e0c-b825fb43e517.svg'
AUTHOR = 'astra-chatgpt'


class DropEarringsWithDiamondBeads(Solo48):
    icon_id = 'drop-earrings-with-diamond-beads'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('earring', 'earrings', 'drop earring', 'jewellery', 'jewelry', 'diamond', 'bead', 'accessory', 'fashion')

    def build(self) -> None:
        # VRECT_XL: authored directly to its SOLO48 centerline extremes.
        self.add_arc('left-hook', (7, 8), (19, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('left-curl', (19, 8), (13, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('left-wire', (13, 14), (13, 26))
        self.add_contour('left-hanger', 'left-hook', 'left-curl', 'left-wire', closed=False)
        self.add_polyline('left-diamond', (13, 26), (21, 36), (13, 46), (5, 36), closed=True)
        self.relate("connect", 'left-hanger', 'left-diamond')
        self.add_arc('right-hook', (29, 8), (41, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-curl', (41, 8), (35, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('right-wire', (35, 14), (35, 26))
        self.add_contour('right-hanger', 'right-hook', 'right-curl', 'right-wire', closed=False)
        self.add_polyline('right-diamond', (35, 26), (43, 36), (35, 46), (27, 36), closed=True)
        self.relate("connect", 'right-hanger', 'right-diamond')
