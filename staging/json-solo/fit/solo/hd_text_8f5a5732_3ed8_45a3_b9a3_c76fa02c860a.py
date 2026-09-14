"""Hd (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f5a5732-3ed8-45a3-b9a3-c76fa02c860a'
SOURCE_PATH = 'icons-json/symbol/HD (text)_8f5a5732-3ed8-45a3-b9a3-c76fa02c860a.json'
AUTHOR = 'json_to_solo'

class HdTextSymbol(Solo48):
    icon_id = 'hd-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('hd', 'text', 'symbol')

    def build(self):
        self.add_line('sym-e0', (4, 8), (4, 24))
        self.add_line('sym-e1', (4, 24), (4, 40))
        self.add_line('sym-e2', (19, 24), (4, 24))
        self.add_line('sym-e3', (19, 40), (19, 24))
        self.add_line('sym-e4', (19, 24), (19, 8))
        self.add_line('sym-e5', (44, 24), (44, 20))
        self.add_arc('sym-e7', (44, 20), (35, 8), radius_x=13, sweep=False)
        self.add_line('sym-e10', (35, 8), (29, 8))
        self.add_line('sym-e11', (29, 8), (29, 24))
        self.add_line('sym-e12', (29, 24), (29, 40))
        self.add_line('sym-e13', (29, 40), (35, 40))
        self.add_arc('sym-e16', (35, 40), (44, 28), radius_x=13, sweep=False)
        self.add_line('sym-e18', (44, 28), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e18', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
