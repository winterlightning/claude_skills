"""Check Mark: An angular check has a short descending left arm followed by a much longer ascending right arm. Generate this component alone; exclude Speech Bubble.

Construction: The original open check uses one short descending arm and one long rising arm.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ced4c938-1a05-47c7-b02a-abba1ffc225a'
SOURCE_PATH = 'pictographic-primitives/state/message check_ced4c938-1a05-47c7-b02a-abba1ffc225a.svg'
AUTHOR = 'gpt-6'


class CheckMarkState166(Sub32):
    icon_id = 'check-mark-state-166'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'angular', 'short', 'descending', 'left', 'arm', 'followed')

    def build(self):
        self.add_polyline('check',(2,18),(12,28),(30,4))
