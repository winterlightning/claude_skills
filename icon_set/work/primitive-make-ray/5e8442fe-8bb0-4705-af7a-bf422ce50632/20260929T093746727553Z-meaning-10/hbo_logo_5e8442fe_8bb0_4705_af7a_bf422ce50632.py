from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5e8442fe-8bb0-4705-af7a-bf422ce50632'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hbo-logo/20260929T093041Z-thuan-mac/reference/hbo logo_5e8442fe-8bb0-4705-af7a-bf422ce50632.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hbo-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore aligned H, rounded double-bowl B and a broader O; preserve the reference wordmark without extra symbols.
    # Original/current comparison: The old B is narrow and pointed and the O is a thin ellipse; the lettering reads as unrelated symbols.
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
        self.line('h-left',(4,12),(4,36))
        self.line('h-right',(10,12),(10,36))
        self.line('h-crossbar',(4,24),(10,24))
        self.path('b',(17,12), [('A',(17,24),6,6,True),('A',(17,36),6,6,True),('L',(17,12))],True)
        self.oval('o',37,24,7,12)
