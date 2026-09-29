"""Restored the reaching hand and diagonal pinch across the identity card’s corner, keeping the portrait centered.
Before: The rejected hand becomes a robotic three-prong claw sitting above the card; the reference shows a hand pinching and taking its upper-right edge.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3ba267b5-9ca9-4999-a24d-b73d45e0c937'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-stealing-identity-card-solo-b005-06'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'identity stolen id card')

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

        # Card and avatar behind a right-entering hand; thumb crosses the upper-right card corner.
        self.path('card',(25,18),(10,18),(6,22,4,4,False),(6,40),(10,44,4,4,False),(31,44),(35,40,4,4,False),(35,25))
        self.circle('portrait-head',18,25,3)
        self.path('portrait-shoulders',(11,38),(25,38,7,2,True))
        self.path('hand-top',(44,4),(37,9),(29,9),(23,14),(19,18))
        self.path('thumb',(31,15),(25,21),(29,25,3,3,False),(36,20),(40,19),(44,16))
        # Portrait head ends y28 and shoulder apex y36: exact 4px ink clearance.

