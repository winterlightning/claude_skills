"""The wordmark IMDb in bold condensed letters, with a lowercase b at the end.

Plan: Two rows IM then Db; equal row height and nine-unit row gap.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide wordmark match; serif stem and rounded bowls.
Simplification: Wordmark arranged as IM / Db to retain every letter at this size.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c150dd43-0e25-485e-8fce-960140ad0999'
SOURCE_PATH = 'pictographic-primitives/logos/imdb logo_c150dd43-0e25-485e-8fce-960140ad0999.svg'
AUTHOR = 'gpt-6'


class ImdbLogo(Solo48):
    icon_id = 'imdb-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('imdb', 'movies', 'database', 'wordmark', 'logo', 'brand', 'film')

    def build(self):
        self.add_polyline('itop',(6,6),(10,6),(14,6))
        self.add_line('istem',(10,6),(10,20))
        self.add_polyline('ibase',(6,20),(10,20),(14,20))
        for p in ('itop','ibase'): self.relate('connect',p,'istem')
        self.add_polyline('m',(24,20),(24,6),(33,16),(42,6),(42,20))
        self.add_line('dleft',(6,29),(6,42))
        self.add_bezier('dround',(6,42),((23,42),(23,29),(6,29)))
        self.add_contour('d','dleft','dround',closed=True)
        self.add_line('bstem',(34,29),(34,38))
        self.add_arc('bowl1',(34,38),(42,38),radius_x=4)
        self.add_arc('bowl2',(42,38),(34,38),radius_x=4)
        self.add_contour('bowl','bowl1','bowl2',closed=True)
        self.relate('connect','bowl','bstem')
