"""Gardening Push Lawn Mower.
Plan: Long sloping mower deck above unequal wheels and backward rising handle. Extrema (4,8)-(44,40).
Reference: Lucide tractor: clear unequal circular wheels and sparse machine outline.
Reduction: Wheel hubs and doubled frame omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36ab8da5-52f6-52a3-b9fe-8aaba0d88371'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/gardening lawn mower_36ab8da5-52f6-52a3-b9fe-8aaba0d88371.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'lawn-mower-sloping-deck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('gardening', 'push', 'lawn', 'mower')

    def build(self):

        self.add_polyline('handle',(4,8),(10,8),(18,20))
        self.add_polyline('deck',(12,28),(12,20),(18,20),(32,24),(40,32))
        self.relate('connect','handle','deck')
        self.add_polyline('engine',(18,20),(20,12),(30,12),(32,24));self.relate('connect','engine','deck')
        for n,x,y,r in (('rear',12,34,6),('front',40,36,4)):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.relate('connect','deck','front');self.relate('connect','deck','rear')
