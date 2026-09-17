"""Play Triangle: A large outlined triangle points right with three sharp corners and an empty interior. Its left edge is vertical, with matching slopes meeting at the rightmost tip.

Construction: The source standalone right triangle keeps its vertical rear edge and empty interior.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '74cb6db1-68af-42f0-a7c9-81a431cfff0e'
SOURCE_PATH = 'pictographic-primitives/state/play button_74cb6db1-68af-42f0-a7c9-81a431cfff0e.svg'
AUTHOR = 'gpt-6'


class PlayTriangleState211(Sub32):
    icon_id = 'play-triangle-state-211'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('play', 'triangle', 'large', 'outlined', 'points', 'right', 'sharp', 'corners')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
