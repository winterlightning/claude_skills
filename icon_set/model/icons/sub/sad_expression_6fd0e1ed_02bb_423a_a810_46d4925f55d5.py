"""Sad Expression: Two short upright eyes sit above a broad downturned mouth, with the features arranged symmetrically across an open centre. Generate this component alone; exclude Speech Bubble.

Construction: Two short eyes sit above a wide arched frown, mirrored about x16.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6fd0e1ed-02bb-423a-a810-46d4925f55d5'
SOURCE_PATH = 'pictographic-primitives/state/comment box sad_6fd0e1ed-02bb-423a-a810-46d4925f55d5.svg'
AUTHOR = 'gpt-6'


class SadExpression(Sub32):
    icon_id = 'sad-expression'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('sad', 'expression', 'short', 'upright', 'eyes', 'sit', 'broad', 'downturned')

    def build(self):
        for x in (8,24):self.add_line(f'eye-{x}',(x,4),(x,8))
        self.add_arc('frown',(2,28),(30,28),radius_x=14,radius_y=10)
