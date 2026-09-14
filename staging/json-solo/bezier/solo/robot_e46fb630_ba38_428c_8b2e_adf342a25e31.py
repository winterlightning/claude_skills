"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e46fb630-ba38-428c-8b2e-adf342a25e31'
SOURCE_PATH = 'icons-json/artificial-intelligence/robot_e46fb630-ba38-428c-8b2e-adf342a25e31.json'
AUTHOR = 'json_to_solo'

class Robot(Solo48):
    icon_id = 'robot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 17))
        self.add_line('sym-e1', (24, 17), (13, 17))
        self.add_bezier('sym-e2', (13, 17), ((9.924, 17), (6.72, 19.055), (6, 22)))
        self.add_bezier('sym-e3', (6, 22), ((6, 22.694), (6, 23.253), (6, 24)))
        self.add_bezier('sym-e4', (6, 24), ((6, 24.257), (6, 24.757), (6, 25)))
        self.add_bezier('sym-e5', (6, 25), ((6, 25.262), (6, 25.738), (6, 26)))
        self.add_line('sym-e6', (6, 26), (6, 35))
        self.add_bezier('sym-e7', (6, 35), ((6, 35.155), (6, 35.845), (6, 36)))
        self.add_bezier('sym-e8', (6, 36), ((6, 38.716), (8.325, 41.37), (11, 42)))
        self.add_bezier('sym-e9', (11, 42), ((11.605, 42), (12.378, 42), (13, 42)))
        self.add_bezier('sym-e10', (13, 42), ((13.548, 42), (13.444, 42), (14, 42)))
        self.add_line('sym-e11', (14, 42), (24, 42))
        self.add_line('sym-e12', (24, 42), (34, 42))
        self.add_bezier('sym-e13', (34, 42), ((34.556, 42), (34.452, 42), (35, 42)))
        self.add_bezier('sym-e14', (35, 42), ((35.622, 42), (36.395, 42), (37, 42)))
        self.add_bezier('sym-e15', (37, 42), ((39.675, 41.37), (42, 38.716), (42, 36)))
        self.add_bezier('sym-e16', (42, 36), ((42, 35.845), (42, 35.155), (42, 35)))
        self.add_line('sym-e17', (42, 35), (42, 26))
        self.add_bezier('sym-e18', (42, 26), ((42, 25.738), (42, 25.262), (42, 25)))
        self.add_bezier('sym-e19', (42, 25), ((42, 24.757), (42, 24.257), (42, 24)))
        self.add_bezier('sym-e20', (42, 24), ((42, 23.253), (42, 22.694), (42, 22)))
        self.add_bezier('sym-e21', (42, 22), ((41.28, 19.055), (38.076, 17), (35, 17)))
        self.add_line('sym-e22', (35, 17), (24, 17))
        self.add_line('sym-e23', (17, 27), (17, 32))
        self.add_line('sym-e24', (31, 27), (31, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c1', 'sym-e23')
        self.add_contour('sym-c2', 'sym-e24')
