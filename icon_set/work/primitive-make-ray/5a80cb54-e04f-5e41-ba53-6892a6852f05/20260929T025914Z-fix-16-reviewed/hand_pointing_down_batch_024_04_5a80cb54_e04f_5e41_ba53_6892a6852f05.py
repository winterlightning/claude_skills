"""Rebalanced the wrist and palm, lengthened the pointing index, and gave the curled fingers distinct stepped ends.
Before: The rejected fist has an uneven row of fused circular finger bumps; the reference has a clearly extended index and stepped curled fingers.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a80cb54-e04f-5e41-ba53-6892a6852f05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The curled finger divisions are tighter than the general spacing rule but preserve a familiar pointing-hand silhouette. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'c9b423f1b3588418ea8a9e4e8e20a980aa5b5edf589575ef3bfcc7dbcf29c8ea'}
    icon_id = 'hand-pointing-down-batch-024-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('hand', 'hand pointer bottom')

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

        # Continuous pointing-hand outline; finger seams terminate on the shared outer contour.
        self.path('outline',(17,6),(27,6),(40,19,13,13,True),(40,29),(34,29,3,3,True),(34,31),(28,31,3,3,True),(28,34),(22,34,3,3,True),(22,40),(14,40,4,4,True),(14,21),(11,24),(7,20,3,3,True),(17,6),closed=True)
        for i,(x,y) in enumerate(((34,29),(28,31),(22,34))):
            self.add_line(f'finger-{i}',(x,y-5),(x,y))
            self.relate('connect','outline',f'finger-{i}')

