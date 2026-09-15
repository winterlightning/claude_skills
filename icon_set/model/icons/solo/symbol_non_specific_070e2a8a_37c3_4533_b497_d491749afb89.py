"""Symbol non specific (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '070e2a8a-37c3-4533-b497-d491749afb89'
SOURCE_PATH = 'icons-json/protection/symbol non specific_070e2a8a-37c3-4533-b497-d491749afb89.json'
AUTHOR = 'gpt-6'

class SymbolNonSpecific(Solo48):
    icon_id = 'symbol-non-specific'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'non', 'specific', 'protection')

    def build(self):
        self.add_line('sym-e0', (24, 8), (43, 8))
        self.add_line('sym-e2', (43, 8), (44, 10))
        self.add_line('sym-e3', (44, 10), (44, 38))
        self.add_line('sym-e5', (44, 38), (43, 40))
        self.add_line('sym-e6', (43, 40), (6, 40))
        self.add_arc('sym-e9', (6, 40), (5, 40), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e10', (5, 40), (4, 38))
        self.add_line('sym-e11', (4, 38), (4, 10))
        self.add_line('sym-e13', (4, 10), (5, 8))
        self.add_line('sym-e14', (5, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', closed=True)
