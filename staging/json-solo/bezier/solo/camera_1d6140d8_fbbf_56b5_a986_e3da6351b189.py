"""Camera (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d6140d8-fbbf-56b5-a986-e3da6351b189'
SOURCE_PATH = 'icons-json/photography/camera_1d6140d8-fbbf-56b5-a986-e3da6351b189.json'
AUTHOR = 'json_to_solo'

class Camera1d6140d8(Solo48):
    icon_id = 'camera-1d6140d8'
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
        self.add_bezier('sym-e3', (19, 8), ((18.782, 8.13), (18.191, 8), (18, 8)))
        self.add_bezier('sym-e4', (18, 8), ((16.8, 9.12), (16.536, 11.46), (16, 13)))
        self.add_line('sym-e5', (16, 13), (9, 13))
        self.add_bezier('sym-e6', (9, 13), ((8.191, 13), (7.8, 12.88), (7, 13)))
        self.add_bezier('sym-e7', (7, 13), ((5.4, 13.25), (4, 15.19), (4, 17)))
        self.add_bezier('sym-e8', (4, 17), ((4, 17.15), (4, 16.85), (4, 17)))
        self.add_line('sym-e9', (4, 17), (4, 34))
        self.add_bezier('sym-e10', (4, 34), ((4, 34.5), (4, 35.49), (4, 36)))
        self.add_bezier('sym-e11', (4, 36), ((4, 38.46), (5.718, 40), (8, 40)))
        self.add_bezier('sym-e12', (8, 40), ((8.164, 40), (8.836, 40), (9, 40)))
        self.add_line('sym-e13', (9, 40), (24, 40))
        self.add_line('sym-e14', (24, 40), (39, 40))
        self.add_bezier('sym-e15', (39, 40), ((39.164, 40), (39.836, 40), (40, 40)))
        self.add_bezier('sym-e16', (40, 40), ((42.282, 40), (44, 38.46), (44, 36)))
        self.add_bezier('sym-e17', (44, 36), ((44, 35.49), (44, 34.5), (44, 34)))
        self.add_line('sym-e18', (44, 34), (44, 17))
        self.add_bezier('sym-e19', (44, 17), ((44, 16.85), (44, 17.15), (44, 17)))
        self.add_bezier('sym-e20', (44, 17), ((44, 15.19), (42.6, 13.25), (41, 13)))
        self.add_bezier('sym-e21', (41, 13), ((40.2, 12.88), (39.809, 13), (39, 13)))
        self.add_line('sym-e22', (39, 13), (32, 13))
        self.add_bezier('sym-e23', (32, 13), ((31.464, 11.46), (31.2, 9.12), (30, 8)))
        self.add_bezier('sym-e24', (30, 8), ((29.809, 8), (29.218, 8.13), (29, 8)))
        self.add_line('sym-e25', (29, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
