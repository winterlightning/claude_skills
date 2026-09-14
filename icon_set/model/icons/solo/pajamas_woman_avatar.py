"""Head-and-body portrait corresponding to avatar-pajamas-woman.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 24; shoulder top 32; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: soft sleep shirt with a low curved neckline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-pajamas-woman.svg'
SOURCE_HEAD_ICON_ID = 'avatar-pajamas-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class PajamasWomanAvatar(Solo48):
    icon_id = 'pajamas-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('avatar', 'pajamas', 'woman', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('wrap-left', (14, cy), (cx, 4), radius_x=radius)
        self.add_arc('wrap-right', (cx, 4), (34, cy), radius_x=radius)
        self.add_arc('jaw', (34, cy), (14, cy), radius_x=radius)
        self.add_contour('head', 'wrap-left', 'wrap-right', 'jaw', closed=True)
        self.add_bezier('twist', (cx, 4), ((34, 9), (26, 14), (14, 14)))
        self.relate('connect', 'head', 'twist')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: soft sleep shirt with a low curved neckline.
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
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect', 'body-neckline', 'body-top')
        self.relate('connect', 'body-neckline', 'body-top-right')
