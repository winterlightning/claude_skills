from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6125bb03-817d-547b-932c-5f4a4b4f96ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-profile-wearing-broad-protective-mask/20260929T093041Z-thuan-mac/reference/air pollution mask_6125bb03-817d-547b-932c-5f4a4b4f96ed.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'head-profile-wearing-broad-protective-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore the domed skull, one eye, projecting mask cup, two straps and neck.
    # Original/current comparison: The rejected mask is a rectangular box across a generic helmet, with no eye or visible head profile.
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
        self.path('head',(12,22), [('A',(40,22),14,18,True),('A',(34,35),17,17,True),('L',(34,44))])
        self.path('mask',(12,22), [('L',(25,25)),('L',(25,37)),('L',(17,39)),('A',(8,30),9,9,True),('L',(8,25)),('A',(12,22),4,3,True)],True)
        self.line('upper-strap',(25,25),(40,21))
        self.line('lower-strap',(25,37),(37,32))
        self.line('neck',(19,40),(19,44))
        self.add_dot('eye',(18,17))
        self.relate('connect','head','mask')
        self.relate('connect','mask','upper-strap')
        self.relate('connect','mask','lower-strap')
