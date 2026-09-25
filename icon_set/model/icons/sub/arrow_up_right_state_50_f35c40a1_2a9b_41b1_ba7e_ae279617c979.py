"""Arrow Up Right: A diagonal shaft rises rightward into an open arrowhead whose two short arms extend left and downward. Generate this component alone; exclude Circle Frame.

Construction: A long rising-right shaft terminates at the source tilted arrowhead.
Keyshape: VRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f35c40a1-2a9b-41b1-ba7e-ae279617c979'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow up right_f35c40a1-2a9b-41b1-ba7e-ae279617c979.svg'
AUTHOR = 'gpt-6'


class ArrowUpRightState50(Sub32):
    icon_id = 'arrow-up-right-state-50'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('arrow', 'up', 'right', 'diagonal', 'shaft', 'rises', 'rightward', 'open')

    def build(self):
        self.add_line('shaft',(4,30),(26,2))
        self.add_polyline('head',(14,4),(26,2),(28,14))
        self.relate('connect','shaft','head')
