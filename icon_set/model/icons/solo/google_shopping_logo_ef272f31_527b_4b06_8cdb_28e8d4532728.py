"""A price tag points to the lower left with a round hole near its upper right corner and a capital G at its centre.

Plan: Horizontal left-pointing tag with an intrinsic angular G.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: tag: diagonal contour and round eyelet.
Simplification: Tag reoriented horizontally; small eyelet omitted to preserve a readable G.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef272f31-527b-4b06-8cdb-28e8d4532728'
SOURCE_PATH = 'pictographic-primitives/logos/google shopping logo_ef272f31-527b-4b06-8cdb-28e8d4532728.svg'
AUTHOR = 'gpt-6'


class GoogleShoppingLogo(Solo48):
    icon_id = 'google-shopping-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-shopping', 'google', 'shopping', 'price-tag', 'logo', 'brand', 'commerce')

    def build(self):
        # Reorient the tag horizontally to give its intrinsic G a readable opening.
        self.add_polyline('tag',(4,24),(20,8),(44,8),(44,40),(20,40),closed=True)
        self.add_polyline('g',(36,16),(24,16),(24,32),(36,32),(36,24),(32,24))
