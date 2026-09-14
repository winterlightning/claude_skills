"""Anklet (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83499877-9f6d-4f70-975d-59ade9b78b2f'
SOURCE_PATH = 'icons-json/_uncategorized_03/anklet_83499877-9f6d-4f70-975d-59ade9b78b2f.json'
AUTHOR = 'json_to_solo'

class Anklet(Solo48):
    icon_id = 'anklet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('anklet', '_uncategorized_03')

    def build(self):
        self.add_arc('sym-e0', (21, 39), (24, 35), radius_x=3)
        self.add_arc('sym-e1', (24, 35), (27, 39), radius_x=3)
        self.add_arc('sym-e2', (27, 39), (21, 39), radius_x=3)
        self.add_line('sym-e3', (24, 35), (24, 31))
        self.add_line('sym-e4', (24, 31), (16, 29))
        self.add_arc('sym-e5', (16, 29), (6, 14), radius_x=18)
        self.add_line('sym-e6', (6, 14), (6, 13))
        self.add_line('sym-e7', (6, 13), (6, 12))
        self.add_arc('sym-e8', (6, 12), (8, 6), radius_x=16)
        self.add_arc('sym-e9', (40, 6), (42, 12), radius_x=15)
        self.add_arc('sym-e10', (42, 12), (42, 13), radius_x=1, sweep=False)
        self.add_arc('sym-e11', (42, 13), (42, 14), radius_x=1, sweep=False)
        self.add_arc('sym-e12', (42, 14), (32, 29), radius_x=18)
        self.add_line('sym-e13', (32, 29), (24, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
