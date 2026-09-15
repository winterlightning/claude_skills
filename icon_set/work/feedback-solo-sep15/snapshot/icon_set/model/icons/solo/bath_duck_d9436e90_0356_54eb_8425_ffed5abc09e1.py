'Bath duck v3. Refit bill and quarter-ellipse body to the current horizontal envelope.\nOriginal subject geometry is retained and refitted to the current native keyshape. Directional asymmetry is intentional. Construction review: original drawing; sprout or bug principles for the plant and beetle.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9436e90-0356-54eb-8425-ffed5abc09e1'
SOURCE_PATH = 'pictographic-primitives/babies/toys duck_d9436e90-0356-54eb-8425-ffed5abc09e1.svg'
AUTHOR = 'gpt-6'

class BathDuck(Solo48):
    icon_id = 'bath-duck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('bath', 'duck', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        self.add_arc('head-top', (10, 18), (20, 8), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('head-back', (20, 8), (30, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('neck', (30, 18), (26, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('back', (26, 26), (44, 23), radius_x=22, radius_y=12, sweep=False)
        self.add_contour('upper', 'head-top', 'head-back', 'neck', 'back', closed=False)
        self.add_line('tail', (44, 23), (44, 26))
        self.add_arc('body-right', (44, 26), (32, 40), radius_x=12, radius_y=14, sweep=True)
        self.add_line('belly', (32, 40), (22, 40))
        self.add_arc('body-left', (22, 40), (10, 28), radius_x=12, radius_y=12, sweep=True)
        self.add_line('throat', (10, 28), (13, 26))
        self.add_line('bill-1', (13, 26), (4, 26))
        self.add_line('bill-2', (4, 26), (4, 18))
        self.add_line('bill-3', (4, 18), (10, 18))
        self.add_contour('lower', 'tail', 'body-right', 'belly', 'body-left', 'throat', 'bill-1', 'bill-2', 'bill-3', closed=False)
        self.relate('connect', 'upper', 'lower')
