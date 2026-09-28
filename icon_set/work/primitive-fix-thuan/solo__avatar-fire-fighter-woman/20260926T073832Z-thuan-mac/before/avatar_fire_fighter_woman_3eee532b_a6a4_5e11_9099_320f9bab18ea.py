"""Head-and-body portrait corresponding to avatar-fire-fighter-woman.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: protective coat with a chest band and centre fastening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '3eee532b-a6a4-5e11-9099-320f9bab18ea'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar fire fighter woman_3eee532b-a6a4-5e11-9099-320f9bab18ea.svg'
SOURCE_HEAD_ICON_ID = 'avatar-fire-fighter-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class AvatarFireFighterWoman(Solo48):
    icon_id = 'avatar-fire-fighter-woman'
    human_construction = 'bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
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
            self.add_bezier('hair-' + side, (cx + sign * 10, 16), ((cx + sign * 10, 20), (cx + sign * 13, 22), (cx + sign * 15, 24)))
            self.relate('connect', 'hair-' + side, 'face')
            self.relate('connect', 'hair-' + side, 'brim')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side', (8, 44), (8, 42))
        self.add_arc('body-left-shoulder', (8, 42), (18, top), radius_x=10, radius_y=42 - top)
        self.add_contour('body-left', 'body-left-side', 'body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder', (30, top), (40, 42), radius_x=10, radius_y=42 - top)
        self.add_line('body-right-side', (40, 42), (40, 44))
        self.add_contour('body-right', 'body-right-shoulder', 'body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-band', (8, 42), (40, 42))
        self.relate('connect', 'body-band', 'body-left')
        self.relate('connect', 'body-band', 'body-right')
        self.add_line('body-fastening', (24, top), (24, 42))
        self.relate('connect', 'body-fastening', 'body-top')
        self.relate('connect', 'body-fastening', 'body-top-right')
        self.relate('connect', 'body-fastening', 'body-band')
        self.relate('connect', 'face', 'body-top')
        self.relate('connect', 'face', 'body-top-right')
