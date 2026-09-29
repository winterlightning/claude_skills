from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '56435dba-6f8c-40dc-9770-3098c81d92d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mecha-head-with-v-antennae/20260929T094854Z-thuan-mac/reference/robot war crime gundam_56435dba-6f8c-40dc-9770-3098c81d92d5.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'mecha-head-with-v-antennae'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore V antennae, paired angular eyes, side ear housings and a tapered armored jaw.
    # Original/current comparison: The rejected mecha head is a Y-shaped antenna above a rounded box with no eyes or mechanical cheek structure.
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
        self.poly('crest',(6,6),(24,19),(42,6))
        self.line('crest-stem',(24,19),(24,23))
        self.poly('helmet',(12,19),(12,33),(18,40),(24,42),(30,40),(36,33),(36,19))
        for side in (-1,1):
            x=lambda v:24+side*v
            self.poly(f'eye-{side}',(x(9),25),(x(3),27))
            self.poly(f'ear-{side}',(x(12),23),(x(18),23),(x(18),35),(x(12),35))
        self.poly('mask',(19,34),(24,31),(29,34))
        self.line('chin',(24,35),(24,40))
