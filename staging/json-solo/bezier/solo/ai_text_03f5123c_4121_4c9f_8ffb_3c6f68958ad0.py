"""Ai (text) (text), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03f5123c-4121-4c9f-8ffb-3c6f68958ad0'
SOURCE_PATH = 'icons-json/text/ai (text)_03f5123c-4121-4c9f-8ffb-3c6f68958ad0.json'
AUTHOR = 'json_to_solo'

class AiTextText(Solo48):
    icon_id = 'ai-text-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('ai', 'text')

    def build(self):
        self.add_line('e0', (24, 40), (16, 11))
        self.add_line('e1', (12, 10), (4, 40))
        self.add_line('e2', (8, 29), (20, 29))
        self.add_line('e3', (44, 8), (34, 8))
        self.add_line('e4', (39, 8), (39, 40))
        self.add_line('e5', (34, 40), (44, 40))
        self.add_bezier('e6', (16, 11), ((15.718, 10.01), (15.082, 8), (13.864, 8)), ((13.809, 8), (13.745, 8.01), (13.682, 8.01)), ((12.955, 8.01), (12.173, 9.36), (12, 10)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c4')
