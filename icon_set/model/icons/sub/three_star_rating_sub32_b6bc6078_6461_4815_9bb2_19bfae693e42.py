"""Complete reference reconstruction; unresolved findings are retained for review."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b6bc6078-6461-4815-9bb2-19bfae693e42'
SOURCE_PATH = 'pictographic-primitives/other/three stars_b6bc6078-6461-4815-9bb2-19bfae693e42.svg'
AUTHOR = "gpt-6"
REFERENCE_PARTS = ('three outlined five-point stars', 'one above two; equal star dimensions')

class Drawing(Sub32):
    icon_id = 'three-star-rating-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'star', 'rating', 'symbol')

    def build(self):
        # One shared five-point outline repeated in a triangular arrangement.
        star=[(0,-6),(2,-2),(5,-1),(3,2),(4,6),(0,4),(-4,6),(-3,2),(-5,-1),(-2,-2)]
        for n,(cx,cy) in enumerate(((16,8),(7,24),(25,24))):
            self.add_polyline(f'star-{n}',*((cx+x,cy+y) for x,y in star),closed=True)

