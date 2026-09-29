from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4d6b18c3-9c28-4f4a-8e22-8679e1c298f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__merlion-statue-solo/20260929T094854Z-thuan-mac/reference/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'merlion-statue-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore the lion muzzle, open mouth, sweeping mane and rounded fish-body base from the source.
    # Original/current comparison: The old Merlion is a generic animal blob with a zigzag nose and no mane crescent or projecting lion muzzle.
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
        self.path('outline',(16,11), [('A',(26,4),10,10,True),('L',(32,4)),('A',(38,14),10,10,True),('L',(38,33)),('A',(14,33),12,11,True),('L',(16,26)),('L',(12,26)),('A',(10,24),2,2,True),('L',(10,22)),('L',(16,22)),('A',(16,17),3,3,False),('L',(12,17)),('A',(10,15),2,2,True),('L',(10,13)),('A',(12,11),2,2,True),('L',(16,11))],True)
        self.path('mane',(26,10), [('A',(24,27),11,11,True)])
        self.poly('fish-collar',(15,30),(21,35),(27,30),(37,33))
