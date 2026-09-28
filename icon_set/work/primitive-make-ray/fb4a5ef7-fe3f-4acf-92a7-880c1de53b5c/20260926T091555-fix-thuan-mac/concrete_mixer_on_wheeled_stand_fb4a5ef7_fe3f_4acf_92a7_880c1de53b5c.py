"""Concrete Mixer on Wheeled Stand.

Symbol plan: A rounded mixing drum with an open upper profile and seam, axle frame, two solid dot wheels and a rising handle. The frame sits clear of the drum.
Lucide construction: construction; original and atomic-debug inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fb4a5ef7-fe3f-4acf-92a7-880c1de53b5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__concrete-mixer-on-wheeled-stand/20260926T085631Z-thuan-mac/reference/construction mortar machine_fb4a5ef7-fe3f-4acf-92a7-880c1de53b5c.svg'
AUTHOR = 'claude-opus-5-5'


class ConcreteMixerOnWheeledStand(Solo48):
    icon_id = 'concrete-mixer-on-wheeled-stand'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('concrete', 'mixer', 'on', 'wheeled', 'stand')

    def build(self):
        self.path('drum',(4,16),(10,8),(26,8),(32,16),(18,23,14,7,True),(4,16,14,7,True),closed=True)
        self.add_line('seam',(4,16),(32,16));self.relate('connect','seam','drum')
        self.path('stand',(4,32),(18,32),(44,32),(44,12),(42,8))
        self.add_line('support',(18,23),(18,32));self.relate('connect','support','drum');self.relate('connect','support','stand')
        # Review: wheels become two dots, 8 below the stand (straight-to-dot).
        for n,x in [('left',12),('right',36)]:
            self.add_dot(n+'-wheel',(x,40))

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
