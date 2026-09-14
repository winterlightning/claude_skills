"""Hexagon (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96421daf-8508-4131-bcb0-05c368fcbc6a'
SOURCE_PATH = 'icons-json/design/hexagon_96421daf-8508-4131-bcb0-05c368fcbc6a.json'
AUTHOR = 'json_to_solo'

class HexagonDesign(Solo48):
    icon_id = 'hexagon-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'design')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 15))
        self.add_arc('sym-e1', (8, 15), (9, 13), radius_x=3)
        self.add_line('sym-e2', (9, 13), (23, 4))
        self.add_arc('sym-e3', (23, 4), (24, 4), radius_x=69, sweep=False)
        self.add_arc('sym-e6', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_line('sym-e7', (25, 4), (39, 13))
        self.add_arc('sym-e8', (39, 13), (40, 15), radius_x=3)
        self.add_line('sym-e9', (40, 15), (40, 24))
        self.add_line('sym-e10', (40, 24), (40, 33))
        self.add_arc('sym-e11', (40, 33), (39, 35), radius_x=3)
        self.add_line('sym-e12', (39, 35), (25, 44))
        self.add_line('sym-e13', (25, 44), (24, 44))
        self.add_arc('sym-e16', (24, 44), (23, 44), radius_x=29, sweep=False)
        self.add_line('sym-e17', (23, 44), (9, 35))
        self.add_arc('sym-e18', (9, 35), (8, 33), radius_x=3)
        self.add_line('sym-e19', (8, 33), (8, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
