"""The capital letters OS in a light geometric sans-serif, a tall oval O beside a flowing S.

Plan: Tall oval O beside smooth S; nine-unit interletter clearance.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide letter match; ellipse and smooth cubic lettering.
Simplification: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'baad114d-97bb-4626-bf75-b1f3b0925636'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__os-wordmark/20260927T160114Z-thuan-mac-1/reference/ios logo 1_baad114d-97bb-4626-bf75-b1f3b0925636.svg'
AUTHOR = 'gpt-6'


class OsWordmark(Solo48):
    icon_id = 'os-wordmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('os', 'operating-system', 'ios', 'wordmark', 'logo', 'brand', 'apple')

    def build(self):
        self.add_arc('oa',(20,24),(4,24),radius_x=8,radius_y=16)
        self.add_arc('ob',(4,24),(20,24),radius_x=8,radius_y=16)
        self.add_contour('O','oa','ob',closed=True)
        self.add_bezier('S',(44,11),((38,8),(29,8),(29,16)),((29,23),(44,25),(44,32)),((44,39),(36,41),(29,37)))
