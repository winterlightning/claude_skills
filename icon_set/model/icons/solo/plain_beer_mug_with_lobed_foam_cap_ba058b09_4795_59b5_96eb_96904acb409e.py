"""Foaming Beer Mug.

Plan: Plain beer mug with uneven foam crown and attached right handle. Bounds (6,6)-(42,42). No ribs are added.
Construction reference: Lucide beer: foam silhouette and attached handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ba058b09-4795-59b5-96eb-96904acb409e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer glass foam_ba058b09-4795-59b5-96eb-96904acb409e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'plain-beer-mug-with-lobed-foam-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('foaming', 'beer', 'mug')

    def build(self):
        path(self,'mug',(10,18),('L',(8,18)),('L',(8,38)),('A',4,4,False,(12,42)),('L',(30,42)),('A',4,4,False,(34,38)),('L',(34,34)),('L',(34,20)),('L',(34,18)))
        path(self,'foam',(10,18),('A',4,4,True,(10,10)),('A',8,4,True,(18,6)),('A',8,4,True,(26,10)),('A',8,8,True,(34,18)),('L',(10,18)),closed=True)
        path(self,'handle',(34,20),('A',8,7,True,(34,34)))
        contacts(self)
