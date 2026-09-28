"""Gemstone Ring: A large circular ring band supports a polygonal gemstone above it. The gem has a flat top, angled upper corners, and sloping lower sides partly hidden by the band.

Construction: Empty round ring meets a simple faceted gemstone above; no extra facets added.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '91065c0d-d056-4c23-a604-1f2b872fca43'
SOURCE_PATH = 'pictographic-primitives/state/ring_91065c0d-d056-4c23-a604-1f2b872fca43.svg'
AUTHOR = 'gpt-6'


class GemstoneRingState242(Sub32):
    icon_id = 'gemstone-ring-state-242'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('gemstone', 'ring', 'large', 'circular', 'band', 'supports', 'polygonal', 'gem')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('band',16,20,10)
        self.add_polyline('gem',(10,12),(6,6),(10,2),(22,2),(26,6),(22,12))
        self.relate('connect','band','gem')
