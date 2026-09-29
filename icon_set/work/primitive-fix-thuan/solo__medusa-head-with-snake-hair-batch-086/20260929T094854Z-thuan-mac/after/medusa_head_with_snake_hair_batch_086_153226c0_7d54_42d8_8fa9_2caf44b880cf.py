from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '153226c0-7d54-42d8-8fa9-2caf44b880cf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__medusa-head-with-snake-hair-batch-086/20260929T094854Z-thuan-mac/reference/meduza gorgon_153226c0-7d54-42d8-8fa9-2caf44b880cf.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'medusa-head-with-snake-hair-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Retain six directional curling snakes around a circular face. Small coil openings and hair/face contacts are intentional; reducing to straight stems would lose Medusa meaning.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': 'bf36236303206634939d39e515d930e64bbe6557b1af7ce2f9b6f54d58fbdb53'}
    aliases = ()
    keywords = ()
    # Plan: Give Medusa a circular jaw, two eyes and four curling snakes with directional heads around the face.
    # Original/current comparison: The old hair consists of four vertical flame-like stems, with no clearly outward-facing snakes.
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
        self.path('jaw',(12,24), [('L',(12,30)),('A',(36,30),12,12,False),('L',(36,24))])
        self.add_dot('eye-left',(19,29))
        self.add_dot('eye-right',(29,29))
        self.line('mouth',(22,36),(26,36))
        for side in (-1,1):
            x=lambda v:24+side*v
            self.path(f'snake-top-{side}',(x(3),22), [('L',(x(3),15)),('A',(x(8),10),5,5,side>0),('L',(x(12),10)),('A',(x(12),6),2,2,side<0),('L',(x(8),6))])
            self.path(f'snake-side-{side}',(x(9),22), [('L',(x(14),22)),('A',(x(18),18),4,4,side<0),('L',(x(18),16))])
            self.path(f'snake-low-{side}',(x(12),30), [('L',(x(17),30)),('A',(x(17),36),3,3,side>0),('L',(x(15),36))])
