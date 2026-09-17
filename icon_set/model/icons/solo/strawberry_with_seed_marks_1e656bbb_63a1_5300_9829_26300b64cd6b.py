"""Fresh Strawberry Fruit with Seeds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e656bbb-63a1-5300-9829-26300b64cd6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/strawberry_1e656bbb-63a1-5300-9829-26300b64cd6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'strawberry-with-seed-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('strawberry', 'berry', 'fruit', 'seed', 'leaf', 'produce', 'food')

    def build(self):
        # Plan: Strawberry with two pointed leaves and three seed dots. Lucide apple curved fruit structure. Tiny stem and surplus seeds omitted; shared mirror axis. Envelope (8,4)-(40,44).
        self.add_bezier('fruit',(24,16),((16,16),(8,16),(8,23)),((8,31),(19,44),(24,44)),((29,44),(40,31),(40,23)),((40,16),(32,16),(24,16)))
        self.add_contour('berry','fruit',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'leaf-{side}',p(0,16),(p(0,8),p(4,4),p(14,4)),(p(12,12),p(6,16),p(0,16)))
         self.add_contour(f'leaf-outline-{side}',f'leaf-{side}',closed=True);self.relate('connect',f'leaf-outline-{side}','berry')
        self.relate('connect','leaf-outline--1','leaf-outline-1')
        for i,pt in enumerate(((18,25),(30,25),(24,34))):self.add_dot(f'seed-{i}',pt)
