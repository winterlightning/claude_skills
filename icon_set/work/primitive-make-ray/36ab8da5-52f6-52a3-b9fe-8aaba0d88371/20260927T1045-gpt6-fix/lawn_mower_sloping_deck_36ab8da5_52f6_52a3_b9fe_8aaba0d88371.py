"""Gardening Push Lawn Mower.
Plan: Long sloping mower deck above unequal wheels and backward rising handle. Extrema (4,8)-(44,40).
Reference: Lucide tractor: clear unequal circular wheels and sparse machine outline.
Reduction: Wheel hubs and doubled frame omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '36ab8da5-52f6-52a3-b9fe-8aaba0d88371'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lawn-mower-sloping-deck/20260927T104148Z-thuan-mac-1/reference/gardening lawn mower_36ab8da5-52f6-52a3-b9fe-8aaba0d88371.svg'
AUTHOR = "gpt-6"

class Batch28Icon(Solo48):
    icon_id = 'lawn-mower-sloping-deck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('gardening', 'push', 'lawn', 'mower')

    def build(self):

        self.add_polyline('handle',(4,8),(10,8),(18,20))
        self.add_polyline('deck',(12,28),(12,20),(18,20),(32,24),(40,32))
        self.relate('connect','handle','deck')
        self.add_line('engine-left',(18,20),(20,12))
        self.add_arc('engine-top',(20,12),(30,12),radius_x=5,radius_y=3)
        self.add_line('engine-right',(30,12),(32,24))
        self.add_contour('engine','engine-left','engine-top','engine-right')
        self.relate('connect','engine','deck')
        for n,x,y,r in (('rear',12,34,6),('front',40,36,4)):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.relate('connect','deck','front');self.relate('connect','deck','rear')
