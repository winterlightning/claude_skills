"""Warp arc (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff0084ba-2ada-5798-95e0-4660fe7cdf66'
SOURCE_PATH = 'icons-json/design/warp arc_ff0084ba-2ada-5798-95e0-4660fe7cdf66.json'
AUTHOR = 'json_to_solo'

class WarpArcDesign(Solo48):
    icon_id = 'warp-arc-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arc', 'design')

    def build(self):
        self.add_arc('sym-e1', (44, 14), (43, 13), radius_x=2)
        self.add_arc('sym-e2', (43, 13), (25, 8), radius_x=36, sweep=False)
        self.add_line('sym-e3', (25, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (23, 8))
        self.add_arc('sym-e5', (23, 8), (5, 13), radius_x=36, sweep=False)
        self.add_arc('sym-e6', (5, 13), (4, 14), radius_x=2)
        self.add_line('sym-e8', (4, 14), (14, 40))
        self.add_line('sym-e10', (14, 40), (15, 39))
        self.add_line('sym-e11', (15, 39), (18, 38))
        self.add_arc('sym-e12', (18, 38), (24, 36), radius_x=14)
        self.add_arc('sym-e13', (24, 36), (30, 38), radius_x=14)
        self.add_line('sym-e14', (30, 38), (33, 39))
        self.add_line('sym-e15', (33, 39), (34, 40))
        self.add_line('sym-e17', (34, 40), (44, 14))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', closed=True)
