"""Move top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c0dcfa4-103d-504c-8cea-c6c6ffd99639'
SOURCE_PATH = 'pictographic-primitives/arrows/move top_7c0dcfa4-103d-504c-8cea-c6c6ffd99639.svg'
AUTHOR = 'gpt-6'

class MoveTop(Solo48):
    icon_id = 'move-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('move', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 24))
        self.add_line('sym-e1', (16, 11), (24, 4))
        self.add_line('sym-e2', (24, 4), (32, 11))
        self.add_line('sym-e3', (8, 41), (8, 35))
        self.add_arc('sym-e5', (8, 35), (11, 32), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e6', (11, 32), (37, 32))
        self.add_arc('sym-e8', (37, 32), (40, 35), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e9', (40, 35), (40, 41))
        self.add_arc('sym-e11', (40, 41), (37, 44), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e12', (37, 44), (11, 44))
        self.add_arc('sym-e14', (11, 44), (8, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', closed=False)
        self.add_contour('sym-c2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
