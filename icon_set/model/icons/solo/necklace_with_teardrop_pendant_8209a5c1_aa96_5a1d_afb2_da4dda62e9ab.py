"""A U-shaped necklace with a point-up teardrop pendant; omit links and tiny clasp.

Lucide construction: no useful exact match; mirrored chain quadrants and rounded drop.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8209a5c1-aa96-5a1d-afb2-da4dda62e9ab'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/necklace jewel_8209a5c1-aa96-5a1d-afb2-da4dda62e9ab.svg'
AUTHOR = 'astra-chatgpt'


class NecklaceWithTeardropPendant(Solo48):
    icon_id = 'necklace-with-teardrop-pendant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('necklace', 'pendant', 'teardrop', 'jewel', 'chain', 'jewellery', 'jewelry', 'accessory')

    def build(self) -> None:
        # Exact keyshape envelope: (3, 0, 45, 48).
        self.add_arc('chain-left', (5, 2), (24, 27), radius_x=19, radius_y=25, sweep=False)
        self.add_arc('chain-right', (24, 27), (43, 2), radius_x=19, radius_y=25, sweep=False)
        self.add_contour('chain', 'chain-left', 'chain-right', closed=False)
        self.add_line('drop-left', (24, 34), (19, 39))
        self.add_arc('drop-bottom', (19, 39), (29, 39), radius_x=5, radius_y=7, sweep=False)
        self.add_line('drop-right', (29, 39), (24, 34))
        self.add_contour('pendant', 'drop-left', 'drop-bottom', 'drop-right', closed=True)
