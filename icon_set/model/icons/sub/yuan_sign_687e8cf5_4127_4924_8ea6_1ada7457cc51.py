"""Yuan Sign: Two diagonal upper arms meet an upright stem crossed by two horizontal bars, forming a yuan or yen currency sign. Generate this component alone; exclude Circle Frame.

Construction: A Y-shaped stem has two evenly spaced currency bars across its lower portion.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '687e8cf5-4127-4924-8ea6-1ada7457cc51'
SOURCE_PATH = 'pictographic-primitives/state/circle yuan 1_687e8cf5-4127-4924-8ea6-1ada7457cc51.svg'
AUTHOR = 'gpt-6'


class YuanSign(Sub32):
    icon_id = 'yuan-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('yuan', 'sign', 'diagonal', 'upper', 'arms', 'meet', 'upright', 'stem')

    def build(self):
        self.add_polyline('y',(2,2),(16,14),(30,2))
        self.add_line('stem',(16,14),(16,30))
        self.relate('connect','y','stem')
        for name,y in (('upper',18),('lower',26)):
            self.add_line(name,(6,y),(26,y))
            self.relate('connect','stem',name)
