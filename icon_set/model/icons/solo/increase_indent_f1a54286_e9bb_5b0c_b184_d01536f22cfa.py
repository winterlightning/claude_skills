"""Increase indent (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f1a54286-e9bb-5b0c-b184-d01536f22cfa'
SOURCE_PATH = 'icons-json/interface-essential/increase indent_f1a54286-e9bb-5b0c-b184-d01536f22cfa.json'
AUTHOR = 'gpt-6'

class IncreaseIndent(Solo48):
    icon_id = 'increase-indent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('increase', 'indent', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (23, 29), (44, 29))
        self.add_line('sym-e1', (23, 40), (44, 40))
        self.add_arc('sym-e2', (16, 24), (15, 25), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e3', (15, 25), (13, 28))
        self.add_line('sym-e4', (13, 28), (4, 35))
        self.add_line('sym-e5', (4, 35), (4, 13))
        self.add_line('sym-e7', (4, 13), (13, 20))
        self.add_line('sym-e8', (13, 20), (15, 23))
        self.add_arc('sym-e9', (15, 23), (16, 24), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('sym-e10', (23, 19), (44, 19))
        self.add_line('sym-e11', (23, 8), (44, 8))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', closed=False)
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c3', 'sym-e10', closed=False)
        self.add_contour('sym-c4', 'sym-e11', closed=False)
