'Cactus in rimmed pot v4. Refit the small cactus crown with tangent quarter circles and give the pot eight units of depth; preserve the separately approved larger-arm cactus.\nOriginal subject geometry is retained and refitted to the current native keyshape. Directional asymmetry is intentional. Construction review: original drawing; sprout or bug principles for the plant and beetle.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPot(Solo48):
    icon_id = 'cactus-in-rimmed-pot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        self.add_line('trunk-left-bottom', (18, 28), (18, 22))
        self.add_arc('left-arm-outer', (18, 22), (8, 12), radius_x=10)
        self.add_arc('left-arm-cap', (8, 12), (16, 12), radius_x=4)
        self.add_arc('left-arm-inner', (16, 12), (18, 14), radius_x=2, sweep=False)
        self.add_line('trunk-left-top', (18, 14), (18, 10))
        self.add_arc('head-left', (18, 10), (24, 4), radius_x=6)
        self.add_arc('head-right', (24, 4), (30, 10), radius_x=6)
        self.add_line('trunk-right-top', (30, 10), (30, 14))
        self.add_arc('right-arm-inner', (30, 14), (32, 12), radius_x=2, sweep=False)
        self.add_arc('right-arm-cap', (32, 12), (40, 12), radius_x=4)
        self.add_arc('right-arm-outer', (40, 12), (30, 22), radius_x=10)
        self.add_line('trunk-right-bottom', (30, 22), (30, 28))
        self.add_contour('cactus', 'trunk-left-bottom', 'left-arm-outer', 'left-arm-cap', 'left-arm-inner', 'trunk-left-top', 'head-left', 'head-right', 'trunk-right-top', 'right-arm-inner', 'right-arm-cap', 'right-arm-outer', 'trunk-right-bottom')
        self.add_polyline('rim', (10, 28), (24, 28), (38, 28), (38, 36), (34, 36), (14, 36), (10, 36), closed=True)
        self.add_polyline('pot', (14, 36), (16, 44), (32, 44), (34, 36))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'cactus', 'rim')
