"""A serif capital I with wide bracketed serifs at its top and bottom.

Plan: Capital I with broad mirrored serif bars and a central stem.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful Lucide letter match; shared-axis serif construction.
Simplification: Thick bracketed outline reduced to monoline serif I.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14bd666c-57ca-4f1e-8247-3d1ac09aebf4'
SOURCE_PATH = 'pictographic-primitives/logos/instapaper logo_14bd666c-57ca-4f1e-8247-3d1ac09aebf4.svg'
AUTHOR = 'gpt-6'


class InstapaperLogo(Solo48):
    icon_id = 'instapaper-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('instapaper', 'reading', 'letter-i', 'logo', 'brand', 'read-later', 'articles')

    def build(self):
        for y in (4,44):
         self.add_polyline(f'serif{y}',(8,y),(24,y),(40,y))
        self.add_line('stem',(24,4),(24,44))
        for y in (4,44): self.relate('connect','stem',f'serif{y}')
