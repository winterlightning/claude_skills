"""Push Lawn Mower Machine.
Plan: Left-facing flat-deck mower with matching wheels and one straight rising handle. Extrema (4,8)-(44,40).
Reference: Lucide tractor: circular wheels and shared frame joints.
Reduction: Wheel hubs and thin undercarriage removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94b0b30d-4817-43f4-9e38-d4b8d2336e21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/lawn mower_94b0b30d-4817-43f4-9e38-d4b8d2336e21.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'push-mower-straight-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('push', 'lawn', 'mower', 'machine')

    def build(self):

        for n,x in (('front',10),('rear',34)):
            self.add_arc(n+'-a',(x,28),(x,40),radius_x=6)
            self.add_arc(n+'-b',(x,40),(x,28),radius_x=6)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.add_polyline('deck',(10,28),(10,20),(18,20),(28,20),(34,20),(34,28))
        self.add_polyline('engine',(18,20),(18,12),(28,12),(28,20))
        self.add_line('handle',(34,20),(44,8))
        self.relate('connect','deck','engine');self.relate('connect','deck','handle')
        for n in ('front','rear'):self.relate('connect','deck',n)
