"""Make a wide handled luggage case beside a uniformed officer with a peaked cap and connected carrying arm."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0cf3451d-bb7d-4df0-ac79-82ed86479f64'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__security-officer-with-bag/20260929T085457Z-thuan-mac/reference/security officer luggage_0cf3451d-bb7d-4df0-ac79-82ed86479f64.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'security-officer-with-bag'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Keep a squat luggage case with its handle and a peaked uniform cap. Compact handle/crown openings and the natural bust/prop footprint preserve the reference meaning at native size.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6ba716a204437b4e2930ca0475811ab8e85e61c5916c7afbb30a2b4f2cc9980e'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('security officer luggage',)
    # Symbol plan: Make a wide handled luggage case beside a uniformed officer with a peaked cap and connected carrying arm.
    # Construction: human_ref/user.svg: circular jaw and shoulders; original reference: squat handled luggage.

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

        self.box('bag',4,29,19,43,3)
        self.path('bag-handle',(8,29),(8,24),((15,24),4,4,True,False),(15,29))
        self.path('cap',(28,13),(25,5),(43,8),(41,13),(28,13),closed=True)
        self.add_line('visor',(24,13),(28,13))
        self.path('jaw',(28,13),((40,13),6,6,False,False))
        self.path('body',(27,44),(27,33),(22,37),(19,37))
        self.path('shoulders',(27,33),(29,27),(34,32),(39,27),
                  ((44,35),6,9,True,False),(44,44))
        self.relate('connect','bag','bag-handle')
        self.relate('connect','body','bag')
        self.relate('connect','body','shoulders')
     
