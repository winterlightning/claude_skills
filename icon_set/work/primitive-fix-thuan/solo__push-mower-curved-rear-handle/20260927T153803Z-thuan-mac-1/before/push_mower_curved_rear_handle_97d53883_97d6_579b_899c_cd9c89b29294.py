"""Push Lawn Mower.
Plan: Right-facing mower with smooth backward handle, raised engine and unequal wheels. Extrema (4,8)-(44,40).
Reference: Lucide tractor: unequal wheels and simplified machine silhouette.
Reduction: Hubs and lower frame omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97d53883-97d6-579b-899c-cd9c89b29294'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/gardening lawn mower_97d53883-97d6-579b-899c-cd9c89b29294.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'push-mower-curved-rear-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('push', 'lawn', 'mower')

    def build(self):

        self.add_bezier('handle',(4,8),((12,8),(12,12),(20,20)))
        self.add_polyline('deck',(12,28),(20,20),(32,24),(40,32))
        self.add_polyline('engine',(20,20),(22,12),(30,12),(32,24))
        self.relate('connect','handle','deck');self.relate('connect','engine','deck');self.relate('connect','engine','handle')
        for n,x,y,r in (('rear',12,34,6),('front',40,36,4)):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
            self.relate('connect','deck',n)
