from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__helmet-protection/20260929T093041Z-thuan-mac/reference/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'helmet-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()
    # Plan: Raise the rectangular center ridge above two round shell lobes and preserve a broad protective brim.
    # Original/current comparison: The center ridge of the rejected hard hat is flush with the dome, making it look like a beanie or cage.
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
        self.path('ridge',(20,28), [('L',(20,10)),('A',(22,8),2,2,True),('L',(26,8)),('A',(28,10),2,2,True),('L',(28,28))])
        self.path('shell-left',(8,32), [('L',(8,28)),('A',(20,14),12,14,True)])
        self.path('shell-right',(28,14), [('A',(40,28),12,14,True),('L',(40,32))])
        self.path('brim',(6,32), [('L',(42,32)),('A',(44,34),2,2,True),('L',(44,38)),('A',(42,40),2,2,True),('L',(6,40)),('A',(4,38),2,2,True),('L',(4,34)),('A',(6,32),2,2,True)],True)
