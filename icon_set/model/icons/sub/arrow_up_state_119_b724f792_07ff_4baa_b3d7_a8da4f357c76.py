"""Arrow Up: A tall upright shaft ends in two diagonal arms forming an open upward-pointing arrowhead. Generate this component alone; exclude Bottom-Cut File Frame.

Construction: An upright arrow retains its long stem below a broad open head.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b724f792-07ff-4baa-b3d7-a8da4f357c76'
SOURCE_PATH = 'pictographic-primitives/state/file arrow up_b724f792-07ff-4baa-b3d7-a8da4f357c76.svg'
AUTHOR = 'gpt-6'


class ArrowUpState119(Sub32):
    icon_id = 'arrow-up-state-119'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'up', 'tall', 'upright', 'shaft', 'ends', 'diagonal', 'arms')

    def build(self):
        self.add_line('shaft',(16,30),(16,2))
        self.add_polyline('head',(4,14),(16,2),(28,14))
        self.relate('connect','shaft','head')
