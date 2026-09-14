"""Batch-03/astrology gemini (culture), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7629f1dd-dc6f-5a09-a98f-f5af67d076a4'
SOURCE_PATH = 'icons-json/culture/batch-03/astrology gemini_7629f1dd-dc6f-5a09-a98f-f5af67d076a4.json'
AUTHOR = 'json_to_solo'

class Batch03AstrologyGemini(Solo48):
    icon_id = 'batch-03-astrology-gemini'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'gemini', 'culture')

    def build(self):
        self.add_arc('sym-e0', (24, 36), (17, 37), radius_x=34)
        self.add_arc('sym-e1', (17, 37), (6, 42), radius_x=32, sweep=False)
        self.add_line('sym-e2', (17, 37), (17, 24))
        self.add_line('sym-e3', (17, 24), (17, 11))
        self.add_arc('sym-e4', (17, 11), (24, 12), radius_x=34)
        self.add_line('sym-e5', (24, 12), (31, 11))
        self.add_arc('sym-e6', (31, 11), (42, 6), radius_x=32, sweep=False)
        self.add_line('sym-e7', (24, 36), (31, 37))
        self.add_arc('sym-e8', (31, 37), (42, 42), radius_x=32)
        self.add_line('sym-e9', (31, 37), (31, 24))
        self.add_line('sym-e10', (31, 24), (31, 11))
        self.add_arc('sym-e11', (17, 11), (6, 6), radius_x=32)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c3', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
