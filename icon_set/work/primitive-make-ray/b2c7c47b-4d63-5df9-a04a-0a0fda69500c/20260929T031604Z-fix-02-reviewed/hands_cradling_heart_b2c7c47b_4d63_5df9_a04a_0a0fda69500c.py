"""Restored the heart’s broad lobes and two symmetrical cupped palms with visible thumbs.
Before: The rejected hands are two tall bent bars without thumbs or proper palms; the original shows cupped palms supporting a broad heart.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b2c7c47b-4d63-5df9-a04a-0a0fda69500c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-heart/20260929T031604Z-recovered-thuan-mac/reference/love heart hands hold_b2c7c47b-4d63-5df9-a04a-0a0fda69500c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The hand and heart combination retains close supporting contacts while keeping its principal openings readable. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6184186fae34bf30ae53f63387742577c92a9bf3322b810eb97a4a04be03cab0'}
    icon_id = 'hands-cradling-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('hand', 'love heart hands hold')

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

        self.path('heart',(24,10),(12,10,6,6,False),(14,17,10,10,False),(24,26),(34,17),(36,10,10,10,False),(24,10,6,6,False),closed=True)

        # Two open-wrist palms; shortened thumb creases stay clear of the outer thumb curve.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),34),(x(6),27),(x(12),27,3,3,side==-1),(x(12),33),(x(15),36))
            self.path(f'hand-inner-{side}',(x(12),33),(x(18),32,4,4,side==-1),(x(20),37,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')

