"""Head-and-body portrait corresponding to bartainder.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 26; shoulder top 34; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: bib apron with rounded shoulders and open outer sleeves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/bartainder.svg'
SOURCE_HEAD_ICON_ID = 'bartainder'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class BartenderAvatar(Solo48):
    icon_id = 'bartender-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/avatars'
    aliases = ()
    keywords = ('bartainder', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown-left', (10, 8), (cx, 4), radius_x=14, radius_y=4)
        self.add_arc('crown-right', (cx, 4), (38, 8), radius_x=14, radius_y=4)
        self.add_line('cap-right', (38, 8), (34, 16))
        self.add_line('brim', (34, 16), (14, 16))
        self.add_line('cap-left', (14, 16), (10, 8))
        self.add_contour('hat', 'crown-left', 'crown-right', 'cap-right', 'brim', 'cap-left', closed=True)
        self.add_arc('face', (34, 16), (14, 16), radius_x=10, radius_y=10)
        self.relate('connect', 'hat', 'face')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: bib apron with rounded shoulders and open outer sleeves.
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
        self.add_polyline('body-apron', (18,top), (18,44), (30,44), (30,top))
        self.relate('connect', 'body-apron', 'body-top')
        self.relate('connect', 'body-apron', 'body-top-right')
