from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '81881632-71b6-459a-8cf2-c7d98ac7c325'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-operating-drone/20260929T094854Z-thuan-mac/reference/play drone_81881632-71b6-459a-8cf2-c7d98ac7c325.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'person-operating-drone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore twin rotor arms, landing legs and a person visibly holding a controller.
    # Original/current comparison: The drone is a floating dumbbell and the operator has no hands or controller.
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
        self.rect('drone-body',12,14,16,8,4)
        for side,x in enumerate((8,32)):
            self.line(f'propeller-{side}',(x-4,6),(x+4,6))
            self.path(f'arm-{side}',(x,6), [('L',(x,10)),('A',(12 if side==0 else 28,14),4,4,side==0)])
        self.poly('landing',(16,22),(16,27),(12,29))
        self.circle('head',35,24,4)
        self.path('shoulders',(26,44), [('L',(26,41)),('A',(35,36),9,5,True),('A',(44,41),9,5,True),('L',(44,44))])
        self.line('controller',(31,43),(39,43))
