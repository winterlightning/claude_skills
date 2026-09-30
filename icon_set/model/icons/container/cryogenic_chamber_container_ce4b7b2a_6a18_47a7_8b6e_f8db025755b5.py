"""An empty upright chamber bounded by two straight sides and rounded horizontal caps at top and bottom. Exclude the human figure.

Plan: Two equal rounded cap rails share their side attachment coordinates with the upright walls. Bounds (6,2)-(58,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide briefcase-business: shared attachment points and equal rounded corners.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (cryogenic-chamber-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'ce4b7b2a-6a18-47a7-8b6e-f8db025755b5'
SOURCE_ICON_IDS = ('ce4b7b2a-6a18-47a7-8b6e-f8db025755b5',)
SOURCE_PATH = 'pictographic-primitives/science/human tube_ce4b7b2a-6a18-47a7-8b6e-f8db025755b5.svg'
AUTHOR = 'claude-opus-5-5'


class CryogenicChamberContainer(Container64):
    icon_id = 'cryogenic-chamber-container'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('cryogenic', 'chamber', 'container')

    def build(self) -> None:
        self.add_line('top-cap-0', (14, 4), (50, 4))
        self.add_arc('top-cap-1', (50, 4), (54, 8), radius_x=4)
        self.add_dot('top-cap-2', (54, 8))
        self.add_arc('top-cap-3', (54, 8), (50, 12), radius_x=4)
        self.add_line('top-cap-4', (50, 12), (14, 12))
        self.add_arc('top-cap-5', (14, 12), (10, 8), radius_x=4)
        self.add_dot('top-cap-6', (10, 8))
        self.add_arc('top-cap-7', (10, 8), (14, 4), radius_x=4)
        self.add_line('bottom-cap-0', (14, 52), (50, 52))
        self.add_arc('bottom-cap-1', (50, 52), (54, 56), radius_x=4)
        self.add_dot('bottom-cap-2', (54, 56))
        self.add_arc('bottom-cap-3', (54, 56), (50, 60), radius_x=4)
        self.add_line('bottom-cap-4', (50, 60), (14, 60))
        self.add_arc('bottom-cap-5', (14, 60), (10, 56), radius_x=4)
        self.add_dot('bottom-cap-6', (10, 56))
        self.add_arc('bottom-cap-7', (10, 56), (14, 52), radius_x=4)
        self.add_line('wall-12', (16, 12), (16, 52))
        self.add_line('wall-52', (48, 12), (48, 52))
        self.add_contour('top-cap', 'top-cap-0', 'top-cap-1', 'top-cap-2', 'top-cap-3', 'top-cap-4', 'top-cap-5', 'top-cap-6', 'top-cap-7', closed=True)
        self.add_contour('bottom-cap', 'bottom-cap-0', 'bottom-cap-1', 'bottom-cap-2', 'bottom-cap-3', 'bottom-cap-4', 'bottom-cap-5', 'bottom-cap-6', 'bottom-cap-7', closed=True)
        self.relate('connect', 'wall-12', 'top-cap')
        self.relate('connect', 'wall-12', 'bottom-cap')
        self.relate('connect', 'wall-52', 'top-cap')
        self.relate('connect', 'wall-52', 'bottom-cap')
