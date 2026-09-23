from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77a84225-bc63-404c-8e7b-1890d0aceb3d'
SOURCE_PATH = 'icon_set/work/todo-references/adder_77a84225-bc63-404c-8e7b-1890d0aceb3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'adder'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('adder',)

    def build(self):
        # Pythagorean integer points lie on radius 20; two crossing diameters.
        # Deliberate slight rotation retains integer grid without approximating the circle.
        points=[(12,8),(40,12),(36,40),(8,36)]
        for i,start in enumerate(points):
            self.add_arc(f'ring-{i}',start,points[(i+1)%4],radius_x=20)
        self.add_contour('ring',*[f'ring-{i}' for i in range(4)],closed=True)
        self.add_line('diagonal-one',points[0],points[2])
        self.add_line('diagonal-two',points[1],points[3])
        self.relate('connect','ring','diagonal-one')
        self.relate('connect','ring','diagonal-two')
        self.relate('connect','diagonal-one','diagonal-two')
