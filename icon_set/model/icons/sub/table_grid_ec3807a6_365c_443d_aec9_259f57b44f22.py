"""Table Grid: Two upright parallel lines cross two horizontal parallel lines to form an open grid. The strokes extend beyond their four intersections; no letters or outer rectangular border are visible.

Construction: Two vertical and two horizontal strokes form four intentional crossings.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ec3807a6-365c-443d-aec9-259f57b44f22'
SOURCE_PATH = 'pictographic-primitives/state/csv text_ec3807a6-365c-443d-aec9-259f57b44f22.svg'
AUTHOR = 'gpt-6'


class TableGrid(Sub32):
    icon_id = 'table-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('table', 'grid', 'upright', 'parallel', 'lines', 'cross', 'horizontal', 'form')

    def build(self):
        for x in (10,22):self.add_line(f'v-{x}',(x,2),(x,30))
        for y in (10,22):
            self.add_line(f'h-{y}',(2,y),(30,y))
            for x in (10,22):self.relate('connect',f'v-{x}',f'h-{y}')
