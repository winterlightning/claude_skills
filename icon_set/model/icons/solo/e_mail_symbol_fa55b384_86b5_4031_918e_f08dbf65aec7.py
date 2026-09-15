"""E mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa55b384-86b5-4031-918e-f08dbf65aec7'
SOURCE_PATH = 'pictographic-primitives/symbol/e mail_fa55b384-86b5-4031-918e-f08dbf65aec7.svg'
AUTHOR = 'gpt-6'

class EMailSymbol(Solo48):
    icon_id = 'e-mail-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('e', 'mail', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 27), (20, 25))
        self.add_line('sym-e1', (20, 25), (4, 9))
        self.add_line('sym-e2', (4, 9), (4, 39))
        self.add_arc('sym-e4', (4, 39), (6, 40), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e6', (6, 40), (42, 40))
        self.add_line('sym-e11', (42, 40), (44, 39))
        self.add_line('sym-e12', (44, 39), (44, 9))
        self.add_line('sym-e14', (44, 9), (28, 25))
        self.add_line('sym-e15', (28, 25), (24, 27))
        self.add_line('sym-e16', (4, 9), (4, 8))
        self.add_line('sym-e17', (4, 8), (44, 8))
        self.add_line('sym-e19', (44, 8), (44, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e6', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e19', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
