"""A serif capital H with thick bracketed serifs at the top and bottom of both stems.

Plan: Serif H with mirrored stems and a shared central crossbar.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide wordmark match; shared-axis serif construction.
Simplification: Thick outlined bracket serifs reduced to rounded strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a08dce58-bc2a-4e25-bd53-f469ccddb795'
SOURCE_PATH = 'pictographic-primitives/logos/hyves logo_a08dce58-bc2a-4e25-bd53-f469ccddb795.svg'
AUTHOR = 'gpt-6'


class HyvesLogo(Solo48):
    icon_id = 'hyves-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('hyves', 'social', 'letter-h', 'logo', 'brand', 'network', 'dutch')

    def build(self):
        for x in (12,36):
         self.add_line(f'stem{x}',(x,6),(x,24))
         self.add_line(f'lower{x}',(x,24),(x,42))
         self.add_contour(f'leg{x}',f'stem{x}',f'lower{x}')
         for y in (6,42):
          self.add_polyline(f'serif{x}-{y}',(x-6,y),(x,y),(x+6,y))
          self.relate('connect',f'leg{x}',f'serif{x}-{y}')
        self.add_line('cross',(12,24),(36,24))
        for x in (12,36): self.relate('connect','cross',f'leg{x}')
