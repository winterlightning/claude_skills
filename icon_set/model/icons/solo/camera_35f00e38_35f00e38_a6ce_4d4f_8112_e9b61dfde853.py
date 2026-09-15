"""Camera (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35f00e38-a6ce-4d4f-8112-e9b61dfde853'
SOURCE_PATH = 'icons-json/video/camera_35f00e38-a6ce-4d4f-8112-e9b61dfde853.json'
AUTHOR = 'gpt-6'

class Camera35f00e38(Solo48):
    icon_id = 'camera-35f00e38'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')

    def build(self):
        self.add_line('sym-e0', (24, 8), (30, 8))
        self.add_line('sym-e1', (30, 8), (34, 14))
        self.add_line('sym-e2', (34, 14), (40, 14))
        self.add_line('sym-e4-1', (40, 14), (43, 16))
        self.add_line('sym-e4-2', (43, 16), (44, 20))
        self.add_line('sym-e6', (44, 20), (44, 35))
        self.add_line('sym-e9-1', (44, 35), (43, 38))
        self.add_arc('sym-e9-2', (43, 38), (40, 40), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e10', (40, 40), (8, 40))
        self.add_arc('sym-e12-1', (8, 40), (5, 38), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e12-2', (5, 38), (4, 35))
        self.add_line('sym-e14', (4, 35), (4, 20))
        self.add_line('sym-e17-1', (4, 20), (5, 16))
        self.add_line('sym-e17-2', (5, 16), (8, 14))
        self.add_line('sym-e18', (8, 14), (14, 14))
        self.add_line('sym-e20', (14, 14), (18, 8))
        self.add_line('sym-e21', (18, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4-1', 'sym-e4-2', 'sym-e6', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e12-1', 'sym-e12-2', 'sym-e14', 'sym-e17-1', 'sym-e17-2', 'sym-e18', 'sym-e20', 'sym-e21', closed=True)
