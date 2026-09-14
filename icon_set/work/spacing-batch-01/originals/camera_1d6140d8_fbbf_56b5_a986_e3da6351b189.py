"""Camera (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6140d8-fbbf-56b5-a986-e3da6351b189'
SOURCE_PATH = 'icons-json/photography/camera_1d6140d8-fbbf-56b5-a986-e3da6351b189.json'
AUTHOR = 'json_to_solo'

class CameraPhotography(Solo48):
    icon_id = 'camera-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('camera', 'photography')

    def build(self):
        self.add_arc('sym-e0', (15, 26), (33, 26), radius_x=9, radius_y=10)
        self.add_arc('sym-e1', (33, 26), (15, 26), radius_x=9, radius_y=10)
        self.add_line('sym-e2', (24, 8), (19, 8))
        self.add_line('sym-e3', (19, 8), (18, 8))
        self.add_arc('sym-e4', (18, 8), (16, 13), radius_x=10, sweep=False)
        self.add_line('sym-e5', (16, 13), (9, 13))
        self.add_line('sym-e6', (9, 13), (7, 13))
        self.add_arc('sym-e7-1', (7, 13), (5, 14), radius_x=4, sweep=False)
        self.add_line('sym-e7-2', (5, 14), (4, 17))
        self.add_line('sym-e9', (4, 17), (4, 34))
        self.add_line('sym-e10', (4, 34), (4, 36))
        self.add_arc('sym-e11', (4, 36), (8, 40), radius_x=4, sweep=False)
        self.add_arc('sym-e12', (8, 40), (9, 40), radius_x=20)
        self.add_line('sym-e13', (9, 40), (24, 40))
        self.add_line('sym-e14', (24, 40), (39, 40))
        self.add_line('sym-e15', (39, 40), (40, 40))
        self.add_arc('sym-e16', (40, 40), (44, 36), radius_x=4, sweep=False)
        self.add_line('sym-e17-1', (44, 36), (44, 35))
        self.add_line('sym-e17-2', (44, 35), (44, 34))
        self.add_line('sym-e18', (44, 34), (44, 17))
        self.add_line('sym-e20-1', (44, 17), (43, 14))
        self.add_arc('sym-e20-2', (43, 14), (41, 13), radius_x=4, sweep=False)
        self.add_line('sym-e21', (41, 13), (39, 13))
        self.add_line('sym-e22', (39, 13), (32, 13))
        self.add_arc('sym-e23', (32, 13), (30, 8), radius_x=10, sweep=False)
        self.add_line('sym-e24', (30, 8), (29, 8))
        self.add_line('sym-e25', (29, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17-1', 'sym-e17-2', 'sym-e18', 'sym-e20-1', 'sym-e20-2', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
