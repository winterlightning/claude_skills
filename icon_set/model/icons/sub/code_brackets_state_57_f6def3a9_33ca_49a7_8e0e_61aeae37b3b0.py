"""Code Brackets: Two broad angle brackets face outward on either side of an open central space, their ends rounded. Generate this component alone; exclude Circle Frame.

Construction: Two opposing angle brackets retain the empty centre; the original surrounding circle is excluded.
Keyshape: HRECT_M; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f6def3a9-33ca-49a7-8e0e-61aeae37b3b0'
SOURCE_PATH = 'pictographic-primitives/state/circle code_f6def3a9-33ca-49a7-8e0e-61aeae37b3b0.svg'
AUTHOR = 'gpt-6'


class CodeBracketsState57(Sub32):
    icon_id = 'code-brackets-state-57'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('code', 'brackets', 'broad', 'angle', 'face', 'outward', 'either', 'side')

    def build(self):
        self.add_polyline('left',(10,8),(2,16),(10,24))
        self.add_polyline('right',(22,8),(30,16),(22,24))
