from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2723da16-ddad-4fba-89e3-2da6909c1ad1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mother-nursing-baby-2723da16-solo/20260929T094944Z-thuan-mac/reference/mother baby 1_2723da16-ddad-4fba-89e3-2da6909c1ad1.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mother-nursing-baby-2723da16-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the enclosing maternal body, baby head, diagonal baby body and supporting arm. Close anatomical contacts in the nursing/cradling pose are intentional; the two heads and supported baby remain clearly distinguishable.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': '566ce5bec442df1ca14c05f5f90319d40fb15d5d1c2c203c09f5010cc53e3816'}
    aliases = ()
    keywords = ()
    # Plan: Restore a continuous seated maternal silhouette, baby head and diagonal baby body supported by a curved arm.
    # Original/current comparison: The mother and baby are detached rings above an open cradle line, losing the enclosing maternal body and nursing pose.
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
        self.circle('mother-head',20,10,6)
        self.circle('baby-head',35,26,5)
        self.path('body',(15,20), [('A',(8,31),13,13,False),('A',(24,44),16,13,False),('A',(40,34),16,12,False)])
        self.path('arm',(15,31), [('A',(23,37),8,6,False),('L',(31,37))])
        self.path('baby-body',(32,31), [('A',(23,37),13,13,False)])
        self.line('shoulder',(25,20),(29,23))
