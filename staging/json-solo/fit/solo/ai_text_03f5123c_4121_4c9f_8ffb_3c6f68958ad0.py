"""Ai (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6-1', (16, 11), (14, 8), radius_x=4, sweep=False)
        self.add_arc('e6-2', (14, 8), (12, 10), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c4')
