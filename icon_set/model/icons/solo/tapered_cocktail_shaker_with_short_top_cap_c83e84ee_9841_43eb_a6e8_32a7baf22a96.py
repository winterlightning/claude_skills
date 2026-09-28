"""Professional Bar Cocktail Shaker.

Plan: Cocktail shaker with short rounded cap, broad shoulders and tapered body. Bounds (10,4)-(38,44). Reflection dropped to keep the lid band open.
Construction reference: Lucide bottle-wine: cap and shoulders; glass-water: tapered lower body.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c83e84ee-9841-43eb-a6e8-32a7baf22a96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/cocktail shaker_c83e84ee-9841-43eb-a6e8-32a7baf22a96.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-cocktail-shaker-with-short-top-cap'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('professional', 'bar', 'cocktail', 'shaker')

    def build(self):
        box(self,'cap',18,4,30,12,3)
        poly(self,'shoulder',(21,12),(10,22),(38,22),(27,12))
        path(self,'body',(10,22),('L',(14,40)),('A',4,4,False,(18,44)),('L',(30,44)),('A',4,4,False,(34,40)),('L',(38,22)))
        contacts(self)
