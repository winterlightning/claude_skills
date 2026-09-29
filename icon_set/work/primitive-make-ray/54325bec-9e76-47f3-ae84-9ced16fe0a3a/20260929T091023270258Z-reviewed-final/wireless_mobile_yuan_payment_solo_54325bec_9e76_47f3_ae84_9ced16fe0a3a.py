"""Restore a closed rounded phone, two separated wireless arcs and a legible yuan symbol; omit the crowded bottom divider."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '54325bec-9e76-47f3-ae84-9ced16fe0a3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-mobile-yuan-payment-solo/20260929T085457Z-thuan-mac/reference/mobile phone yuan sign wireless_54325bec-9e76-47f3-ae84-9ced16fe0a3a.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'wireless-mobile-yuan-payment-solo'
    keyshape = Keyshape.VRECT_L
    exception = {'reason': 'Keep the closed phone, two distinct wireless arcs and readable yuan glyph. Local arc/device and glyph spacing is tighter than the solo guide but visibly separated at 48px. The bottom divider was removed to avoid a crowded small opening.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9d6cb54391f60fe1dc94f9149354fe9555d1d6be35afe19e767aef5464a6bed5'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('mobile phone yuan sign wireless',)
    # Symbol plan: Restore a closed rounded phone, two separated wireless arcs and a legible yuan symbol; omit the crowded bottom divider.
    # Construction: lucide/original/smartphone.svg and atomic-debug/smartphone.svg: closed rounded phone housing; source: two wireless arcs.

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        self.box('phone',13,18,35,44,3)
        self.path('wireless-outer',(8,8),((40,8),24,18,True,False))
        self.path('wireless-inner',(16,13),((32,13),14,10,True,False))
        self.path('yuan',(20,24),(24,30),(28,24))
        self.add_line('yuan-stem',(24,30),(24,36))
        self.add_line('yuan-bar',(20,32),(28,32))
        self.relate('connect','yuan','yuan-stem')
        self.relate('connect','yuan-stem','yuan-bar')
     
