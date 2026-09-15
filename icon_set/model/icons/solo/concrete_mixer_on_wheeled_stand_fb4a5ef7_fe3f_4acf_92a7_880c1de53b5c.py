"""Concrete Mixer on Wheeled Stand.

Symbol plan: A rounded mixing drum with an open upper profile and seam, axle frame, two circular wheels and a rising handle. The frame sits clear of the drum.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb4a5ef7-fe3f-4acf-92a7-880c1de53b5c'
SOURCE_PATH = 'pictographic-primitives/construction/construction mortar machine_fb4a5ef7-fe3f-4acf-92a7-880c1de53b5c.svg'
AUTHOR = 'gpt-6'


class ConcreteMixerOnWheeledStand(Solo48):
    icon_id = 'concrete-mixer-on-wheeled-stand'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('concrete', 'mixer', 'on', 'wheeled', 'stand')

    def build(self):
        self.path('drum',(4,18),(10,8),(26,8),(32,18),(18,26,14,8,True),(4,18,14,8,True),closed=True)
        self.add_line('seam',(4,18),(32,18));self.relate('connect','seam','drum')
        self.path('stand',(4,34),(12,34),(18,34),(36,34),(44,34),(44,12),(42,8))
        self.add_line('support',(18,26),(18,34));self.relate('connect','support','drum');self.relate('connect','support','stand')
        for n,x in [('left',12),('right',36)]:
            self.path(n+'-wheel',(x,34),(x,40,3,3,True),(x,34,3,3,True),closed=True);self.relate('connect',n+'-wheel','stand')

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
