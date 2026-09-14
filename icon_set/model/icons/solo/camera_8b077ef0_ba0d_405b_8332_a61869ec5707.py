"""Camera (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b077ef0-ba0d-405b-8332-a61869ec5707'
SOURCE_PATH = 'icons-json/photography/camera_8b077ef0-ba0d-405b-8332-a61869ec5707.json'
AUTHOR = 'json_to_solo'

class Camera8b077ef0(Solo48):
    icon_id = 'camera-8b077ef0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'photography')

    def build(self):
        self.add_line('e0', (18, 8), (30, 8))
        self.add_line('e1', (30, 8), (34, 14))
        self.add_line('e2', (34, 14), (39, 14))
        self.add_line('e3', (44, 21), (44, 35))
        self.add_line('e4', (38, 40), (9, 40))
        self.add_line('e5', (4, 35), (4, 19))
        self.add_line('e6', (14, 14), (18, 8))
        self.add_arc('e7-1', (39, 14), (43, 16), radius_x=5)
        self.add_line('e7-2', (43, 16), (44, 20))
        self.add_arc('e7-3', (44, 20), (44, 21), radius_x=26, sweep=False)
        self.add_arc('e8-1', (44, 35), (42, 39), radius_x=5)
        self.add_line('e8-2', (42, 39), (38, 40))
        self.add_arc('e9', (9, 40), (4, 35), radius_x=5)
        self.add_arc('e10', (4, 19), (14, 14), radius_x=7)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e3', 'e8-1', 'e8-2', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
