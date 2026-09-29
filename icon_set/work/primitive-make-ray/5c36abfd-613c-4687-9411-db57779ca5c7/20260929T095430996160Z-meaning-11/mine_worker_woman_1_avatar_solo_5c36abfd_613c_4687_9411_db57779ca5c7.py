from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5c36abfd-613c-4687-9411-db57779ca5c7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mine-worker-woman-1-avatar-solo/20260929T094854Z-thuan-mac/reference/mine worker woman_5c36abfd-613c-4687-9411-db57779ca5c7.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mine-worker-woman-1-avatar-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore a broad helmet brim, distinct headlamp, round jaw and outward-flaring hair.
    # Original/current comparison: The miner has a box-like jaw and hanging vertical hair, losing the female portrait and flared hair of the reference.
    # References: claimed original; Lucide smartphone/lock-open/headset/memory-stick/drone
    # original and atomic-debug where applicable; human_ref/user.svg and full_body_ref.png.
    # Paired anatomical parts share parameters; directional profiles stay asymmetric.

    def path(self, name, start, steps, closed=False):
        members = []
        here = start
        for i, step in enumerate(steps):
            member = f"{name}-{i}"
            if step[0] == "L":
                self.add_line(member, here, step[1])
            else:
                self.add_arc(member, here, step[1], radius_x=step[2], radius_y=step[3], sweep=step[4])
            here = step[1]
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)], True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), [("A",(x+rx,y),rx,ry,True),("A",(x-rx,y),rx,ry,True)], True)

    def poly(self, name, *points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def line(self, name, a, b):
        self.add_line(name, a, b)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),[("L",(x+w-r,y)),("A",(x+w,y+r),r,r,True),("L",(x+w,y+h-r)),("A",(x+w-r,y+h),r,r,True),("L",(x+r,y+h)),("A",(x,y+h-r),r,r,True),("L",(x,y+r)),("A",(x+r,y),r,r,True)],True)

    def phone(self):
        self.rect('phone',10,4,28,40,4)
        self.add_line('screen-bottom',(10,36),(38,36))
        self.relate('connect','phone','screen-bottom')

    def wireless(self):
        self.add_arc('signal-outer',(8,9),(40,9),radius_x=24,radius_y=16,sweep=True)
        self.add_arc('signal-inner',(17,14),(31,14),radius_x=12,radius_y=9,sweep=True)

    def build(self):
        self.circle('lamp',24,10,4)
        self.path('helmet-left',(9,23), [('A',(19,10),15,15,True)])
        self.path('helmet-right',(29,10), [('A',(39,23),15,15,True)])
        self.line('brim',(6,23),(42,23))
        self.path('jaw',(14,24), [('A',(34,24),10,10,False)])
        for side in (-1,1):
            x=lambda v:24+side*v
            self.path(f'hair-{side}',(x(13),26), [('A',(x(18),38),25,25,side<0),('A',(x(7),39),10,6,side<0)])
