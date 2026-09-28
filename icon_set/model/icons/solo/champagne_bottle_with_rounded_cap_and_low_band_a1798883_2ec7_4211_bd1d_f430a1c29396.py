"""Champagne Sparkling Wine Bottle.

Plan: Symmetric tall bottle with cap and lower band; bounds (10,4)-(38,44). Mirrored smooth shoulders.
Construction reference: Lucide bottle-wine: narrow neck and paired shoulder transitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a1798883-2ec7-4211-bd1d-f430a1c29396'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/champagne bottle_a1798883-2ec7-4211-bd1d-f430a1c29396.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'champagne-bottle-with-rounded-cap-and-low-band'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('champagne', 'sparkling', 'wine', 'bottle')

    def build(self):
        path(self,'outline',(18,14),('L',(18,10)),('A',6,6,True,(30,10)),('L',(30,14)),('L',(30,16)),('A',8,10,False,(34,24)),('A',8,10,True,(38,32)),('L',(38,36)),('L',(38,40)),('A',4,4,True,(34,44)),('L',(14,44)),('A',4,4,True,(10,40)),('L',(10,36)),('L',(10,32)),('A',8,10,True,(14,24)),('A',8,10,False,(18,16)),('L',(18,14)),closed=True)
        line(self,'cap-seam',(18,14),(30,14))
        line(self,'low-band',(10,36),(38,36))
        contacts(self)
