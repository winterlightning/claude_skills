"""Panoramic (video), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1886bf3f-c98c-584f-835e-85f7ec5deb73'
SOURCE_PATH = 'icons-json/video/panoramic_1886bf3f-c98c-584f-835e-85f7ec5deb73.json'
AUTHOR = 'json_to_solo'

class PanoramicVideo(Solo48):
    icon_id = 'panoramic-video'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('panoramic', 'video')

    def build(self):
        self.add_line('e0', (32, 11), (32, 37))
        self.add_line('e1', (16, 37), (16, 11))
        self.add_line('e2', (10, 10), (5, 8))
        self.add_line('e3', (4, 8), (4, 39))
        self.add_line('e4', (4, 39), (18, 37))
        self.add_line('e5', (39, 39), (43, 40))
        self.add_line('e6', (44, 39), (44, 8))
        self.add_bezier('e7', (44, 8), ((40.045, 9.01), (36.2, 10.29), (32.182, 11)), ((26.8, 11.95), (21.2, 11.95), (15.818, 11)), ((14.018, 10.68), (11.736, 10.64), (10, 10)))
        self.add_bezier('e8', (5, 8), ((4.7, 8), (4.3, 8), (4, 8)))
        self.add_bezier('e9', (18, 37), ((22.864, 36.29), (27.318, 36.27), (32.182, 37)), ((34.391, 37.33), (36.827, 38.52), (39, 39)))
        self.add_bezier('e10', (43, 40), ((43.227, 40), (43.536, 40), (43.764, 40)), ((43.8, 40), (43.991, 39.24), (43.991, 39.16)), ((43.991, 39.1), (44, 39.05), (44, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
