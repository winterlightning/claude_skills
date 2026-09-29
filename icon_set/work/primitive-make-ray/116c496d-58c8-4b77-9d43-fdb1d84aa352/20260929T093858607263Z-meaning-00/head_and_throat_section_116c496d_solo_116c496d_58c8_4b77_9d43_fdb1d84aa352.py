from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '116c496d-58c8-4b77-9d43-fdb1d84aa352'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-and-throat-section-116c496d-solo/20260929T093041Z-thuan-mac/reference/throat problem_116c496d-58c8-4b77-9d43-fdb1d84aa352.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-and-throat-section-116c496d-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore a left-facing skull profile and an open oral passage flowing into the throat; keep the tongue separate.
    # Original/current comparison: The old parallel bent strokes read like plumbing, losing the mouth, tongue and anatomical neck.
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
        self.path('skull',(12,20), [('A',(40,20),14,16,True),('L',(40,27)),('A',(37,34),10,10,True),('L',(37,44))])
        self.poly('nose-mouth',(12,20),(8,27),(18,27))
        self.path('throat',(18,27), [('A',(29,38),11,11,True),('L',(29,44))])
        self.path('tongue',(12,36), [('L',(17,36)),('A',(20,39),3,3,True),('L',(20,44))])
        self.relate('connect','skull','nose-mouth')
        self.relate('connect','nose-mouth','throat')
