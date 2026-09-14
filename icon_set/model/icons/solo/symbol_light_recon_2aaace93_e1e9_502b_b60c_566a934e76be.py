"""Symbol light recon (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2aaace93-e1e9-502b-b60c-566a934e76be'
SOURCE_PATH = 'icons-json/war/symbol light recon_2aaace93-e1e9-502b-b60c-566a934e76be.json'
AUTHOR = 'json_to_solo'

class SymbolLightRecon(Solo48):
    icon_id = 'symbol-light-recon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'light', 'recon', 'war')

    def build(self):
        self.add_line('e0', (4, 40), (4, 9))
        self.add_line('e1', (5, 8), (44, 8))
        self.add_line('e2', (44, 8), (5, 40))
        self.add_line('e3', (5, 40), (43, 40))
        self.add_line('e4', (44, 39), (44, 8))
        self.add_arc('e5', (4, 9), (5, 8), radius_x=1)
        self.add_arc('e6', (43, 40), (44, 39), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e6', 'e4')
