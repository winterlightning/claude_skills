"""Head-and-body portrait corresponding to arabian-man.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: rounded robe with a central placket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/arabian-man.svg'
SOURCE_HEAD_ICON_ID = 'arabian-man'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class ArabianManAvatar(Solo48):
    icon_id = 'arabian-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('arabian', 'man', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        brim = 14
        self.add_arc('cap', (14, brim), (34, brim), radius_x=10)
        self.add_arc('face', (34, brim), (14, brim), radius_x=10, radius_y=10)
        self.add_contour('head', 'cap', 'face', closed=True)
        self.add_polyline('brim', (8, brim), (14, brim), (34, brim), (40, brim))
        self.relate('connect', 'head', 'brim')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('drape-' + side, (cx + sign * 10, 14), ((cx + sign * 12, 20), (cx + sign * 13, 23), (cx + sign * 16, 26)))
            self.relate('connect', 'head', 'drape-' + side)
            self.relate('connect', 'brim', 'drape-' + side)

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: rounded robe with a central placket.
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
        self.add_line('body-placket', (24, top), (24, 44))
        self.relate('connect', 'body-placket', 'body-top')
        self.relate('connect', 'body-placket', 'body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
