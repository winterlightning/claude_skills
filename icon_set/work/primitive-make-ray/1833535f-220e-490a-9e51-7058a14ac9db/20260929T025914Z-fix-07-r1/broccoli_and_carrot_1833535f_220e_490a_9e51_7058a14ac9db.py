"""Restored a broad diagonal carrot with greens and score mark, plus a scalloped broccoli crown and branched stem.
Before: The rejected carrot is a thin upright spike beside a squat broccoli; the reference shows a rounded diagonal carrot and a branching broccoli stalk.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1833535f-220e-490a-9e51-7058a14ac9db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broccoli-and-carrot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'broccoli carrot')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        # Broccoli canopy at upper left; carrot tilts down-left beside it.
        self.path('crown',(7,22),(4,17,5,5,True),(8,11,6,6,True),(15,6,6,6,True),(22,10,6,6,True),(28,15,6,6,True),(23,22,6,6,True),(17,23),(12,25),(7,22,5,5,True),closed=True)
        self.path('stalk',(12,25),(15,35),(20,36),(22,24))
        self.path('carrot',(24,42),(23,37),(32,24),(39,22,6,6,True),(44,28,6,6,True),(39,35),(28,43),(24,42,4,4,True),closed=True)
        self.add_line('green-up',(38,21),(38,13))
        self.add_line('green-side',(41,23),(45,19))
        self.add_line('carrot-score',(30,29),(33,32))

