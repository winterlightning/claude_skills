"""Underwear bra (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3b3183b-a5c5-5cf0-9723-f3424e6fedf1'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear bra_c3b3183b-a5c5-5cf0-9723-f3424e6fedf1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class UnderwearBraClothes(Solo48):
    icon_id = 'underwear-bra-clothes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('underwear', 'bra', 'clothes')

    def build(self):
        self.add_line('sym-e0', (26, 34), (22, 34))
        self.add_arc('sym-e1', (22, 34), (14, 40), radius_x=9)
        self.add_arc('sym-e3', (14, 40), (13, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e4-1', (13, 40), (6, 36), radius_x=9)
        self.add_arc('sym-e4-2', (6, 36), (4, 30), radius_x=10)
        self.add_line('sym-e6', (4, 30), (4, 29))
        self.add_arc('sym-e7', (4, 29), (8, 20), radius_x=18)
        self.add_arc('sym-e8', (8, 20), (8, 16), radius_x=21)
        self.add_arc('sym-e9', (8, 16), (9, 9), radius_x=52)
        self.add_arc('sym-e10', (9, 9), (9, 8), radius_x=28, sweep=False)
        self.add_arc('sym-e11', (39, 8), (39, 9), radius_x=28, sweep=False)
        self.add_arc('sym-e12', (39, 9), (40, 16), radius_x=51, sweep=False)
        self.add_line('sym-e13', (40, 16), (40, 20))
        self.add_arc('sym-e14', (40, 20), (44, 29), radius_x=18)
        self.add_line('sym-e15', (44, 29), (44, 30))
        self.add_arc('sym-e17-1', (44, 30), (42, 36), radius_x=10)
        self.add_arc('sym-e17-2', (42, 36), (35, 40), radius_x=9)
        self.add_line('sym-e18', (35, 40), (34, 40))
        self.add_arc('sym-e20', (34, 40), (26, 34), radius_x=9)
        self.add_arc('sym-e21', (26, 34), (31, 25), radius_x=14)
        self.add_line('sym-e22', (31, 25), (35, 24))
        self.add_arc('sym-e23', (35, 24), (39, 22), radius_x=13)
        self.add_arc('sym-e24', (39, 22), (40, 20), radius_x=9)
        self.add_arc('sym-e25', (22, 34), (17, 25), radius_x=14, sweep=False)
        self.add_line('sym-e26', (17, 25), (13, 24))
        self.add_arc('sym-e27', (13, 24), (9, 22), radius_x=13, sweep=False)
        self.add_line('sym-e28', (9, 22), (8, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17-1', 'sym-e17-2', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c2', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
