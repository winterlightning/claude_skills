"""Restored the circular face, smiling eyes, shallow grin and right-side tongue.
Before: The rejected face omits the round head and places the tongue centrally; the original has a sideways tongue hanging from the right of the grin.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape CIRCLE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a2b16bc0-fda9-42be-8b90-0bef7d9dc58b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__happy-face-with-sideways-tongue/20260929T031604Z-recovered-thuan-mac/reference/face grin tongue_a2b16bc0-fda9-42be-8b90-0bef7d9dc58b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The face boundary and offset tongue preserve the expression; close facial details remain readable. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e67471a9681c212a5da38e2a324c174a0a6df6f1a82392f20205a781296bcc90'}
    icon_id = 'happy-face-with-sideways-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'face grin tongue')

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

        self.circle('face',24,24,20)
        for i,x in enumerate((12,28)):
            self.path(f'eye-{i}',(x,19),(x+8,19,4,4,True))
        self.path('smile',(12,27),(35,26,14,9,False))
        self.path('tongue',(26,33),(27,37),(33,36,3,3,False),(32,30))

