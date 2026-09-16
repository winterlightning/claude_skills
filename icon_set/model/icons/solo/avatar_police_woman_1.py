"""Head-and-body portrait corresponding to avatar-police-woman-1.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: curved uniform shoulders and a simple uniform front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-police-woman-1.svg'
SOURCE_HEAD_ICON_ID = 'avatar-police-woman-1'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 30

class AvatarPoliceWoman1(Solo48):
    icon_id = 'avatar-police-woman-1'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'police', 'woman', '1', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_polyline('cap', (8, 12), (cx, 4), (40, 12), (34, 20), (14, 20), (8, 12))
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'cap', 'band')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'cap', 'face')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 10, 20), ((cx + sign * 10, 24), (cx + sign * 13, 26), (cx + sign * 16, 28)))
            self.relate('connect', 'hair-' + side, 'cap')
            self.relate('connect', 'hair-' + side, 'face')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side', (8, 44), (8, 42))
        self.add_arc('body-left-shoulder', (8, 42), (16, top), radius_x=8, radius_y=42 - top)
        self.add_contour('body-left', 'body-left-side', 'body-left-shoulder')
        self.add_line('body-top', (16, top), (24, top))
        self.add_line('body-top-right', (24, top), (32, top))
        self.add_arc('body-right-shoulder', (32, top), (40, 42), radius_x=8, radius_y=42 - top)
        self.add_line('body-right-side', (40, 42), (40, 44))
        self.add_contour('body-right', 'body-right-shoulder', 'body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.relate('connect', 'face', 'body-top')
        self.relate('connect', 'face', 'body-top-right')
        self.add_line('body-front', (24, top), (24, 44))
        self.relate('connect', 'body-front', 'body-top')
        self.relate('connect', 'body-front', 'body-top-right')
