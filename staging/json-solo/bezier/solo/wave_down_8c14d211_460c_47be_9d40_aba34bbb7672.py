"""Wave down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c14d211-460c-47be-9d40-aba34bbb7672'
SOURCE_PATH = 'icons-json/arrows/wave down_8c14d211-460c-47be-9d40-aba34bbb7672.json'
AUTHOR = 'json_to_solo'

class WaveDownArrows(Solo48):
    icon_id = 'wave-down-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (4, 12))
        self.add_line('e1', (17, 12), (17, 36))
        self.add_line('e2', (27, 36), (27, 13))
        self.add_line('e3', (39, 13), (39, 27))
        self.add_line('e4', (35, 23), (39, 27))
        self.add_line('e5', (44, 23), (39, 27))
        self.add_bezier('e6', (4, 12), ((4, 11.613), (4.218, 11.486), (4.391, 11.149)), ((5.345, 9.246), (7.164, 8.623), (9.227, 8.253)), ((9.755, 8.16), (10.309, 8.008), (10.836, 8.008)), ((10.971, 8.008), (11.096, 8), (11.23, 8)), ((11.232, 8), (11.234, 8), (11.236, 8)), ((11.3, 8), (11.373, 8.008), (11.436, 8.008)), ((13.618, 8.008), (16.036, 9.802), (16.555, 11.739)), ((16.591, 11.857), (17, 11.899), (17, 12)))
        self.add_bezier('e7', (17, 36), ((17, 36.093), (16.891, 36.194), (16.927, 36.312)), ((17.409, 37.92), (19.591, 39.992), (21.5, 39.992)), ((21.527, 39.992), (21.564, 40), (21.591, 40)), ((21.682, 40), (21.782, 39.992), (21.873, 39.992)), ((23.845, 39.992), (25.982, 37.962), (26.527, 36.328)), ((26.573, 36.202), (27, 36.109), (27, 36)))
        self.add_bezier('e8', (27, 13), ((27, 12.899), (26.873, 12.648), (26.909, 12.522)), ((27.436, 10.712), (28.845, 9.423), (30.664, 8.648)), ((31.318, 8.371), (32.027, 8.017), (32.773, 8.017)), ((32.873, 8.017), (32.964, 8), (33.064, 8)), ((33.127, 8), (33.2, 8.008), (33.264, 8.008)), ((35.6, 8.008), (39, 10.667), (39, 13)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
