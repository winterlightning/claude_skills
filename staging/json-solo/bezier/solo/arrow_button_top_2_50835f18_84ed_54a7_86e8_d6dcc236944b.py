"""Arrow button top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50835f18-84ed-54a7-86e8-d6dcc236944b'
SOURCE_PATH = 'icons-json/arrows/arrow button top 2_50835f18-84ed-54a7-86e8-d6dcc236944b.json'
AUTHOR = 'json_to_solo'

class ArrowButtonTop2Arrows(Solo48):
    icon_id = 'arrow-button-top-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (43, 35), (26, 9))
        self.add_line('e1', (21, 11), (5, 35))
        self.add_line('e2', (8, 40), (41, 40))
        self.add_line('e3', (42, 35), (40, 31))
        self.add_bezier('e4', (26, 9), ((25.709, 8.56), (24.991, 8.02), (24.455, 8.02)), ((24.355, 8.01), (24.264, 8.01), (24.164, 8)), ((24.163, 8), (24.162, 8), (24.162, 8)), ((24.117, 8), (24.072, 8.01), (24.018, 8.01)), ((22.645, 8.01), (21.664, 10.03), (21, 11)))
        self.add_bezier('e5', (5, 35), ((4.627, 35.55), (4.018, 36.29), (4.018, 37.01)), ((4.009, 37.17), (4.009, 37.33), (4, 37.5)), ((4, 37.501), (4, 37.502), (4, 37.503)), ((4, 37.572), (4.009, 37.641), (4.009, 37.71)), ((4.009, 37.9), (4.155, 38.19), (4.227, 38.35)), ((4.736, 39.54), (5.755, 39.99), (6.891, 39.99)), ((7.136, 39.99), (7.755, 40), (8, 40)))
        self.add_bezier('e6', (41, 40), ((41.155, 40), (41.591, 39.98), (41.745, 39.98)), ((42.573, 39.98), (43.982, 39.24), (43.982, 38.16)), ((43.991, 38.121), (44, 38.072), (44, 38.022)), ((44, 38.022), (44, 38.021), (44, 38.02)), ((44, 37.38), (42.345, 35.77), (42, 35)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3')
