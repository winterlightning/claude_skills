"""Equals Sign: Two straight horizontal lines of equal length sit one above the other with a clear gap. Generate this component alone; exclude Circle Frame.

Construction: Two equal horizontal strokes, vertically mirrored.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '204ecec0-870d-4feb-9da5-e8ed98b8f9c3'
SOURCE_PATH = 'pictographic-primitives/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.svg'
AUTHOR = 'gpt-6'


class EqualsSign(Sub32):
    icon_id = 'equals-sign'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('equals', 'sign', 'straight', 'horizontal', 'lines', 'equal', 'length', 'sit')

    def build(self):
        for name,y in (('upper',8),('lower',24)):
            self.add_line(name,(2,y),(30,y))
