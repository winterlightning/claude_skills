"""Right Pointing Dashed Arrow on SYMBOL32.

Plan: Two equal detached dashes precede a short shaft joined to a mirrored head. Lucide move-right informs the long horizontal axis.
Centerline extremes use the HRECT_L contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'd801c28f-04d2-45ff-8e4f-3e9bea4892a3'
SOURCE_PATH = 'published/gallery/combination-originals/d801c28f-04d2-45ff-8e4f-3e9bea4892a3.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'right-pointing-dashed-arrow-symbol32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('Right Pointing Dashed Arrow',)
    keywords = ('symbol', 'container content')

    def build(self):

        axis_y, dash_length, step = 16, 2, 9
        for index in range(2):
            x = 2 + index * step
            self.add_line(f'dash-{index}', (x, axis_y), (x + dash_length, axis_y))
        tip = (30, axis_y)
        self.add_line('shaft', (22, axis_y), tip)
        self.add_polyline('head', (20, 6), tip, (20, 26))
        for member in ('head-1', 'head-2'):
            self.relate('connect', 'shaft', member)
