"""Restored the center-parted hairstyle, rounded face, broad shoulders and two open-wrist hands.
Before: The rejected woman loses the parted fringe and is reduced to a generic hair arch over a dot.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '980cf59c-d36f-4ecd-b2a3-868c7b401314'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-woman-with-parted-hair/20260929T031604Z-recovered-thuan-mac/reference/donation charity care person female_980cf59c-d36f-4ecd-b2a3-868c7b401314.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The parted fringe and small portrait between the palms need compact optical spacing. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'c9cfd4ba5ae87e4cde576a9860dd5c2f3b0d471554add79a8a5b52efba514d7a'}
    icon_id = 'hands-cradling-woman-with-parted-hair'
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

        self.path('head',(17,12),(31,12,7,7,True),(17,12,7,7,True),closed=True)
        self.path('fringe',(17,12),(24,8),(31,12))
        self.add_line('hair-left',(17,12),(15,22))
        self.add_line('hair-right',(31,12),(33,22))
        self.path('shoulders',(18,29),(30,29,6,2,True))
        # Circular head bottom y19 to shoulder apex y27 gives 4px clear ink.

        # Two open-wrist palms; shortened thumb creases stay clear of the outer thumb curve.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),34),(x(6),27),(x(12),27,3,3,side==-1),(x(12),33),(x(15),36))
            self.path(f'hand-inner-{side}',(x(12),33),(x(18),32,4,4,side==-1),(x(20),37,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')

