from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__harp/20260929T093041Z-thuan-mac/reference/harp_c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'harp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Give the harp a curved neck, upright pillar, sloping soundboard, three unequal strings and a distinct foot.
    # Original/current comparison: The rejected harp is a rigid triangular ladder; it loses the curved neck and sounding-board shape.
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
        self.path('neck',(10,10), [('A',(24,15),15,12,True),('A',(38,17),10,8,False),('L',(42,15))])
        self.poly('frame',(10,6),(10,42),(42,15))
        self.line('base',(6,42),(27,42))
        for i,(x,top,bottom) in enumerate(((18,12,35),(26,16,28))):
            self.line(f'string-{i}',(x,top),(x,bottom))
        self.relate('connect','frame','base')
