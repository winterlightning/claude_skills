"""Eggs in Carton."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fdd4b62-8157-48bc-92dc-008ab4c1e760'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/eggs_9fdd4b62-8157-48bc-92dc-008ab4c1e760.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-eggs-in-carton'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('egg', 'carton', 'packaging', 'breakfast', 'poultry', 'food', 'groceries')

    def build(self):
        # Plan: Three touching egg arches above three carton pockets. Lucide egg cubic silhouettes. One rim replaces double rail; all neighboring forms share explicit nodes. Envelope (4,8)-(44,40).
        intervals=((4,18,11),(18,30,24),(30,44,37))
        for i,(l,r,x) in enumerate(intervals):
         self.add_bezier(f'egg-{i}',(l,26),((l,18),(x-3,8),(x,8)),((x+3,8),(r,18),(r,26)))
         self.add_bezier(f'pocket-{i}',(l,26),((l+2,40),(x-4,40),(x,40)),((x+4,40),(r-2,40),(r,26)))
         self.relate('connect',f'egg-{i}',f'pocket-{i}')
        self.add_polyline('rim',(4,26),(18,26),(30,26),(44,26))
        for i in range(3):
         for prefix in ('egg','pocket'):self.relate('connect',f'{prefix}-{i}','rim')
        for i in range(2):
         for a in ('egg','pocket'):
          for b in ('egg','pocket'):self.relate('connect',f'{a}-{i}',f'{b}-{i+1}')
