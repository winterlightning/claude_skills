"""Symbol non specific (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '070e2a8a-37c3-4533-b497-d491749afb89'
SOURCE_PATH = 'icons-json/protection/symbol non specific_070e2a8a-37c3-4533-b497-d491749afb89.json'
AUTHOR = 'json_to_solo'

class SymbolNonSpecificProtection(Solo48):
    icon_id = 'symbol-non-specific-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('symbol', 'non', 'specific', 'protection')

    def build(self):
        self.add_line('sym-e0', (24, 8), (42, 8))
        self.add_bezier('sym-e1', (42, 8), ((42.191, 8.135), (42.809, 8), (43, 8)))
        self.add_bezier('sym-e2', (43, 8), ((43.8, 8.689), (43.645, 8.991), (44, 10)))
        self.add_line('sym-e3', (44, 10), (44, 24))
        self.add_line('sym-e4', (44, 24), (44, 38))
        self.add_bezier('sym-e5', (44, 38), ((43.645, 39.009), (43.8, 39.311), (43, 40)))
        self.add_bezier('sym-e6', (43, 40), ((42.809, 40), (42.191, 39.865), (42, 40)))
        self.add_line('sym-e7', (42, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (6, 40))
        self.add_bezier('sym-e9', (6, 40), ((5.809, 39.865), (5.191, 40), (5, 40)))
        self.add_bezier('sym-e10', (5, 40), ((4.2, 39.311), (4.355, 39.009), (4, 38)))
        self.add_line('sym-e11', (4, 38), (4, 24))
        self.add_line('sym-e12', (4, 24), (4, 10))
        self.add_bezier('sym-e13', (4, 10), ((4.355, 8.991), (4.2, 8.689), (5, 8)))
        self.add_bezier('sym-e14', (5, 8), ((5.191, 8), (5.809, 8.135), (6, 8)))
        self.add_line('sym-e15', (6, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
