"""Head-and-body portrait corresponding to avatar-fire-fighter-woman.

AVATAR48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 26; shoulder top 34; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs and tangent shoulders. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Shared axis x24 and radius8 shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Avatar48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-fire-fighter-woman.svg'
SOURCE_HEAD_ICON_ID = 'avatar-fire-fighter-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class FireFighterWomanAvatar(Avatar48):
    icon_id = 'fire-fighter-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('avatar', 'fire', 'fighter', 'woman', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('helmet-left', (8, 16), (cx, 4), radius_x=16, radius_y=12)
        self.add_arc('helmet-right', (cx, 4), (40, 16), radius_x=16, radius_y=12)
        self.add_contour('helmet', 'helmet-left', 'helmet-right')
        self.add_polyline('brim', (8, 16), (14, 16), (34, 16), (40, 16))
        self.relate('connect', 'helmet', 'brim')
        self.add_arc('face', (34, 16), (14, 16), radius_x=10, radius_y=10)
        self.relate('connect', 'face', 'brim')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 10, 16), ((cx + sign * 10, 20), (cx + sign * 13, 24), (cx + sign * 15, 26)))
            self.relate('connect', 'hair-' + side, 'face')
            self.relate('connect', 'hair-' + side, 'brim')

        # Shoulders are a separate symbol: mirrored tangent quarter circles.
        # The jaw bottom lies over the plateau, certifying the exact ink gap.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        left, right, bottom, shoulder_radius = 8, 40, 44, 8
        self.add_line('body-left',(left,bottom),(left,top+shoulder_radius))
        self.add_arc('body-shoulder-left',(left,top+shoulder_radius),(left+shoulder_radius,top),radius_x=shoulder_radius)
        self.add_line('body-top',(left+shoulder_radius,top),(right-shoulder_radius,top))
        self.add_arc('body-shoulder-right',(right-shoulder_radius,top),(right,top+shoulder_radius),radius_x=shoulder_radius)
        self.add_line('body-right',(right,top+shoulder_radius),(right,bottom))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-shoulder-right','body-right')
