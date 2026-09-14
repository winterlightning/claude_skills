"""Double arrow top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f48252b8-8cf1-53e8-9803-326efcd0feb3'
SOURCE_PATH = 'icons-json/arrows/double arrow top 2_f48252b8-8cf1-53e8-9803-326efcd0feb3.json'
AUTHOR = 'json_to_solo'

class DoubleArrowTop2Arrows(Solo48):
    icon_id = 'double-arrow-top-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_bezier('sym-e0', (24, 22), ((23.007, 22), (21.789, 23.269), (21, 24)))
        self.add_line('sym-e1', (21, 24), (4, 40))
        self.add_line('sym-e2', (4, 25), (22, 9))
        self.add_bezier('sym-e3', (22, 9), ((22.436, 8.621), (23.336, 8), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((24.064, 8), (23.945, 8), (24, 8)))
        self.add_bezier('sym-e5', (24, 8), ((24.035, 8), (23.967, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((24.033, 8), (23.965, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.055, 8), (23.936, 8), (24, 8)))
        self.add_bezier('sym-e8', (24, 8), ((24.664, 8), (25.564, 8.621), (26, 9)))
        self.add_line('sym-e9', (26, 9), (44, 25))
        self.add_bezier('sym-e10', (24, 22), ((24.993, 22), (26.211, 23.269), (27, 24)))
        self.add_line('sym-e11', (27, 24), (44, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
