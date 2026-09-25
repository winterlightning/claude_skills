"""Steaming Hot Coffee Cup.

Plan: Broad hot cup with two equal S-shaped steam strokes and right handle. Bounds (6,6)-(42,42); same steam rhythm repeated about cup axis.
Construction reference: Lucide coffee: rounded base, attached handle and spare steam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b3563c1c-6c48-4e0d-9e2e-a4064526d073'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cup hot_b3563c1c-6c48-4e0d-9e2e-a4064526d073.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rounded-coffee-cup-with-two-thick-steam-curves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('steaming', 'hot', 'coffee', 'cup')

    def build(self):
        path(self,'cup',(6,24),('L',(32,24)),('L',(32,36)),('A',6,6,True,(26,42)),('L',(12,42)),('A',6,6,True,(6,36)),('L',(6,24)),closed=True)
        path(self,'handle',(32,24),('A',10,6,True,(32,36)))
        for i,x in enumerate((13,25)):
         path(self,f'steam-{i}',(x,6),('A',1,2,False,(x,10)),('A',1,2,True,(x,14)))
        contacts(self)
