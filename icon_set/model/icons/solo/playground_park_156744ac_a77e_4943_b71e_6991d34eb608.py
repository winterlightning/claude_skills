"""A playground wheel on a stand beside an arched climbing frame. SQUARE extremes (6,6)-(42,42). Lucide ferris-wheel informs circular hub and explicit stand contacts. Simplify the stand to a triangle while preserving the round disc, center dot, two tall frame legs and connecting brace."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '156744ac-a77e-4943-b71e-6991d34eb608'
SOURCE_PATH = 'pictographic-primitives/symbol/park_156744ac-a77e-4943-b71e-6991d34eb608.svg'
AUTHOR = 'gpt-6'


class PlaygroundPark(Solo48):
    icon_id = 'playground-park'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('park', 'playground', 'amusement', 'ferris-wheel', 'fun', 'kids', 'recreation', 'fair')

    def build(self) -> None:
        points=[(15,6),(24,15),(15,24),(6,15)]
        for i,p in enumerate(points):
            self.add_arc(f'wheel-{i}',p,points[(i+1)%4],radius_x=9)
        self.add_contour('wheel',*(f'wheel-{i}' for i in range(4)),closed=True)
        self.add_dot('hub',(15,15))
        self.add_polyline('stand',(15,24),(6,42),(24,42),(21,36),(15,24),closed=True)
        self.relate('connect','wheel','stand')
        self.add_polyline('frame-left',(34,10),(34,24),(34,42))
        self.add_arc('frame-top',(34,10),(42,10),radius_x=4)
        self.add_line('frame-right',(42,10),(42,42))
        self.add_contour('frame-round','frame-top','frame-right')
        self.relate('connect','frame-left','frame-round')
        self.add_line('brace',(21,36),(34,24))
        self.relate('connect','stand','brace')
        self.relate('connect','frame-left','brace')
