"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1'
SOURCE_PATH = 'icons-json/interface-essential/skull_c8f4a237-2d49-56fe-b32e-7b5ef8c9b2b1.json'
AUTHOR = 'json_to_solo'

class Skull(Solo48):
    icon_id = 'skull'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (28, 23), (35, 23), radius_x=3, radius_y=4)
        self.add_arc('sym-e1', (35, 23), (28, 23), radius_x=3, radius_y=4)
        self.add_arc('sym-e2', (20, 23), (13, 23), radius_x=3, radius_y=4, sweep=False)
        self.add_arc('sym-e3', (13, 23), (20, 23), radius_x=3, radius_y=4, sweep=False)
        self.add_line('sym-e4', (27, 37), (27, 44))
        self.add_line('sym-e5', (27, 44), (29, 44))
        self.add_bezier('sym-e6', (29, 44), ((29.371, 44), (29.629, 44), (30, 44)))
        self.add_bezier('sym-e7', (30, 44), ((30.312, 44), (30.714, 44), (31, 44)))
        self.add_bezier('sym-e8', (31, 44), ((33.038, 43.136), (34, 41.318), (34, 39)))
        self.add_line('sym-e9', (34, 39), (34, 36))
        self.add_bezier('sym-e10', (34, 36), ((34, 32.682), (36.358, 32.027), (38, 30)))
        self.add_bezier('sym-e11', (38, 30), ((39.347, 28.336), (40, 26.2), (40, 24)))
        self.add_bezier('sym-e12', (40, 24), ((40, 23.809), (40, 24.191), (40, 24)))
        self.add_bezier('sym-e13', (40, 24), ((40, 23.745), (40, 23.255), (40, 23)))
        self.add_bezier('sym-e14', (40, 23), ((40, 19.409), (39.549, 15.245), (38, 12)))
        self.add_bezier('sym-e15', (38, 12), ((35.373, 6.491), (29.592, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((23.907, 4), (24.093, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((23.907, 4), (24.093, 4), (24, 4)))
        self.add_bezier('sym-e18', (24, 4), ((18.408, 4), (12.627, 6.491), (10, 12)))
        self.add_bezier('sym-e19', (10, 12), ((8.451, 15.245), (8, 19.409), (8, 23)))
        self.add_bezier('sym-e20', (8, 23), ((8, 23.255), (8, 23.745), (8, 24)))
        self.add_bezier('sym-e21', (8, 24), ((8, 24.191), (8, 23.809), (8, 24)))
        self.add_bezier('sym-e22', (8, 24), ((8, 26.2), (8.653, 28.336), (10, 30)))
        self.add_bezier('sym-e23', (10, 30), ((11.642, 32.027), (14, 32.682), (14, 36)))
        self.add_line('sym-e24', (14, 36), (14, 39))
        self.add_bezier('sym-e25', (14, 39), ((14, 41.318), (14.962, 43.136), (17, 44)))
        self.add_bezier('sym-e26', (17, 44), ((17.286, 44), (17.688, 44), (18, 44)))
        self.add_bezier('sym-e27', (18, 44), ((18.371, 44), (18.629, 44), (19, 44)))
        self.add_line('sym-e28', (19, 44), (21, 44))
        self.add_line('sym-e29', (21, 44), (21, 37))
        self.add_line('sym-e30', (27, 44), (24, 44))
        self.add_line('sym-e31', (24, 44), (21, 44))
        self.add_bezier('sym-e32', (26, 31), ((25.958, 29.336), (24.825, 29.382), (24, 28)))
        self.add_bezier('sym-e33', (24, 28), ((23.94, 27.891), (24.164, 27.229), (24, 27)))
        self.add_bezier('sym-e34', (24, 27), ((23.836, 27.229), (24.06, 27.891), (24, 28)))
        self.add_bezier('sym-e35', (24, 28), ((23.175, 29.382), (22.042, 29.336), (22, 31)))
        self.add_bezier('sym-e36', (22, 31), ((22.567, 31.154), (23.44, 32), (24, 32)))
        self.add_bezier('sym-e37', (24, 32), ((24.56, 32), (25.433, 31.154), (26, 31)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c3', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c4', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', closed=True)
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
