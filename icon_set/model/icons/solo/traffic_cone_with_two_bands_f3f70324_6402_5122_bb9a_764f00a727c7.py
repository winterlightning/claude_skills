"""Traffic Cone with Two Bands.

Symbol plan: A symmetric cone on a wide base; shared slopes own both band joins. Base is a single ground bar.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3f70324-6402-5122-bb9a-764f00a727c7'
SOURCE_PATH = 'pictographic-primitives/construction/construction cone_f3f70324-6402-5122-bb9a-764f00a727c7.svg'
AUTHOR = 'gpt-6'


class TrafficConeWithTwoBands(Solo48):
    icon_id = 'traffic-cone-with-two-bands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('traffic', 'cone', 'with', 'two', 'bands')

    def build(self):
        axis=24
        self.path('cone',(9,44),(13,28),(15,20),(19,4),(29,4),(33,20),(35,28),(39,44),(9,44),closed=True)
        for name,y,x in [('upper-band',20,15),('lower-band',28,13)]:
            self.add_line(name,(x,y),(2*axis-x,y));self.relate('connect',name,'cone')
        self.add_line('base-left',(8,44),(9,44));self.add_line('base-right',(39,44),(40,44))
        self.relate('connect','base-left','cone');self.relate('connect','base-right','cone')

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
