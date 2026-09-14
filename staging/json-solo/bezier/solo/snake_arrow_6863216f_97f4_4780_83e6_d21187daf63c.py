"""Snake arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6863216f-97f4-4780-83e6-d21187daf63c'
SOURCE_PATH = 'icons-json/arrows/snake arrow_6863216f-97f4-4780-83e6-d21187daf63c.json'
AUTHOR = 'json_to_solo'

class SnakeArrowArrows(Solo48):
    icon_id = 'snake-arrow-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('snake', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (22, 6), (22, 13))
        self.add_line('e1', (24, 14), (38, 14))
        self.add_line('e2', (38, 22), (10, 22))
        self.add_line('e3', (10, 31), (22, 31))
        self.add_line('e4', (25, 34), (25, 42))
        self.add_line('e5', (25, 42), (20, 37))
        self.add_line('e6', (25, 42), (30, 37))
        self.add_bezier('e7', (22, 13), ((22, 13.892), (23.108, 14), (24, 14)))
        self.add_bezier('e8', (38, 14), ((40.07, 14), (41.992, 15.933), (41.992, 18.085)), ((42, 18.141), (42, 18.205), (42, 18.27)), ((42, 18.271), (42, 18.272), (42, 18.273)), ((42, 18.338), (42, 18.404), (41.992, 18.461)), ((41.992, 20.613), (40.07, 22), (38, 22)))
        self.add_bezier('e9', (10, 22), ((8.036, 22), (6.008, 24.205), (6.008, 26.258)), ((6.008, 26.323), (6, 26.387), (6, 26.451)), ((6, 26.453), (6, 26.454), (6, 26.455)), ((6, 26.52), (6.008, 26.585), (6.008, 26.651)), ((6.008, 28.705), (8.036, 31), (10, 31)))
        self.add_bezier('e10', (22, 31), ((23.906, 31), (25, 32.094), (25, 34)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e5')
        self.add_contour('c1', 'e6')
        self.relate('connect', 'c0', 'c1')
