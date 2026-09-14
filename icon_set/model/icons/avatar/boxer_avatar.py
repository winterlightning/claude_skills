"""Head-and-body portrait corresponding to boxer.

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
SOURCE_PATH = 'work/head-solo/batch-01/references/boxer.svg'
SOURCE_HEAD_ICON_ID = 'boxer'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class BoxerAvatar(Avatar48):
    icon_id = 'boxer-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('boxer', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown', (12, 16), (36, 16), radius_x=12)
        self.add_line('side-right', (36, 16), (34, 22))
        self.add_arc('jaw', (34, 22), (14, 22), radius_x=10, radius_y=4)
        self.add_line('side-left', (14, 22), (12, 16))
        self.add_contour('head', 'side-left', 'crown', 'side-right')
        self.relate('connect', 'head', 'jaw')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('guard-' + side, (cx + sign * 12, 16), ((cx + sign * 8, 16), (cx + sign * 6, 20), (cx, 20)))
            self.relate('connect', 'head', 'guard-' + side)
        self.relate('connect', 'guard-left', 'guard-right')

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
