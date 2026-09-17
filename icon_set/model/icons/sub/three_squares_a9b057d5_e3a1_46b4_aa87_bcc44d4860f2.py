"""Three Squares: Three equal upright square outlines form a triangular arrangement, with one centred above two separated lower squares. Each square has an empty interior and remains detached from its neighbours.

Construction: Three identical ten-unit squares; top centred, bottom pair separated by eight units.
Keyshape: SQUARE; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a9b057d5-e3a1-46b4-aa87-bcc44d4860f2'
SOURCE_PATH = 'pictographic-primitives/state/3 three squares_a9b057d5-e3a1-46b4-aa87-bcc44d4860f2.svg'
AUTHOR = 'gpt-6'


class ThreeSquares(Sub32):
    icon_id = 'three-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('squares', 'equal', 'upright', 'square', 'outlines', 'form', 'triangular', 'arrangement')

    def build(self):
        for i,(x,y) in enumerate(((11,2),(2,20),(20,20))):
            side=10
            self.add_polyline(f"square-{i}",(x,y),(x+side,y),(x+side,y+side),(x,y+side),closed=True)
