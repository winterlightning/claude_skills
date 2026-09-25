"""Classic Farm Barn.
Plan: Mirrored gambrel roof, inset door frame and diagonal door braces. Extrema (6,6)-(42,42).
Reference: Lucide warehouse: outer building contour and inset doorway with shared base.
Reduction: Loft window omitted to keep the distinctive gambrel roof and braced door open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6e3c185-7515-53d2-9db1-1e36949b6a6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/barn_f6e3c185-7515-53d2-9db1-1e36949b6a6e.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'barn-gambrel-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('classic', 'farm', 'barn')

    def build(self):

        self.add_polyline('barn',(6,42),(6,22),(12,12),(24,6),(36,12),(42,22),(42,42),(34,42),(14,42),(6,42))
        self.add_polyline('door',(14,42),(14,26),(34,26),(34,42));self.relate('connect','barn','door')
        self.add_polyline('brace-left',(14,26),(24,34),(34,42))
        self.add_polyline('brace-right',(34,26),(24,34),(14,42))
        for n in ('brace-left','brace-right'):
            self.relate('connect',n,'door');self.relate('connect',n,'barn')
        self.relate('connect','brace-left','brace-right')
