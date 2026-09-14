"""Headphones (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90ffd8be-8c2b-43c1-9cda-658b2b74c820'
SOURCE_PATH = 'icons-json/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.json'
AUTHOR = 'json_to_solo'

class Headphones90ffd8be(Solo48):
    icon_id = 'headphones-90ffd8be'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self):
        self.add_line('e0', (37, 40), (37, 28))
        self.add_line('e1', (37, 28), (37, 20))
        self.add_line('e2', (11, 40), (11, 28))
        self.add_line('e3', (11, 28), (11, 20))
        self.add_bezier('e4', (11, 21), ((11, 20.722), (11.273, 20.067), (11.273, 19.789)), ((11.345, 13.785), (16.418, 8.017), (23.2, 8.017)), ((23.345, 8.008), (23.5, 8.008), (23.645, 8)), ((23.651, 8), (23.656, 8), (23.661, 8)), ((23.983, 8), (24.314, 8.017), (24.636, 8.017)), ((29.682, 8.017), (34.327, 11.495), (35.936, 15.815)), ((36.418, 17.12), (36.891, 18.636), (37, 20)))
        self.add_bezier('e5', (37, 40), ((37.555, 40), (37.836, 40), (38.391, 40)), ((41.055, 40), (43.991, 36.96), (43.991, 34.543)), ((43.991, 34.459), (44, 34.375), (44, 34.299)), ((44, 34.298), (44, 34.296), (44, 34.295)), ((44, 34.212), (44, 34.129), (43.991, 34.046)), ((43.991, 33.288), (43.6, 32.505), (43.245, 31.84)), ((41.709, 28.977), (40.245, 28.126), (37, 28)))
        self.add_bezier('e6', (11, 28), ((7.891, 28.244), (6.6, 28.859), (4.918, 31.427)), ((4.5, 32.076), (4.009, 32.893), (4.009, 33.676)), ((4.009, 33.717), (4, 33.751), (4, 33.792)), ((4, 33.792), (4, 33.793), (4, 33.794)), ((4, 33.928), (4.009, 34.072), (4.009, 34.215)), ((4.009, 36.463), (6.673, 39.983), (9.273, 39.983)), ((9.591, 39.983), (9.909, 40), (10.218, 40)), ((10.573, 40), (10.645, 40), (11, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e6', 'e2', closed=True)
        self.add_contour('c5', 'e3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c5', 'c1')
