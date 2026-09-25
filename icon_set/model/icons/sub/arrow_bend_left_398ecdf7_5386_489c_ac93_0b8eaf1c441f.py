"""Arrow Bend Left: An arrow curves upward from the lower right and turns left, ending in an open left-pointing arrowhead. Generate this component alone; exclude Circle Frame.

Construction: A quarter-circle bend joins horizontal and vertical runs tangentially; an open head points left.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '398ecdf7-5386-489c-ac93-0b8eaf1c441f'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow back_398ecdf7-5386-489c-ac93-0b8eaf1c441f.svg'
AUTHOR = 'gpt-6'


class ArrowBendLeft(Sub32):
    icon_id = 'arrow-bend-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'bend', 'left', 'curves', 'upward', 'lower', 'right', 'turns')

    def build(self):
        self.add_line('horizontal',(2,10),(16,10))
        self.add_arc('bend',(16,10),(30,24),radius_x=14)
        self.add_line('vertical',(30,24),(30,30))
        self.add_contour('shaft','horizontal','bend','vertical')
        self.add_polyline('head',(10,2),(2,10),(10,18))
        self.relate('connect','shaft','head')
