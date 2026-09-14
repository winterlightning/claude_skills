"""Head-and-body portrait corresponding to avatar-woman-store-clerk-3.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 24; shoulder top 32; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: tailored blazer with broad lapels and a centre opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/avatar-woman-store-clerk-3.svg'
SOURCE_HEAD_ICON_ID = 'avatar-woman-store-clerk-3'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class WomanStoreClerk3Avatar(Solo48):
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

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: tailored blazer with broad lapels and a centre opening.
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
        self.add_polyline('body-lapels', (16, top), (24,40), (32, top))
        self.relate('connect', 'body-lapels', 'body-top')
        self.relate('connect', 'body-lapels', 'body-top-right')
        self.add_line('body-opening', (24,40), (24,44))
        self.relate('connect', 'body-lapels', 'body-opening')
