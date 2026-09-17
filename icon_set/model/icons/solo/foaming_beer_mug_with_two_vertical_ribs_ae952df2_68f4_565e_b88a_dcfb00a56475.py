"""Beer Mug with Foam.

Plan: Foam crown, mug body, right handle, paired ribs; bounds (6,6)-(42,42).
Construction reference: Lucide beer: scalloped foam and parallel ribs; coffee: rounded base and handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ae952df2-68f4-565e-b88a-dcfb00a56475'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/beer mug_ae952df2-68f4-565e-b88a-dcfb00a56475.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'foaming-beer-mug-with-two-vertical-ribs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('beer', 'mug', 'with', 'foam')

    def build(self):
        path(self,'body',(10,18),('L',(8,18)),('L',(8,38)),('A',4,4,False,(12,42)),('L',(30,42)),('A',4,4,False,(34,38)),('L',(34,34)),('L',(34,20)),('L',(34,14)))
        path(self,'foam',(10,18),('A',4,4,True,(10,10)),('A',8,4,True,(18,6)),('A',8,4,True,(26,10)),('A',8,8,True,(34,18)),('L',(18,18)),('A',4,2,True,(10,18)))
        path(self,'handle',(34,20),('A',8,7,True,(34,34)))
        for x in (17,25): line(self,f'rib-{x}',(x,28),(x,33))
        contacts(self)
