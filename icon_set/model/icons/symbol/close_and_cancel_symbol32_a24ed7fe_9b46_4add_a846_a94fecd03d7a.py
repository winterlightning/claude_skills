"""Close and Cancel Symbol on SYMBOL32.

Plan: Two equal diagonals share the center junction; mirrored about x=16. Lucide x supplies the crossed-stroke construction.
Centerline extremes use the SQUARE contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'a24ed7fe-9b46-4add-a846-a94fecd03d7a'
SOURCE_PATH = 'published/gallery/combination-originals/a24ed7fe-9b46-4add-a846-a94fecd03d7a.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'close-and-cancel-symbol32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ('Close and Cancel Symbol',)
    keywords = ('symbol', 'container content')

    def build(self):

        center = (16, 16)
        for name, start, end in [('falling', (2, 2), (30, 30)), ('rising', (2, 30), (30, 2))]:
            self.add_polyline(name, start, center, end)
        for a in ('falling-1', 'falling-2'):
            for b in ('rising-1', 'rising-2'):
                self.relate('connect', a, b)
