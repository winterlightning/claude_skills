from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8e5f188b-2874-56f0-8538-ccc3b48f76fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hat-lady-cowboy-avatar-solo/20260929T093041Z-thuan-mac/reference/hat lady cowboy_8e5f188b-2874-56f0-8538-ccc3b48f76fc.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hat-lady-cowboy-avatar-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Use a curved cowboy brim, creased crown, circular jaw, flowing hair and shoulder lines.
    # Original/current comparison: The rejected avatar has square hair and no shoulders; its hat and face merge into a stick-like symbol.
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
        self.poly('crown',(13,17),(16,6),(24,9),(32,6),(35,17))
        self.path('brim',(6,16), [('A',(42,16),21,12,False)])
        self.path('face',(14,22), [('A',(34,22),10,10,False)])
        for side in (-1,1):
            x=lambda v:24+side*v
            self.path(f'hair-{side}',(x(13),24), [('L',(x(15),31)),('A',(x(12),38),7,7,side<0)])
            self.line(f'shoulder-{side}',(x(5),36),(x(13),42))
