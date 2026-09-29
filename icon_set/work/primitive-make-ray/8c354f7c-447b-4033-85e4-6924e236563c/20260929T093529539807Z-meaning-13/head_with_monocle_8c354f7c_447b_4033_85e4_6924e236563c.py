from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c354f7c-447b-4033-85e4-6924e236563c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-with-monocle/20260929T093041Z-thuan-mac/reference/face with monocle_8c354f7c-447b-4033-85e4-6924e236563c.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-with-monocle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore the circular head, monocle lens, one uncovered eye, short mouth and hanging curved cord.
    # Original/current comparison: The old monocle face is an open C with a disconnected lens and no eye, losing the full-face emoji.
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
        self.circle('face',24,24,20)
        self.circle('monocle',31,19,7)
        self.add_dot('eye',(15,19))
        self.line('mouth',(20,33),(26,33))
        self.path('cord',(38,19), [('L',(38,30)),('A',(34,34),4,4,True)])
