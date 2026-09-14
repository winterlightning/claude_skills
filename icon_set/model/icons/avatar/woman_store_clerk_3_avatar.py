"""Head-and-body portrait corresponding to avatar-woman-store-clerk-3.

AVATAR48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 24; shoulder top 32; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs and tangent shoulders. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Shared axis x24 and radius10 shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Avatar48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-woman-store-clerk-3.svg'
SOURCE_HEAD_ICON_ID = 'avatar-woman-store-clerk-3'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class WomanStoreClerk3Avatar(Avatar48):
    icon_id = 'woman-store-clerk-3-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('avatar', 'woman', 'store', 'clerk', '3', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (14, cy), (34, cy), radius_x=radius)
        self.add_arc('jaw', (34, cy), (14, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((20, 14), (24, 13), (27, 11)), ((29, 13), (32, 14), (34, 14)))
        self.relate('connect', 'head', 'fringe')
        self.add_bezier('ponytail', (34, 14), ((40, 14), (34, 20), (39, 24)))
        self.relate('connect', 'head', 'ponytail')
        self.relate('connect', 'fringe', 'ponytail')

        # Shoulders are a separate symbol: mirrored tangent quarter circles.
        # The jaw bottom lies over the plateau, certifying the exact ink gap.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        left, right, bottom, shoulder_radius = 8, 40, 44, 10
        self.add_line('body-left',(left,bottom),(left,top+shoulder_radius))
        self.add_arc('body-shoulder-left',(left,top+shoulder_radius),(left+shoulder_radius,top),radius_x=shoulder_radius)
        self.add_line('body-top',(left+shoulder_radius,top),(right-shoulder_radius,top))
        self.add_arc('body-shoulder-right',(right-shoulder_radius,top),(right,top+shoulder_radius),radius_x=shoulder_radius)
        self.add_line('body-right',(right,top+shoulder_radius),(right,bottom))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-shoulder-right','body-right')
