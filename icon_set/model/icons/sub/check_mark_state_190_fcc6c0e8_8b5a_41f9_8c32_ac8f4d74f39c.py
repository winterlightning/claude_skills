"""Check Mark: A short descending stroke meets a longer rising stroke at an angular lower point. Generate this component alone; exclude Capsule Frame.

Construction: The source check retains a short left arm and longer rising right arm.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = 'pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'
AUTHOR = 'gpt-6'


class CheckMarkState190(Sub32):
    icon_id = 'check-mark-state-190'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'descending', 'stroke', 'meets', 'longer', 'rising')

    def build(self):
        self.add_polyline('check',(2,14),(12,24),(30,8))
