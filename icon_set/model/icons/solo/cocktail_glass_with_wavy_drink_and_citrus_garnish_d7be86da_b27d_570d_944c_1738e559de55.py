"""Cocktail Glass with Citrus Slice.

Plan: Cocktail bowl with citrus attached at rim, stem and foot; bounds (6,6)-(42,42). Wavy drink line simplified to protect bowl opening.
Construction reference: Lucide martini: broad bowl over narrow stem and shared foot junction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd7be86da-b27d-570d-944c-1738e559de55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/cocktail glass_d7be86da-b27d-570d-944c-1738e559de55.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cocktail-glass-with-wavy-drink-and-citrus-garnish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('cocktail', 'glass', 'with', 'citrus', 'slice')

    def build(self):
        poly(self,'bowl',(6,14),(24,32),(34,22),(42,14),(26,14),(6,14))
        path(self,'citrus',(26,14),('A',8,8,True,(34,6)),('A',8,8,True,(42,14)))
        line(self,'stem',(24,32),(24,42))
        poly(self,'foot',(14,42),(24,42),(34,42))
        contacts(self)
