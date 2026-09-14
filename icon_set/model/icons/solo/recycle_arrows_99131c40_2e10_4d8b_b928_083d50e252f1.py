"""Three arrows chase around a triangular route. Lucide recycle informs three separate bent strokes and open arrowheads; clockwise circulation and rounded turns retained.

SOLO48 SQUARE, live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99131c40-2e10-4d8b-b928-083d50e252f1'
SOURCE_PATH = 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'
AUTHOR = 'gpt-6'


class RecycleArrows(Solo48):
    icon_id = 'recycle-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('recycle', 'recycling', 'eco', 'environment', 'reuse', 'green', 'sustainability', 'waste')

    def build(self) -> None:

        self.add_arc('top-turn',(18,12),(30,12),radius_x=6)
        self.add_line('top-run',(30,12),(36,22))
        self.add_contour('top-arrow','top-turn','top-run')
        self.add_polyline('top-head',(28,20),(36,22),(38,14))
        self.relate('connect','top-arrow','top-head')
        self.add_line('right-run',(42,28),(42,30))
        self.add_arc('right-turn',(42,30),(36,36),radius_x=6)
        self.add_line('bottom-run',(36,36),(24,36))
        self.add_contour('right-arrow','right-run','right-turn','bottom-run')
        self.add_polyline('bottom-head',(30,30),(24,36),(30,42))
        self.relate('connect','right-arrow','bottom-head')
        self.add_line('left-base',(15,36),(12,36))
        self.add_arc('left-turn',(12,36),(6,30),radius_x=6)
        self.add_line('left-rise',(6,30),(12,20))
        self.add_contour('left-arrow','left-base','left-turn','left-rise')
        self.add_polyline('left-head',(6,22),(12,20),(14,28))
        self.relate('connect','left-arrow','left-head')
