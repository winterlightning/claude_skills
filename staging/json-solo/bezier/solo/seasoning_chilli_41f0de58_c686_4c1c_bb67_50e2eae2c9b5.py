"""Seasoning chilli (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41f0de58-c686-4c1c-bb67-50e2eae2c9b5'
SOURCE_PATH = 'icons-json/food/seasoning chilli_41f0de58-c686-4c1c-bb67-50e2eae2c9b5.json'
AUTHOR = 'json_to_solo'

class SeasoningChilliFood(Solo48):
    icon_id = 'seasoning-chilli-food'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('seasoning', 'chilli', 'food')

    def build(self):
        self.add_line('e0', (6, 30), (6, 32))
        self.add_bezier('e1', (42, 6), ((41.967, 6), (41.935, 6.008), (41.894, 6.008)), ((41.305, 6.008), (40.642, 6.262), (40.135, 6.54)), ((38.114, 7.628), (37.483, 9.922), (37, 12)))
        self.add_bezier('e2', (6, 32), ((8.725, 37.752), (14.444, 41.992), (20.932, 41.992)), ((20.988, 41.992), (21.053, 42), (21.109, 42)), ((21.11, 42), (21.111, 42), (21.112, 42)), ((21.423, 42), (21.734, 41.992), (22.045, 41.992)), ((23.501, 41.992), (24.99, 41.697), (26.389, 41.321)), ((34.031, 39.284), (39.462, 32.601), (41, 25)))
        self.add_bezier('e3', (6, 30), ((8.405, 32.152), (10.721, 34.006), (13.838, 35.045)), ((19.402, 36.895), (25.743, 34.972), (28.885, 29.924)), ((30.619, 27.134), (30.804, 24.224), (31, 21)))
        self.add_bezier('e4', (31, 21), ((31.728, 21.303), (32.918, 21.243), (33.458, 21.848)), ((34.08, 22.535), (34.235, 23.525), (34.775, 24.278)), ((35.864, 25.775), (37.811, 26.111), (39.488, 25.53)), ((40.028, 25.342), (40.887, 24.998), (41.182, 24.818)), ((41.264, 24.769), (41.313, 24.041), (41.329, 23.926)), ((41.485, 22.969), (41.583, 21.995), (41.624, 21.03)), ((41.812, 16.865), (42, 13.211), (37, 12)))
        self.add_bezier('e5', (31, 21), ((30.869, 17.564), (30.725, 13.331), (34.874, 12.014)), ((35.61, 11.776), (36.239, 12.025), (37, 12)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
