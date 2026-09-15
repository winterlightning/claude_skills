"""Mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75ad5383-92bd-435c-984f-c475f5f845c1'
SOURCE_PATH = 'pictographic-primitives/symbol/mail_75ad5383-92bd-435c-984f-c475f5f845c1.svg'
AUTHOR = 'gpt-6'

class Mail(Solo48):
    icon_id = 'mail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('mail', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 25), (4, 13))
        self.add_line('sym-e1', (4, 13), (4, 34))
        self.add_line('sym-e3-1', (4, 34), (5, 38))
        self.add_arc('sym-e3-2', (5, 38), (8, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e4', (8, 40), (9, 40), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('sym-e5', (9, 40), (40, 40))
        self.add_arc('sym-e8-1', (40, 40), (43, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e8-2', (43, 38), (44, 34))
        self.add_line('sym-e9', (44, 34), (44, 13))
        self.add_line('sym-e11', (44, 13), (24, 25))
        self.add_line('sym-e12', (24, 8), (8, 8))
        self.add_arc('sym-e14-1', (8, 8), (5, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('sym-e14-2', (5, 10), (4, 13), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e16', (24, 8), (40, 8))
        self.add_arc('sym-e18-1', (40, 8), (43, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e18-2', (43, 10), (44, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e5', 'sym-e8-1', 'sym-e8-2', 'sym-e9', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e14-1', 'sym-e14-2', closed=False)
        self.add_contour('sym-c2', 'sym-e16', 'sym-e18-1', 'sym-e18-2', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
