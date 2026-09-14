"""Camera (video), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35f00e38-a6ce-4d4f-8112-e9b61dfde853'
SOURCE_PATH = 'icons-json/video/camera_35f00e38-a6ce-4d4f-8112-e9b61dfde853.json'
AUTHOR = 'json_to_solo'

class Camera(Solo48):
    icon_id = 'camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')

    def build(self):
        self.add_line('sym-e0', (24, 8), (30, 8))
        self.add_line('sym-e1', (30, 8), (34, 14))
        self.add_line('sym-e2', (34, 14), (39, 14))
        self.add_bezier('sym-e3', (39, 14), ((39.255, 14), (39.736, 13.93), (40, 14)))
        self.add_bezier('sym-e4', (40, 14), ((42.391, 14.61), (44, 17.44), (44, 20)))
        self.add_bezier('sym-e5', (44, 20), ((44, 20.19), (44, 19.81), (44, 20)))
        self.add_bezier('sym-e6', (44, 20), ((44, 20.22), (44, 20.78), (44, 21)))
        self.add_line('sym-e7', (44, 21), (44, 35))
        self.add_bezier('sym-e8', (44, 35), ((43.991, 35.16), (44, 34.84), (44, 35)))
        self.add_bezier('sym-e9', (44, 35), ((44, 37.5), (41.982, 39.41), (40, 40)))
        self.add_line('sym-e10', (40, 40), (24, 40))
        self.add_line('sym-e11', (24, 40), (8, 40))
        self.add_bezier('sym-e12', (8, 40), ((6.018, 39.41), (4, 37.5), (4, 35)))
        self.add_bezier('sym-e13', (4, 35), ((4, 34.84), (4.009, 35.16), (4, 35)))
        self.add_line('sym-e14', (4, 35), (4, 21))
        self.add_bezier('sym-e15', (4, 21), ((4, 20.78), (4, 20.22), (4, 20)))
        self.add_bezier('sym-e16', (4, 20), ((4, 19.81), (4, 20.19), (4, 20)))
        self.add_bezier('sym-e17', (4, 20), ((4, 17.44), (5.609, 14.61), (8, 14)))
        self.add_bezier('sym-e18', (8, 14), ((8.264, 13.93), (8.745, 14), (9, 14)))
        self.add_line('sym-e19', (9, 14), (14, 14))
        self.add_line('sym-e20', (14, 14), (18, 8))
        self.add_line('sym-e21', (18, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
