"""Restored the extended horizontal fingers, gently curved palm, and three rising heat waves beneath.
Before: The rejected hand is an angular downward hook, rather than the flat hovering palm in the reference.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape HRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The flat hovering hand and repeated heat waves keep their natural silhouette despite keyshape and compact palm-spacing findings. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9fad8b7d446517c09c8473c2d3562a84edefc77176521340d34cce40095f8d46'}
    icon_id = 'hand-over-heat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hand', 'hand with flame')

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

        # Flat hand enters from upper right above a three-wave heat series.
        self.path('fingers',(34,6),(25,6),(8,13),(5,18,4,4,False),(9,21,4,4,False),(19,16),(26,16))
        self.path('palm',(16,18),(20,22),(30,22),(35,18,8,8,False),(42,6))
        for i,x in enumerate((11,24,37)):
            self.path(f'heat-{i}',(x,30),(x-1,36,5,5,False),(x,43,6,6,True))

