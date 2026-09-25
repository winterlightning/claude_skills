"""Coffee Maker with Cup.

Plan: Coffee machine with overhead filter and mug on base; bounds (6,6)-(42,42). Support and nozzle simplified for native-size clarity.
Construction reference: Lucide coffee: rounded mug base and right handle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0e2b7e1f-e2d9-4454-b5fe-2a7bd7d71030'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee machine_0e2b7e1f-e2d9-4454-b5fe-2a7bd7d71030.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'coffee-machine-with-overhead-filter-and-mug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('coffee', 'maker', 'with', 'cup')

    def build(self):
        poly(self,'stand',(6,42),(6,6),(38,6),(38,14),(30,14),(16,14),(6,14))
        poly(self,'filter',(16,14),(20,22),(30,22),(34,14))
        path(self,'cup',(18,30),('L',(34,30)),('L',(34,36)),('A',6,6,True,(28,42)),('L',(24,42)),('A',6,6,True,(18,36)),('L',(18,30)),closed=True)
        path(self,'handle',(34,30),('A',8,6,True,(42,36)))
        poly(self,'base',(6,42),(24,42),(28,42),(42,42))
        contacts(self)
