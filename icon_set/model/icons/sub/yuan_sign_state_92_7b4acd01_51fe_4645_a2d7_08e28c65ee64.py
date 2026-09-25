"""Yuan Sign: A Y-shaped currency glyph has two diagonal upper arms and a single horizontal bar crossing its lower stem. Generate this component alone; exclude Circle Frame.

Construction: The Y-shaped currency glyph retains exactly one crossbar, as in this source.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b4acd01-51fe-4645-a2d7-08e28c65ee64'
SOURCE_PATH = 'pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'
AUTHOR = 'gpt-6'


class YuanSignState92(Sub32):
    icon_id = 'yuan-sign-state-92'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('yuan', 'sign', 'y', 'shaped', 'currency', 'glyph', 'diagonal', 'upper')

    def build(self):
        self.add_polyline('arms',(4,2),(16,18),(28,2))
        self.add_line('stem',(16,18),(16,30))
        self.add_line('bar',(8,18),(24,18))
        self.relate('connect','arms','stem')
        self.relate('connect','arms','bar')
        self.relate('connect','stem','bar')
