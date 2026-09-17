"""Storefront with Awning.
Plan: Shop root owns three equal scallops, paired panel divisions, walls and centered doorway. Extrema (6,6)-(42,42).
Reference: Lucide store: shared panel/scallop construction and centered doorway.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d9e1f0d-89f1-5379-bdee-f0e4f12da344'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/carnival shop_0d9e1f0d-89f1-5379-bdee-f0e4f12da344.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'storefront-three-scallop-awning'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/celebrations"
    aliases = ()
    keywords = ('storefront', 'with', 'awning')

    def build(self):

        self.add_polyline('roof',(6,16),(10,6),(18,6),(30,6),(38,6),(42,16))
        for i,x in enumerate((6,18,30)):
            self.add_arc(f'scallop-{i}',(x,16),(x+12,16),radius_x=6,radius_y=4,sweep=False)
        self.relate('connect','roof','scallop-0');self.relate('connect','roof','scallop-2')
        for i in range(2):self.relate('connect',f'scallop-{i}',f'scallop-{i+1}')
        for i,x in enumerate((18,30)):
            self.add_line(f'panel-{i}',(x,6),(x,16))
            for other in ('roof',f'scallop-{i}',f'scallop-{i+1}'):self.relate('connect',f'panel-{i}',other)
        self.add_polyline('walls',(6,16),(6,30),(6,42),(18,42),(30,42),(42,42),(42,30),(42,16))
        for other in ('roof','scallop-0','scallop-2'):self.relate('connect','walls',other)
        self.add_polyline('door',(18,42),(18,30),(30,30),(30,42))
        self.relate('connect','door','walls')
        for i,(a,b) in enumerate((((6,30),(18,30)),((30,30),(42,30)))):
            self.add_line(f'frontage-{i}',a,b)
            self.relate('connect',f'frontage-{i}','door');self.relate('connect',f'frontage-{i}','walls')
