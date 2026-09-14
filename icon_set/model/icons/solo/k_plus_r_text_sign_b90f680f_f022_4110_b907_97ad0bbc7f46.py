"""K+R Text Sign, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b90f680f-f022-4110-b907-97ad0bbc7f46'
SOURCE_PATH = 'pictographic-primitives/transportation/kiss and ride_b90f680f-f022-4110-b907-97ad0bbc7f46.svg'
AUTHOR = 'gpt-6'

class KPlusRTextSign(Solo48):
    icon_id = 'k-plus-r-text-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('kiss and ride', 'k+r', 'drop off', 'pick up', 'parking', 'text', 'sign', 'station')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('k-stem',(6,8),(6,24),(6,40))
        self.add_polyline('k-arms',(11,8),(6,24),(11,40))
        self.relate('connect','k-stem','k-arms')
        self.add_polyline('plus-horizontal',(20,24),(24,24),(28,24))
        self.add_polyline('plus-vertical',(24,20),(24,24),(24,28))
        self.relate('connect','plus-horizontal','plus-vertical')
        self.add_polyline('r-stem',(37,8),(37,24),(37,40))
        self.add_arc('r-bowl',(37,8),(37,24),radius_x=7,radius_y=8)
        self.add_line('r-leg',(37,24),(42,40))
        self.relate('connect','r-stem','r-bowl')
        self.relate('connect','r-stem','r-leg')
        self.relate('connect','r-bowl','r-leg')
