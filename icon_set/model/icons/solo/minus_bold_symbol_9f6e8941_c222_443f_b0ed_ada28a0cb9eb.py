"""Minus bold (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f6e8941-c222-443f-b0ed-ada28a0cb9eb'
SOURCE_PATH = 'icons-json/symbol/minus bold_9f6e8941-c222-443f-b0ed-ada28a0cb9eb.json'
AUTHOR = 'gpt-6'

class MinusBoldSymbol(Solo48):
    icon_id = 'minus-bold-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('minus', 'bold', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 40), (8, 40))
        self.add_arc('sym-e2', (8, 40), (4, 32), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e3', (4, 32), (4, 31))
        self.add_arc('sym-e4', (4, 31), (4, 29), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e5', (4, 29), (4, 19))
        self.add_arc('sym-e9', (4, 19), (4, 17), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e10', (4, 17), (4, 16))
        self.add_arc('sym-e11', (4, 16), (8, 8), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e12', (8, 8), (40, 8))
        self.add_arc('sym-e14', (40, 8), (44, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e15', (44, 16), (44, 17))
        self.add_arc('sym-e16', (44, 17), (44, 19), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e17', (44, 19), (44, 29))
        self.add_arc('sym-e21', (44, 29), (44, 31), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('sym-e22', (44, 31), (44, 32))
        self.add_arc('sym-e23', (44, 32), (40, 40), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
