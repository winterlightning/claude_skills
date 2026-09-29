from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '27b13dec-64c9-52f3-b0c7-06e23b9be3cf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headache-profile-27b13dec/20260929T093041Z-thuan-mac/reference/medical condition head pain_27b13dec-64c9-52f3-b0c7-06e23b9be3cf.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'headache-profile-27b13dec'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore two continuous heat/pain waves and a recognizable forehead, nose, chin and neck.
    # Original/current comparison: The old pain marks are stacked dots and the head looks like a question-mark bulb.
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
        self.path('skull',(13,22), [('A',(40,28),14,13,True),('A',(35,37),13,13,True),('L',(35,44))])
        self.path('profile',(13,22), [('L',(8,31)),('L',(14,31)),('L',(14,35)),('A',(21,40),7,5,False),('L',(21,44))])
        for n,x in enumerate((22,31)):
            self.path(f'pain-wave-{n}',(x,4), [('A',(x+2,9),5,4,False),('A',(x,14),5,4,True)])
        self.relate('connect','skull','profile')
