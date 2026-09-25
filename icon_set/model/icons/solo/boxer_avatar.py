"""Head-and-body portrait corresponding to boxer.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: raised boxing gloves and bent forearms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'pictographic-primitives/avatars/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
SOURCE_HEAD_ICON_ID = 'boxer'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 28

class BoxerAvatar(Solo48):
    icon_id = 'boxer-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('boxer', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown',(12,16),(36,16),radius_x=12)
        self.add_arc('jaw',(36,16),(12,16),radius_x=12)
        self.add_contour('head','crown','jaw',closed=True)

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: raised boxing gloves and bent forearms.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_arc('body-left',(16,38),(20,top),radius_x=4,radius_y=38-top)
        self.add_line('body-top', (20,top), (24, top))
        self.add_line('body-top-right', (24, top), (28,top))
        self.add_arc('body-right',(28,top),(32,38),radius_x=4,radius_y=38-top)
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        for side, x in [('left',12),('right',36)]:
            self.add_arc('body-glove-top-'+side,(x-4,38),(x+4,38),radius_x=4)
            self.add_arc('body-glove-bottom-'+side,(x+4,38),(x-4,38),radius_x=4)
            self.add_contour('body-glove-'+side,'body-glove-top-'+side,'body-glove-bottom-'+side,closed=True)
            self.relate('connect','body-glove-'+side,'body-'+side)
            end = 16 if side == 'left' else 32
            self.add_bezier('body-forearm-'+side,(x,42),((end,42),(end,43),(end,44)))
            self.relate('connect','body-glove-'+side,'body-forearm-'+side)

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
