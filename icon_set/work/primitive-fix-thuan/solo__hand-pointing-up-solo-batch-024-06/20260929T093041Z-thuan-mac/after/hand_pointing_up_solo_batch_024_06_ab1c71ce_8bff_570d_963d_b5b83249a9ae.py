from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ab1c71ce-8bff-570d-963d-b5b83249a9ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-up-solo-batch-024-06/20260929T093041Z-thuan-mac/reference/hand pointer top_ab1c71ce-8bff-570d-963d-b5b83249a9ae.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'hand-pointing-up-solo-batch-024-06'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Three curled fingers need 6-unit centerline pitch (2px visible gaps). Native-size inspection confirms separated folds and an unmistakable upright pointing index.', 'approved_by': 'user-authorized-agent-review', 'approved_on': '2026-09-29', 'svg_sha256': '6607fec5e2acc68fab4d135b8727215aba83108fa0635a4f9626c50995d33743'}
    aliases = ()
    keywords = ()
    # Plan: Keep the upright index and add three distinct curled fingers, a natural thumb and a round palm.
    # Original/current comparison: The old pointer has only two curled fingertips and an oversized thumb, weakening its hand silhouette.
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
        self.path('hand',(8,27), [('L',(8,24)),('A',(14,24),3,3,True),('L',(14,21)),('A',(20,21),3,3,True),('L',(20,19)),('A',(26,19),3,3,True),('L',(26,8)),('A',(34,8),4,4,True),('L',(34,25)),('A',(40,27),5,4,True),('L',(40,30)),('L',(33,40)),('A',(25,44),10,10,True),('L',(23,44)),('A',(8,29),15,15,True),('L',(8,27))],True)
        self.line('finger-fold-a',(14,24),(14,29))
        self.line('finger-fold-b',(20,21),(20,28))
        self.line('finger-fold-c',(26,19),(26,27))
