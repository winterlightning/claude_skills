"""Roadwork Barricade with Lamps.

Symbol plan: A wide board has two matching warning lamps, two legs, and one diagonal stripe. All joints reuse board nodes.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '020121c8-002f-41bd-b16f-1e79c57331e8'
SOURCE_PATH = 'pictographic-primitives/construction/construction sign_020121c8-002f-41bd-b16f-1e79c57331e8.svg'
AUTHOR = 'gpt-6'


class RoadworkBarricadeWithLamps(Solo48):
    icon_id = 'roadwork-barricade-with-lamps'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('roadwork', 'barricade', 'with', 'lamps')

    def build(self):
        self.path('board',(6,20),(14,20),(26,20),(34,20),(42,20),(44,22,2,2,True),(44,28),(42,30,2,2,True),(34,30),(22,30),(14,30),(6,30),(4,28,2,2,True),(4,22),(6,20,2,2,True),closed=True)
        for n,x in [('left',14),('right',34)]:
            self.path(n+'-lamp',(x,12),(x,8,2,2,True),(x,12,2,2,True),closed=True)
            self.add_line(n+'-post',(x,12),(x,20));self.relate('connect',n+'-post',n+'-lamp');self.relate('connect',n+'-post','board')
            self.add_line(n+'-leg',(x,30),(x,40));self.relate('connect',n+'-leg','board')
        self.add_line('stripe',(26,20),(22,30));self.relate('connect','stripe','board')

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
