"""Fresh Cilantro Herb Sprig."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dff6770-6d28-4114-ba4d-94dc1f630b89'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cilantro colliander_9dff6770-6d28-4114-ba4d-94dc1f630b89.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-cilantro-sprig'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cilantro', 'coriander', 'herb', 'leaf', 'sprig', 'seasoning', 'plant')

    def build(self):
        # Plan: Three lobed cilantro leaves on a common stem. Lucide sprout branching topology; tiny teeth and veins omitted. Mirror axis x24, envelope (6,6)-(42,42).
        self.add_polyline('top-leaf',(24,22),(17,16),(16,11),(20,12),(20,10),(24,6),(28,10),(28,12),(32,11),(31,16),closed=True)
        self.add_polyline('stem',(24,22),(24,34),(24,42));self.relate('connect','top-leaf','stem')
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_polyline(f'leaf-{side}',p(8,32),p(8,24),p(14,24),p(18,28),p(18,34),p(14,38),p(8,38),p(8,32))
         self.add_line(f'stalk-{side}',p(8,32),(24,34));self.relate('connect',f'stalk-{side}',f'leaf-{side}');self.relate('connect',f'stalk-{side}','stem')
        self.relate('connect','stalk--1','stalk-1')
