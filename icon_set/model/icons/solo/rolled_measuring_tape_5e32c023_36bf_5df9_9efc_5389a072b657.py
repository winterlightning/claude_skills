"""Rolled Measuring Tape.

Symbol plan: A shallow top coil over a taller cylindrical front, loose tail and two scale ticks. The fine spiral becomes a short centre mark.
Lucide construction: ruler; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e32c023-36bf-5df9-9efc-5389a072b657'
SOURCE_PATH = 'pictographic-primitives/clothes/clothes design tape measure_5e32c023-36bf-5df9-9efc-5389a072b657.svg'
AUTHOR = 'gpt-6'


class RolledMeasuringTape(Solo48):
    icon_id = 'rolled-measuring-tape'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('rolled', 'measuring', 'tape')

    def build(self):
        self.path('roll',(4,17),(32,17,14,9,True),(4,17,14,9,True),closed=True)
        self.path('front',(4,17),(4,32),(18,40,14,8,False),(30,40),(44,40),(44,28),(32,28),(32,17))
        self.relate('connect','roll','front')
        for n,x in [('left',18),('right',30)]:
            self.add_line(n+'-tick',(x,40),(x,36));self.relate('connect','front',n+'-tick')
        self.add_line('coil-centre',(14,17),(22,17))

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
