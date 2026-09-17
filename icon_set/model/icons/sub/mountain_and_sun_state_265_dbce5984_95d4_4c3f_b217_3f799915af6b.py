"""Mountain and Sun: Two unequal mountain peaks share a straight baseline, with a detached circular sun above the smaller right peak. Generate this component alone; exclude Square Frame.

Construction: Two unequal mountains share a baseline with an outlined sun above the smaller right peak.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dbce5984-95d4-4c3f-b217-3f799915af6b'
SOURCE_PATH = 'pictographic-primitives/state/square image_dbce5984-95d4-4c3f-b217-3f799915af6b.svg'
AUTHOR = 'gpt-6'


class MountainAndSunState265(Sub32):
    icon_id = 'mountain-and-sun-state-265'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('mountain', 'sun', 'unequal', 'peaks', 'share', 'straight', 'baseline', 'detached')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        self.add_polyline('ridge',(2,28),(12,10),(20,22),(24,18),(30,28),closed=True)
        circle('sun',26,8,4)
