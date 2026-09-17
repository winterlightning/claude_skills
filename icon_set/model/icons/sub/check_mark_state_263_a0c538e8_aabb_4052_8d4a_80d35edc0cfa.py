"""Check Mark: A short downstroke joins a longer rising stroke at a sharp low point. Generate this component alone; exclude Rounded Square Frame.

Construction: The source check retains the long, steep rising right arm.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a0c538e8-aabb-4052-8d4a-80d35edc0cfa'
SOURCE_PATH = 'pictographic-primitives/state/square check_a0c538e8-aabb-4052-8d4a-80d35edc0cfa.svg'
AUTHOR = 'gpt-6'


class CheckMarkState263(Sub32):
    icon_id = 'check-mark-state-263'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'downstroke', 'joins', 'longer', 'rising', 'stroke')

    def build(self):
        self.add_polyline('check',(2,18),(12,28),(30,4))
