"""Head-and-body portrait corresponding to avatar-ship-crew-navy-1.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: wide sailor collar and rounded shoulders.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'cba73ce9-9aea-4551-91dd-9549fb2c89f4'
SOURCE_PATH = 'pictographic-primitives/avatars/ship crew navy_cba73ce9-9aea-4551-91dd-9549fb2c89f4.svg'
SOURCE_HEAD_ICON_ID = 'avatar-ship-crew-navy-1'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 30

class AvatarShipCrewNavy1Variant2(Solo48):
    icon_id = 'avatar-ship-crew-navy-1-v2'
    variant_of = 'avatar-ship-crew-navy-1'
    variant_label = 'Refined solo portrait after visual rejection'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'ship', 'crew', 'navy', '1', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown', (16, 12), (32, 12), radius_x=8)
        self.add_polyline('band', (16, 12), (10, 12), (14, 20), (34, 20), (38, 12), (32, 12), (16, 12))
        self.relate('connect', 'crown', 'band')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'face', 'band')
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
        self.add_arc('body-sailor-collar', (16, top), (32, top), radius_x=8, radius_y=6, sweep=False)
        self.relate('connect', 'body-sailor-collar', 'body-top')
        self.relate('connect', 'body-sailor-collar', 'body-top-right')
        self.relate('connect', 'face', 'body-top')
        self.relate('connect', 'face', 'body-top-right')
