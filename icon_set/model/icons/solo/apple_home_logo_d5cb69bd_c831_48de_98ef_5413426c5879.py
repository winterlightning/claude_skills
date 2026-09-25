"""A house outline with a pitched roof holds a smaller nested house outline, with a horizontal floor bar near the bottom joining them.

Plan: Two nested houses mirror around x=24 and share the outer baseline; inner floor is 8 units above it.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: house: pitched roof and shared wall attachments.
Simplification: Nested house and floor retained; small roof cap rounding omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5cb69bd-c831-48de-98ef-5413426c5879'
SOURCE_PATH = 'pictographic-primitives/logos/home apps logo_d5cb69bd-c831-48de-98ef-5413426c5879.svg'
AUTHOR = 'gpt-6'


class AppleHomeLogo(Solo48):
    icon_id = 'apple-home-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('home', 'apple-home', 'house', 'smart-home', 'logo', 'brand', 'apps')

    def build(self):
        self.add_polyline('outer',(6,23),(24,6),(42,23),(42,42),(33,42),(15,42),(6,42),closed=True)
        self.add_polyline('inner',(15,42),(15,34),(15,27),(24,18),(33,27),(33,34),(33,42))
        self.relate('connect','outer','inner')
        self.add_line('floor',(15,34),(33,34))
        self.relate('connect','inner','floor')
