'Three flowers in a vase: equal round blossoms and mirrored leaves attach to real stems; simplify tiny petal lobes while preserving the bouquet.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d236e3c-000a-4b02-9065-9a95cf6d2b26'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/vase plant_0d236e3c-000a-4b02-9065-9a95cf6d2b26.svg'
AUTHOR = 'gpt-6'


class ThreeBlossomVaseWithPairedLeaves(Solo48):
    icon_id = 'three-blossom-vase-with-paired-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'flowers', 'blossoms', 'bouquet', 'leaves', 'plant', 'decor')

    def build(self) -> None:
        self.add_arc('flower-left-top', (8,10), (16,10), radius_x=4, radius_y=4)
        self.add_arc('flower-left-bottom', (16,10), (8,10), radius_x=4, radius_y=4)
        self.add_contour('flower-left', 'flower-left-top', 'flower-left-bottom', closed=True)

        self.add_arc('flower-right-top', (32,10), (40,10), radius_x=4, radius_y=4)
        self.add_arc('flower-right-bottom', (40,10), (32,10), radius_x=4, radius_y=4)
        self.add_contour('flower-right', 'flower-right-top', 'flower-right-bottom', closed=True)

        self.add_arc('flower-front-top', (20,26), (28,26), radius_x=4, radius_y=4)
        self.add_arc('flower-front-bottom', (28,26), (20,26), radius_x=4, radius_y=4)
        self.add_contour('flower-front', 'flower-front-top', 'flower-front-bottom', closed=True)

        self.add_line('stem-left',(12,14),(24,22));self.add_line('stem-right',(36,14),(24,22))
        self.relate('connect','stem-left','flower-left');self.relate('connect','stem-right','flower-right')
        self.relate('connect','stem-left','flower-front');self.relate('connect','stem-right','flower-front');self.relate('connect','stem-left','stem-right')
        self.add_bezier('leaf-left',(6,24),((10,24),(13,28),(14,33)))
        self.add_bezier('leaf-right',(42,24),((38,24),(35,28),(34,33)))
        self.add_polyline('vase',(14,33),(14,42),(24,42),(34,42),(34,33));self.relate('connect','vase','main-stem')
        self.relate('connect','leaf-left','vase')
        self.relate('connect','leaf-right','vase')
        self.add_line('main-stem',(24,30),(24,42))
        self.relate('connect','main-stem','flower-front')
