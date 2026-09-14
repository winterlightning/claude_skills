"""State mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f42c1e62-6183-4903-b7ff-5d9817c49685'
SOURCE_PATH = 'icons-json/symbol/state mail_f42c1e62-6183-4903-b7ff-5d9817c49685.json'
AUTHOR = 'json_to_solo'

class StateMailSymbol(Solo48):
    icon_id = 'state-mail-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('state', 'mail', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 28), (26, 27))
        self.add_line('sym-e1', (26, 27), (44, 12))
        self.add_line('sym-e2', (44, 12), (44, 37))
        self.add_arc('sym-e3', (44, 37), (41, 40), radius_x=4)
        self.add_line('sym-e4', (41, 40), (24, 40))
        self.add_line('sym-e5', (24, 40), (7, 40))
        self.add_arc('sym-e6', (7, 40), (4, 37), radius_x=4)
        self.add_line('sym-e7', (4, 37), (4, 12))
        self.add_line('sym-e8', (4, 12), (22, 27))
        self.add_line('sym-e9', (22, 27), (24, 28))
        self.add_line('sym-e10', (24, 8), (41, 8))
        self.add_arc('sym-e11', (41, 8), (44, 11), radius_x=3)
        self.add_arc('sym-e13', (44, 11), (44, 12), radius_x=23, sweep=False)
        self.add_line('sym-e14', (24, 8), (7, 8))
        self.add_arc('sym-e15', (7, 8), (4, 11), radius_x=3, sweep=False)
        self.add_line('sym-e17', (4, 11), (4, 12))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
