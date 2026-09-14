"""Architecture window (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aecf4d3e-720a-5d7f-afaa-a2e827b671ff'
SOURCE_PATH = 'icons-json/building/architecture window_aecf4d3e-720a-5d7f-afaa-a2e827b671ff.json'
AUTHOR = 'json_to_solo'

class ArchitectureWindowBuilding(Solo48):
    icon_id = 'architecture-window-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('architecture', 'window', 'building')

    def build(self):
        self.add_line('sym-e0', (40, 26), (8, 26))
        self.add_line('sym-e1', (8, 26), (8, 19))
        self.add_bezier('sym-e2', (8, 19), ((8, 17.809), (8.63, 16.145), (9, 15)))
        self.add_bezier('sym-e3', (9, 15), ((10.91, 9.118), (16.96, 4), (24, 4)))
        self.add_bezier('sym-e4', (24, 4), ((24.16, 4), (23.84, 4), (24, 4)))
        self.add_line('sym-e5', (24, 4), (24, 44))
        self.add_line('sym-e6', (24, 44), (40, 44))
        self.add_line('sym-e7', (40, 44), (40, 26))
        self.add_line('sym-e8', (40, 26), (40, 19))
        self.add_bezier('sym-e9', (40, 19), ((40, 17.809), (39.37, 16.145), (39, 15)))
        self.add_bezier('sym-e10', (39, 15), ((37.09, 9.118), (31.04, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((23.84, 4), (24.16, 4), (24, 4)))
        self.add_line('sym-e12', (8, 26), (8, 44))
        self.add_line('sym-e13', (8, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
