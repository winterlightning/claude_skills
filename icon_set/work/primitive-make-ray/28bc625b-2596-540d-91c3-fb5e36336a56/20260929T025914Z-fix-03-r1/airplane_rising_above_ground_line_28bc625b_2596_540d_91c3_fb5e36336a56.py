"""Restored the swept lower wing, tail fin, rounded nose and rising aircraft silhouette above the ground.
Before: The rejected aircraft loses the prominent downward wing and looks like a sloping boat above a line.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape HRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28bc625b-2596-540d-91c3-fb5e36336a56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'airplane-rising-above-ground-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'plane land')

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

        # Plane rises right; a distinct lower swept wing interrupts the fuselage underside.
        self.path('plane',(4,19),(9,18),(15,23),(37,10),(43,12,5,4,True),(41,18,5,4,True),(31,23),(26,34),(20,37),(22,27),(14,30),(9,28,6,6,True),(4,19),closed=True)
        self.add_line('ground',(4,42),(44,42))

