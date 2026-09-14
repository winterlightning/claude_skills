"""Head-and-body portrait corresponding to avatar-jockey-man.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: riding jersey with short sleeves and a centre seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-jockey-man.svg'
SOURCE_HEAD_ICON_ID = 'avatar-jockey-man'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class JockeyManAvatar(Solo48):
    icon_id = 'jockey-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'jockey', 'man', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('helmet-left', (cx - radius, cy), (cx, 4), radius_x=radius)
        self.add_arc('helmet-right', (cx, 4), (cx + radius, cy), radius_x=radius)
        self.add_arc('face', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'helmet-left', 'helmet-right', 'face', closed=True)
        self.add_line('brim', (cx - radius, cy), (cx + radius, cy))
        self.relate('connect', 'head', 'brim')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: riding jersey with short sleeves and a centre seam.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-seam', (24,top), (24,44))
        self.relate('connect', 'body-seam', 'body-top')
        self.relate('connect', 'body-seam', 'body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
