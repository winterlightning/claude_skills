"""Cursor target (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39b81aef-5006-5f09-bd89-8a5d46b7dde8'
SOURCE_PATH = 'icons-json/interface-essential/cursor target_39b81aef-5006-5f09-bd89-8a5d46b7dde8.json'
AUTHOR = 'json_to_solo'

class CursorTarget(Solo48):
    icon_id = 'cursor-target'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'target', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 31), (24, 36))
        self.add_line('sym-e1', (24, 36), (24, 42))
        self.add_line('sym-e2', (24, 17), (24, 12))
        self.add_line('sym-e3', (24, 12), (24, 6))
        self.add_line('sym-e4', (17, 24), (6, 24))
        self.add_arc('sym-e5', (24, 12), (17, 14), radius_x=12, sweep=False)
        self.add_arc('sym-e6', (17, 14), (12, 24), radius_x=13, sweep=False)
        self.add_line('sym-e7', (12, 24), (12, 26))
        self.add_arc('sym-e8', (12, 26), (24, 36), radius_x=12, sweep=False)
        self.add_arc('sym-e9', (24, 36), (36, 26), radius_x=12, sweep=False)
        self.add_line('sym-e10', (36, 26), (36, 24))
        self.add_arc('sym-e11', (36, 24), (31, 14), radius_x=13, sweep=False)
        self.add_arc('sym-e12', (31, 14), (24, 12), radius_x=12, sweep=False)
        self.add_line('sym-e13', (31, 24), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
        self.add_contour('sym-c4', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
