"""Billboard (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fd374e9-da7b-4096-9042-21a95621b89a'
SOURCE_PATH = 'icons-json/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.json'
AUTHOR = 'json_to_solo'

class BillboardBusiness(Solo48):
    icon_id = 'billboard-business'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('billboard', 'business')

    def build(self):
        self.add_line('sym-e0', (11, 42), (11, 34))
        self.add_line('sym-e1', (11, 34), (24, 34))
        self.add_line('sym-e2', (24, 34), (37, 34))
        self.add_line('sym-e3', (37, 34), (37, 42))
        self.add_line('sym-e4', (37, 42), (40, 42))
        self.add_line('sym-e5', (8, 42), (11, 42))
        self.add_line('sym-e6', (11, 42), (13, 42))
        self.add_arc('sym-e7', (10, 34), (6, 32), radius_x=3)
        self.add_line('sym-e8', (6, 32), (6, 8))
        self.add_arc('sym-e10', (6, 8), (8, 6), radius_x=3)
        self.add_arc('sym-e11', (8, 6), (9, 6), radius_x=10, sweep=False)
        self.add_line('sym-e12', (9, 6), (24, 6))
        self.add_line('sym-e13', (24, 6), (39, 6))
        self.add_line('sym-e14', (39, 6), (40, 6))
        self.add_arc('sym-e15', (40, 6), (42, 8), radius_x=3)
        self.add_line('sym-e17', (42, 8), (42, 32))
        self.add_arc('sym-e18', (42, 32), (38, 34), radius_x=3)
        self.add_line('sym-e19', (38, 34), (37, 34))
        self.add_line('sym-e20', (11, 34), (10, 34))
        self.add_line('sym-e21', (37, 42), (35, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c3', 'sym-e20')
        self.add_contour('sym-c4', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
