"""Layout four columns 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e6ab6ab-9563-453f-b186-5fff824eaf12'
SOURCE_PATH = 'icons-json/interface-essential/layout four columns 1_2e6ab6ab-9563-453f-b186-5fff824eaf12.json'
AUTHOR = 'json_to_solo'

class LayoutFourColumns1(Solo48):
    icon_id = 'layout-four-columns-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'four', 'columns', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (30, 15), (18, 15))
        self.add_line('sym-e1', (18, 15), (18, 42))
        self.add_line('sym-e2', (18, 42), (30, 42))
        self.add_line('sym-e3', (30, 42), (30, 15))
        self.add_line('sym-e4', (30, 15), (42, 15))
        self.add_line('sym-e5', (42, 15), (42, 8))
        self.add_line('sym-e6', (42, 8), (40, 6))
        self.add_line('sym-e8', (40, 6), (24, 6))
        self.add_line('sym-e9', (24, 6), (8, 6))
        self.add_line('sym-e11', (8, 6), (6, 8))
        self.add_line('sym-e12', (6, 8), (6, 15))
        self.add_line('sym-e13', (6, 15), (18, 15))
        self.add_line('sym-e14', (18, 42), (8, 42))
        self.add_arc('sym-e15', (8, 42), (6, 40), radius_x=4)
        self.add_line('sym-e16', (6, 40), (6, 15))
        self.add_line('sym-e17', (30, 42), (40, 42))
        self.add_line('sym-e18', (40, 42), (42, 40))
        self.add_line('sym-e19', (42, 40), (42, 15))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
