"""Pour Over Coffee Maker.

Plan: Domed coffee maker with tapered upper chamber, left handle and raised right spout. Bounds (4,8)-(44,40).
Construction reference: Lucide coffee: handle and lower vessel; no useful exact maker match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7b497a79-d5cc-43a6-98ba-cd8d83a4f562'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cold press_7b497a79-d5cc-43a6-98ba-cd8d83a4f562.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'domed-coffee-maker-with-side-spout-and-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('pour', 'over', 'coffee', 'maker')

    def build(self):
        poly(self,'upper',(10,16),(38,16),(44,16),(34,28),(14,28),(10,16))
        path(self,'dome',(10,16),('A',14,8,True,(24,8)),('A',14,8,True,(38,16)))
        box(self,'lower',14,28,34,40,4)
        path(self,'handle',(10,16),('A',6,6,False,(10,28)),('L',(14,28)))
        contacts(self)
