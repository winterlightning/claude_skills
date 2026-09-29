from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c27f28b7-bb52-4f56-a0e7-d5b311d3ed63'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mother-child-silhouette-c27f28b7/20260929T094944Z-thuan-mac/reference/primitive symbols mother_c27f28b7-bb52-4f56-a0e7-d5b311d3ed63.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mother-child-silhouette-c27f28b7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore the child head, torso, arms and legs within the mother silhouette, and add the mother hair tips.
    # Original/current comparison: The child is just a dot and T-shape inside a dress; the source shows a complete little person and maternal hair.
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
        self.circle('mother-head',24,9,5)
        self.path('hair-left',(19,10), [('A',(15,15),7,7,True)])
        self.path('hair-right',(29,10), [('A',(33,15),7,7,False)])
        self.path('mother-body',(8,44), [('L',(15,25)),('A',(33,25),10,7,True),('L',(40,44)),('L',(8,44))],True)
        self.circle('child-head',24,28,3)
        self.line('child-torso',(24,35),(24,39))
        self.poly('child-arms',(20,37),(24,35),(28,37))
        self.poly('child-legs',(20,43),(24,39),(28,43))
        self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
        self.relate('connect','child-torso','child-arms')
        self.relate('connect','child-torso','child-legs')
