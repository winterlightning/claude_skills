"""Broaden the tapered cup body, retaining the lid and straw.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (takeaway-cup-with-straw-container VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '13dcc618-4810-41aa-a6d9-2196457533c6'
SOURCE_PATH = 'pictographic-primitives/drinks/bubble tea_13dcc618-4810-41aa-a6d9-2196457533c6.svg'
AUTHOR = 'claude-opus-5-5'


class TakeawayCupWithStrawContainer(Container64):
    icon_id = 'takeaway-cup-with-straw-container'
    keyshape = Keyshape.VRECT_L
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # The cup tapers less (10..54 under the lid, 14..50 at the base; was 16..48), so it holds a symbol of 25
        # with a 4 px gap (was 23). Mirrored about x = 32.
        self.add_line('cup-1', (10, 20), (54, 20))
        self.add_line('cup-2', (54, 20), (50, 60))
        self.add_line('cup-3', (50, 60), (14, 60))
        self.add_line('cup-4', (14, 60), (10, 20))
        self.add_line('rim', (10, 12), (54, 12))
        self.add_line('straw', (32, 4), (32, 12))
        self.add_line('lid-6', (10, 12), (10, 20))
        self.add_line('lid-58', (54, 12), (54, 20))
        self.add_contour('cup', 'cup-1', 'cup-2', 'cup-3', 'cup-4', closed=True)
        self.relate('connect', 'rim', 'straw')
        self.relate('connect', 'lid-6', 'rim')
        self.relate('connect', 'lid-6', 'cup')
        self.relate('connect', 'lid-58', 'rim')
        self.relate('connect', 'lid-58', 'cup')
