"""Batch-03/astrology gemini (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e0', (24, 36), ((21.529, 36), (19.422, 36.472), (17, 37)))
        self.add_bezier('sym-e1', (17, 37), ((13.163, 37.835), (9.265, 39.865), (6, 42)))
        self.add_line('sym-e2', (17, 37), (17, 24))
        self.add_line('sym-e3', (17, 24), (17, 11))
        self.add_bezier('sym-e4', (17, 11), ((19.422, 11.528), (21.529, 12), (24, 12)))
        self.add_bezier('sym-e5', (24, 12), ((26.471, 12), (28.578, 11.528), (31, 11)))
        self.add_bezier('sym-e6', (31, 11), ((34.837, 10.165), (38.735, 8.135), (42, 6)))
        self.add_bezier('sym-e7', (24, 36), ((26.471, 36), (28.578, 36.472), (31, 37)))
        self.add_bezier('sym-e8', (31, 37), ((34.837, 37.835), (38.735, 39.865), (42, 42)))
        self.add_line('sym-e9', (31, 37), (31, 24))
        self.add_line('sym-e10', (31, 24), (31, 11))
        self.add_bezier('sym-e11', (17, 11), ((13.163, 10.165), (9.265, 8.135), (6, 6)))
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
