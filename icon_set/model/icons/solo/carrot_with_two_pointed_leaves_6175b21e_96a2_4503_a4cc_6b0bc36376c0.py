"""Fresh Carrot Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = 'pictographic-primitives/food/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carrot-with-two-pointed-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('food', 'state')
    tags = ('sub icon',)
    aliases = ()
    keywords = ('carrot', 'root', 'vegetable', 'leaf', 'produce', 'food', 'garden')

    def build(self):
        # Plan: Upright tapered carrot root below two pointed spreading leaves. Lucide carrot organic taper and shared foliage junction. Fine root notches omitted. Leaf span sets the wide envelope (8,4)-(40,44).
        self.add_bezier('root',(24,18),((19,16),(14,20),(14,24)),((14,31),(22,44),(24,44)),((26,44),(34,31),(34,24)),((34,20),(29,16),(24,18)))
        self.add_contour('carrot','root',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'leaf-{side}',p(0,18),(p(6,18),p(16,14),p(16,4)),(p(8,6),p(0,10),p(0,18)))
         self.add_contour(f'leaf-shape-{side}',f'leaf-{side}',closed=True);self.relate('connect',f'leaf-shape-{side}','carrot')
        self.relate('connect','leaf-shape--1','leaf-shape-1')
