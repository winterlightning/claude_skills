"""Cell border full (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '074b16f1-51d9-4e55-89de-bf26c54041c1'
SOURCE_PATH = 'icons-json/interface-essential/cell border full_074b16f1-51d9-4e55-89de-bf26c54041c1.json'
AUTHOR = 'json_to_solo'

class CellBorderFullInterfaceEssential(Solo48):
    icon_id = 'cell-border-full-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cell', 'border', 'full', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 24), (24, 24))
        self.add_line('sym-e1', (24, 24), (6, 24))
        self.add_line('sym-e2', (6, 24), (6, 8))
        self.add_bezier('sym-e3', (6, 8), ((6.09, 7.787), (6, 8.205), (6, 8)))
        self.add_bezier('sym-e4', (6, 8), ((6.45, 7.264), (7.026, 6), (8, 6)))
        self.add_line('sym-e5', (8, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (40, 6))
        self.add_bezier('sym-e7', (40, 6), ((41.023, 6.368), (42, 6.683), (42, 8)))
        self.add_line('sym-e8', (42, 8), (42, 24))
        self.add_line('sym-e9', (42, 24), (42, 40))
        self.add_bezier('sym-e10', (42, 40), ((42, 41.317), (41.023, 41.632), (40, 42)))
        self.add_line('sym-e11', (40, 42), (24, 42))
        self.add_line('sym-e12', (24, 42), (8, 42))
        self.add_bezier('sym-e13', (8, 42), ((7.026, 42), (6.45, 40.736), (6, 40)))
        self.add_bezier('sym-e14', (6, 40), ((6, 39.795), (6.09, 40.213), (6, 40)))
        self.add_line('sym-e15', (6, 40), (6, 24))
        self.add_line('sym-e16', (24, 6), (24, 24))
        self.add_line('sym-e17', (24, 24), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
