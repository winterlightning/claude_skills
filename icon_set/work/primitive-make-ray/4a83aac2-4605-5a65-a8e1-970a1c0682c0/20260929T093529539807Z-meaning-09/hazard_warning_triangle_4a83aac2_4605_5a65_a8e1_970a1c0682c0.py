from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4a83aac2-4605-5a65-a8e1-970a1c0682c0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hazard-warning-triangle/20260929T093041Z-thuan-mac/reference/hazard warning flasher_4a83aac2-4605-5a65-a8e1-970a1c0682c0.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hazard-warning-triangle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore two nested upright triangles with a generous open central triangle.
    # Original/current comparison: The rejected drawing substitutes an exclamation mark for the inner triangle of the automotive hazard switch.
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
        self.poly('outer',(24,6),(42,42),(6,42),closed=True)
        self.poly('inner',(24,23),(32,35),(16,35),closed=True)
