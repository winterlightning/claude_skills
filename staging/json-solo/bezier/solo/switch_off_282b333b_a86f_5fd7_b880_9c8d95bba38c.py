"""Switch off (furnitures), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '282b333b-a86f-5fd7-b880-9c8d95bba38c'
SOURCE_PATH = 'icons-json/furnitures/switch off_282b333b-a86f-5fd7-b880-9c8d95bba38c.json'
AUTHOR = 'json_to_solo'

class SwitchOffFurnitures(Solo48):
    icon_id = 'switch-off-furnitures'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('switch', 'off', 'furnitures')

    def build(self):
        self.add_line('sym-e0', (30, 24), (18, 24))
        self.add_line('sym-e1', (18, 24), (18, 33))
        self.add_bezier('sym-e2', (18, 33), ((18.286, 33.882), (18.931, 35), (20, 35)))
        self.add_line('sym-e3', (20, 35), (24, 35))
        self.add_line('sym-e4', (24, 35), (28, 35))
        self.add_bezier('sym-e5', (28, 35), ((29.069, 35), (29.714, 33.882), (30, 33)))
        self.add_line('sym-e6', (30, 33), (30, 24))
        self.add_line('sym-e7', (30, 24), (30, 15))
        self.add_bezier('sym-e8', (30, 15), ((29.714, 14.118), (29.069, 13), (28, 13)))
        self.add_line('sym-e9', (28, 13), (24, 13))
        self.add_line('sym-e10', (24, 13), (20, 13))
        self.add_bezier('sym-e11', (20, 13), ((18.931, 13), (18.286, 14.118), (18, 15)))
        self.add_line('sym-e12', (18, 15), (18, 24))
        self.add_line('sym-e13', (24, 44), (37, 44))
        self.add_bezier('sym-e14', (37, 44), ((37.093, 44), (36.907, 44), (37, 44)))
        self.add_bezier('sym-e15', (37, 44), ((38.465, 44), (40, 42.782), (40, 41)))
        self.add_line('sym-e16', (40, 41), (40, 24))
        self.add_line('sym-e17', (40, 24), (40, 7))
        self.add_bezier('sym-e18', (40, 7), ((40, 5.218), (38.465, 4), (37, 4)))
        self.add_bezier('sym-e19', (37, 4), ((36.907, 4), (37.093, 4), (37, 4)))
        self.add_line('sym-e20', (37, 4), (24, 4))
        self.add_line('sym-e21', (24, 4), (11, 4))
        self.add_bezier('sym-e22', (11, 4), ((10.907, 4), (11.093, 4), (11, 4)))
        self.add_bezier('sym-e23', (11, 4), ((9.535, 4), (8, 5.218), (8, 7)))
        self.add_line('sym-e24', (8, 7), (8, 24))
        self.add_line('sym-e25', (8, 24), (8, 41))
        self.add_bezier('sym-e26', (8, 41), ((8, 42.782), (9.535, 44), (11, 44)))
        self.add_bezier('sym-e27', (11, 44), ((11.093, 44), (10.907, 44), (11, 44)))
        self.add_line('sym-e28', (11, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', closed=True)
