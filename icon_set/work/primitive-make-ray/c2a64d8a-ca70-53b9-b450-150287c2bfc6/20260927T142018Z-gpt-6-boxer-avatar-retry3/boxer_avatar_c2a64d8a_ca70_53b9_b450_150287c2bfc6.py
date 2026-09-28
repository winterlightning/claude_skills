"""Head-and-body portrait corresponding to boxer.

SOLO48 construction on VRECT_L: visible ink (6,2)-(42,46).
Circular face; head and shoulder ink touch with zero visible gap.
References: human_ref/user.svg for head/body proportions and open shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg for cardinal
arcs; Lucide shirt for garment edges and sleeve construction. Retain the source hair/headwear silhouette;
omit facial microdetails at 48. Body: raised boxing gloves and bent forearms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer-avatar/20260927T140835Z-thuan-mac-1/reference/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
SOURCE_HEAD_ICON_ID = 'boxer'
AUTHOR = "gpt-6"
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
        # One continuous bob hairstyle frames a deliberately blank portrait.
        # The source avatar has no facial marks; hair shape and shoulders carry it.
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_bezier('hair-right',(34,14),((36,18),(38,23),(36,28)))
        self.add_bezier('hair-left',(12,28),((10,23),(12,18),(14,14)))
        self.add_contour('hair','hair-left','crown','hair-right')
        self.add_bezier('body-left',(8,44),((9,38),(16,36),(20,36)))
        self.add_line('shoulders',(20,36),(28,36))
        self.add_bezier('body-right',(28,36),((32,36),(39,38),(40,44)))
        self.add_contour('bust','body-left','shoulders','body-right')
