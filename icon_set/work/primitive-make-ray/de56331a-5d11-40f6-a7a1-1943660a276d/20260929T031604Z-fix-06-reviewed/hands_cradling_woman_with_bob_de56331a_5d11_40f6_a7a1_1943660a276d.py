"""Restored the flared bob haircut, parted fringe, rounded face and neck above two cupped hands.
Before: The rejected bob-haired portrait is a dot under a tiny arch and the hands overlap its shoulders; the bob silhouette and neck are lost.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'de56331a-5d11-40f6-a7a1-1943660a276d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-woman-with-bob/20260929T031604Z-recovered-thuan-mac/reference/donation charity care person female_de56331a-5d11-40f6-a7a1-1943660a276d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The bob, face and two hands need compact placement; the flared haircut remains distinct. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '06099930f57a7c485bb446287659c941a40cd4414262ee17583e811375e4f60e'}
    icon_id = 'hands-cradling-woman-with-bob'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('hand', 'donation charity care person female')

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

        self.path('hair',(15,21),(16,12),(24,4,8,8,True),(32,12,8,8,True),(33,21),(29,22))
        self.path('fringe',(19,12),(24,9),(29,12))
        self.path('face',(19,12),(19,16),(24,21,5,5,False),(29,16,5,5,False),(29,12))
        self.path('shoulder-left',(22,21),(22,24),(17,26))
        self.path('shoulder-right',(26,21),(26,24),(31,26))

        # Two open-wrist palms; shortened thumb creases stay clear of the outer thumb curve.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),34),(x(6),27),(x(12),27,3,3,side==-1),(x(12),33),(x(15),36))
            self.path(f'hand-inner-{side}',(x(12),33),(x(18),32,4,4,side==-1),(x(20),37,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')

