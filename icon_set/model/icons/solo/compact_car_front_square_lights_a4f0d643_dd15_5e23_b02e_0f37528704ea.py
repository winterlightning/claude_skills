"""A compact car front with an arched cabin and square lamps. Lucide car-front informed bilateral construction. Square keyshape fits the frontal view; interior lamp dashes and tyre loops reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4f0d643-dd15-5e23-b02e-0f37528704ea'
SOURCE_PATH = 'pictographic-primitives/transportation/car smart_a4f0d643-dd15-5e23-b02e-0f37528704ea.svg'
SOURCE_REFERENCES = (('a4f0d643-dd15-5e23-b02e-0f37528704ea', 'pictographic-primitives/transportation/car smart_a4f0d643-dd15-5e23-b02e-0f37528704ea.svg'),)
AUTHOR = 'gpt-6'

class CompactCarFrontSquareLights(Solo48):
    icon_id = 'compact-car-front-square-lights'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'front', 'compact', 'smart car', 'headlights', 'vehicle', 'city car', 'head-on')

    def build(self) -> None:
        self.add_line('body-top-0',(8, 18),(10, 18))
        self.add_line('body-top-1',(10, 18),(38, 18))
        self.add_line('body-top-2',(38, 18),(40, 18))
        self.add_arc('body-top-corner',(40, 18),(42, 20),radius_x=2)
        self.add_line('body-right-0',(42, 20),(42, 26))
        self.add_line('body-right-1',(42, 26),(42, 34))
        self.add_arc('body-right-corner',(42, 34),(40, 36),radius_x=2)
        self.add_line('body-bottom-0',(40, 36),(38, 36))
        self.add_line('body-bottom-1',(38, 36),(34, 36))
        self.add_line('body-bottom-2',(34, 36),(14, 36))
        self.add_line('body-bottom-3',(14, 36),(10, 36))
        self.add_line('body-bottom-4',(10, 36),(8, 36))
        self.add_arc('body-bottom-corner',(8, 36),(6, 34),radius_x=2)
        self.add_line('body-left-0',(6, 34),(6, 26))
        self.add_line('body-left-1',(6, 26),(6, 20))
        self.add_arc('body-left-corner',(6, 20),(8, 18),radius_x=2)
        self.add_contour('body','body-top-0','body-top-1','body-top-2','body-top-corner','body-right-0','body-right-1','body-right-corner','body-bottom-0','body-bottom-1','body-bottom-2','body-bottom-3','body-bottom-4','body-bottom-corner','body-left-0','body-left-1','body-left-corner',closed=True)

        self.add_arc('cabin',(10,18),(38,18),radius_x=14,radius_y=12)
        self.relate('connect','cabin','body')
        for side,x,inner in [('left',6,14),('right',42,34)]:
            self.add_polyline(side+'-light',(x,26),(inner,26),(inner,36))
            self.relate('connect',side+'-light','body')
        for x in (10,38):
            self.add_line(f'wheel-{x}',(x,36),(x,42))
            self.relate('connect',f'wheel-{x}','body')
