"""Head-and-body portrait corresponding to boxer.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Head bottom 26; shoulder top 34; measured head/body ink gap 4.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: raised boxing gloves and bent forearms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-01/references/boxer.svg'
SOURCE_HEAD_ICON_ID = 'boxer'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26

class BoxerAvatar(Solo48):
    icon_id = 'boxer-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('boxer', 'bust', 'body', 'portrait')

    def build(self):
        cx = 24
        self.add_arc('crown', (12, 16), (36, 16), radius_x=12)
        self.add_line('side-right', (36, 16), (34, 22))
        self.add_arc('jaw', (34, 22), (14, 22), radius_x=10, radius_y=4)
        self.add_line('side-left', (14, 22), (12, 16))
        self.add_contour('head', 'side-left', 'crown', 'side-right')
        self.relate('connect', 'head', 'jaw')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('guard-' + side, (cx + sign * 12, 16), ((cx + sign * 8, 16), (cx + sign * 6, 20), (cx, 20)))
            self.relate('connect', 'head', 'guard-' + side)
        self.relate('connect', 'guard-left', 'guard-right')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: raised boxing gloves and bent forearms.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_arc('body-left',(16,38),(20,top),radius_x=4,radius_y=4)
        self.add_line('body-top', (20,top), (24, top))
        self.add_line('body-top-right', (24, top), (28,top))
        self.add_arc('body-right',(28,top),(32,38),radius_x=4,radius_y=4)
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
