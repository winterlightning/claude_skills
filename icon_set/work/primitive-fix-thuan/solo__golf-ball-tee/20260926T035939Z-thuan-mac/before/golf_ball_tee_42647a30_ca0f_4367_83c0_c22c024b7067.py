"""A dimpled golf ball floats above a T-shaped tee. CIRCLE radial envelope reaches y4 and y44 while preserving the narrow subject. Lucide circle informs the round ball; no useful exact tee match found. Reduce two source dimples to one, shrink the ball, and enlarge the ball-to-tee gap to leave a clearly visible peg."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42647a30-ca0f-4367-83c0-c22c024b7067'
SOURCE_PATH = 'pictographic-primitives/symbol/golf_42647a30-ca0f-4367-83c0-c22c024b7067.svg'
AUTHOR = 'gpt-6'


class GolfBallTee(Solo48):
    icon_id = 'golf-ball-tee'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('golf', 'ball', 'tee', 'sport', 'course', 'club', 'game', 'dimples')

    def build(self) -> None:
        cx, cy, radius = 24, 15, 11
        self.add_arc('ball-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('ball-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
        self.add_dot('dimple',(24,15))
        self.add_polyline('tee-top',(16,35),(24,35),(32,35))
        self.add_line('tee-peg',(24,35),(24,42))
        self.relate('connect','tee-top','tee-peg')
