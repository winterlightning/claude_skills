"""Diagonal Slash: A long diagonal line descends from upper left to lower right. Generate this component alone; exclude Heart.

Construction: The source falling diagonal slash is isolated from the heart; direction is preserved.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '00d83c6d-7ad8-492b-9d49-4bc79c61758b'
SOURCE_PATH = 'pictographic-primitives/state/slash heart_00d83c6d-7ad8-492b-9d49-4bc79c61758b.svg'
AUTHOR = 'gpt-6'


class DiagonalSlashState255(Sub32):
    icon_id = 'diagonal-slash-state-255'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('diagonal', 'slash', 'long', 'line', 'descends', 'upper', 'left', 'lower')

    def build(self):
        self.add_line('slash',(2,2),(30,30))
