"""Two skewered cocktail cherries.

Plan: Two round cocktail cherries on a diagonal pick. Bounds (8,4)-(40,44). Two naturally touching cherries share their true tangent point as in the source; highlights and tiny finial reduced away. Pick ends follow the fruit axis and meet exact arc endpoints.
Construction reference: Lucide cherry: equal repeated fruit, adapted to an intentionally diagonal skewered pair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '683191b9-6168-4c96-b365-29741ad3a61d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/cocktail cherry_683191b9-6168-4c96-b365-29741ad3a61d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-cocktail-cherries-on-diagonal-pick'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('two', 'skewered', 'cocktail', 'cherries')

    def build(self):
        # The 6-8-10 points place both pick ends on the same 3:4 diagonal fruit axis.
        path(self,'lower',(24,24),('A',10,10,True,(28,32)),('A',10,10,True,(18,42)),('A',10,10,True,(12,40)),('A',10,10,True,(8,32)),('A',10,10,True,(18,22)),('A',10,10,True,(24,24)),closed=True)
        path(self,'upper',(24,24),('A',10,10,True,(20,16)),('A',10,10,True,(30,6)),('A',10,10,True,(36,8)),('A',10,10,True,(40,16)),('A',10,10,True,(30,26)),('A',10,10,True,(24,24)),closed=True)
        line(self,'pick-tip',(12,40),(9,44))
        line(self,'pick-top',(36,8),(39,4))
        contacts(self)
