"""Restored a pinching hand across the ID card corner and a recognizable circular-head portrait.
Before: The rejected card replaces the portrait with a dot and dash, and its hand is only two detached lines.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cb16642c-e584-52b6-ae9d-bff1579af112'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-identity-card-solo-b001-03/20260929T031604Z-recovered-thuan-mac/reference/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-identity-card-solo-b001-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'digital policies data breach user')

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

        self.path('card',(25,18),(10,18),(6,22,4,4,False),(6,40),(10,44,4,4,False),(31,44),(35,40,4,4,False),(35,25))
        self.circle('portrait-head',18,25,3)
        self.path('portrait-shoulders',(11,38),(25,38,7,2,True))
        self.path('hand-top',(44,4),(37,9),(29,9),(23,14),(19,18))
        self.path('thumb',(31,15),(25,21),(29,25,3,3,False),(36,20),(40,19),(44,16))
        # Portrait head bottom y28 to shoulder apex y36 gives 4px clear ink.

