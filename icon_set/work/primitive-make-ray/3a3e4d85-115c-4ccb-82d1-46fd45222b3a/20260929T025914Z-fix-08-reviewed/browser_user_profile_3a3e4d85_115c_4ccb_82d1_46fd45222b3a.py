"""Restored the full browser chrome, header controls, and centered user profile inside the page.
Before: The rejected browser has short inward tabs rather than a full header separator; reviewer explicitly asks for Browser.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3a3e4d85-115c-4ccb-82d1-46fd45222b3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Full browser chrome and the enclosed profile need compact header spacing; the content remains distinct from the frame. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0c9cb502430df5452a90715526a4561fcd3bdf5764546b2bbe9db9cacb070a91'}
    icon_id = 'browser-user-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('hand', 'browser person')

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

        # Rounded browser frame with full-width header; centered detached avatar beneath.
        self.path('frame',(10,6),(38,6),(42,10,4,4,True),(42,38),(38,42,4,4,True),(10,42),(6,38,4,4,True),(6,10),(10,6,4,4,True),closed=True)
        self.add_line('header',(6,16),(42,16))
        for i,x in enumerate((14,22)):self.add_dot(f'control-{i}',(x,11))
        self.circle('head',24,24,3)
        self.path('shoulders',(16,38),(32,38,8,3,True))
        self.relate('connect','frame','header')
        # Head lower edge y27 to shoulder apex y35: exact 4px visible gap.

