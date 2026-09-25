"""Glass Coffee Pot Carafe.

Plan: Round coffee carafe with raised left pouring lip, sloping collar, open handle and water line. Bounds (4,8)-(44,40).
Construction reference: Lucide coffee: coherent bowl curves and handle; no exact carafe match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9f84487f-01c8-57b4-9884-2e9c021c06a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee pot_9f84487f-01c8-57b4-9884-2e9c021c06a0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'round-coffee-carafe-with-sloping-upper-collar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('glass', 'coffee', 'pot', 'carafe')

    def build(self):
        poly(self,'collar',(6,8),(32,12),(32,20),(12,20),(6,8))
        path(self,'bowl',(12,20),('A',8,12,False,(4,32)),('A',8,8,False,(12,40)),('L',(28,40)),('A',8,8,False,(36,32)),('A',8,12,False,(32,20)))
        line(self,'water',(4,32),(36,32))
        path(self,'handle',(32,12),('L',(36,12)),('A',8,8,True,(44,20)),('L',(44,28)))
        contacts(self)
