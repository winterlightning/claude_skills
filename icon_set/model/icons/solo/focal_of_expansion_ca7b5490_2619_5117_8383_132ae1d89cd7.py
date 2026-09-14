"""Focal of expansion (technology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca7b5490-2619-5117-8383-132ae1d89cd7'
SOURCE_PATH = 'icons-json/technology/focal of expansion_ca7b5490-2619-5117-8383-132ae1d89cd7.json'
AUTHOR = 'json_to_solo'

class FocalOfExpansion(Solo48):
    icon_id = 'focal-of-expansion'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('focal', 'of', 'expansion', 'technology')

    def build(self):
        self.add_line('sym-e0', (24, 8), (24, 22))
        self.add_line('sym-e1', (24, 22), (24, 40))
        self.add_line('sym-e2', (24, 40), (20, 36))
        self.add_line('sym-e3', (24, 8), (19, 13))
        self.add_line('sym-e4', (4, 22), (24, 22))
        self.add_line('sym-e5', (24, 22), (44, 22))
        self.add_line('sym-e6', (44, 22), (39, 18))
        self.add_line('sym-e7', (4, 22), (9, 18))
        self.add_line('sym-e8', (4, 22), (8, 26))
        self.add_line('sym-e9', (24, 8), (29, 13))
        self.add_line('sym-e10', (44, 22), (40, 26))
        self.add_line('sym-e11', (28, 36), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7')
        self.add_contour('sym-c4', 'sym-e8')
        self.add_contour('sym-c5', 'sym-e9')
        self.add_contour('sym-c6', 'sym-e10')
        self.add_contour('sym-c7', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c7')
        self.relate('connect', 'sym-c2', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c3', 'sym-c4')
