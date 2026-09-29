"""Restored the raised left arm, broad upper-body silhouette, lowered right hand and handled briefcase.
Before: The rejected full stick figure reverses the waving arm and reduces the briefcase to a small square; the reference shows a waving upper-body figure with a handled case.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '459ca9bc-41c3-44a7-bd18-4322e40df660'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The raised arm and handled briefcase define the hailing action; close handle/case anatomy is retained. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '553a805e200b263c62e9b14dc1a3eb5b4a2cb36adf08f35fefdfadf10b9d05a3'}
    icon_id = 'briefcase-carrying-hailing-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'taxi wave businessman')

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

        # Circular head above broad shoulders; left arm hails, right arm holds a case.
        self.circle('head',24,9,5)
        self.path('body',(16,44),(16,28),(6,15),(10,11,3,3,True),(20,22),(31,22),(36,27,5,5,True),(36,32))
        self.add_line('arm-inside',(31,28),(31,32))
        self.path('case-handle',(31,34),(31,31),(37,31,3,3,True),(37,34))
        self.path('case',(28,34),(41,34),(44,37,3,3,True),(44,42),(41,45,3,3,True),(28,45),(25,42,3,3,True),(25,37),(28,34,3,3,True),closed=True)
        # Head lower centerline y14 to shoulder y22 is exactly 8: 4px clear ink.

