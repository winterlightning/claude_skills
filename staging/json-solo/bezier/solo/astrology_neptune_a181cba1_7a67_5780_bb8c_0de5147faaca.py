"""Batch-05/astrology neptune (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a181cba1-7a67-5780-bb8c-0de5147faaca'
SOURCE_PATH = 'icons-json/culture/batch-05/astrology neptune_a181cba1-7a67-5780-bb8c-0de5147faaca.json'
AUTHOR = 'json_to_solo'

class Batch05AstrologyNeptune(Solo48):
    icon_id = 'batch-05-astrology-neptune'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'neptune', 'culture')

    def build(self):
        self.add_line('sym-e0', (18, 37), (30, 37))
        self.add_line('sym-e1', (24, 4), (24, 30))
        self.add_line('sym-e2', (24, 30), (24, 44))
        self.add_line('sym-e3', (12, 11), (12, 19))
        self.add_bezier('sym-e4', (12, 19), ((12, 20.336), (12.512, 21.791), (13, 23)))
        self.add_bezier('sym-e5', (13, 23), ((14.934, 27.823), (19.493, 30), (24, 30)))
        self.add_bezier('sym-e6', (24, 30), ((28.507, 30), (33.066, 27.823), (35, 23)))
        self.add_bezier('sym-e7', (35, 23), ((35.488, 21.791), (36, 20.336), (36, 19)))
        self.add_line('sym-e8', (36, 19), (36, 11))
        self.add_line('sym-e9', (36, 11), (32, 17))
        self.add_line('sym-e10', (12, 11), (16, 17))
        self.add_line('sym-e11', (12, 11), (8, 17))
        self.add_line('sym-e12', (20, 9), (24, 4))
        self.add_line('sym-e13', (24, 4), (28, 9))
        self.add_line('sym-e14', (36, 11), (40, 17))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.add_contour('sym-c5', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c6', 'sym-e14')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c2', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c5')
