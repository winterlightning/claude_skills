"""Double arrow bottom 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e096684e-b720-5a03-9201-7eb483af7b1a'
SOURCE_PATH = 'icons-json/arrows/double arrow bottom 2_e096684e-b720-5a03-9201-7eb483af7b1a.json'
AUTHOR = 'json_to_solo'

class DoubleArrowBottom2Arrows(Solo48):
    icon_id = 'double-arrow-bottom-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_bezier('sym-e0', (24, 26), ((24.993, 26), (26.211, 24.731), (27, 24)))
        self.add_line('sym-e1', (27, 24), (44, 8))
        self.add_line('sym-e2', (44, 23), (26, 39))
        self.add_bezier('sym-e3', (26, 39), ((25.564, 39.379), (24.664, 40), (24, 40)))
        self.add_bezier('sym-e4', (24, 40), ((23.936, 40), (24.055, 40), (24, 40)))
        self.add_bezier('sym-e5', (24, 40), ((23.965, 40), (24.033, 40), (24, 40)))
        self.add_bezier('sym-e6', (24, 40), ((23.967, 40), (24.035, 40), (24, 40)))
        self.add_bezier('sym-e7', (24, 40), ((23.945, 40), (24.064, 40), (24, 40)))
        self.add_bezier('sym-e8', (24, 40), ((23.336, 40), (22.436, 39.379), (22, 39)))
        self.add_line('sym-e9', (22, 39), (4, 23))
        self.add_bezier('sym-e10', (24, 26), ((23.007, 26), (21.789, 24.731), (21, 24)))
        self.add_line('sym-e11', (21, 24), (4, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
