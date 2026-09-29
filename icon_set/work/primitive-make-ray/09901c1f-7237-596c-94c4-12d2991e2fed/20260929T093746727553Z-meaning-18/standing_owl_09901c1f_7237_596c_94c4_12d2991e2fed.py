from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '09901c1f-7237-596c-94c4-12d2991e2fed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-owl/20260929T093041Z-thuan-mac/reference/wild bird owl body_09901c1f-7237-596c-94c4-12d2991e2fed.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'standing-owl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore paired eyes, V-shaped beak, brow, one folded wing and a visible standing foot.
    # Original/current comparison: The owl has only one eye and no beak or feet, so its silhouette reads as an abstract leaf.
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
        self.path('outline',(13,18), [('A',(37,18),12,14,True),('L',(36,27)),('A',(26,38),13,13,True),('L',(8,40)),('A',(13,18),58,58,True)],True)
        self.poly('brow',(12,7),(25,17),(39,7))
        self.add_dot('eye-left',(19,21))
        self.add_dot('eye-right',(31,21))
        self.poly('beak',(23,26),(25,28),(27,26))
        self.path('wing',(24,35), [('A',(15,39),15,15,True)])
        self.poly('foot',(29,38),(32,44),(38,44))
