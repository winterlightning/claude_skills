"""Play Triangle: An outlined triangle points right, with a vertical left edge and gently rounded corners around its empty centre. Generate this component alone; exclude Speech Bubble.

Construction: The source right triangle retains its empty centre and soft stroke joins.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3cced727-8e6e-4892-8b05-4251a81e3257'
SOURCE_PATH = 'pictographic-primitives/state/massage bubble with play button_3cced727-8e6e-4892-8b05-4251a81e3257.svg'
AUTHOR = 'gpt-6'


class PlayTriangleState160(Sub32):
    icon_id = 'play-triangle-state-160'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('play', 'triangle', 'outlined', 'points', 'right', 'vertical', 'left', 'edge')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
