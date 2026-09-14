"""Head-and-body portrait corresponding to avatar-woman-air-hostess-1.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 26; shoulder top 34; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: fitted uniform with an asymmetric neck scarf.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-woman-air-hostess-1.svg'
SOURCE_HEAD_ICON_ID = 'avatar-woman-air-hostess-1'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class WomanAirHostess1Avatar(Solo48):
    icon_id = 'woman-air-hostess-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'woman', 'air', 'hostess', '1', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_polyline('hat', (14, 16), (18, 4), (30, 4), (34, 16), (14, 16))
        self.add_arc('face', (34, 16), (14, 16), radius_x=10, radius_y=10)
        self.relate('connect', 'hat', 'face')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 10, 16), ((cx + sign * 16, 18), (cx + sign * 16, 22), (cx + sign * 16, 26)))
            self.relate('connect', 'hair-' + side, 'hat')
            self.relate('connect', 'hair-' + side, 'face')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: fitted uniform with an asymmetric neck scarf.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16, top), (24, top))
        self.add_line('body-top-right', (24, top), (32, top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-scarf', (16, top), (24,42), (32, top))
        self.relate('connect', 'body-scarf', 'body-top')
        self.relate('connect', 'body-scarf', 'body-top-right')
        self.add_line('body-scarf-tail', (24,42), (30,44))
        self.relate('connect', 'body-scarf', 'body-scarf-tail')
