"""Rebuilt a shallow canoe hull with raised ends and a gently dipping rim, removing the invented braces.
Before: The rejected canoe has two vertical towers and interior braces; the original is a shallow curved hull with a continuous rim.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape HRECT_M; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2f08daf6-071b-5ac7-9717-2239ffbb2925'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'canoe'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'canoe')

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

        # One closed hull contour; raised bow/stern and a dipping gunwale, no interior struts.
        self.path('hull',(6,14),(42,14,18,8,False),(44,25),(4,25,20,10,True),(6,14),closed=True)

