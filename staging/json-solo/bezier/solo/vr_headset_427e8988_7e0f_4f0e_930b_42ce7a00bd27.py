"""Vr headset (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = 'icons-json/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.json'
AUTHOR = 'json_to_solo'

class VrHeadset427e8988(Solo48):
    icon_id = 'vr-headset-427e8988'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 8), (29, 8))
        self.add_bezier('sym-e1', (29, 8), ((29.736, 8), (30.264, 8), (31, 8)))
        self.add_bezier('sym-e2', (31, 8), ((32.327, 8), (33.7, 8.6), (35, 9)))
        self.add_bezier('sym-e3', (35, 9), ((36.464, 9.432), (37.636, 9.944), (39, 11)))
        self.add_bezier('sym-e4', (39, 11), ((41.982, 13.304), (44, 19.32), (44, 25)))
        self.add_bezier('sym-e5', (44, 25), ((44, 25.144), (44, 24.856), (44, 25)))
        self.add_bezier('sym-e6', (44, 25), ((44, 25.32), (44, 25.68), (44, 26)))
        self.add_bezier('sym-e7', (44, 26), ((44, 32.784), (41.136, 40), (37, 40)))
        self.add_bezier('sym-e8', (37, 40), ((36.9, 40), (37.1, 40), (37, 40)))
        self.add_bezier('sym-e9', (37, 40), ((36.918, 40), (36.082, 40), (36, 40)))
        self.add_bezier('sym-e10', (36, 40), ((31.015, 40), (28.382, 29), (24, 29)))
        self.add_bezier('sym-e11', (24, 29), ((23.916, 29), (24.085, 28.992), (24, 29)))
        self.add_bezier('sym-e12', (24, 29), ((23.915, 28.992), (24.084, 29), (24, 29)))
        self.add_bezier('sym-e13', (24, 29), ((19.618, 29), (16.985, 40), (12, 40)))
        self.add_bezier('sym-e14', (12, 40), ((11.918, 40), (11.082, 40), (11, 40)))
        self.add_bezier('sym-e15', (11, 40), ((10.9, 40), (11.1, 40), (11, 40)))
        self.add_bezier('sym-e16', (11, 40), ((6.864, 40), (4, 32.784), (4, 26)))
        self.add_bezier('sym-e17', (4, 26), ((4, 25.68), (4, 25.32), (4, 25)))
        self.add_bezier('sym-e18', (4, 25), ((4, 24.856), (4, 25.144), (4, 25)))
        self.add_bezier('sym-e19', (4, 25), ((4, 19.32), (6.018, 13.304), (9, 11)))
        self.add_bezier('sym-e20', (9, 11), ((10.364, 9.944), (11.536, 9.432), (13, 9)))
        self.add_bezier('sym-e21', (13, 9), ((14.3, 8.6), (15.673, 8), (17, 8)))
        self.add_bezier('sym-e22', (17, 8), ((17.736, 8), (18.264, 8), (19, 8)))
        self.add_line('sym-e23', (19, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
