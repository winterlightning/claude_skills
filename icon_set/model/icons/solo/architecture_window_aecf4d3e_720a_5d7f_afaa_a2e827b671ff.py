"""Architecture window (building), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aecf4d3e-720a-5d7f-afaa-a2e827b671ff'
SOURCE_PATH = 'icons-json/building/architecture window_aecf4d3e-720a-5d7f-afaa-a2e827b671ff.json'
AUTHOR = 'json_to_solo'

class ArchitectureWindow(Solo48):
    icon_id = 'architecture-window'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'window', 'building')

    def build(self):
        self.add_line('sym-e0', (40, 26), (8, 26))
        self.add_line('sym-e1', (8, 26), (8, 19))
        self.add_line('sym-e2', (8, 19), (9, 15))
        self.add_arc('sym-e3', (9, 15), (24, 4), radius_x=16)
        self.add_line('sym-e5', (24, 4), (24, 44))
        self.add_line('sym-e6', (24, 44), (40, 44))
        self.add_line('sym-e7', (40, 44), (40, 26))
        self.add_line('sym-e8', (40, 26), (40, 19))
        self.add_line('sym-e9', (40, 19), (39, 15))
        self.add_arc('sym-e10', (39, 15), (24, 4), radius_x=17, sweep=False)
        self.add_line('sym-e12', (8, 26), (8, 44))
        self.add_line('sym-e13', (8, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
