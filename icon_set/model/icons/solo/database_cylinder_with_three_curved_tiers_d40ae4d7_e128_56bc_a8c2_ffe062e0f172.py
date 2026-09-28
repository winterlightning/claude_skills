"""Three Tiered Database Storage.

Plan: Cylinder with elliptical lid and three tiers; bounds (8,4)-(40,44). Repeated curved seams at a shared pitch.
Construction reference: Lucide database: elliptic tiers and tangent upright sides.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd40ae4d7-e128-56bc-a8c2-ffe062e0f172'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/database_d40ae4d7-e128-56bc-a8c2-ffe062e0f172.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'database-cylinder-with-three-curved-tiers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'tiered', 'database', 'storage')

    def build(self):
        ellipse(self,'lid',24,8,16,4)
        for side,x in [('left',8),('right',40)]:
         poly(self,side,(x,8),(x,18),(x,28),(x,40))
        for i,y in enumerate((18,28,40)):
         path(self,f'tier-{i}',(8,y),('A',16,4,False,(40,y)))
        contacts(self)
