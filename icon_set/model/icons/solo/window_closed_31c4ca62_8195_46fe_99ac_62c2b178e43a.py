"""Window closed (building), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31c4ca62-8195-46fe-99ac-62c2b178e43a'
SOURCE_PATH = 'icons-json/building/window closed_31c4ca62-8195-46fe-99ac-62c2b178e43a.json'
AUTHOR = 'gpt-6'

class WindowClosed(Solo48):
    icon_id = 'window-closed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('window', 'closed', 'building')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 8))
        self.add_line('sym-e2', (24, 8), (39, 8))
        self.add_arc('sym-e3', (39, 8), (40, 9), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e4', (40, 9), (40, 24))
        self.add_line('sym-e5', (40, 24), (8, 24))
        self.add_line('sym-e7', (8, 24), (8, 40))
        self.add_line('sym-e8', (8, 40), (4, 40))
        self.add_line('sym-e9', (44, 40), (40, 40))
        self.add_line('sym-e10', (40, 40), (40, 24))
        self.add_line('sym-e11', (40, 40), (8, 40))
        self.add_line('sym-e13', (8, 24), (8, 9))
        self.add_arc('sym-e14', (8, 9), (9, 8), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('sym-e15', (9, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', closed=False)
        self.add_contour('sym-c1', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c2', 'sym-e11', closed=False)
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
