from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '24a9c868-e028-5cb9-abe7-46d997efd4de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-hyena/20260929T093041Z-thuan-mac/reference/hyena_24a9c868-e028-5cb9-abe7-46d997efd4de.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'standing-hyena'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Restore low rump, rising back, large rounded ear, heavy muzzle, long front legs and lowered tail.
    # Original/current comparison: The rejected hyena is a generic boxy dog; it lacks the sloping back, heavy front and low hindquarters.
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
        self.path('body',(10,27), [('A',(16,22),7,6,True),('L',(30,16)),('L',(31,12)),('A',(36,12),3,4,True),('L',(37,18)),('L',(44,23)),('L',(41,28)),('L',(36,27)),('L',(34,40)),('L',(29,40)),('L',(28,31)),('A',(18,32),12,6,True),('L',(15,40)),('L',(10,40)),('L',(12,31)),('L',(10,27))],True)
        self.path('tail',(10,27), [('A',(4,35),9,9,False)])
