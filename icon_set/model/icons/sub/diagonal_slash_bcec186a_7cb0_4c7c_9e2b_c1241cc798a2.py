"""Diagonal Slash: A long rising diagonal stroke extends from lower-left to upper-right. Generate this component alone; exclude Document.

Construction: One rising diagonal slash preserves the source angle and excludes the document.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bcec186a-7cb0-4c7c-9e2b-c1241cc798a2'
SOURCE_PATH = 'pictographic-primitives/state/rectangle slash_bcec186a-7cb0-4c7c-9e2b-c1241cc798a2.svg'
AUTHOR = 'gpt-6'


class DiagonalSlash(Sub32):
    icon_id = 'diagonal-slash'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('diagonal', 'slash', 'long', 'rising', 'stroke', 'extends', 'lower', 'left')

    def build(self):
        self.add_line('slash',(6,30),(26,2))
