"""A flat hexagonal nut with one circular bore; no surface decoration."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46378f89-29b6-5b96-8c27-5894c4198d51'
SOURCE_PATH = 'pictographic-primitives/tools/hardware nut_46378f89-29b6-5b96-8c27-5894c4198d51.svg'
AUTHOR = 'gpt-6'

class HexNut(Solo48):
    icon_id = 'hex-nut'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('nut', 'hex nut', 'hexagon', 'bolt', 'hardware', 'fastener', 'screw', 'metal')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        self.add_polyline('hexagon',(6,24),(14,8),(34,8),(42,24),(34,40),(14,40),closed=True)
        circle('bore',24,24,7)
