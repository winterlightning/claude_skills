"""Beaker (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1cab2ea-f7f8-47a0-972d-7983402b29a8'
SOURCE_PATH = 'icons-json/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.json'
AUTHOR = 'json_to_solo'

class BeakerSymbol(Solo48):
    icon_id = 'beaker-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('beaker', 'symbol')

    def build(self):
        self.add_line('sym-e0', (15, 4), (19, 4))
        self.add_line('sym-e1', (19, 4), (29, 4))
        self.add_line('sym-e2', (29, 4), (33, 4))
        self.add_line('sym-e3', (19, 4), (19, 12))
        self.add_line('sym-e5', (19, 12), (17, 13))
        self.add_line('sym-e6', (17, 13), (14, 15))
        self.add_arc('sym-e7', (14, 15), (8, 27), radius_x=15, sweep=False)
        self.add_line('sym-e9', (8, 27), (8, 28))
        self.add_arc('sym-e10', (8, 28), (9, 32), radius_x=13, sweep=False)
        self.add_arc('sym-e11', (9, 32), (23, 44), radius_x=16, sweep=False)
        self.add_arc('sym-e12', (23, 44), (24, 44), radius_x=29)
        self.add_line('sym-e17', (24, 44), (25, 44))
        self.add_arc('sym-e18', (25, 44), (39, 32), radius_x=16, sweep=False)
        self.add_arc('sym-e19', (39, 32), (40, 28), radius_x=13, sweep=False)
        self.add_line('sym-e20', (40, 28), (40, 27))
        self.add_arc('sym-e22', (40, 27), (34, 15), radius_x=15, sweep=False)
        self.add_arc('sym-e23', (34, 15), (31, 13), radius_x=13)
        self.add_line('sym-e24', (31, 13), (29, 12))
        self.add_line('sym-e26', (29, 12), (29, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
