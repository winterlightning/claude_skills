"""Restored double-walled cuffs with locking shoulders and a curved link in the reference’s diagonal arrangement.
Before: The rejected drawing shows two plain rings connected by a hook, omitting the cuff thickness and locking shoulders.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ad5f17ec-d6f2-402a-8907-dbd8532598e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Small annular gaps and locking shoulders are essential for cuffs rather than generic rings; the diagonal link stays clear. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'daadeaa8f569245eeb8f7eece4728a71f252a0df0fb3bd007af879d3905d6828'}
    icon_id = 'handcuffs-with-curved-link'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'crime'
    aliases = ()
    keywords = ('hand', 'tools shackle')

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

        # Lower-left and upper-right cuff assemblies share a loose curved connector.
        self.path('link',(11,26),(8,21),(5,14,9,9,True),(10,6,8,8,True),(20,7,10,10,True),(28,13))
        self.path('lower-cuff',(8,26),(16,26),(17,30),(21,36,8,8,True),(12,44,9,8,True),(3,36,9,8,True),(7,30),(8,26),closed=True)
        self.circle('lower-hole',12,36,4)
        self.path('upper-cuff',(27,12),(26,9),(30,5),(34,9),(35,8),(44,17,9,9,True),(35,26,9,9,True),(26,17,9,9,True),(27,12),closed=True)
        self.circle('upper-hole',35,17,4)

