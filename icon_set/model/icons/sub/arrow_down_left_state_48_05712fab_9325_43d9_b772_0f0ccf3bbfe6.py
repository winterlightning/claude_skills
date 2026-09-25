"""Arrow Down Left: A diagonal arrow points down and left, with two short diverging arms meeting the shaft at its lower-left endpoint. Generate this component alone; exclude Circle Frame.

Construction: A long descending-left shaft has the source tilted, non-cardinal arrowhead.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '05712fab-9325-43d9-b772-0f0ccf3bbfe6'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow down left_05712fab-9325-43d9-b772-0f0ccf3bbfe6.svg'
AUTHOR = 'gpt-6'


class ArrowDownLeftState48(Sub32):
    icon_id = 'arrow-down-left-state-48'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('arrow', 'down', 'left', 'diagonal', 'points', 'short', 'diverging', 'arms')

    def build(self):
        self.add_line('shaft',(28,2),(6,30))
        self.add_polyline('head',(4,18),(6,30),(18,28))
        self.relate('connect','shaft','head')
