"""Folding Bike, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd426cd8-b947-5b9a-b3dc-7e153ef7aa2e'
SOURCE_PATH = 'pictographic-primitives/transportation/folding bike_bd426cd8-b947-5b9a-b3dc-7e153ef7aa2e.svg'
AUTHOR = 'gpt-6'

class FoldingBike(Solo48):
    icon_id = 'folding-bike'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('folding bike', 'bicycle', 'compact', 'commute', 'cycling', 'bike', 'portable', 'city')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        for i,x in enumerate((12,36)):
            self.add_arc(f'wheel-{i}-a',(x,24),(x,40),radius_x=8)
            self.add_arc(f'wheel-{i}-b',(x,40),(x,24),radius_x=8)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-a',f'wheel-{i}-b',closed=True)
        self.add_polyline('main-tube',(12,24),(23,20),(34,16))
        self.relate('connect','main-tube','wheel-0')
        self.add_polyline('steering',(32,8),(34,16),(36,24))
        self.relate('connect','steering','main-tube')
        self.relate('connect','steering','wheel-1')
        self.add_polyline('saddle',(16,8),(20,8),(24,8))
        self.add_line('seat-post',(20,8),(23,20))
        self.relate('connect','seat-post','saddle')
        self.relate('connect','seat-post','main-tube')
        self.add_line('handlebar',(32,8),(40,8))
        self.relate('connect','handlebar','steering')
