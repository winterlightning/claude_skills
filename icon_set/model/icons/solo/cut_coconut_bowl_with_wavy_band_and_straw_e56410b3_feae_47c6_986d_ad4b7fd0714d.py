"""Coconut Drink with Straw.

Plan: Low coconut bowl with wavy cut band and curved straw; bounds (6,6)-(42,42).
Construction reference: Lucide database: curved bowl edge; no useful coconut match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e56410b3-feae-47c6-986d-ad4b7fd0714d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coconut_e56410b3-feae-47c6-986d-ad4b7fd0714d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cut-coconut-bowl-with-wavy-band-and-straw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('coconut', 'drink', 'with', 'straw')

    def build(self):
        path(self,'shell',(6,20),('L',(6,30)),('A',18,12,False,(42,30)),('L',(42,20)),('L',(30,20)),('L',(6,20)))
        path(self,'wave',(6,30),('A',9,2,True,(24,30)),('A',9,2,False,(42,30)))
        path(self,'straw',(30,20),('L',(33,10)),('A',4,4,True,(37,6)),('L',(42,6)))
        contacts(self)
