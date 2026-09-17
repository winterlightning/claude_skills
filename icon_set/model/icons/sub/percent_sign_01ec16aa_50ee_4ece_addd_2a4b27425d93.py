"""Percent Sign: A rising diagonal slash separates two tiny dots, one at the upper left and one at the lower right. Generate this component alone; exclude Circle Frame.

Construction: One diagonal slash with paired dot marks, isolated from the original outer badge.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '01ec16aa-50ee-4ece-addd-2a4b27425d93'
SOURCE_PATH = 'pictographic-primitives/state/percent symbol circle_01ec16aa-50ee-4ece-addd-2a4b27425d93.svg'
AUTHOR = 'gpt-6'


class PercentSign(Sub32):
    icon_id = 'percent-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('percent', 'sign', 'rising', 'diagonal', 'slash', 'separates', 'tiny', 'dots')

    def build(self):
        self.add_line("slash",(2,30),(30,2))
        self.add_dot("upper-dot",(7,7))
        self.add_dot("lower-dot",(25,25))
