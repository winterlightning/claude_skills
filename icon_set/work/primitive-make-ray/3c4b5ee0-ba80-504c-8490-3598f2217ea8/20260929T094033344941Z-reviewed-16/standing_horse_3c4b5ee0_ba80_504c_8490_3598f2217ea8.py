from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3c4b5ee0-ba80-504c-8490-3598f2217ea8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-horse/20260929T093041Z-thuan-mac/reference/animal horse_3c4b5ee0-ba80-504c-8490-3598f2217ea8.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'standing-horse'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the horse muzzle, long neck, slim outlined legs and curved tail. Natural tapered limbs and optical bounds are intentionally retained rather than reverting to blocky proportions.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': '1f6a1f28d5c12a6d27e6f26d2814e2bf86e661a6d2fb0389ac17e65a1b737049'}
    aliases = ()
    keywords = ()
    # Plan: Restore an upright equine neck, pointed ear, long muzzle, slim separated legs and curved tail.
    # Original/current comparison: The old horse is a blocky dog shape with a short neck, square legs and no mane.
    # References: claimed original; Lucide hand/hard-hat/ear/triangle-alert
    # construction where applicable; human_ref/user.svg and full_body_ref.png.
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

    def build(self):
        self.path('horse',(6,20), [('L',(13,16)),('L',(17,8)),('L',(21,17)),('L',(23,24)),('A',(27,27),4,4,False),('L',(35,27)),('A',(40,32),5,5,True),('L',(39,40)),('L',(34,40)),('L',(33,33)),('L',(21,33)),('L',(19,40)),('L',(14,40)),('L',(15,25)),('L',(8,27)),('A',(6,20),4,4,True)],True)
        self.path('tail',(38,28), [('A',(44,36),8,8,True)])
        self.line('mane',(21,18),(25,25))
