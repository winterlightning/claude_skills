"""Redrew a long pointing index, progressively lower finger knuckles, a rounded thumb and a broad smooth palm.
Before: The rejected pointing hand has a squared thumb and abrupt palm transition; the reference has a round palm and stepped curled fingers.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-up/20260929T031604Z-recovered-thuan-mac/reference/finger point 1_6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The curled fingers need compact internal spacing while the long index and palm stay clear. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '968209c350b148ce7eaa2fca3b98e379b575fc81198375a6b365f4d098f222cf'}
    icon_id = 'hand-pointing-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('hand', 'finger point 1')

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

        self.path('hand',(16,28),(16,8),(24,8,4,4,True),(24,22),(30,22,3,3,True),(30,24),(36,24,3,3,True),(36,26),(42,26,3,3,True),(42,33),(31,44,11,11,True),(22,44),(12,38,14,14,True),(5,28),(11,22,4,4,True),(16,28),closed=True)
        for i,(x,y) in enumerate(((24,22),(30,24),(36,26))):
            self.add_line(f'finger-seam-{i}',(x,y),(x,y+4))
            self.relate('connect','hand',f'finger-seam-{i}')

