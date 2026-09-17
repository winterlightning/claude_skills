"""Coconut Drink with Straw.

Plan: Round coconut with elliptical cut rim and bent straw; bounds (6,6)-(42,42). Straw leans naturally to right.
Construction reference: Lucide database: elliptical opening; no useful coconut match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '468bae11-e7af-5854-8fd7-775adebf1161'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/soft drinks coconut_468bae11-e7af-5854-8fd7-775adebf1161.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-coconut-with-open-rim-and-angled-straw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('coconut', 'drink', 'with', 'straw')

    def build(self):
        path(self,'shell',(10,18),('A',4,10,False,(6,28)),('A',18,14,False,(24,42)),('A',18,14,False,(42,28)),('A',4,10,False,(38,18)))
        ellipse(self,'rim',24,18,14,4)
        poly(self,'straw',(24,14),(32,6),(40,6))
        contacts(self)
