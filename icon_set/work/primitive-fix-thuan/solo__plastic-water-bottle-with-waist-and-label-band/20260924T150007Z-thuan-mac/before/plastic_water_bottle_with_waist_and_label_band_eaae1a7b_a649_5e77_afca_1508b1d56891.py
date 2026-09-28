"""Plastic Water Bottle.

Plan: Plastic water bottle with cap, shoulders, label band and pinched waist. Bounds (10,4)-(38,44). Lower seam omitted to leave the waist clear.
Construction reference: Lucide bottle-wine and milk: paired shoulders and rounded base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'eaae1a7b-a649-5e77-afca-1508b1d56891'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water bottle_eaae1a7b-a649-5e77-afca-1508b1d56891.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'plastic-water-bottle-with-waist-and-label-band'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('plastic', 'water', 'bottle')

    def build(self):
        path(self,'outline',(18,12),('L',(18,4)),('L',(30,4)),('L',(30,12)),('L',(38,20)),('L',(38,28)),('A',4,4,True,(34,32)),('A',4,4,False,(38,36)),('L',(38,40)),('A',4,4,True,(34,44)),('L',(14,44)),('A',4,4,True,(10,40)),('L',(10,36)),('A',4,4,False,(14,32)),('A',4,4,True,(10,28)),('L',(10,20)),('L',(18,12)),closed=True)
        line(self,'cap-seam',(18,12),(30,12))
        for y in (20,28):line(self,f'label-{y}',(10,y),(38,y))
        contacts(self)
