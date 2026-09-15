"""The capital letters OS in a light geometric sans-serif, a tall oval O beside a flowing S.

Plan: Tall oval O beside smooth S; nine-unit interletter clearance.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide letter match; ellipse and smooth cubic lettering.
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'baad114d-97bb-4626-bf75-b1f3b0925636'
SOURCE_PATH = 'pictographic-primitives/logos/ios logo 1_baad114d-97bb-4626-bf75-b1f3b0925636.svg'
AUTHOR = 'gpt-6'


class OsWordmark(Solo48):
    icon_id = 'os-wordmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('os', 'operating-system', 'ios', 'wordmark', 'logo', 'brand', 'apple')

    def build(self):
        self.add_arc('oa',(20,24),(4,24),radius_x=8,radius_y=16)
        self.add_arc('ob',(4,24),(20,24),radius_x=8,radius_y=16)
        self.add_contour('O','oa','ob',closed=True)
        self.add_bezier('S',(44,11),((38,8),(29,8),(29,16)),((29,24),(44,24),(44,32)),((44,40),(35,40),(29,37)))
