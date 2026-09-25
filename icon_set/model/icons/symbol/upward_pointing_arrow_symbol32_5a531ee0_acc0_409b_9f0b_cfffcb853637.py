"""Upward Pointing Directional Arrow on SYMBOL32.

Plan: Upright shaft and mirrored chevron share the top tip. Lucide arrow-up informs the centered directional junction.
Centerline extremes use the VRECT_L contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '5a531ee0-acc0-409b-9f0b-cfffcb853637'
SOURCE_PATH = 'published/gallery/combination-originals/5a531ee0-acc0-409b-9f0b-cfffcb853637.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'upward-pointing-arrow-symbol32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ('Upward Pointing Directional Arrow',)
    keywords = ('symbol', 'container content')

    def build(self):

        axis, tip_y, half_width = 16, 2, 10
        tip = (axis, tip_y)
        self.add_polyline('head', (axis-half_width, 12), tip, (axis+half_width, 12))
        self.add_line('shaft', (axis, 30), tip)
        for member in ('head-1', 'head-2'):
            self.relate('connect', 'shaft', member)
