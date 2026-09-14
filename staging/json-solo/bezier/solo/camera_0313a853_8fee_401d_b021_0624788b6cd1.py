"""Camera (video), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0313a853-8fee-401d-b021-0624788b6cd1'
SOURCE_PATH = 'icons-json/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.json'
AUTHOR = 'json_to_solo'

class Camera0313a853(Solo48):
    icon_id = 'camera-0313a853'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')

    def build(self):
        self.add_bezier('sym-e0', (24, 26), ((24, 26.33), (24, 26.67), (24, 27)))
        self.add_line('sym-e1', (24, 8), (19, 8))
        self.add_bezier('sym-e2', (19, 8), ((18.891, 8), (19.109, 8), (19, 8)))
        self.add_bezier('sym-e3', (19, 8), ((16.718, 8), (16.518, 10.02), (16, 12)))
        self.add_line('sym-e4', (16, 12), (9, 12))
        self.add_bezier('sym-e5', (9, 12), ((7.009, 12), (6.009, 11.89), (5, 14)))
        self.add_bezier('sym-e6', (5, 14), ((4.7, 14.62), (4, 15.28), (4, 16)))
        self.add_bezier('sym-e7', (4, 16), ((4, 16.08), (4.009, 16.91), (4, 17)))
        self.add_bezier('sym-e8', (4, 17), ((4, 17.08), (4, 16.92), (4, 17)))
        self.add_line('sym-e9', (4, 17), (4, 34))
        self.add_bezier('sym-e10', (4, 34), ((4, 34.2), (4, 34.81), (4, 35)))
        self.add_bezier('sym-e11', (4, 35), ((4, 38.06), (6.136, 40), (9, 40)))
        self.add_bezier('sym-e12', (9, 40), ((9.145, 40), (8.855, 39.99), (9, 40)))
        self.add_bezier('sym-e13', (9, 40), ((9.082, 40), (8.927, 40), (9, 40)))
        self.add_line('sym-e14', (9, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (39, 40))
        self.add_bezier('sym-e16', (39, 40), ((39.073, 40), (38.918, 40), (39, 40)))
        self.add_bezier('sym-e17', (39, 40), ((39.145, 39.99), (38.855, 40), (39, 40)))
        self.add_bezier('sym-e18', (39, 40), ((41.864, 40), (44, 38.06), (44, 35)))
        self.add_bezier('sym-e19', (44, 35), ((44, 34.81), (44, 34.2), (44, 34)))
        self.add_line('sym-e20', (44, 34), (44, 17))
        self.add_bezier('sym-e21', (44, 17), ((44, 16.92), (44, 17.08), (44, 17)))
        self.add_bezier('sym-e22', (44, 17), ((43.991, 16.91), (44, 16.08), (44, 16)))
        self.add_bezier('sym-e23', (44, 16), ((44, 15.28), (43.3, 14.62), (43, 14)))
        self.add_bezier('sym-e24', (43, 14), ((41.991, 11.89), (40.991, 12), (39, 12)))
        self.add_line('sym-e25', (39, 12), (32, 12))
        self.add_bezier('sym-e26', (32, 12), ((31.482, 10.02), (31.282, 8), (29, 8)))
        self.add_bezier('sym-e27', (29, 8), ((28.891, 8), (29.109, 8), (29, 8)))
        self.add_line('sym-e28', (29, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', closed=True)
