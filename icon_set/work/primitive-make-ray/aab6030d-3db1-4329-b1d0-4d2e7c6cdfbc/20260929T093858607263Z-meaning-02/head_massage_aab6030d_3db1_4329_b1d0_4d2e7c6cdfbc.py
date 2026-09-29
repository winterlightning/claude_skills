from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'aab6030d-3db1-4329-b1d0-4d2e7c6cdfbc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-massage/20260929T093041Z-thuan-mac/reference/thai massage head_aab6030d-3db1-4329-b1d0-4d2e7c6cdfbc.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-massage'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Show the therapist behind, two hands at the temples, a larger seated head and curved shoulders.
    # Original/current comparison: The old masseur and client merge into a table-like loop; hands do not clearly touch the client head.
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
        self.circle('therapist-head',24,8,4)
        self.path('therapist-body',(17,30), [('L',(12,30)),('A',(8,26),4,4,True),('L',(8,25)),('A',(16,20),8,5,True),('L',(32,20)),('A',(40,25),8,5,True),('L',(40,26)),('A',(36,30),4,4,True),('L',(31,30))])
        self.circle('client-head',24,30,4)
        self.path('client-shoulders',(12,44), [('A',(36,44),12,2,True)])
        self.line('left-hand',(17,27),(17,33))
        self.line('right-hand',(31,27),(31,33))
        self.relate('connect','therapist-body','left-hand')
        self.relate('connect','therapist-body','right-hand')
