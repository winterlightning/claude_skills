"""An upright document with a folded top right corner holds a table grid of two columns and three rows.

Plan: Folded page with a 16-unit interior panel; shared eight-unit cell pitch.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: file-text: folded page silhouette.
Simplification: Inner fold seam omitted; three rows reduce to two.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b10704f2-58af-44bd-849f-dcd977ac9d2f'
SOURCE_PATH = 'pictographic-primitives/logos/google sheets logo_b10704f2-58af-44bd-849f-dcd977ac9d2f.svg'
AUTHOR = 'gpt-6'


class GoogleSheetsLogo(Solo48):
    icon_id = 'google-sheets-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-sheets', 'google', 'spreadsheet', 'table', 'logo', 'brand', 'office')

    def build(self):
        self.add_polyline('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)
        self.add_polyline('panel',(16,20),(24,20),(32,20),(32,28),(32,36),(24,36),(16,36),(16,28),closed=True)
        self.add_polyline('row',(16,28),(24,28),(32,28))
        self.relate('connect','panel','row')

        self.add_polyline('column',(24,20),(24,28),(24,36))
        self.relate('connect','panel','column')
        self.relate('connect','row','column')
