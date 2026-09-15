"""A round speech bubble with a short tail at the bottom centre holds a pair of quotation marks.

Plan: Circular bubble with directional lower tail; identical quotation hooks at x=18 and 29.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: message-circle: continuous bubble outline.
Simplification: Quotation marks reduce to equal single-stroke hooks; tail stays intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76f5ee0d-8275-463e-9169-cf2623f4cc81'
SOURCE_PATH = 'pictographic-primitives/logos/google hangouts logo_76f5ee0d-8275-463e-9169-cf2623f4cc81.svg'
AUTHOR = 'gpt-6'


class GoogleHangoutsLogo(Solo48):
    icon_id = 'google-hangouts-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-hangouts', 'hangouts', 'google', 'chat', 'quotes', 'logo', 'brand')

    def build(self):
        self.add_arc('bubble-top',(6,24),(42,24),radius_x=18)
        self.add_bezier('bubble-right',(42,24),((42,33),(32,39),(23,42)))
        self.add_line('tail',(23,42),(23,36))
        self.add_bezier('bubble-left',(23,36),((13,36),(6,32),(6,24)))
        self.add_contour('bubble','bubble-top','bubble-right','tail','bubble-left',closed=True)

        for i,x in enumerate((19,29)):
            self.add_polyline(f'quote-{i}',(x,17),(x,24),(x-2,26))
