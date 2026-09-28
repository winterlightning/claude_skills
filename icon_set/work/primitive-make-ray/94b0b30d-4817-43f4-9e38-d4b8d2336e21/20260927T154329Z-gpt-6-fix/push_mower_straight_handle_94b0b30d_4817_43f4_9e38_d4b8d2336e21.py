"""Fresh revision of push-mower-straight-handle.

Original and rejected SVG compared before drawing. The engine housing and deck were too tall and boxy; lowered the housing and extended the cutting deck toward the wheels.
"""
"""Push Lawn Mower Machine.
Plan: Left-facing flat-deck mower with matching wheels and one straight rising handle. Extrema (4,8)-(44,40).
Reference: Lucide tractor: circular wheels and shared frame joints.
Reduction: Wheel hubs and thin undercarriage removed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '94b0b30d-4817-43f4-9e38-d4b8d2336e21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__push-mower-straight-handle/20260927T153833Z-thuan-mac-1/reference/lawn mower_94b0b30d-4817-43f4-9e38-d4b8d2336e21.svg'
AUTHOR = "gpt-6"

class Batch29Icon(Solo48):
    icon_id = 'push-mower-straight-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('push', 'lawn', 'mower', 'machine')

    def build(self):

        for n,x in (('front',10),('rear',34)):
            self.add_arc(n+'-a',(x,28),(x,40),radius_x=6)
            self.add_arc(n+'-b',(x,40),(x,28),radius_x=6)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        self.add_polyline('deck',(10,28),(10,22),(16,22),(30,22),(34,22),(34,28))
        self.add_polyline('engine',(16,22),(16,16),(28,16),(28,22))
        self.add_line('handle',(34,22),(44,8))
        self.relate('connect','deck','engine');self.relate('connect','deck','handle')
        for n in ('front','rear'):self.relate('connect','deck',n)
