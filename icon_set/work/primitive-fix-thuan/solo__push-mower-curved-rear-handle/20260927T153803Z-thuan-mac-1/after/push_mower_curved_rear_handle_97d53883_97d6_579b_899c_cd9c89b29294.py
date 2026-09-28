"""Push Lawn Mower.
Plan: Right-facing mower with smooth backward handle, raised engine and unequal wheels. Extrema (4,8)-(44,40).
Reference: Lucide tractor: unequal wheels and simplified machine silhouette.
Reduction: Hubs and lower frame omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '97d53883-97d6-579b-899c-cd9c89b29294'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__push-mower-curved-rear-handle/20260927T153803Z-thuan-mac-1/reference/gardening lawn mower_97d53883-97d6-579b-899c-cd9c89b29294.svg'
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
        # Rear handle rises behind a low deck and a compact engine.
        self.add_bezier('handle',(4,8),((9,8),(10,11),(12,28)))
        self.add_polyline('deck-top',(12,28),(20,26),(32,27),(40,32))
        self.add_polyline('engine',(20,26),(22,17),(30,17),(32,27))
        self.relate('connect','handle','deck-top')
        self.relate('connect','engine','deck-top')
        for n,x,y,r in (('rear',12,34,6),('front',40,36,4)):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
            self.relate('connect','deck-top',n)
