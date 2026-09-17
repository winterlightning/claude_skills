"""Check Mark: A short descending left arm joins a longer ascending right arm at an angular low point. Generate this component alone; exclude Magnifying Glass Frame.

Construction: A short downstroke and a longer rising stroke retain the source check shape.
Keyshape: HRECT_M; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b711cb0e-31b4-4a64-a43d-8da9f23cbd45'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass check_b711cb0e-31b4-4a64-a43d-8da9f23cbd45.svg'
AUTHOR = 'gpt-6'


class CheckMarkState155(Sub32):
    icon_id = 'check-mark-state-155'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'descending', 'left', 'arm', 'joins', 'longer')

    def build(self):
        self.add_polyline('check',(2,14),(11,24),(30,8))
