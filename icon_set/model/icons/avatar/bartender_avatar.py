"""Head-and-body portrait corresponding to bartainder.

AVATAR48 construction on VRECT_L: visible ink (6,0)-(42,48).
Head bottom 24; shoulder top 32; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs and tangent shoulders. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Shared axis x24 and radius10 shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Avatar48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/bartainder.svg'
SOURCE_HEAD_ICON_ID = 'bartainder'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class BartenderAvatar(Avatar48):
    icon_id = 'bartender-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('bartainder', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown-left',(10,6),(cx,2),radius_x=14,radius_y=4)
        self.add_arc('crown-right',(cx,2),(38,6),radius_x=14,radius_y=4)
        self.add_line('cap-right',(38,6),(34,14))
        self.add_line('brim',(34,14),(14,14))
        self.add_line('cap-left',(14,14),(10,6))
        self.add_contour('hat','crown-left','crown-right','cap-right','brim','cap-left',closed=True)
        self.add_arc('face',(34,14),(14,14),radius_x=10,radius_y=10)
        self.relate('connect','hat','face')

        # Shoulders are a separate symbol: mirrored tangent quarter circles.
        # The jaw bottom lies over the plateau, certifying the exact ink gap.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        left, right, bottom, shoulder_radius = 8, 40, 46, 10
        self.add_line('body-left',(left,bottom),(left,top+shoulder_radius))
        self.add_arc('body-shoulder-left',(left,top+shoulder_radius),(left+shoulder_radius,top),radius_x=shoulder_radius)
        self.add_line('body-top',(left+shoulder_radius,top),(right-shoulder_radius,top))
        self.add_arc('body-shoulder-right',(right-shoulder_radius,top),(right,top+shoulder_radius),radius_x=shoulder_radius)
        self.add_line('body-right',(right,top+shoulder_radius),(right,bottom))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-shoulder-right','body-right')
