"""Right Pointing Arrow on SYMBOL32.

Plan: Horizontal shaft and a single mirrored chevron share the arrow tip. Lucide arrow-right supplies the three-run structure.
Centerline extremes use the HRECT_L contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'a25a30ed-7ea9-4fb7-ad5e-dbe539b69b84'
SOURCE_PATH = 'published/gallery/combination-originals/a25a30ed-7ea9-4fb7-ad5e-dbe539b69b84.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'right-pointing-arrow-symbol32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'other', 'primitives-generate')
    aliases = ('Right Pointing Arrow',)
    keywords = ('symbol', 'container content')

    def build(self):

        tip = (30, 16)
        self.add_polyline('head', (20, 6), tip, (20, 26))
        self.add_line('shaft', (2, 16), tip)
        for member in ('head-1', 'head-2'):
            self.relate('connect', 'shaft', member)
