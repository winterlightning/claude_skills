"""Wave down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61'
SOURCE_PATH = 'icons-json/arrows/wave down large head_8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61.json'
AUTHOR = 'json_to_solo'

class WaveDownLargeHeadArrows(Solo48):
    icon_id = 'wave-down-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (13, 13), (13, 34))
        self.add_line('e1', (27, 34), (27, 14))
        self.add_line('e2', (39, 14), (39, 26))
        self.add_line('e3', (34, 21), (39, 26))
        self.add_line('e4', (44, 21), (39, 26))
        self.add_bezier('e5', (4, 8), ((5.264, 8), (6.527, 8.02), (7.782, 8.02)), ((10.018, 8.02), (12.218, 9.85), (12.864, 12.18)), ((12.918, 12.39), (13, 12.8), (13, 13)))
        self.add_bezier('e6', (13, 34), ((13, 34.4), (13.382, 35.05), (13.518, 35.43)), ((14.482, 38.15), (17.064, 39.99), (19.7, 39.99)), ((19.825, 39.99), (19.951, 40), (20.076, 40)), ((20.078, 40), (20.08, 40), (20.082, 40)), ((20.209, 40), (20.336, 39.99), (20.464, 39.99)), ((23.155, 39.99), (25.736, 37.88), (26.473, 35.03)), ((26.536, 34.75), (27, 34.27), (27, 34)))
        self.add_bezier('e7', (27, 14), ((27.045, 13.87), (26.818, 13.73), (26.864, 13.6)), ((27.418, 11.15), (30.591, 8.01), (32.964, 8.01)), ((33.1, 8.01), (33.236, 8), (33.382, 8)), ((33.445, 8), (33.518, 8.01), (33.591, 8.01)), ((35.627, 8.01), (39, 11.66), (39, 14)))
        self.add_contour('c0', 'e5', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
