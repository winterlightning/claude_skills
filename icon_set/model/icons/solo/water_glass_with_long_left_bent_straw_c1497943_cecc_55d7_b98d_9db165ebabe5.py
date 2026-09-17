"""Glass of Water with Straw.

Plan: Tall tapered glass, wavy water and left-bent straw. Bounds (10,4)-(38,44). Mirrored leftward straw preserves the source direction.
Construction reference: Lucide cup-soda and glass-water: tapered sides and water wave.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'c1497943-cecc-55d7-b98d-9db165ebabe5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/water straw_c1497943-cecc-55d7-b98d-9db165ebabe5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'water-glass-with-long-left-bent-straw'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('glass', 'of', 'water', 'with', 'straw')

    def build(self):
        axis=24
        side=-1
        p=lambda x,y:(axis+side*(x-axis),y)
        path(self,'glass',p(10,12),('L',p(28,12)),('L',p(38,12)),('L',p(36,26)),('L',p(34,40)),('A',4,4,side>0,p(30,44)),('L',p(18,44)),('A',4,4,side>0,p(14,40)),('L',p(12,26)),('L',p(10,12)),closed=True)
        path(self,'water',p(12,26),('A',6,2,side>0,p(24,26)),('A',6,2,side<0,p(36,26)))
        poly(self,'straw',p(24,34),p(24,26),p(28,12),p(30,4),p(38,4))
        contacts(self)
