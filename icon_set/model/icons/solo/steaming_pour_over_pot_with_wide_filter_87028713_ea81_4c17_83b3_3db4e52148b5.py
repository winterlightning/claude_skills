"""Hot Pour Over Coffee Pot.

Plan: Three steam strokes over a broad filter on a rounded coffee pot with right handle. Bounds (8,4)-(40,44). Tiny pouring lip simplified.
Construction reference: Lucide funnel and coffee: tapered filter and coherent pot/handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '87028713-ea81-4c17-83b3-3db4e52148b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee filter_87028713-ea81-4c17-83b3-3db4e52148b5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'steaming-pour-over-pot-with-wide-filter'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('hot', 'pour', 'over', 'coffee', 'pot')

    def build(self):
        poly(self,'filter',(8,18),(36,18),(28,26),(16,26),(8,18))
        path(self,'pot',(16,26),('L',(8,38)),('A',6,6,False,(14,44)),('L',(28,44)),('A',6,6,False,(34,38)),('L',(28,26)))
        path(self,'handle',(28,26),('L',(32,26)),('A',8,6,True,(40,32)),('A',6,6,True,(34,38)))
        for i,x in enumerate((12,22,32)):
         path(self,f'steam-{i}',(x,4),('A',1,1,True,(x,6)),('A',1,2,False,(x,10)))
        contacts(self)
