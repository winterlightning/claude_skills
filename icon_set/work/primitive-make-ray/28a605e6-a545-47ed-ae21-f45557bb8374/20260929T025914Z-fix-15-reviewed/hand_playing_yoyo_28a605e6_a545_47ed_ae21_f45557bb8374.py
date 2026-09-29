"""Restored a pinching hand, a diagonal string, a complete yo-yo with central axle, and two motion arcs.
Before: The rejected yo-yo has a broken second circle and a thick connector, losing the thin string and spinning motion.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28a605e6-a545-47ed-ae21-f45557bb8374'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The thin string, axle and two motion arcs require close spacing but keep the toy’s mechanism legible. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0c4c4b990443cb7f9da96d0e6874a3a96404ca534b58285ce5b8d6e63fd43936'}
    icon_id = 'hand-playing-yoyo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'kids'
    aliases = ()
    keywords = ('hand', 'playing yoyo')

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

        # Pinching hand above a hanging yo-yo; twin arcs indicate swinging/spinning motion.
        self.path('hand-top',(42,6),(31,6),(20,10),(11,10),(6,14,4,4,False),(10,20,4,4,False),(17,15),(25,17))
        self.path('hand-bottom',(18,17),(27,21),(35,18),(42,14))
        self.add_line('string',(16,16),(24,29))
        self.circle('yoyo',32,35,9)
        self.circle('axle',32,35,2)
        self.path('motion-outer',(8,28),(8,43,12,12,False))
        self.path('motion-inner',(14,31),(14,40,8,8,False))

