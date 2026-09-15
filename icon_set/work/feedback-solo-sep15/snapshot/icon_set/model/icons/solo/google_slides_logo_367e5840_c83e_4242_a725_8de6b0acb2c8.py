"""An upright document with a folded top right corner holds a wide rectangle split by a horizontal line, like a presentation slide.

Plan: Folded page with a 16-unit interior panel; shared eight-unit cell pitch.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: file-text: folded page silhouette.
Simplification: Inner fold seam omitted; two slide zones retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '367e5840-c83e-4242-a725-8de6b0acb2c8'
SOURCE_PATH = 'pictographic-primitives/logos/google slides logo_367e5840-c83e-4242-a725-8de6b0acb2c8.svg'
AUTHOR = 'gpt-6'


class GoogleSlidesLogo(Solo48):
    icon_id = 'google-slides-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-slides', 'google', 'presentation', 'slide', 'logo', 'brand', 'office')

    def build(self):
        self.add_polyline('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)
        self.add_polyline('panel',(16,20),(24,20),(32,20),(32,28),(32,36),(24,36),(16,36),(16,28),closed=True)
        self.add_line('row',(16,28),(32,28))
        self.relate('connect','panel','row')
