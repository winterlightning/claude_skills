"""Code Brackets: Two opposing angle brackets face away from a central gap, with a left-pointing bracket and a right-pointing bracket. Generate this component alone; exclude Circle Frame.

Construction: Two opposing angle brackets retain the empty centre; the original surrounding circle is excluded.
Keyshape: HRECT_M; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3699b0e7-2691-4335-9f29-5124f5d2d5cb'
SOURCE_PATH = 'pictographic-primitives/state/circle code bracket_3699b0e7-2691-4335-9f29-5124f5d2d5cb.svg'
AUTHOR = 'gpt-6'


class CodeBracketsState56(Sub32):
    icon_id = 'code-brackets-state-56'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('code', 'brackets', 'opposing', 'angle', 'face', 'away', 'central', 'gap')

    def build(self):
        self.add_polyline('left',(10,8),(2,16),(10,24))
        self.add_polyline('right',(22,8),(30,16),(22,24))
