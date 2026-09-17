"""Check Mark: An open check mark has a short downstroke on the left and a longer rising stroke on the right. Generate this component alone; exclude House Frame.

Construction: The source check remains open, with a longer upper-right arm.
Keyshape: HRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a1b0e0fc-7f62-498d-a7b8-77469b4c75dc'
SOURCE_PATH = 'pictographic-primitives/state/house with line and check_a1b0e0fc-7f62-498d-a7b8-77469b4c75dc.svg'
AUTHOR = 'gpt-6'


class CheckMarkState137(Sub32):
    icon_id = 'check-mark-state-137'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'open', 'short', 'downstroke', 'left', 'longer', 'rising')

    def build(self):
        self.add_polyline('check',(2,16),(12,26),(30,6))
