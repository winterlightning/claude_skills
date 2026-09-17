"""Code Brackets: Two detached angular brackets face outward, with a broad clear gap separating the left-facing and right-facing chevrons. Generate this component alone; exclude Round Speech Bubble.

Construction: Two opposing angle brackets mirror about x16, isolated from the speech bubble.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '005b4ba3-8d0e-4db6-81ea-d18259d3e702'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble circle code_005b4ba3-8d0e-4db6-81ea-d18259d3e702.svg'
AUTHOR = 'gpt-6'


class CodeBrackets(Sub32):
    icon_id = 'code-brackets'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('code', 'brackets', 'detached', 'angular', 'face', 'outward', 'broad', 'clear')

    def build(self):
        self.add_polyline("left",(10,4),(2,16),(10,28))
        self.add_polyline("right",(22,4),(30,16),(22,28))
