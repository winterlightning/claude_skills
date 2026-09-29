from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'acc6f9a7-f1e5-46cf-961e-ce00f3dd0639'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-facing-down-batch-024-02/20260929T093041Z-thuan-mac/reference/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hand-facing-down-batch-024-02'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore a closed wrist, horizontal back of hand, angled pointing index, thumb and palm crease.
    # Original/current comparison: The open wrist and bulbous hooked finger of the old drawing read like a bent arrow.
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
        self.path('hand',(4,15), [('L',(12,15)),('L',(23,11)),('A',(29,12),8,8,True),('L',(42,24)),('A',(38,30),4,4,True),('L',(29,23)),('L',(24,31)),('A',(17,35),9,8,True),('L',(4,31)),('L',(4,15))],True)
        self.path('thumb',(16,25), [('L',(26,22)),('A',(30,25),4,4,True)])
