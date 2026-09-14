"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2de22ab7-b36e-43f7-805d-727e72c62f15'
SOURCE_PATH = 'icons-json/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.json'
AUTHOR = 'json_to_solo'

class TShirt(Solo48):
    icon_id = 't-shirt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        self.add_line('e0', (36, 26), (44, 26))
        self.add_line('e1', (44, 26), (44, 16))
        self.add_line('e2', (4, 18), (4, 26))
        self.add_line('e3', (4, 26), (12, 26))
        self.add_line('e4', (36, 21), (36, 40))
        self.add_line('e5', (36, 40), (12, 40))
        self.add_line('e6', (12, 40), (12, 21))
        self.add_bezier('e7', (44, 16), ((44, 15.503), (43.618, 14.526), (43.427, 14.046)), ((41.991, 10.434), (37.882, 8.008), (33.773, 8.008)), ((33.406, 8.008), (33.039, 8), (32.672, 8)), ((32.666, 8), (32.66, 8), (32.655, 8)), ((32.3, 8.017), (31.955, 8.034), (31.6, 8.051)), ((31.527, 8.067), (31.373, 8.766), (31.345, 8.842)), ((31.073, 9.726), (30.8, 10.484), (30.264, 11.259)), ((29.027, 13.036), (26.873, 14.282), (24.591, 14.467)), ((21.818, 14.695), (19.082, 13.423), (17.618, 11.225)), ((17.091, 10.434), (16.873, 9.583), (16.609, 8.707)), ((16.582, 8.615), (16.491, 8.093), (16.4, 8.059)), ((15.845, 8), (12.927, 8.152), (12.2, 8.278)), ((7.573, 9.423), (4, 13.162), (4, 17.718)), ((4, 17.785), (4, 17.853), (4, 17.912)), ((4, 17.979), (4, 17.933), (4, 18)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
