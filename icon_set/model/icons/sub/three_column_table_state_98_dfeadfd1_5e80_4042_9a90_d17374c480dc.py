"""Three-Column Table: Two evenly spaced vertical dividers split a rectangular outline into three matching blank panels. The top and bottom edges run continuously across the full width of the table.

Construction: Three blank columns share a rectangular outline; no selection fill or extra cells are added.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dfeadfd1-5e80-4042-9a90-d17374c480dc'
SOURCE_PATH = 'pictographic-primitives/state/column selected single 1_dfeadfd1-5e80-4042-9a90-d17374c480dc.svg'
AUTHOR = 'gpt-6'


class ThreeColumnTableState98(Sub32):
    icon_id = 'three-column-table-state-98'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('column', 'table', 'evenly', 'spaced', 'vertical', 'dividers', 'split', 'rectangular')

    def build(self):
        self.add_polyline('outline',(2,6),(30,6),(30,26),(2,26),closed=True)
        for x in (11,21):
            self.add_line(f'divider-{x}',(x,6),(x,26))
            self.relate('connect','outline',f'divider-{x}')
