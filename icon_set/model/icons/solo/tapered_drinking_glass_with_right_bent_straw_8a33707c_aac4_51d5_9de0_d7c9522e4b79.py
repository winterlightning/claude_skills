"""Drink Glass with Straw.

Plan: Tall tapered glass, wavy water and right-bent straw. Bounds (10,4)-(38,44). Water/straw/rim crossings share exact nodes.
Construction reference: Lucide cup-soda and glass-water: tapered sides and water wave.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8a33707c-aac4-51d5-9de0-d7c9522e4b79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/soft drinks glass_8a33707c-aac4-51d5-9de0-d7c9522e4b79.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tapered-drinking-glass-with-right-bent-straw'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('drink', 'glass', 'with', 'straw')

    def build(self):
        axis=24
        side=1
        p=lambda x,y:(axis+side*(x-axis),y)
        path(self,'glass',p(10,12),('L',p(28,12)),('L',p(38,12)),('L',p(36,26)),('L',p(34,40)),('A',4,4,side>0,p(30,44)),('L',p(18,44)),('A',4,4,side>0,p(14,40)),('L',p(12,26)),('L',p(10,12)),closed=True)
        path(self,'water',p(12,26),('A',6,2,side>0,p(24,26)),('A',6,2,side<0,p(36,26)))
        poly(self,'straw',p(24,34),p(24,26),p(28,12),p(30,4),p(38,4))
        contacts(self)
