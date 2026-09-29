"""Restored the squared hair cap, rounded jaw, continuous neck/shoulders and distinct cupped hands.
Before: The rejected squared-haired man is a generic circle/arch symbol and the hands are short hooks.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9cfaacff-026a-4070-9a84-684d32d863c5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-man-with-squared-hair/20260929T031604Z-recovered-thuan-mac/reference/donation charity care person male_9cfaacff-026a-4070-9a84-684d32d863c5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The flat hairline and close supporting palms preserve the specific male portrait. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2ef906940bd4e46c97a6782f7073a2c2b2b9fcf70ba07ea01ad2a79a4191e31a'}
    icon_id = 'hands-cradling-man-with-squared-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('hand', 'donation charity care person male')

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

        self.path('person',(17,25),(20,23),(20,20),(18,16,5,5,True),(18,8),(21,5,3,3,True),(27,5),(30,8,3,3,True),(30,16),(28,20,5,5,True),(28,23),(31,25))
        self.add_line('hairline',(18,11),(29,11))

        # Two open-wrist palms; shortened thumb creases stay clear of the outer thumb curve.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),34),(x(6),27),(x(12),27,3,3,side==-1),(x(12),33),(x(15),36))
            self.path(f'hand-inner-{side}',(x(12),33),(x(18),32,4,4,side==-1),(x(20),37,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')

