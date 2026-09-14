"""Lamp (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fffde25-08b0-46d2-9123-537377f28274'
SOURCE_PATH = 'icons-json/office/lamp_8fffde25-08b0-46d2-9123-537377f28274.json'
AUTHOR = 'json_to_solo'

class LampOffice(Solo48):
    icon_id = 'lamp-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('lamp', 'office')

    def build(self):
        self.add_line('e0', (33, 35), (39, 23))
        self.add_line('e1', (21, 41), (22, 40))
        self.add_line('e2', (38, 42), (22, 42))
        self.add_line('e3', (37, 20), (22, 12))
        self.add_line('e4', (18, 7), (16, 9))
        self.add_line('e5', (16, 9), (8, 9))
        self.add_line('e6', (6, 12), (18, 23))
        self.add_line('e7', (22, 22), (21, 14))
        self.add_arc('e8-top', (38, 21), (42, 21), radius_x=2)
        self.add_arc('e8-bottom', (42, 21), (38, 21), radius_x=2)
        self.add_bezier('e9', (22, 40), ((24.234, 36.032), (28.565, 33.54), (33, 34.636)), ((35.291, 35.201), (37.075, 36.657), (38.212, 38.719)), ((38.678, 39.57), (39.341, 41.165), (38.302, 41.861)), ((38.179, 41.943), (38.115, 41.918), (38, 42)))
        self.add_bezier('e10', (22, 42), ((21.722, 41.812), (20.965, 41.853), (20.776, 41.485)), ((20.76, 41.386), (21.016, 41.098), (21, 41)))
        self.add_bezier('e11', (8, 9), ((7.501, 9.131), (6, 9.6), (6, 10.353)), ((6, 10.467), (6.008, 10.574), (6.016, 10.688)), ((6.016, 10.852), (6, 11.024), (6, 11.179)), ((6, 11.245), (6, 11.302), (6, 11.367)), ((6, 11.482), (6, 11.877), (6, 12)))
        self.add_bezier('e12', (18, 23), ((18.916, 23.417), (20.408, 23.992), (21.218, 23.084)), ((21.423, 22.863), (21.861, 22.245), (22, 22)))
        self.add_bezier('e13', (21, 14), ((21.458, 13.092), (21.799, 12.57), (22.364, 11.727)), ((23.476, 10.075), (24.098, 8.127), (22.184, 6.736)), ((21.635, 6.335), (20.891, 6.008), (20.195, 6.008)), ((20.155, 6), (20.115, 6), (20.075, 6)), ((20.074, 6), (20.073, 6), (20.073, 6)), ((20.04, 6), (19.999, 6), (19.958, 6.008)), ((19.345, 6.008), (18.417, 6.583), (18, 7)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', closed=True)
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e5', 'e11', 'e6', 'e12', 'e7', 'e13', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c2', 'c3')
