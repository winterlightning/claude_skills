"""Horizontal rectangle (combination), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c273f28f-c71b-4dd4-8240-ef4705a59b28'
SOURCE_PATH = 'pictographic-primitives/combination/horizontal rectangle_c273f28f-c71b-4dd4-8240-ef4705a59b28.svg'
AUTHOR = 'gpt-6'

class HorizontalRectangle(Solo48):
    icon_id = 'horizontal-rectangle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'combination'
    aliases = ()
    keywords = ('horizontal', 'rectangle', 'combination')

    def build(self):
        self.add_line('sym-e0', (4, 37), (4, 11))
        self.add_arc('sym-e2', (4, 11), (7, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e3', (7, 8), (41, 8))
        self.add_arc('sym-e5', (41, 8), (44, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e6', (44, 11), (44, 37))
        self.add_arc('sym-e8', (44, 37), (41, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e9', (41, 40), (7, 40))
        self.add_arc('sym-e11', (7, 40), (4, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', closed=True)
