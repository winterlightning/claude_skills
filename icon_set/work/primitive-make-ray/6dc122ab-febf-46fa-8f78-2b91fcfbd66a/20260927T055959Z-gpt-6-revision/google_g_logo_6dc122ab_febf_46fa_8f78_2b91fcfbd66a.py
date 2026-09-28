"""A bold capital G drawn as a thick outline, its open ring closing into a horizontal bar that reaches in from the right.

Plan: Open circular G, radius 20, with a distinct right terminal and inward crossbar.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: No useful brand match; coherent circular letter stroke.
Simplification: Double outline and colour seams merge into one stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6dc122ab-febf-46fa-8f78-2b91fcfbd66a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-g-logo/20260927T055620Z-thuan-mac-1/reference/google logo_6dc122ab-febf-46fa-8f78-2b91fcfbd66a.svg'
AUTHOR = "gpt-6"


class GoogleGLogo(Solo48):
    icon_id = 'google-g-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google', 'letter-g', 'search', 'logo', 'brand', 'g', 'web')

    def build(self):
        self.add_arc('upper',(38,10),(4,24),radius_x=20,sweep=False)
        self.add_arc('lower',(4,24),(42,30),radius_x=20,sweep=False)
        self.add_line('terminal',(42,30),(42,24))
        self.add_line('bar',(42,24),(26,24))
        self.add_contour('g','upper','lower','terminal','bar')
