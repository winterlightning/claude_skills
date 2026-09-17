"""Three-Column Table: A wide upright rectangle is divided by two full-height vertical lines into three equal columns. All three interiors remain blank, with no visibly selected or shaded column.

Construction: Three blank columns share a rectangular outline; no selection fill or extra cells are added.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '64eb4890-2023-4ac4-afc0-9cf653b75a72'
SOURCE_PATH = 'pictographic-primitives/state/column selected single 1_64eb4890-2023-4ac4-afc0-9cf653b75a72.svg'
AUTHOR = 'gpt-6'


class ThreeColumnTableState97(Sub32):
    icon_id = 'three-column-table-state-97'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('column', 'table', 'wide', 'upright', 'rectangle', 'divided', 'full', 'height')

    def build(self):
        self.add_polyline('outline',(2,6),(30,6),(30,26),(2,26),closed=True)
        for x in (11,21):
            self.add_line(f'divider-{x}',(x,6),(x,26))
            self.relate('connect','outline',f'divider-{x}')
