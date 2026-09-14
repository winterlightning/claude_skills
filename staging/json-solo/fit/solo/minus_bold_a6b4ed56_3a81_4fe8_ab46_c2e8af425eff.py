"""Minus bold (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'icons-json/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.json'
AUTHOR = 'json_to_solo'

class MinusBoldState(Solo48):
    icon_id = 'minus-bold-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('minus', 'bold', 'state')

    def build(self):
        self.add_line('sym-e0', (40, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (8, 40))
        self.add_arc('sym-e2', (8, 40), (4, 32), radius_x=10)
        self.add_line('sym-e3', (4, 32), (4, 31))
        self.add_arc('sym-e4', (4, 31), (4, 29), radius_x=9, sweep=False)
        self.add_line('sym-e5', (4, 29), (4, 24))
        self.add_line('sym-e6', (4, 24), (4, 19))
        self.add_arc('sym-e7', (4, 19), (4, 17), radius_x=9, sweep=False)
        self.add_line('sym-e8', (4, 17), (4, 16))
        self.add_arc('sym-e9', (4, 16), (8, 8), radius_x=10)
        self.add_line('sym-e10', (8, 8), (24, 8))
        self.add_line('sym-e11', (24, 8), (40, 8))
        self.add_arc('sym-e12', (40, 8), (44, 16), radius_x=10)
        self.add_line('sym-e13', (44, 16), (44, 17))
        self.add_arc('sym-e14', (44, 17), (44, 19), radius_x=9, sweep=False)
        self.add_line('sym-e15', (44, 19), (44, 24))
        self.add_line('sym-e16', (44, 24), (44, 29))
        self.add_arc('sym-e17', (44, 29), (44, 31), radius_x=9, sweep=False)
        self.add_line('sym-e18', (44, 31), (44, 32))
        self.add_arc('sym-e19', (44, 32), (40, 40), radius_x=10)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
