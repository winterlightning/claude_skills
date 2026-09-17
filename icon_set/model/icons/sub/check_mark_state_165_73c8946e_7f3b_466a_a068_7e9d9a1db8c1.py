"""Check Mark: An angular check has a short descending left arm followed by a much longer ascending right arm. Generate this component alone; exclude Speech Bubble.

Construction: The original open check uses one short descending arm and one long rising arm.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '73c8946e-7f3b-466a-a068-7e9d9a1db8c1'
SOURCE_PATH = 'pictographic-primitives/state/message check_73c8946e-7f3b-466a-a068-7e9d9a1db8c1.svg'
AUTHOR = 'gpt-6'


class CheckMarkState165(Sub32):
    icon_id = 'check-mark-state-165'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'angular', 'short', 'descending', 'left', 'arm', 'followed')

    def build(self):
        self.add_polyline('check',(2,18),(12,28),(30,4))
