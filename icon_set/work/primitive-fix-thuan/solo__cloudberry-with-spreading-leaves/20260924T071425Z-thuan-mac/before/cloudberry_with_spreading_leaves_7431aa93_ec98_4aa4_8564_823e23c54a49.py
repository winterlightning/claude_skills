"""Cloudberry Fruit with Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7431aa93-ec98-4aa4-8564-823e23c54a49'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cloud berry_7431aa93-ec98-4aa4-8564-823e23c54a49.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloudberry-with-spreading-leaves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('cloudberry', 'berry', 'fruit', 'leaf', 'stem', 'produce', 'food')

    def build(self):
        # Plan: Three-lobed cloudberry above two spreading leaves. Shared axis and leaf junction. Lucide grape for reduced fruit grouping; inner segment omitted. Wide envelope (4,8)-(44,40).
        self.add_bezier('fruit',(24,30),((17,30),(10,26),(10,20)),((10,14),(16,12),(18,16)),((16,10),(20,8),(24,8)),((28,8),(32,10),(30,16)),((32,12),(38,14),(38,20)),((38,26),(31,30),(24,30)))
        self.add_contour('berry','fruit',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'leaf-{side}',p(0,30),(p(8,32),p(17,30),p(20,24)),(p(20,38),p(9,40),p(0,30)))
         self.add_contour(f'leaf-outline-{side}',f'leaf-{side}',closed=True)
         self.relate('connect',f'leaf-outline-{side}','berry')
        self.relate('connect','leaf-outline--1','leaf-outline-1')
        self.add_line('stem',(24,30),(24,40))
        for s in ('berry','leaf-outline--1','leaf-outline-1'):self.relate('connect','stem',s)
