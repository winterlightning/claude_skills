"""Layout module (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ec55e96-6ff4-4c05-871a-b5ac12d7e8d1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/layout module_1ec55e96-6ff4-4c05-871a-b5ac12d7e8d1.svg'
AUTHOR = 'gpt-6'

class LayoutModule(Solo48):
    icon_id = 'layout-module'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'module', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (44, 24), (4, 24))
        self.add_line('sym-e2', (4, 24), (4, 38))
        self.add_arc('sym-e3', (4, 38), (7, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e4', (7, 40), (41, 40))
        self.add_arc('sym-e6', (41, 40), (44, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e7', (44, 38), (44, 11))
        self.add_arc('sym-e10', (44, 11), (44, 10), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (44, 10), (41, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e12', (41, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (24, 40))
        self.add_line('sym-e15', (24, 8), (7, 8))
        self.add_arc('sym-e16', (7, 8), (4, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e17', (4, 10), (4, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=False)
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', 'sym-e17', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
