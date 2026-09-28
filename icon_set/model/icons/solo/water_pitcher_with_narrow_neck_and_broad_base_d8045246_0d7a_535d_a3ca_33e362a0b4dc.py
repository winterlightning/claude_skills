"""Kitchen Water Serving Pitcher.

Plan: Tall water pitcher with inward-curving neck, left lip and broad lower body plus right handle. Bounds (6,6)-(42,42).
Construction reference: Lucide milk: S-shaped neck transition; coffee: attached handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd8045246-0d7a-535d-a3ca-33e362a0b4dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water pitcher_d8045246-0d7a-535d-a3ca-33e362a0b4dc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'water-pitcher-with-narrow-neck-and-broad-base'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('kitchen', 'water', 'serving', 'pitcher')

    def build(self):
        path(self,'body',(6,6),('L',(30,6)),('L',(30,14)),('A',4,8,False,(34,22)),('L',(34,34)),('A',8,8,True,(26,42)),('L',(14,42)),('A',8,8,True,(6,34)),('L',(6,30)),('A',4,8,True,(10,22)),('A',4,8,False,(14,14)),('A',8,8,False,(6,6)),closed=True)
        path(self,'handle',(30,6),('A',12,12,True,(42,18)),('A',8,16,True,(34,34)))
        contacts(self)
