"""Batch-01/diy jewelry (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'icons-json/accessories/batch-01/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.json'
AUTHOR = 'json_to_solo'

class Batch01DiyJewelry(Solo48):
    icon_id = 'batch-01-diy-jewelry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'diy', 'jewelry', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (30, 32), (38, 32), radius_x=4, radius_y=3)
        self.add_arc('sym-e1', (38, 32), (30, 32), radius_x=4, radius_y=3)
        self.add_arc('sym-e2', (18, 32), (10, 32), radius_x=4, radius_y=3, sweep=False)
        self.add_arc('sym-e3', (10, 32), (18, 32), radius_x=4, radius_y=3, sweep=False)
        self.add_line('sym-e4', (37, 8), (38, 10))
        self.add_bezier('sym-e5', (38, 10), ((38.355, 10.749), (38.309, 11.453), (39, 12)))
        self.add_bezier('sym-e6', (39, 12), ((40.982, 13.592), (44, 12.817), (44, 16)))
        self.add_bezier('sym-e7', (44, 16), ((44, 16.109), (44, 16.891), (44, 17)))
        self.add_bezier('sym-e8', (44, 17), ((44, 17.152), (44, 16.857), (44, 17)))
        self.add_bezier('sym-e9', (44, 17), ((44, 18.726), (42.655, 20.425), (42, 22)))
        self.add_line('sym-e10', (42, 22), (38, 28))
        self.add_bezier('sym-e11', (38, 28), ((37.755, 28.32), (37.3, 28.722), (37, 29)))
        self.add_bezier('sym-e12', (24, 29), ((24.547, 29), (25.433, 28.867), (26, 29)))
        self.add_bezier('sym-e13', (26, 29), ((26.627, 29.152), (27.527, 29.562), (28, 30)))
        self.add_line('sym-e14', (28, 30), (30, 32))
        self.add_bezier('sym-e15', (30, 32), ((30, 32.019), (30, 31.981), (30, 32)))
        self.add_bezier('sym-e16', (30, 32), ((30, 32.929), (30.232, 35.051), (30, 36)))
        self.add_bezier('sym-e17', (30, 36), ((29.391, 38.518), (26.773, 40), (24, 40)))
        self.add_bezier('sym-e18', (24, 40), ((23.933, 40), (24.067, 40), (24, 40)))
        self.add_bezier('sym-e19', (24, 40), ((23.933, 40), (24.067, 40), (24, 40)))
        self.add_bezier('sym-e20', (24, 40), ((21.227, 40), (18.609, 38.518), (18, 36)))
        self.add_bezier('sym-e21', (18, 36), ((17.768, 35.051), (18, 32.929), (18, 32)))
        self.add_bezier('sym-e22', (18, 32), ((18, 31.981), (18, 32.019), (18, 32)))
        self.add_line('sym-e23', (18, 32), (20, 30))
        self.add_bezier('sym-e24', (20, 30), ((20.473, 29.562), (21.373, 29.152), (22, 29)))
        self.add_bezier('sym-e25', (22, 29), ((22.567, 28.867), (23.453, 29), (24, 29)))
        self.add_line('sym-e26', (11, 8), (10, 10))
        self.add_bezier('sym-e27', (10, 10), ((9.645, 10.749), (9.691, 11.453), (9, 12)))
        self.add_bezier('sym-e28', (9, 12), ((7.018, 13.592), (4, 12.817), (4, 16)))
        self.add_bezier('sym-e29', (4, 16), ((4, 16.109), (4, 16.891), (4, 17)))
        self.add_bezier('sym-e30', (4, 17), ((4, 17.152), (4, 16.857), (4, 17)))
        self.add_bezier('sym-e31', (4, 17), ((4, 18.726), (5.345, 20.425), (6, 22)))
        self.add_line('sym-e32', (6, 22), (10, 28))
        self.add_bezier('sym-e33', (10, 28), ((10.245, 28.32), (10.7, 28.722), (11, 29)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c3', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
        self.add_contour('sym-c4', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
