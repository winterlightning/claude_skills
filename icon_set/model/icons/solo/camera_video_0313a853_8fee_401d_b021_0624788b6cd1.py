"""Camera (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0313a853-8fee-401d-b021-0624788b6cd1'
SOURCE_PATH = 'pictographic-primitives/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.svg'
AUTHOR = 'gpt-6'

class CameraVideo(Solo48):
    icon_id = 'camera-video'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')

    def build(self):
        self.add_arc('sym-e0', (24, 26), (24, 27), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_line('sym-e1', (24, 8), (19, 8))
        self.add_arc('sym-e3', (19, 8), (16, 12), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e4', (16, 12), (9, 12))
        self.add_arc('sym-e5', (9, 12), (5, 14), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (5, 14), (4, 16), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e7', (4, 16), (4, 35))
        self.add_arc('sym-e11', (4, 35), (9, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e14', (9, 40), (39, 40))
        self.add_arc('sym-e18', (39, 40), (44, 35), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e19', (44, 35), (44, 16))
        self.add_line('sym-e23', (44, 16), (43, 14))
        self.add_arc('sym-e24', (43, 14), (39, 12), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e25', (39, 12), (32, 12))
        self.add_arc('sym-e26', (32, 12), (29, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e28', (29, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e11', 'sym-e14', 'sym-e18', 'sym-e19', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e28', closed=True)
