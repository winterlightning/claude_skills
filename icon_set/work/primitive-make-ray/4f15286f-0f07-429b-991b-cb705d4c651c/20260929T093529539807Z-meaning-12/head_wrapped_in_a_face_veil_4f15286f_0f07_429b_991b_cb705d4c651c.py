from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4f15286f-0f07-429b-991b-cb705d4c651c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-wrapped-in-a-face-veil/20260929T093041Z-thuan-mac/reference/avatar islamic women niqab 2_4f15286f-0f07-429b-991b-cb705d4c651c.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-wrapped-in-a-face-veil'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Make a narrow eye opening and a full draped face veil with a diagonal fabric fold and broad shoulders.
    # Original/current comparison: The old niqab reads as a smiling helmet; the entire lower face is exposed by the U-shaped opening.
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
        self.path('hood',(11,21), [('A',(37,21),13,17,True),('L',(40,44))])
        self.path('left-drape',(11,21), [('L',(8,44))])
        self.line('slit-top',(11,21),(37,21))
        self.path('slit-bottom',(12,28), [('A',(36,28),25,8,False)])
        self.path('fold',(12,28), [('A',(37,38),27,15,False)])
        self.path('shoulders',(8,44), [('A',(18,39),14,14,True)])
