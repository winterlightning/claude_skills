"""Camera glasses (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31079e61-3ff6-5151-ac76-c4202759aded'
SOURCE_PATH = 'icons-json/photography/camera glasses_31079e61-3ff6-5151-ac76-c4202759aded.json'
AUTHOR = 'json_to_solo'

class CameraGlassesPhotography(Solo48):
    icon_id = 'camera-glasses-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'glasses', 'photography')

    def build(self):
        self.add_line('e0', (16, 40), (10, 40))
        self.add_line('e1', (6, 34), (5, 30))
        self.add_line('e2', (4, 29), (4, 25))
        self.add_line('e3', (10, 15), (15, 15))
        self.add_line('e4', (20, 8), (28, 8))
        self.add_line('e5', (31, 10), (33, 15))
        self.add_line('e6', (33, 15), (39, 15))
        self.add_line('e7', (44, 29), (44, 25))
        self.add_line('e8-1', (4, 25), (17, 24))
        self.add_arc('e8-2', (17, 24), (20, 27), radius_x=4)
        self.add_arc('e8-3', (20, 27), (16, 40), radius_x=11)
        self.add_arc('e9', (10, 40), (6, 34), radius_x=6)
        self.add_arc('e10', (5, 30), (4, 29), radius_x=2, sweep=False)
        self.add_arc('e11', (20, 28), (28, 28), radius_x=6)
        self.add_arc('e12', (6, 22), (10, 15), radius_x=7)
        self.add_arc('e13', (15, 15), (20, 8), radius_x=8)
        self.add_arc('e14', (28, 8), (31, 10), radius_x=4)
        self.add_arc('e15', (39, 15), (42, 22), radius_x=7)
        self.add_line('e16-1', (44, 25), (33, 24))
        self.add_arc('e16-2', (33, 24), (28, 27), radius_x=5, sweep=False)
        self.add_arc('e16-3', (28, 27), (29, 37), radius_x=21, sweep=False)
        self.add_arc('e16-4', (29, 37), (34, 40), radius_x=6, sweep=False)
        self.add_line('e16-5', (34, 40), (40, 39))
        self.add_arc('e16-6', (40, 39), (42, 36), radius_x=5, sweep=False)
        self.add_arc('e16-7', (42, 36), (44, 29), radius_x=8)
        self.add_contour('c0', 'e8-1', 'e8-2', 'e8-3', 'e0', 'e9', 'e1', 'e10', 'e2', closed=True)
        self.add_contour('c1', 'e11')
        self.add_contour('c2', 'e12', 'e3', 'e13', 'e4', 'e14', 'e5', 'e6', 'e15')
        self.add_contour('c3', 'e16-1', 'e16-2', 'e16-3', 'e16-4', 'e16-5', 'e16-6', 'e16-7', 'e7', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
