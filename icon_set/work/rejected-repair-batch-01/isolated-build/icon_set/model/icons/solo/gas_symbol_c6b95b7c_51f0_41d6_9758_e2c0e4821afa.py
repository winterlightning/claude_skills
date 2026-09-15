"""Gas (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'pictographic-primitives/symbol/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
AUTHOR = 'gpt-6'

class GasSymbol(Solo48):
    icon_id = 'gas-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('gas', 'symbol')

    def build(self):
        self.add_line('sym-e0', (12, 4), (36, 4))
        self.add_line('sym-e3', (32, 4), (32, 13))
        self.add_arc('sym-e4', (32, 13), (39, 15), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e5', (39, 15), (40, 18))
        self.add_line('sym-e6', (40, 18), (40, 39))
        self.add_arc('sym-e8', (40, 39), (34, 44), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e11', (34, 44), (14, 44))
        self.add_arc('sym-e15', (14, 44), (8, 39), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e17', (8, 39), (8, 18))
        self.add_arc('sym-e18', (8, 18), (9, 15), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (9, 15), (16, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e20', (16, 13), (16, 4))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e11', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
