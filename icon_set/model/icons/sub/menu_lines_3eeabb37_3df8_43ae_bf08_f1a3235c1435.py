"""Menu Lines: Three long horizontal strokes are stacked with equal spacing and aligned ends. Each stroke remains separate, creating an open three-line menu glyph without an enclosing shape.

Construction: Three equal horizontal strokes share a common length and vertical step.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3eeabb37-3df8-43ae-bf08-f1a3235c1435'
SOURCE_PATH = 'pictographic-primitives/state/menu_3eeabb37-3df8-43ae-bf08-f1a3235c1435.svg'
AUTHOR = 'gpt-6'


class MenuLines(Sub32):
    icon_id = 'menu-lines'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('menu', 'lines', 'long', 'horizontal', 'strokes', 'are', 'stacked', 'equal')

    def build(self):
        for i,y in enumerate((4,16,28)):self.add_line(f'line-{i}',(2,y),(30,y))
