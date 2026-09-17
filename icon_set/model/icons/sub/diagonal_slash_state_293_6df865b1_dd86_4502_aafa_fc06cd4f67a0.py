"""Diagonal Slash: A long diagonal stroke descends from upper left to lower right. Generate this component alone; exclude Video Camera.

Construction: The source diagonal slash runs down-right; the video camera is excluded.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6df865b1-dd86-4502-aafa-fc06cd4f67a0'
SOURCE_PATH = 'pictographic-primitives/state/video with slash_6df865b1-dd86-4502-aafa-fc06cd4f67a0.svg'
AUTHOR = 'gpt-6'


class DiagonalSlashState293(Sub32):
    icon_id = 'diagonal-slash-state-293'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('diagonal', 'slash', 'long', 'stroke', 'descends', 'upper', 'left', 'lower')

    def build(self):
        self.add_line('slash',(2,2),(30,30))
