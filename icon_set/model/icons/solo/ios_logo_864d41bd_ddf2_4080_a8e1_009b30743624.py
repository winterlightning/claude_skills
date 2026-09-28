"""A rounded square frame holds the wordmark iOS in bold rounded letters.

Plan: Complete horizontal iOS lettering with shared cap height and baseline.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide wordmark match; geometric letters.
Simplification: Tile boundary omitted to preserve all three letters and required spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '864d41bd-ddf2-4080-a8e1-009b30743624'
SOURCE_PATH = 'pictographic-primitives/logos/ios logo_864d41bd-ddf2-4080-a8e1-009b30743624.svg'
AUTHOR = 'gpt-6'


class IosLogo(Solo48):
    icon_id = 'ios-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('ios', 'apple', 'mobile', 'operating-system', 'logo', 'brand', 'iphone')

    def build(self):
        self.add_dot('idot',(4,8))
        self.add_line('i',(4,20),(4,40))
        self.add_arc('oa',(24,24),(12,24),radius_x=6,radius_y=16)
        self.add_arc('ob',(12,24),(24,24),radius_x=6,radius_y=16)
        self.add_contour('O','oa','ob',closed=True)
        self.add_bezier('S',(44,11),((39,8),(32,8),(32,16)),((32,24),(44,24),(44,32)),((44,40),(37,40),(32,37)))
