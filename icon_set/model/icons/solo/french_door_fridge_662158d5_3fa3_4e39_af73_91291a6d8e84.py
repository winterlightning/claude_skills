"""French Door Refrigerator."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '662158d5-3fa3-4e39-af73-91291a6d8e84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fridge double door_662158d5-3fa3-4e39-af73-91291a6d8e84.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'french-door-fridge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('refrigerator', 'fridge', 'freezer', 'door', 'appliance', 'kitchen', 'storage')

    def build(self):
        # Plan: French-door fridge with central split and lower freezer drawer. Lucide refrigerator rounded box and door seams. Tiny feet and freezer handle omitted to keep clear compartments. Mirrored envelope (8,4)-(40,44).
        self.add_line('top-l',(14,4),(24,4));self.add_line('top-r',(24,4),(34,4))
        self.add_arc('tr',(34,4),(40,10),radius_x=6);self.add_polyline('right',(40,10),(40,30),(40,38));self.add_arc('br',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44));self.add_arc('bl',(14,44),(8,38),radius_x=6);self.add_polyline('left',(8,38),(8,30),(8,10));self.add_arc('tl',(8,10),(14,4),radius_x=6)
        for a,b in (('top-l','top-r'),('top-r','tr'),('tr','right'),('right','br'),('br','bottom'),('bottom','bl'),('bl','left'),('left','tl'),('tl','top-l')):self.relate('connect',a,b)
        self.add_polyline('drawer',(8,30),(24,30),(40,30));self.relate('connect','drawer','left');self.relate('connect','drawer','right')
        self.add_line('split',(24,4),(24,30))
        for n in ('drawer','top-l','top-r'):self.relate('connect','split',n)

        for x in (16,32):self.add_line(f'handle-{x}',(x,14),(x,20))
