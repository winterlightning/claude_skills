from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-and-tablet-devices-solo/20260929T094854Z-thuan-mac/reference/responsive_5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mobile-and-tablet-devices-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore rounded tablet edges and a bottom bezel behind an overlapping, fully outlined phone.
    # Original/current comparison: The tablet is just an open angular bracket, so the pair reads as a phone beside an incomplete shape.
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
        self.path('tablet',(18,17), [('L',(18,10)),('A',(22,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(32,36))])
        self.line('tablet-bezel',(32,29),(42,29))
        self.rect('phone',6,22,19,20,3)
        self.line('phone-bezel',(6,35),(25,35))
        self.relate('connect','tablet','tablet-bezel')
        self.relate('connect','phone','phone-bezel')
