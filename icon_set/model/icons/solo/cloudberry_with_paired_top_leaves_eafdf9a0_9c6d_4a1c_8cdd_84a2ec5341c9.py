"""Cloudberry Fruit with Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eafdf9a0-9c6d-4a1c-8cdd-84a2ec5341c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cloud berry_eafdf9a0-9c6d-4a1c-8cdd-84a2ec5341c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloudberry-with-paired-top-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cloudberry', 'berry', 'fruit', 'leaf', 'cluster', 'stem', 'food')

    def build(self):
        # Plan: Four rounded berry lobes with paired pointed top leaves. Lucide grape grouping; small inner ring reduced to dot and tiny stem omitted. Mirrored envelope (8,4)-(40,44).
        self.add_bezier('berry',(24,20),((16,14),(8,20),(8,26)),((8,31),(11,34),(16,34)),((10,39),(17,44),(20,44)),((22,44),(23,43),(24,42)),((25,43),(26,44),(28,44)),((31,44),(38,39),(32,34)),((37,34),(40,31),(40,26)),((40,20),(32,14),(24,20)))
        self.add_contour('fruit','berry',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'leaf-{side}',p(0,20),(p(0,10),p(5,4),p(12,4)),(p(12,12),p(9,18),p(0,20)))
         self.add_contour(f'leaf-shape-{side}',f'leaf-{side}',closed=True);self.relate('connect',f'leaf-shape-{side}','fruit')
        self.relate('connect','leaf-shape--1','leaf-shape-1')
        self.add_dot('center',(24,31))
