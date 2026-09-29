from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '911ac869-135a-4c07-a867-4ded07c4f4e7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-figure-aiming-a-pistol/20260929T093041Z-thuan-mac/reference/athletics shooting_911ac869-135a-4c07-a867-4ded07c4f4e7.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'standing-figure-aiming-a-pistol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Use upright torso, two grounded legs, a straight aiming arm and a distinct barrel above the hand.
    # Original/current comparison: The rejected figure appears seated or running, and the large diagonal stroke obscures the pistol.
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
        self.circle('head',16,10,4)
        self.line('torso',(16,22),(16,32))
        self.poly('legs',(9,42),(16,32),(23,42))
        self.line('aiming-arm',(16,22),(33,22))
        self.line('resting-arm',(16,22),(6,31))
        self.poly('pistol',(33,25),(34,16),(42,16),(42,20),(34,20))
        self.mark_human_figure('shooter',head='head',torso='torso',torso_junction='start')
        self.relate('connect','torso','legs')
        self.relate('connect','torso','aiming-arm')
        self.relate('connect','torso','resting-arm')
