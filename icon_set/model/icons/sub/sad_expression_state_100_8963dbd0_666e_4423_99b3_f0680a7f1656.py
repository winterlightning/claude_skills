"""Sad Expression: A frowning expression has two separated vertical eyes and a wide curved mouth whose ends turn downward. Generate this component alone; exclude Speech Bubble.

Construction: Two short eyes and a downturned mouth retain the source expression without its bubble.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8963dbd0-666e-4423-99b3-f0680a7f1656'
SOURCE_PATH = 'pictographic-primitives/state/comment box sad_8963dbd0-666e-4423-99b3-f0680a7f1656.svg'
AUTHOR = 'gpt-6'


class SadExpressionState100(Sub32):
    icon_id = 'sad-expression-state-100'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('sad', 'expression', 'frowning', 'separated', 'vertical', 'eyes', 'wide', 'curved')

    def build(self):
        for x in (8,24):self.add_line(f'eye-{x}',(x,4),(x,8))
        self.add_arc('frown',(2,28),(30,28),radius_x=14,radius_y=10)
