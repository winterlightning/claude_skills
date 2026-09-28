"""A circle overlaps a tall slanted parallelogram bar at its right, together forming a lowercase d.

Plan: Slanted d assembled from a round bowl and a single ascender; shared junction at bowl right.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact logo match; circular bowl with shared attachment.
Simplification: Slanted outlined bar becomes a single ascender, retaining the lowercase d.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '736f5f12-9937-43b3-9e38-dc6ced29e872'
SOURCE_PATH = 'pictographic-primitives/logos/google domain logo_736f5f12-9937-43b3-9e38-dc6ced29e872.svg'
AUTHOR = 'gpt-6'


class GoogleDomainsLogo(Solo48):
    icon_id = 'google-domains-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-domains', 'google', 'domain', 'letter-d', 'logo', 'brand', 'web')

    def build(self):
        self.add_arc('bowl-top',(6,28),(34,28),radius_x=14)
        self.add_arc('bowl-bottom',(34,28),(6,28),radius_x=14)
        self.add_contour('bowl','bowl-top','bowl-bottom',closed=True)
        self.add_line('ascender',(34,28),(42,6))
        self.relate('connect','bowl','ascender')
