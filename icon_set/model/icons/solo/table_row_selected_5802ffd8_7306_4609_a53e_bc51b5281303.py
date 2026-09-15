"""Table row selected (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5802ffd8-7306-4609-a53e-bc51b5281303'
SOURCE_PATH = 'icons-json/interface-essential/table row selected_5802ffd8-7306-4609-a53e-bc51b5281303.json'
AUTHOR = 'gpt-6'

class TableRowSelected(Solo48):
    icon_id = 'table-row-selected'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('table', 'row', 'selected', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (4, 24), (44, 24))
        self.add_line('sym-e2', (44, 24), (44, 38))
        self.add_arc('sym-e4', (44, 38), (41, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e5', (41, 40), (24, 40))
        self.add_line('sym-e6', (24, 40), (24, 8))
        self.add_line('sym-e8', (24, 8), (7, 8))
        self.add_arc('sym-e9', (7, 8), (4, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e10', (4, 10), (4, 38))
        self.add_arc('sym-e14', (4, 38), (7, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e15', (7, 40), (24, 40))
        self.add_line('sym-e16', (44, 24), (44, 11))
        self.add_arc('sym-e17', (44, 11), (44, 10), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e18', (44, 10), (41, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e19', (41, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e14', 'sym-e15', closed=False)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
