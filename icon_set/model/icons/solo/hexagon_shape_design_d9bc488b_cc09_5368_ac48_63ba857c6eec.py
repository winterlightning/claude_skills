"""Hexagon shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9bc488b-cc09-5368-ac48-63ba857c6eec'
SOURCE_PATH = 'icons-json/design/hexagon shape_d9bc488b-cc09-5368-ac48-63ba857c6eec.json'
AUTHOR = 'gpt-6'

class HexagonShapeDesign(Solo48):
    icon_id = 'hexagon-shape-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'shape', 'design')

    def build(self):
        self.add_arc('sym-e0', (24, 44), (25, 44), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_line('sym-e1', (25, 44), (38, 35))
        self.add_arc('sym-e2', (38, 35), (40, 32), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e4', (40, 32), (40, 31), radius_x=32, radius_y=32, large_arc=False, sweep=True)
        self.add_line('sym-e5', (40, 31), (40, 17))
        self.add_arc('sym-e7', (40, 17), (40, 16), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (40, 16), (38, 13), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e10', (38, 13), (25, 4))
        self.add_arc('sym-e11', (25, 4), (24, 4), radius_x=75, radius_y=75, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (24, 4), (23, 4), radius_x=70, radius_y=70, large_arc=False, sweep=True)
        self.add_line('sym-e13', (23, 4), (10, 13))
        self.add_arc('sym-e14', (10, 13), (8, 16), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e16', (8, 16), (8, 32))
        self.add_arc('sym-e21', (8, 32), (10, 35), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e22', (10, 35), (23, 44))
        self.add_arc('sym-e23', (23, 44), (24, 44), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
