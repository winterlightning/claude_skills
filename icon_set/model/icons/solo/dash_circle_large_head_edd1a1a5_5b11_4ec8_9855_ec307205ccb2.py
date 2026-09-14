"""Dash circle large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edd1a1a5-5b11-4ec8-9855-ec307205ccb2'
SOURCE_PATH = 'icons-json/arrows/dash circle large head_edd1a1a5-5b11-4ec8-9855-ec307205ccb2.json'
AUTHOR = 'json_to_solo'

class DashCircleLargeHead(Solo48):
    icon_id = 'dash-circle-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'circle', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (17, 32), (10, 27))
        self.add_line('e1', (4, 32), (9, 28))
        self.add_line('e2', (9, 28), (10, 27))
        self.add_bezier('e3', (9, 22), ((9.718, 14.278), (16.9, 8.017), (25.345, 8.017)), ((25.524, 8.017), (25.703, 8), (25.882, 8)), ((25.885, 8), (25.888, 8), (25.891, 8)), ((26.309, 8), (26.727, 8.017), (27.145, 8.017)), ((35.664, 8.017), (43.991, 15.276), (43.991, 23.259)), ((43.991, 23.358), (44, 23.45), (44, 23.549)), ((44, 23.551), (44, 23.552), (44, 23.554)), ((44, 23.832), (43.991, 24.118), (43.991, 24.396)), ((43.991, 33.019), (35.118, 39.992), (26.118, 39.992)), ((26.02, 39.992), (25.912, 40), (25.814, 40)), ((25.812, 40), (25.811, 40), (25.809, 40)), ((25.455, 40), (25.109, 39.992), (24.755, 39.992)), ((19.3, 39.992), (12.373, 36.985), (10.645, 31.865)), ((10.136, 30.341), (9.927, 28.617), (10, 27)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
