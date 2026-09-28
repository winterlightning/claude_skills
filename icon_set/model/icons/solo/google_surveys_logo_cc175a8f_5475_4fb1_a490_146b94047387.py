"""A bold check mark drawn as a thick outline, its short arm at the left and long arm rising to the upper right.

Plan: Single check stroke with a short arm and long rising arm.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: check: two joined diagonal strokes.
Simplification: Outlined check becomes one rounded stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc175a8f-5475-4fb1-a490-146b94047387'
SOURCE_PATH = 'pictographic-primitives/logos/google surveys logo_cc175a8f-5475-4fb1-a490-146b94047387.svg'
AUTHOR = 'gpt-6'


class GoogleSurveysLogo(Solo48):
    icon_id = 'google-surveys-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-surveys', 'google', 'survey', 'check', 'logo', 'brand', 'feedback')

    def build(self):
        self.add_polyline('check',(6,26),(20,42),(42,6))
