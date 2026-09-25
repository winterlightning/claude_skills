"""Diagonal skateboard deck with kicked ends, trucks and two wheels. No exact local Lucide match; shared wheel radii and a segmented attachment run preserve the subject.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c33a78-abee-41dd-9464-8dd7be126a9c'
SOURCE_PATH = 'pictographic-primitives/symbol/skate_52c33a78-abee-41dd-9464-8dd7be126a9c.svg'
AUTHOR = 'gpt-6'


class SkateboardDiagonal(Solo48):
    icon_id = 'skateboard-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('skateboard', 'skate', 'board', 'sport', 'skating', 'street', 'wheels', 'youth')

    def build(self) -> None:

        self.add_polyline('deck',(6,34),(12,32),(18,26),(30,14),(36,8),(38,6))
        for name,cx,cy,start in [('rear',24,39,(18,26)),('front',39,24,(30,14))]:
            self.add_arc(name+'-wheel-top',(cx,cy-3),(cx,cy+3),radius_x=3)
            self.add_arc(name+'-wheel-bottom',(cx,cy+3),(cx,cy-3),radius_x=3)
            self.add_contour(name+'-wheel',name+'-wheel-top',name+'-wheel-bottom',closed=True)
            self.add_line(name+'-truck',start,(cx,cy-3))
            self.relate('connect',name+'-truck','deck')
            self.relate('connect',name+'-truck',name+'-wheel')
