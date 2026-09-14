"""Horizontal rectangle (combination), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c273f28f-c71b-4dd4-8240-ef4705a59b28'
SOURCE_PATH = 'icons-json/combination/horizontal rectangle_c273f28f-c71b-4dd4-8240-ef4705a59b28.json'
AUTHOR = 'json_to_solo'

class HorizontalRectangleCombination(Solo48):
    icon_id = 'horizontal-rectangle-combination'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'combination'
    aliases = ()
    keywords = ('horizontal', 'rectangle', 'combination')

    def build(self):
        self.add_line('sym-e0', (4, 37), (4, 24))
        self.add_line('sym-e1', (4, 24), (4, 11))
        self.add_bezier('sym-e2', (4, 11), ((4.618, 9.56), (5.391, 8.522), (7, 8)))
        self.add_line('sym-e3', (7, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (41, 8))
        self.add_bezier('sym-e5', (41, 8), ((42.609, 8.522), (43.382, 9.56), (44, 11)))
        self.add_line('sym-e6', (44, 11), (44, 24))
        self.add_line('sym-e7', (44, 24), (44, 37))
        self.add_bezier('sym-e8', (44, 37), ((43.382, 38.44), (42.609, 39.478), (41, 40)))
        self.add_line('sym-e9', (41, 40), (24, 40))
        self.add_line('sym-e10', (24, 40), (7, 40))
        self.add_bezier('sym-e11', (7, 40), ((5.391, 39.478), (4.618, 38.44), (4, 37)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
