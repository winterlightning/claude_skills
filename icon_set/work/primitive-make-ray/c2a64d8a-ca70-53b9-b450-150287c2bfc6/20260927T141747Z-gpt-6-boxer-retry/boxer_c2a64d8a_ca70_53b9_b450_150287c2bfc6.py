"""Raised boxing gloves, guarded shoulders, and bent forearms.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
SQUARE exact envelope; detached head bottom 18, body top 26.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxer/20260927T140835Z-thuan-mac-1/reference/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
AUTHOR = "gpt-6"

class Boxer(Solo48):
    icon_id='boxer'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases=()
    keywords=('boxer', 'bust', 'occupation', 'body')

    def build(self):
        # Hair framing a blank circular face and a broad portrait bust, as in the
        # source avatar. The two hair sides mirror around the face axis.
        self.add_arc('face-top',(14,14),(34,14),radius_x=10)
        self.add_arc('face-bottom',(34,14),(14,14),radius_x=10)
        self.add_contour('face','face-top','face-bottom',closed=True)
        self.add_bezier('body-left',(8,44),((9,36),(15,30),(20,28)))
        self.add_line('neck',(20,28),(28,28))
        self.add_bezier('body-right',(28,28),((33,30),(39,36),(40,44)))
        self.add_contour('bust','body-left','neck','body-right')
        self.relate('connect','face','bust')
