"""Expand 6 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86512d7e-7f89-425c-9c88-cc3440d9dc99'
SOURCE_PATH = 'icons-json/interface-essential/expand 6_86512d7e-7f89-425c-9c88-cc3440d9dc99.json'
AUTHOR = 'gpt-6'

class Expand6(Solo48):
    icon_id = 'expand-6'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (27, 21), (42, 6))
        self.add_line('sym-e1', (42, 6), (31, 6))
        self.add_line('sym-e2', (21, 27), (6, 42))
        self.add_line('sym-e3', (6, 42), (6, 31))
        self.add_line('sym-e5', (42, 17), (42, 6))
        self.add_line('sym-e6', (17, 42), (7, 42))
        self.add_arc('sym-e7-2', (7, 42), (6, 42), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=False)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=False)
        self.add_contour('sym-c2', 'sym-e5', closed=False)
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7-2', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
