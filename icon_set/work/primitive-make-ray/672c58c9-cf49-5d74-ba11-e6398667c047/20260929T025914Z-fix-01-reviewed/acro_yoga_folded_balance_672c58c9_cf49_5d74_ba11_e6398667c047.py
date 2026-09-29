"""Restored the folded upper flyer, its small head, and the reclining supporting person with raised limbs.
Before: The rejected icon reduces the two-person folded acro-yoga pose to one upside-down stick figure; the second head and curled supporting body disappear.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '672c58c9-cf49-5d74-ba11-e6398667c047'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The original is an interlocked two-person pose; compact contacts and an optical envelope preserve its folded arrangement. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'af7b3f02cd5ac7279ddc4d30cdd04b2f20e6526aab88cba8cabb9c223e620f3f'}
    icon_id = 'acro-yoga-folded-balance'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('hand', 'acro yoga pose')

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

        # Two outlined figures; upper folded legs and torso rest over a reclining base.
        self.path('flyer',(28,4),(33,11,8,8,True),(32,19),(29,24),(13,26),(12,20,3,3,True),(25,18),(25,11),(12,18),(8,14,3,3,True),(23,5),(28,4,8,8,True),closed=True)
        self.circle('flyer-head',35,26,3)
        self.path('base-body',(22,26),(20,38),(26,44,6,6,False),(37,44),(43,38,6,6,False),(43,37),(37,37,3,3,False),(28,37),(27,26))
        self.circle('base-head',8,38,4)
        # Base head right edge x12 and its own body x20 at y38: exact 4px ink gap.

