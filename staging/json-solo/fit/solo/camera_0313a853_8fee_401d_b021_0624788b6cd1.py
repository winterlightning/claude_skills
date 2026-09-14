"""Camera (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e0', (24, 26), (24, 27), radius_x=27)
        self.add_line('sym-e1', (24, 8), (19, 8))
        self.add_arc('sym-e3', (19, 8), (16, 12), radius_x=4, sweep=False)
        self.add_line('sym-e4', (16, 12), (9, 12))
        self.add_arc('sym-e5', (9, 12), (5, 14), radius_x=5, sweep=False)
        self.add_arc('sym-e6', (5, 14), (4, 16), radius_x=5, sweep=False)
        self.add_line('sym-e7', (4, 16), (4, 17))
        self.add_line('sym-e9', (4, 17), (4, 34))
        self.add_line('sym-e10', (4, 34), (4, 35))
        self.add_arc('sym-e11', (4, 35), (9, 40), radius_x=5, sweep=False)
        self.add_line('sym-e14', (9, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (39, 40))
        self.add_arc('sym-e18', (39, 40), (44, 35), radius_x=5, sweep=False)
        self.add_line('sym-e19', (44, 35), (44, 34))
        self.add_line('sym-e20', (44, 34), (44, 17))
        self.add_line('sym-e22', (44, 17), (44, 16))
        self.add_line('sym-e23', (44, 16), (43, 14))
        self.add_arc('sym-e24', (43, 14), (39, 12), radius_x=5, sweep=False)
        self.add_line('sym-e25', (39, 12), (32, 12))
        self.add_arc('sym-e26', (32, 12), (29, 8), radius_x=4, sweep=False)
        self.add_line('sym-e28', (29, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e28', closed=True)
