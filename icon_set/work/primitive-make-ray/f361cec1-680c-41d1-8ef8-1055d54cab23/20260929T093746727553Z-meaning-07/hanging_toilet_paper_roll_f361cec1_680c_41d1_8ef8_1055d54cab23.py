from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f361cec1-680c-41d1-8ef8-1055d54cab23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-toilet-paper-roll/20260929T093041Z-thuan-mac/reference/toilet paper_f361cec1-680c-41d1-8ef8-1055d54cab23.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hanging-toilet-paper-roll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Draw a side ellipse and core, a broad hanging sheet, perforations and a gently uneven torn edge.
    # Original/current comparison: The old roll resembles a hanging label; it has no paper/roll boundary or perforation marks.
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
        self.oval('roll-end',33,15,7,11)
        self.line('core',(33,12),(33,18))
        self.path('sheet',(33,4), [('L',(18,4)),('A',(8,14),10,10,False),('L',(8,41)),('L',(14,44)),('L',(20,41)),('L',(26,44)),('L',(26,15))])
        self.line('perforation',(16,23),(18,23))
        self.relate('connect','sheet','roll-end')
