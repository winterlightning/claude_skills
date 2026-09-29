"""Restored a rounded sole, stepped toes, a pressure thumb on the sole and curved fingers around the outside.
Before: The rejected foot is a rectangular shape with tiny bumps and the hand becomes a large angular hook, losing the massage action.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Toe and gripping-finger spacing is intentionally compact so the foot massage remains recognizable. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5f50b242d85e6ec779993f3e0a53abe44b103a44bbbcfd485ac34a3e795969aa'}
    icon_id = 'hand-massaging-foot-8ab52d55'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('hand', 'massage foot')

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

        # Rounded foot outline and a separate open-wrist hand pressing the sole.
        self.path('foot',(6,11),(6,32),(15,41,9,9,False),(23,38))
        self.path('toes',(6,11),(14,11,4,4,True),(14,12),(20,12,3,3,True),(20,13),(26,13,3,3,True),(26,15),(32,15,3,3,True),(32,19))
        for i,(x,y) in enumerate(((14,12),(20,13),(26,15))):
            self.add_line(f'toe-seam-{i}',(x,y),(x,y+3))
            self.relate('connect','toes',f'toe-seam-{i}')
        self.path('thumb',(31,32),(23,25),(18,30,4,4,False),(29,44))
        self.path('hand-back',(40,44),(42,34),(40,27,12,12,False),(35,22),(29,19),(26,23,3,3,False),(31,27),(31,32))
        self.relate('connect','thumb','hand-back')

