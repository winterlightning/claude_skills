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
