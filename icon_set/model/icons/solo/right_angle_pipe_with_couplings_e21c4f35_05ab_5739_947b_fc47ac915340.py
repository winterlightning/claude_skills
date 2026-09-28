"""Right-Angle Pipe with Couplings.

Symbol plan: A right-angle tube uses concentric tangent corner arcs; sleeves become open U-shaped terminal cuffs.
Lucide construction: paint-roller; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e21c4f35-05ab-5739-947b-fc47ac915340'
SOURCE_PATH = 'pictographic-primitives/construction/construction pipe_e21c4f35-05ab-5739-947b-fc47ac915340.svg'
AUTHOR = 'gpt-6'


class RightAnglePipeWithCouplings(Solo48):
    icon_id = 'right-angle-pipe-with-couplings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('right-angle', 'pipe', 'with', 'couplings')

    def build(self):
        self.path('pipe',(10,34),(10,22),(26,6,16,16,True),(34,6))
        self.path('inside',(22,34),(22,22),(26,18,4,4,True),(34,18))
        self.path('bottom-cuff',(6,42),(6,34),(10,34),(22,34),(26,34),(26,42))
        self.path('right-cuff',(42,6),(34,6),(34,18),(34,26),(42,26))
        for a in ('pipe','inside'):
            for b in ('bottom-cuff','right-cuff'):self.relate('connect',a,b)

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
